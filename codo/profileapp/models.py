from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    registered_at = models.DateTimeField(default=timezone.now, editable=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.nickname