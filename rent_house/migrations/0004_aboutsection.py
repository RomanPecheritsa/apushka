# Generated by Django 5.1.5 on 2025-02-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent_house", "0003_alter_herotext_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutSection",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(help_text="Введите заголовок", max_length=50, verbose_name="Заголовок")),
                (
                    "additional_title",
                    models.CharField(
                        help_text="Введите дополнительный заголовок",
                        max_length=50,
                        verbose_name="Дополнительный заголовок",
                    ),
                ),
                ("text", models.TextField(help_text="Введите текст", verbose_name="Текст")),
            ],
            options={
                "verbose_name": "Раздел о нас",
                "verbose_name_plural": "Раздел о нас",
            },
        ),
    ]
