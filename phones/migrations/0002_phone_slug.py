# Generated by Django 5.0.3 on 2024-08-14 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=12),
            preserve_default=False,
        ),
    ]
