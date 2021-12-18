from django.urls import path
from .views import *

urlpatterns = [
    path('', homeViews, name='home'),
    path('all_news/', allViews, name='all_news'),
    path('category/<slug>', ctgViews, name='category'),
    path('news/<int:pk>', newsViews, name='news'),
    path('search/', searchViews, name='search'),
    path('contact/', contactViews, name='contact'),
    path('<int:pk>', newsViews, name='tg')
]
