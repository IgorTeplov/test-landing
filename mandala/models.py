from django.db import models

class Participant(models.Model):
    user_id = models.IntegerField(primary_key = True)
    meeting_date = models.DateField()
    mail = models.EmailField()
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 30)
    registration_date = models.DateField()
    registration_language = models.CharField(max_length = 30)
    
class Language(models.Model):
    en = models.CharField(primary_key = True, max_length = 30)
    ru = models.CharField(max_length = 30)
    ua = models.CharField(max_length = 30)