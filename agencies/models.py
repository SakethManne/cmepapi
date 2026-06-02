from django.db import models

TYPE_CHOICES = (
    ('SERP', 'Society for Elimination of Rural Poverty'),
    ('MEPMA', 'Mission for Elimination of Poverty in Municipal Areas'),
    ('KVIB', 'Khadi & Village Industries Board'),
    ('DIC', 'District Industries Centre'),
)

# Create your models here.
class ImplementingAgency(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(choices=TYPE_CHOICES)


class Bank(models.Model):
    name = models.CharField(max_length=128)


class NodalOffice(models.Model):
    name = models.CharField(max_length=128)