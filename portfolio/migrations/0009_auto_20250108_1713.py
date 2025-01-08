# Generated by Django 4.2.17 on 2025-01-08 14:13

from django.db import migrations
from django.conf import settings
import os
from django.core import serializers
from django.db.utils import OperationalError


def load_fixtures(apps, schema_editor):
    # List of fixture files to load
    fixture_files = [
        'Album.json',
        'Description.json',
        'Element.json',
        'Image.json',
    ]

    # Check if any data exists for the models
    models_to_check = [
        apps.get_model('portfolio', 'Album'),
        apps.get_model('portfolio', 'Description'),
        apps.get_model('portfolio', 'Element'),
        apps.get_model('portfolio', 'Image'),
    ]

    # If any model has data, skip loading fixtures
    for model in models_to_check:
        if model.objects.exists():
            return  # Data already exists, skip loading fixtures

    # Load each fixture file
    for fixture_file in fixture_files:
        fixture_path = os.path.join(settings.BASE_DIR, 'portfolio', 'fixtures', fixture_file)
        if os.path.exists(fixture_path):
            with open(fixture_path, 'rb') as f:
                objects = serializers.deserialize('json', f)
                for obj in objects:
                    obj.save()
        else:
            raise FileNotFoundError(f"Fixture file not found at {fixture_path}")

class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0008_delete_amount_remove_album_element_url_and_more"),
    ]

    operations = [
        migrations.RunPython(load_fixtures),
    ]
