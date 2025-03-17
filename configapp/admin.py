from django.contrib import admin
from .models import Student, Fanlar

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'lastname', 'address', 'yili', 'phone', 'photo')
    list_display_links = ['surname', 'lastname']
    search_fields = ['name', 'surname', 'lastname']
    list_editable = ['phone', 'address']

class FanlarAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Student, StudentAdmin)
admin.site.register(Fanlar, FanlarAdmin)
