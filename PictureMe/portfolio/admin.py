from django import forms
from django.contrib import admin
from django.core.validators import validate_image_file_extension
from django.utils.html import format_html
from multiupload_plus.fields import MultiImageField

from portfolio.models import Album, Description, Element, Image, Order


def hex_to_rgb(hex_color):
    try:
        hex_color = hex_color.strip().lstrip("#")
        if len(hex_color) == 3:
            hex_color = "".join([c * 2 for c in hex_color])
        return "rgb({}, {}, {})".format(
            int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        )
    except (ValueError, AttributeError, IndexError):
        return "Неверный HEX-формат"


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="100" />', obj.image.url)
        return "-"

    preview.short_description = "Превью"


admin.site.register(Album)
admin.site.register(Image)
admin.site.register(Description)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "phone_number",
        "email",
        "vk_url",
        "is_vk_answer",
        "purpose",
        "message",
    )
    list_display = ["get_time"]
    list_filter = ["get_time", "purpose", "is_vk_answer"]
    search_fields = ["purpose", "get_time", "is_vk_answer"]


class ElementAdminForm(forms.ModelForm):
    attachments = MultiImageField(
        required=False,
        min_num=1,
        max_file_size=1024 * 1024 * 15,  # 15 MB
        label="Загрузить фотографии",
        validators=[],
    )

    class Meta:
        model = Element
        fields = "__all__"

    def clean_attachments(self):
        attachments = self.cleaned_data.get("attachments", [])
        for attachment in attachments:
            validate_image_file_extension(attachment)
        return attachments


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    form = ElementAdminForm
    inlines = [ImageInline]
    list_display = (
        "first_name",
        "last_name",
        "album",
        "type",
        "description",
        "style_number",
        "photos_count",
        "text_color",
    )

    def save_model(self, request, obj, form, change):
        # Сначала сохраняем основной объект
        super().save_model(request, obj, form, change)

        # Затем обрабатываем вложенные изображения
        if form.cleaned_data.get("attachments"):
            for image_file in form.cleaned_data["attachments"]:
                Image.objects.create(image=image_file, parent_element=obj)

    def photos_count(self, obj):
        return obj.images.count()
