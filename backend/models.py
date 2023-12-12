from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10, null=True, blank=True)
    repository_link = models.CharField(max_length=100, null=True, blank=True)
    last_commit = models.CharField(max_length=10, null=True, blank=True)
    vulnerabilities = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    upload_date = models.DateField(default=timezone.now)
    last_scan = models.DateField(null=True, blank=True)
    src_code = models.FileField()
 