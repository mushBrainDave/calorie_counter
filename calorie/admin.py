from django.contrib import admin
from .models import Setting, DailyIntake


class SettingList(admin.ModelAdmin):
    list_display = ('user', 'id', 'pk', 'calorie_goal', 'weight_goal', 'fat_perc_goal', 'protein_goal', 'fat_goal', 'carb_goal', 'calorie_min_max', 'set_date')
    list_filter = ('calorie_goal', 'calorie_min_max')


class IntakeList(admin.ModelAdmin):
    list_display = ('user', 'id', 'pk', 'calories', 'current_weight','fat_perc', 'protein', 'fat', 'carbs', 'intake_date')
    list_filter = ('user', 'calories')
    search_fields = ('calories', 'intake_date')
    ordering = ['intake_date']


admin.site.register(Setting, SettingList)
admin.site.register(DailyIntake, IntakeList)
