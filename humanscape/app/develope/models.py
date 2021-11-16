from django.db import models

class ResearchInformation(models.Model):
    
    name           = models.CharField(max_length=100)
    number         = models.CharField(max_length=20, unique=True)
    period         = models.CharField(max_length=10, blank=True, null=True)
    scope          = models.CharField(max_length=20)
    kind           = models.CharField(max_length=20)
    institute      = models.CharField(max_length=20)
    phase          = models.CharField(max_length=20)
    subject_number = models.IntegerField(blank=True, null=True)
    department     = models.CharField(max_length=20)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now= True)

    class Meta:
        db_table   = 'research_information'