from django.db import models
    
class Department(models.Model):
    department = models.CharField(max_length=50)

class Institution(models.Model):
    institution = models.CharField(max_length=50)

class Category(models.Model):
    INTERVENTIONAL, OBSERVATIONAL = ('interventional','observational')
    CATEGORY_CHOICE = (
        (INTERVENTIONAL, '중재연구'),
        (OBSERVATIONAL, '관찰연구')
    )
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=50)

class Phase(models.Model):   
    phase = models.CharField(max_length=20)

class Scope(models.Model):    
    scope = models.CharField(max_length=10)

class Clinical(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    target_number = models.PositiveBigIntegerField(null=True)
    term = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    phase = models.ForeignKey(Phase, on_delete=models.DO_NOTHING)
    scope = models.ForeignKey(Scope, on_delete=models.DO_NOTHING)