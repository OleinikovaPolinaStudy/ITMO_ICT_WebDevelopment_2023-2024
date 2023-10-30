from django.contrib import admin
from .models import Owner, Car, License, Ownership
from django.contrib.auth.admin import UserAdmin

admin.site.register(Owner, UserAdmin)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Ownership)
