from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

from portfolio.form import OrderFrom
from portfolio.models import Album, Description, Element
from portfolio.vk_module import send_to_vk


class RobotsView(TemplateView):
    template_name = "photoUploading/robots.txt"
    content_type = "text/plain"


def index(request):
    context = {
        "description": Description.objects.filter(page="main")[0],
    }
    return render(request, "photoUploading/index.html", context)


def aboutme(request):
    context = {
        "description": Description.objects.filter(page="abme")[0],
    }
    return render(request, "photoUploading/aboutme.html", context)


def contacts(request):
    if request.method == "POST":
        form = OrderFrom(data=request.POST)
        if form.is_valid():
            form.instance.get_time = datetime.now()
            messages.success(request, "Ваше сообщение успешно отправлено!")
            form.instance.purpose = form.get_purpose_label()
            form.save()
            send_to_vk(str(form))
            return JsonResponse(
                {"status": "success", "message": "Ваше сообщение успешно отправлено!"}
            )
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    else:
        form = OrderFrom()
    context = {"form": form}
    return render(request, "photoUploading/contacts.html", context=context)


def series(request):
    context = {
        "serie_els": Album.objects.filter(type="ser"),
    }
    return render(request, "photoUploading/series.html", context=context)


def phototerm(request):
    return render(request, "photoUploading/phototerm.html")


def photoreports(request):
    context = {
        "serie_els": Album.objects.filter(type="rep"),
    }
    return render(request, "photoUploading/photoreports.html", context=context)


def element_detail(request, element_id):
    element = Element.objects.filter(album=element_id)[0]
    return render(request, "photoUploading/element.html", {"element": element})


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin_dashboard")
    return render(request, "templates/admin/login.html")
