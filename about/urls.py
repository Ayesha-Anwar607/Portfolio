from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('extra-curricular/',views.extra,name="extra"),
    path('erorr/',views.error,name='error'),
]
