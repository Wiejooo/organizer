from django.urls import path

from organizationalAPP import views

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main_page')
]