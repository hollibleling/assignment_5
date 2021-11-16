from django.db import models


class ResearchData(models.Model):
    research_id = models.CharField(max_length=7, unique=True)
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=15)
    institution = models.CharField(max_length=15)
    subjects_num = models.CharField(max_length=6, blank=True)
    period = models.CharField(max_length=10, blank=True)
    sort = models.CharField(max_length=10)
    stage = models.CharField(max_length=10, blank=True)
    range = models.CharField(max_length=10)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
