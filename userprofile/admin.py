from django.contrib import admin

from models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio',
        'birth_date',
        'location',
    )

admin.site.register(Profile, ProfileAdmin)
