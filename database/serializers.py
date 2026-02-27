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

class ComplteTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplteTasks
        fields = '__all__'


class MonthlyGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyGoals
        fields = '__all__'
