from django.contrib import admin

from .models import Currency, Date

admin.site.register(Currency)
admin.site.register(Date)

admin.site.site_header = 'CFOremoto'
admin.site.site_title = 'Backend Test'
