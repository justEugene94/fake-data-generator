from django.contrib import admin

from data_generator.models import Schema, Type, Column

admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(Type)
