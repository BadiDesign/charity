from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from charity import settings

handler404 = 'plugins.views.my_custom_page_not_found_view'
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('login/', UserLoginView.as_view(), name='custom_login'),
                  path('change_password/', ChangePasswordForgot.as_view(), name="forgot_password"),
                  path('forgot_password/<str:token_id>/<str:hash_code>', ChangePasswordForgot.as_view(),
                       name="forgot_password"),
                  path('404', my_custom_page_not_found_view, name="404"),
                  path('logout/', UserLogout.as_view(), name='user_logout'),
                  path('api/v1/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
                  path('', IndexView.as_view(), name=''),
                  path('dashboard/user/', include('user.ui.urls')),
                  path('dashboard/setting/', include('setting.ui.urls')),
                  path('dashboard/blog/', include('blog.ui.urls')),
                  path('dashboard/advertisement/', include('advertisement.ui.urls')),
                  path('dashboard/ticket/', include('ticket.urls')),
                  path('dashboard/wallet/', include('wallet.ui.urls')),

                  path('api/v1/', include('user.api.routers')),
                  path('', include('plugins.sitemap_urls')),
                  path('api/v1/', include('ticket.routers')),
                  path('api/v1/', include('setting.api.routers')),
                  path('api/v1/', include('advertisement.api.routers')),
                  path('api/v1/', include('blog.api.routers')),
                  path('api/v1/', include('wallet.api.routers')),
                  path('select2/', include('plugins.select2_urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
