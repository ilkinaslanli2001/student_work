

from django.urls import path
from .views import homeView,newsView

urlpatterns = [
    path('', homeView,name='home'),
    path('news/<int:pk>', newsView,name='news_detail'),

]

