from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),

    # URLs for user registration, login, logout (our accounts app)
    path('accounts/', include('accounts.urls')),

    # URLs for homepage, video upload, listing, etc. (videos app)
    path('', include('videos.urls')),

    # Django's built-in authentication URLs
    # (login/, logout/, password_reset/, etc.)
    path('', include('django.contrib.auth.urls')),
]

# Serve uploaded media files (videos) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
