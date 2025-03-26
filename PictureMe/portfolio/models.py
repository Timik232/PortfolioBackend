import os

from colorfield.fields import ColorField
from django.core.validators import validate_image_file_extension
from django.db import models


class Album(models.Model):
    choices = [("ser", "Серии фотографий"), ("rep", "Репортаж")]
    type = models.CharField(max_length=3, default="ser", choices=choices)
    image = models.ImageField(upload_to="screensaver/")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    style_number = models.PositiveIntegerField(default=1)
    text_color = ColorField(default="#000000", help_text="Выберите цвет текста")
    grad_color = ColorField(
        format="rgba",
        default="rgba(35,59,52,0.7)",
        help_text="Цвет градиента в формате RGBA",
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Альбом " + self.first_name + " " + self.last_name + f" ({self.type})"


class Element(models.Model):
    choices = [("ser", "Серии фотографий"), ("rep", "Репортаж")]
    type = models.CharField(max_length=3, default="ser", choices=choices)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    style_number = models.PositiveIntegerField(default=1)
    description = models.TextField(null=True, blank=True)
    album = models.ForeignKey(to=Album, on_delete=models.PROTECT)
    text_color = ColorField(default="#000000", help_text="Выберите цвет текста")

    def __str__(self):
        return "Элемент " + self.first_name + " " + self.last_name


class Image(models.Model):
    image = models.ImageField(
        upload_to="photo/", validators=[validate_image_file_extension]
    )
    parent_element = models.ForeignKey(
        Element, on_delete=models.CASCADE, related_name="images", null=True, blank=True
    )  # Add this

    def __str__(self):
        return f"Фото {self.id} ({os.path.basename(self.image.name)})"


class Description(models.Model):
    """
    page='main' – текст на главной странице
    page='abme' – текст на странице обо мне
    """

    choices = [("main", "Главная страница"), ("abme", "Страница обо мне")]
    text = models.TextField()
    page = models.CharField(max_length=4, unique=True, choices=choices)
    main_photo = models.ImageField(upload_to="main/")

    def __str__(self):
        return "Описание " + (
            "главной страницы" if self.page == "main" else "страницы обо мне"
        )


class Order(models.Model):
    type_choices = [
        ("", "Выберите тему сообщения"),
        ("question", "Задать вопрос"),
        ("photo", "Заказать съёмку"),
        ("opinion", "Спросить совета"),
        ("other", "Другое"),
    ]
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField()
    vk_url = models.CharField(max_length=30, null=True, blank=True)
    is_vk_answer = models.BooleanField(null=True, blank=True, default=False)
    message = models.TextField()
    purpose = models.CharField(max_length=20)
    get_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ {self.id} с целью '{self.purpose}'"
