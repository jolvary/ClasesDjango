from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm

# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
	list_display  =  ["email", "nombre", "timestamp"]
	form =  RegModelForm
	#list_display_list = ["email"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email", "nombre"]
	#class Meta:
	#	moderl = Registrado

admin.site.register(Registrado, AdminRegistrado)