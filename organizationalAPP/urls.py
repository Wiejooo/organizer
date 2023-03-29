from django.urls import path

from organizationalAPP import views

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main_page'),
    path('wardrobe/', views.WardrobeView.as_view(), name='wardrobe'),
    path('add/', views.AddClothView.as_view(), name='add')
]