from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', registerAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('1recommender/', FirstRecommenderView.as_view()),
    path('2recommender/', SecondRecommenderView.as_view()),
]