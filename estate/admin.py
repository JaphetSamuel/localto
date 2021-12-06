from django.contrib import admin
from django.db.models import fields
from .models import Propriete, Agent, Proximite, ProprieteImage
from django.utils.html import format_html
from django.conf import settings

# Register your models here.
class ProximiteInline(admin.TabularInline):
    model = Proximite
    classes = ('collapse',)

class ProprieteImageInline(admin.TabularInline):
    model = ProprieteImage
    classes = ('collapse',)


@admin.register(Propriete)
class ProprieteAdmin(admin.ModelAdmin):
    list_display = ('nom','adresse','enVente',"enLocation",)
    list_filter = ('enVente','enLocation','nb_etages')

    inlines = [ProprieteImageInline,ProximiteInline]

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('photo_render','nom', 'prenom', 'email', 'telephone',)
    list_display_links = ('nom','prenom','photo_render')

    @admin.display(description='photo')
    def photo_render(self, obj):
        return format_html('<img src="{}{}" width="50px" height="50px" />'.format(settings.MEDIA_URL,obj.photo))


