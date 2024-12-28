from django.contrib import admin
from . import models

# Register your models here.

class SessionsInline(admin.TabularInline):
    model = models.Volunteer.sessions.through


class SessionAdmin(admin.ModelAdmin):
    inlines = [
        SessionsInline,
    ]


class VolunteerAdmin(admin.ModelAdmin):
    inlines = [
        SessionsInline,
    ]
    exclude = ["sessions"]


admin.site.register(models.Session, SessionAdmin)

admin.site.register(models.Volunteer, VolunteerAdmin)