from django.db import models

from django.urls import reverse
import uuid

class Table(models.Model):
    name = models.CharField(max_length=150)
    count = models.IntegerField()
    price = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    class Meta:
        verbose_name = 'Ma\'lumot'
        verbose_name_plural = 'Ma\'lumotlar'
    
    def __str__(self):
        return self.name

    def ochish(self):
        return reverse("post", kwargs={'post_id': self.pk})
    