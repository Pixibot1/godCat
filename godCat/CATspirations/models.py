from django.db import models
from django.utils import timezone

class Theocat(models.Model):
    title = models.CharField(max_length=200)
    preview = models.TextField(default="Another theory. One of many.")
    text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
