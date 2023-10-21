from django.contrib import admin
from.models import *
from tinymce.widgets import TinyMCE

class BlogAdmin(admin.ModelAdmin):
     fieldsets = [ 

            ("Title/ Date", {'fields': ['image', 'file','author','title','date']}),
            ("Blog Detail", {'fields': ['content']})  

    

                ]

     formfield_overrides = {
            models.TextField: {'widget':TinyMCE()}
                          }

admin.site.register(Blog,BlogAdmin)
admin.site.register(Task)