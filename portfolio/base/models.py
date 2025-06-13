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

    class Meta:
        ordering = ['start_date']  # Orders by start_date ascending

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, help_text="Icon class or URL (e.g., 'fa-brands fa-python' or SVG path)")
    proficiency = models.PositiveSmallIntegerField(default=50, help_text="Proficiency from 1 to 100")
    color = models.CharField(max_length=20, default="#2563eb", help_text="Hex color for progress bar (e.g., #2563eb for blue)")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

class Expertise(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100, help_text="Icon class or URL (e.g., 'fa-brands fa-docker' or SVG path)")
    description = models.CharField(max_length=200, blank=True, help_text="Short description or tagline")

    def __str__(self):
        return self.name
