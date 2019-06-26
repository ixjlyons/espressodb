from django.contrib import admin

from lattedb.django.base.admin import BaseAdmin

from lattedb.django.linksmearing.models import Unsmeared
from lattedb.django.linksmearing.models import WilsonFlow

# Register your models here.
admin.site.register(Unsmeared, BaseAdmin)
admin.site.register(WilsonFlow, BaseAdmin)
