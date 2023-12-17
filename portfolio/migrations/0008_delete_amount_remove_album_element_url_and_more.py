# Generated by Django 4.2 on 2023-12-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_image_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Amount',
        ),
        migrations.RemoveField(
            model_name='album',
            name='element_url',
        ),
        migrations.AlterField(
            model_name='element',
            name='type',
            field=models.CharField(choices=[('ser', 'Серии фотографий'), ('rep', 'Репортаж')], default='ser', max_length=3),
        ),
    ]
