from django.urls import path

from organizationalAPP import views

urlpatterns = [
    path("main/", views.MainView.as_view(), name="main_page"),
    path("wardrobe/", views.WardrobeView.as_view(), name="wardrobe"),
    path("wardrobe_table/", views.WardrobeTableView.as_view(), name="wardrobe_table"),
    path("add/", views.AddClothView.as_view(), name="add_cloth"),
    path("add_type/", views.AddTypeView.as_view(), name="add_type"),
    path("<slug:slug>/edit", views.ClothEditView.as_view(), name="edit"),
    path("<slug:slug>/delete", views.ClothDeleteView.as_view(), name="delete"),
    path("<slug:slug>/table", views.ClothDetailTableView.as_view(), name="cloth-detail-table"),
    path("<slug:slug>/", views.ClothDetailView.as_view(), name="cloth-detail"),
]
