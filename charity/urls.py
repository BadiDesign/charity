from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from charity import settings

# handler404 = 'plugins.views.my_custom_page_not_found_view'
from charity.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('dashboard/', include('badi_user.ui.urls')),
                  path('dashboard/', include('badi_ticket.urls')),
                  path('dashboard/wallet/', include('badi_wallet.ui.urls')),
                  path('api/v1/', include('badi_user.api.routers')),
                  path('api/v1/', include('badi_wallet.api.routers')),
                  path('api/v1/', include('badi_ticket.routers')),
                  path('dashboard', DashboardView.as_view(), name='dashboard'),
                  # path('select2/', include('plugins.select2_urls')),
                  # path('', include('plugins.sitemap_urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
