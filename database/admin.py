from django.contrib import admin
from django.contrib.auth.models import User

from .models import *
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Quote', 'Author')


admin.site.register(Quote,QuoteAdmin)