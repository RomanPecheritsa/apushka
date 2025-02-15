from django.db import models

from rent_house.utils.image_utils import album_image_path, create_processed_image_field, upload_to

NULLABLE = {"blank": True, "null": True}


class HeroText(models.Model):
    """Модель Hero-text"""

    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Введите заголовок", **NULLABLE)
    text = models.TextField(verbose_name="Текст", help_text="Введите текст", **NULLABLE)
    image = create_processed_image_field(upload_to=upload_to)
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активный (начальный текст)",
        help_text="Установить это фото и текст первым (начальным)",
    )

    class Meta:
        verbose_name = "Hero-текст"
        verbose_name_plural = "Hero-тексты"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            HeroText.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class AboutCard(models.Model):
    """Модель карточек О НАС"""

    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Введите заголовок карточки")
    description = models.TextField(verbose_name="Описание", help_text="Введиет описание")
    image = create_processed_image_field(upload_to=upload_to)

    class Meta:
        verbose_name = "Карточка о нас"
        verbose_name_plural = "Карточки 'Что мы предоставляем'"

    def __str__(self):
        return self.title


class Album(models.Model):
    """Модель альбома"""

    title = models.CharField(max_length=50, verbose_name="Название альбома", help_text="Введите название альбома")
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активный альбом",
        help_text="Установить этот альбом активным",
    )

    def save(self, *args, **kwargs):
        if self.is_active:
            Album.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Альбом галереи"
        verbose_name_plural = "Альбомы галереи"

    def __str__(self):
        return self.title


class Photo(models.Model):
    """Модель фотографии"""

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos", verbose_name="Галерея")
    image = create_processed_image_field(upload_to=album_image_path)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Фото {self.id} из альбома {self.album.title}"


class WithUsCard(models.Model):
    """Модель карточек Рядом с нами"""

    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Введите заголовок карточки")
    description = models.TextField(verbose_name="Описание", help_text="Введиет описание", **NULLABLE)
    image = create_processed_image_field(upload_to=upload_to)
    link = models.URLField(verbose_name="Ссылка", help_text="Укажите ссылку", **NULLABLE)

    class Meta:
        verbose_name = "Карточка о нас"
        verbose_name_plural = "Карточки 'Рядом с нами'"

    def __str__(self):
        return self.title
