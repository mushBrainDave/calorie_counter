from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Setting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    calorie_goal = models.PositiveIntegerField(default=2000)
    protein_goal = models.PositiveIntegerField(default=150)
    fat_goal = models.PositiveIntegerField(default=70)
    carb_goal = models.PositiveIntegerField(default=130)
    calorie_min_max = models.BooleanField(default=True)
    set_date = models.DateField(default=datetime.date.today, blank=True, null=True)
    fat_perc_goal = models.PositiveIntegerField(default=18)
    weight_goal = models.PositiveIntegerField(default=150)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Setting.objects.create(user=instance)


class DailyIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='intake')
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    carbs = models.PositiveIntegerField()
    intake_date = models.DateField(default=datetime.date.today, blank=True, null=True)
    fat_perc = models.PositiveIntegerField(default=20)
    current_weight = models.PositiveIntegerField(default=140)

    def __str__(self):
        return str(self.user)

    def id(self):
        return self.user.id
