from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = []


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('user/', include('users.urls', namespace='user')),
    path('form/', include('offers_problems.urls', namespace='offers_problems')),
    path('', include('team_faq.urls', namespace='index'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

