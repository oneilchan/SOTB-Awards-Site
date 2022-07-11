# from django.contrib import admin
# from .models import Award, Options
# # Register your models here.
# # frowningdog
# admin.site.register(Award)
# admin.site.register(Options)
from django.contrib import admin

from .models import Options, Award


class OptionsInline(admin.StackedInline):
    model = Options
    extra = 3


class AwardAdmin(admin.ModelAdmin,):
    fieldsets = [
        (None,               {'fields': ['award_title']}), (None,               {'fields': ['description_text']}), (None,               {'fields': ['upload']})
    ]
    inlines = [OptionsInline]

admin.site.register(Award, AwardAdmin)