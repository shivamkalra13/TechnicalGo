from django.contrib import admin
from first_app.models import Classes,Subject,Notes,Videos,Books
# Register your models here
admin.site.register(Classes)
admin.site.register(Subject)
admin.site.register(Notes)
admin.site.register(Videos)
admin.site.register(Books)
