from django.urls import path

from organizationalAPP import views

urlpatterns = [
    path("main/", views.MainView.as_view(), name="main_page"),
    path("wardrobe/", views.WardrobeView.as_view(), name="wardrobe"),
    path("add/", views.AddClothView.as_view(), name="add_cloth"),
    path("add_type/", views.AddTypeView.as_view(), name="add_type"),
    path("<slug:slug>/edit", views.ClothEditView.as_view(), name="edit"),
    path("<slug:slug>/delete", views.ClothDeleteView.as_view(), name="delete"),
    path("<slug:slug>/", views.ClothDetailView.as_view(), name="cloth-detail"),
]
