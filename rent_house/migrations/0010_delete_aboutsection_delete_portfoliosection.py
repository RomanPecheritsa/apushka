# Generated by Django 5.1.5 on 2025-02-05 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rent_house", "0009_album_alter_portfoliosection_options_photo"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AboutSection",
        ),
        migrations.DeleteModel(
            name="PortfolioSection",
        ),
    ]
