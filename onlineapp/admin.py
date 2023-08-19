from django.contrib import admin
from onlineapp.models import UserProfile, Doctor

admin.site.site_header = "Registration | Admin"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'address', 'city', 'state', 'pincode']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Doctor)