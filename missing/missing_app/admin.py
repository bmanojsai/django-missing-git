from django.contrib import admin
from .models import UserProfileInfo,Items_lost,Contact_us
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Items_lost)
admin.site.register(Contact_us)
