# Generated by Django 4.2 on 2023-12-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0006_rename_images_element_photos_alter_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="photo/"),
        ),
    ]
