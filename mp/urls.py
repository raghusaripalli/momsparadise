from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from mp import settings

urlpatterns = [
    url(r'', include("shop.urls")),
    url(r'^cart/', include('cart.urls')),
    url(r'orders/', include('orders.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
