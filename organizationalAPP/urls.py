from django.urls import path

from organizationalAPP import views

urlpatterns = [
    path("main/", views.MainView.as_view(), name="main_page"),
    path("wardrobe/", views.WardrobeView.as_view(), name="wardrobe"),
    path("wardrobe_table/", views.WardrobeTableView.as_view(), name="wardrobe_table"),
    path("add/", views.AddClothView.as_view(), name="add_cloth"),
    path("add_type/", views.AddTypeView.as_view(), name="add_type"),
    path("add_sub_type/", views.AddSubTypeView.as_view(), name="add_sub_type"),
    path("add_measurements/", views.AddMeasurementsView.as_view(), name="add_measurements"),
    path("type_list/", views.TypeListView.as_view(), name="type_list"),
    path("<slug:slug>/type_detail/", views.TypeDetailView.as_view(), name="type_detail"),
    path("<slug:slug>/edit", views.ClothEditView.as_view(), name="edit"),
    path("<slug:slug>/delete", views.ClothDeleteView.as_view(), name="delete"),
    path("<slug:slug>/", views.ClothDetailView.as_view(), name="cloth-detail"),
]
