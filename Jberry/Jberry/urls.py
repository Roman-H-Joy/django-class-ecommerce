from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app1.urls')),
    path('user/', include('authentication.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cartApp.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
