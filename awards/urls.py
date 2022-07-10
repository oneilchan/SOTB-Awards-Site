from django.urls import path 
from . import views

app_name = 'awards'
urlpatterns = [
    path('',views.awards, name='awards'),
    path('<int:award_id>/', views.voting, name='voting'),
    path('<int:award_id>/vote/', views.vote, name='vote'),
    path('<int:award_id>/results', views.results, name='results')
]