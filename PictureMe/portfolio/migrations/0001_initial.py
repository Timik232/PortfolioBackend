# Generated by Django 4.2 on 2023-12-14 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Amounts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reports_amount", models.PositiveIntegerField()),
                ("series_amount", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Elements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="screensaver/")),
                ("first_name", models.CharField(max_length=40)),
                ("last_name", models.CharField(max_length=40)),
                ("style_number", models.PositiveIntegerField(default=1)),
                ("element_url", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="photo/")),
            ],
        ),
        migrations.CreateModel(
            name="SerieElement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=80)),
                ("last_name", models.CharField(max_length=80)),
                ("style_number", models.PositiveIntegerField(default=1)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "images",
                    models.ManyToManyField(
                        related_name="collections", to="portfolio.image"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="image",
            name="collection",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="portfolio.serieelement"
            ),
        ),
    ]
