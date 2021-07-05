from django.contrib import admin
from django.db.models.fields import FloatField
from .models import Follower

# Register your models here.
class FollwerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Follower, FollwerAdmin)