from django.contrib import admin
from django.urls import path, include

from organizationalAPP.views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('notebook/', include('organizationalAPP.urls'))
]
