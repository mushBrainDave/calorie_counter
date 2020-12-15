from djoser.serializers import User
from rest_framework import serializers
from .models import Setting, DailyIntake


class SettingSerializer(serializers.ModelSerializer):

    class Meta:
            model = Setting
            fields = '__all__'


class IntakeSerializer(serializers.ModelSerializer):

    class Meta:
            model = DailyIntake
            fields = '__all__'
