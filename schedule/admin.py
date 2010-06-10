from django.contrib import admin

from schedule.models import Calendar, Event, CalendarRelation, Rule

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']

class EventAdmin(admin.ModelAdmin):
    raw_id_fields = ("creator",)

admin.site.register(Calendar, CalendarAdminOptions)
admin.site.register(Event, EventAdmin)
admin.site.register([Rule, CalendarRelation])
