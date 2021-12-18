from django.urls import path
from api import views


urlpatterns = [
    path('get-news-list/', views.NewsListView.as_view()),
    path('upd-news/<int:pk>', views.NewsUpdView.as_view()),
    path('get-contact-list/', views.ContactListView.as_view()),
    path('upd-contact/<int:pk>', views.ContactUpdView.as_view()),

]
