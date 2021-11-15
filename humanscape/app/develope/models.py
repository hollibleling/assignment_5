from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=32)


class Phase(models.Model):
    name = models.CharField(max_length=32)


class Scope(models.Model):
    name = models.CharField(max_length=32)


class DevelopeList(models.Model):
    number = models.CharField(max_length=128)
    name = models.CharField(max_length=512)
    subject = models.CharField(max_length=128)
    agency = models.CharField(max_length=64)
    target_count = models.PositiveIntegerField(default=0, blank = True, null=True)
    period = models.CharField(max_length=16, null=True)
    kind = models.ForeignKey(Kind, on_delete=models.DO_NOTHING)
    phase = models.ForeignKey(Phase, on_delete=models.DO_NOTHING)
    scope = models.ForeignKey(Scope, on_delete=models.DO_NOTHING)
