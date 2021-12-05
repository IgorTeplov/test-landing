from django.contrib import admin
from django.urls import include, path
from mandala.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing),
    path('indexReact/', indexReact),
    path('indexTest/', ApiView.as_view()),
]
