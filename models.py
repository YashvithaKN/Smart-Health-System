from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        blank=True
    )
    height = models.FloatField(null=True, blank=True, help_text="Height in centimeters")
    weight = models.FloatField(null=True, blank=True, help_text="Weight in kilograms")
    activity_level = models.CharField(
        max_length=20,
        choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')],
        default='moderate'
    )
    
    health_goal = models.CharField(
        max_length=20,
        choices=[('lose', 'Lose weight'), ('maintain', 'Maintain weight'), ('gain', 'Gain weight')],
        default='maintain'
    )

    def bmi(self):
        if self.height and self.weight:
            h = self.height / 100
            return round(self.weight / (h * h), 1)
        return None

    def __str__(self):
        return f"Profile: {self.user.username}"
