from django.db import models
from pytils.translit import slugify as pytils_slugify

from rent_house.utils.image_utils import album_image_path, create_processed_image_field, upload_to

NULLABLE = {"blank": True, "null": True}


class HeroText(models.Model):
    """Модель Hero-text"""

    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Введите заголовок", **NULLABLE)
    text = models.TextField(verbose_name="Текст", help_text="Введите текст", **NULLABLE)
    photo = create_processed_image_field(upload_to=upload_to)
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
    slug = models.SlugField(unique=True, blank=True, verbose_name="slug для фильтрации в шаблоне")
    is_active = models.BooleanField(
        default=False, verbose_name="Активный (начальный альбом)", help_text="Активный альбом"
    )
    is_published = models.BooleanField(default=True, verbose_name="Опубликован", help_text="Опубликован")

    class Meta:
        verbose_name = "Альбомы в галерею"
        verbose_name_plural = "Альбомы в галерею"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            Album.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        if not self.slug:
            base_slug = pytils_slugify(self.title)
            unique_slug = base_slug
            counter = 1

            while Album.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)


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
    description = models.TextField(verbose_name="Описание", help_text="Введиет описание")
    image = create_processed_image_field(upload_to=upload_to)
    link = models.URLField(verbose_name="Ссылка", help_text="Укажите ссылку")

    class Meta:
        verbose_name = "Карточка о нас"
        verbose_name_plural = "Карточки 'Рядом с нами'"

    def __str__(self):
        return self.title
