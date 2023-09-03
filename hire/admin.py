from django.contrib import admin
from .models import AppliedUserData

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['Firstname','Lastname','job_role','phonenumber','address','my_image']


admin.site.register(AppliedUserData,UserProfileAdmin)

