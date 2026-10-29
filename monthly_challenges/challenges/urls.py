from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='all-challenges'),
    path('<int:month>', views.monthlyChallengeByNumber, name='monthly-challenge-by-number'),
    path('<str:month>', views.monthlyChallenge, name='monthly-challenge'),
]