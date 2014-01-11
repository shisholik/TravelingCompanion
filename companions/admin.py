from django.contrib import admin
from companions.models import Route, City, Companion


class CompanionInline(admin.TabularInline):
    model = Companion
    extra = 3

class RouteAdmin(admin.ModelAdmin):
    inlines = [CompanionInline]

admin.site.register(Route,RouteAdmin)
admin.site.register(City)
admin.site.register(Companion)

