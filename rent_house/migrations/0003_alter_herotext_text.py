# Generated by Django 5.1.5 on 2025-02-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent_house", "0002_alter_herotext_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="herotext",
            name="text",
            field=models.TextField(blank=True, help_text="Введите текст", null=True, verbose_name="Текст"),
        ),
    ]
