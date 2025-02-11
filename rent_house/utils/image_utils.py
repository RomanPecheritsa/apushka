import os
import uuid

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from pilkit.processors import Transpose


def upload_to(instance, filename):
    """Функция для формирования пути загрузки изображений"""
    model_name = instance.__class__.__name__.lower()
    random_name = f"{uuid.uuid4().hex[:8]}{os.path.splitext(filename)[1]}"
    return f"{model_name}/{random_name}"


def album_image_path(instance, filename):
    """Функция для формирования пути загрузки изображений альбома"""
    ext = filename.split(".")[-1]
    random_name = uuid.uuid4().hex[:8]
    return f"albums/album_{instance.album.slug}/{random_name}.{ext}"


def create_processed_image_field(upload_to, verbose_name="Фотография", help_text="Загрузите фотографию"):
    """Функция для загрузки изменения размера загружаемых фотографий"""
    return ProcessedImageField(
        upload_to=upload_to,
        processors=[
            Transpose(),
            ResizeToFit(900, 600),
        ],
        format="JPEG",
        options={"quality": 90},
        verbose_name=verbose_name,
        help_text=help_text,
    )
