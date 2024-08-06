from django.contrib import admin
from vercel_deploy.models import Test, Contact, Tag,TimeTest
# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','age', 'email')
    inlines = [TagInline]
    fieldsets = ([
        'Main',{
            'fields':('name','email')
        }
    ],[
        'Advance',{
            'classes':('collapse',),
            'fields':('age',)
        }
    ])
class TestAdmin(admin.ModelAdmin):
    list_display=('name','cons')

class TagAdmin(admin.ModelAdmin):
    list_display=('name','contact')

class TimeTestAdmin(admin.ModelAdmin):
    list_display= ('name','cons','updated_at')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TimeTest, TimeTestAdmin)
admin.site.register(Tag, TagAdmin)
