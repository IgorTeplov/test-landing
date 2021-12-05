from django.contrib import admin
from mandala.models import Participant, Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):    
    pass

