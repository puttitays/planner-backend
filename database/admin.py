from django.contrib import admin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Quote', 'Author')

class DailyTasksAdmin(admin.ModelAdmin):
    list_display = ('id','task_date', 'title', 'status')


class ComplteTasksAdmin(admin.ModelAdmin):
    list_display = ('task_date', 'title', 'status')

class MonthlyGoalsAdmin(admin.ModelAdmin):
    list_display = ('month', 'title', 'status')
admin.site.register(Quote, QuoteAdmin)
admin.site.register(DailyTasks, DailyTasksAdmin)
admin.site.register(ComplteTasks, ComplteTasksAdmin)
admin.site.register(MonthlyGoals, MonthlyGoalsAdmin)