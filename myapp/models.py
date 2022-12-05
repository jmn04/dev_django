from django.db import models
from django.utils import timezone
import uuid


# Create your models here.

class NoteTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='見出し', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True)
    text = models.TextField(verbose_name='本文', max_length=400)
    created_at = models.DateTimeField(verbose_name='作成日時', blank=True, default=timezone.now, editable=False)
    updated_at = models.DateTimeField(verbose_name='最終変更日時', null=False, default=timezone.now)
    # last_updated = models.DateTimeField(verbose_name='最終変更日時', blank=True, )

    def __str__(self):
        return self.title

