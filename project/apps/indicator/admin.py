from django.contrib import admin

from .models import Currency

admin.site.register(Currency)

admin.site.site_header = 'CFOremoto'
admin.site.site_title = 'Backend Test'
