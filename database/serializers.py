from rest_framework import serializers
from .models import *


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTasks
        fields = "__all__"