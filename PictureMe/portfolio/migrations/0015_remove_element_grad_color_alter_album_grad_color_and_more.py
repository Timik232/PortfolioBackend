# Generated by Django 5.0 on 2025-02-15 14:21

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0013_alter_album_text_color_alter_element_text_color"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="element",
            name="grad_color",
        ),
        migrations.AlterField(
            model_name="album",
            name="grad_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="rgba(35,59,52,0.7)",
                help_text="Цвет градиента в формате RGBA",
                image_field=None,
                max_length=25,
                null=True,
                samples=None,
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(
                upload_to="photo/",
                validators=[django.core.validators.validate_image_file_extension],
            ),
        ),
    ]
