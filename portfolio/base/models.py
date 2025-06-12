
from django.db import models

# Create your models here.
class Education(models.Model):
        level = models.CharField(max_length=100)
        institution_name = models.CharField(max_length=100)
        start_date = models.DateField()
        end_date = models.DateField()
        description = models.TextField()
        image = models.ImageField(upload_to='education_images/')
        
        def __str__(self):
            return f"{self.level} at {self.institution_name}"
