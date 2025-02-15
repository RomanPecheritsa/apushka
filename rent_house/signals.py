import os
import shutil

from django.db.models.signals import post_delete
from django.dispatch import receiver
from slugify import slugify

from rent_house.models import Album


@receiver(post_delete)
def delete_uploaded_files(sender, instance, **kwargs):
    """
    Сигнал для удаления файлов и папок после удаления записи.
    """
    if hasattr(instance, "image"):
        if instance.image:
            if os.path.isfile(instance.image.path):
                os.remove(instance.image.path)


@receiver(post_delete, sender=Album)
def delete_album_folder(sender, instance, **kwargs):
    """
    Сигнал для удаления папки альбома после удаления записи альбома.
    """
    album_slug = slugify(instance.title)
    folder_path = os.path.join("media", "albums", f"album_{album_slug}")

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
