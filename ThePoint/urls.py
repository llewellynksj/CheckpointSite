from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('blog/', include('blogPoint.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

