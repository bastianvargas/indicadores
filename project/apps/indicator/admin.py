from django.contrib import admin

from .models import Currency, Date

class DateAdmin(admin.ModelAdmin):
    readonly_fields = (
        'curr',
        'date_currency',
        'value'
    )
    # ordering = (
    #     '-created_at',
    # )
    list_display = (
        'curr',
        'date_currency',
        'value',
    )
    search_fields = [
        'curr__code',
        'date_currency'
    ]


admin.site.register(Currency)
admin.site.register(Date, DateAdmin)

admin.site.site_header = 'CFOremoto'
admin.site.site_title = 'Backend Test'
