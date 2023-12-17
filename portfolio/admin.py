from django.contrib import admin

from portfolio.models import Album, Element, Image, Description, Order
from django import forms


class MultiplyImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

        widgets = {
            'images': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
        }


admin.site.register(Album)
admin.site.register(Element)
admin.site.register(Image)
admin.site.register(Description)
# admin.site.register(Order)


class ImageInline(admin.StackedInline):
    model = Image


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = (
        "name", "phone_number", "email", "vk_url", "is_vk_answer", "purpose",
        "message"
    )
    list_display = ["get_time"]
    list_filter = ["get_time", "purpose", "is_vk_answer"]
    search_fields = ["purpose", "get_time", "is_vk_answer"]






# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     fields = ("none",)
#     inlines = [ImageInline, ]


# @admin.register(Image)
# class ElementAdmin(admin.ModelAdmin):
    # inlines = [ImageInline, ]


# @admin.register(Element)
# class ElementAdmin(admin.ModelAdmin):
    # inlines = [ImageInline, ]


