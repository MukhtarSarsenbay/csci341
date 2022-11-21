from django.contrib import admin
from .models import Users
from .models import Country
from .models import Diseasetype
from .models import Disease
from .models import Discover
from .models import Publicservant
from .models import Doctor
from .models import Specialize
from .models import Record



class DiseaseTypeAdmin(admin.ModelAdmin):
    list_display=['id','description']
class CountryAdmin(admin.ModelAdmin):
    list_display=['cname','population']
class UsersAdmin(admin.ModelAdmin):
    list_display=['email','name','surname','salary','phone','cname']
class DiseaseAdmin(admin.ModelAdmin):
    list_display=['disease_code','pathogen','description','id']
class DiscoverAdmin(admin.ModelAdmin):
    list_display=['cname','disease_code','firstencdate']
class PublicservantAdmin(admin.ModelAdmin):
    list_display=['email','department']
class DoctorAdmin(admin.ModelAdmin):
    list_display=['email','degree']
class SpecializeAdmin(admin.ModelAdmin):
      list_display=['id','email']
class RecordAdmin(admin.ModelAdmin):
    list_display=['cname','disease_code','total_deaths','total_patients']
# Register your models here.
admin.site.register(Diseasetype, DiseaseTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Publicservant, PublicservantAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialize, SpecializeAdmin)
#admin.site.register(Record,RecordAdmin)
#admin.site.register(Discover, DiscoverAdmin)
