from django.urls import path 
from .views import *


urlpatterns = [
    path('MV/',MovieCreateview.as_view(),name='movie_url'),
    path('HV/',MovieDetailview.as_view(),name='home_url'),
    path('update/<int:pk>/',MovieUpdateview.as_view(),name='update_url'),
    path('delete/<int:pk>/',MovieDeleteview.as_view(),name='delete_url'),
    path('<pk>',Movieview.as_view(),name='detail_url')
]
