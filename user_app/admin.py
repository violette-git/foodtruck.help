from django.contrib import admin
from .models import  User
# Register your models here.
admin.site.register(User)
class User(admin.ModelAdmin):
    all_fields = [f.name for f in User._meta.fields]
    parent_fields = User.get_deferred_fields(User)

    list_display = all_fields
    read_only = parent_fields