from django.contrib import admin
from django.urls import path,include
from leleyao import views
urlpatterns = [
   path('leleyao/',views.leleyao)
]
