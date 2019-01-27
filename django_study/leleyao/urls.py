from django.contrib import admin
from django.urls import path,include
from leleyao import views
urlpatterns = [
   path('index.html',views.sxsong),
   path('leleyao/',views.leleyao)
]
