from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(max_length=20, unique=True)