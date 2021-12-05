from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from mandala.models import Participant, Language
from datetime import date, datetime
from django.core.mail import send_mail

def landing(request):
    return HttpResponse("Админ")

def indexReact(request):
    return render(request, 'index.html')

@method_decorator(csrf_exempt, name='dispatch')
class ApiView(View):

    def get(self, request):
        return render(request, 'indexTest.html')

    def post(self, request):
        post_values = request.POST
        
        meeting_date_str = post_values['meeting_date']
        meeting_date_obj = datetime.strptime(meeting_date_str, '%d/%m/%Y')
        mail_str = post_values['mail']
        name_str = post_values['name']
        phone_str = post_values['phone']
        today_obj = date.today()
        registration_language_str = "ru"

        participant = Participant(meeting_date=meeting_date_obj, mail=mail_str, name=name_str, phone=phone_str, registration_date=today_obj, registration_language=registration_language_str)
        participant.save()

        a = meeting_date_str + " " + mail_str + " " + name_str + " " + phone_str

        send_mail("Тестовое сообщение", a, "mr.olegyou@gmail.com", ["mr.olegyou@ukr.net", "marina_melnick@ukr.net"])

        return JsonResponse(post_values)