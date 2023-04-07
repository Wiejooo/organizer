from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from organizationalAPP.views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('notebook/', include('organizationalAPP.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
