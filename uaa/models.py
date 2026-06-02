from django.db import models
from django.contrib.auth.models import AbstractUser

from agencies.models import Bank, ImplementingAgency, NodalOffice

TYPE_CHOICES = (
    ('APPLICANT', 'Applicant'),
    ('IA_OFFICER', 'Implementing Agency Officer'),
    ('IA_ADMIN', 'Implementing Agency Admin'),
    ('BANK_OFFICER', 'Bank Officer'),
    ('BANK_ADMIN', 'Bank Admin'),
    ('NODAL_OFFICER', 'Nodal Officer'),
    ('NODAL_ADMIN', 'Nodal Admin'),
    ('ADMIN', 'Admin'),
)

class Role(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, unique=True)
    type = models.CharField(choices=TYPE_CHOICES)

    class Meta:
        unique_together = ('name', 'type')

    def __str__(self):
        return self.name

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=80)
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.PROTECT)
    is_email_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agency = models.ForeignKey(ImplementingAgency, on_delete=models.SET_NULL, null=True, blank=True)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, null=True, blank=True)
    nodal_office = models.ForeignKey(NodalOffice, on_delete=models.SET_NULL, blank=True, null=True)