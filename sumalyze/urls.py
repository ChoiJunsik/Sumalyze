from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    # path('result/', views.result, name='result'),
    path('video/', include('video.urls', namespace='video')),
    path('audio/', include('audio.urls', namespace='audio')),
    path('pdf/', include('pdf.urls', namespace='pdf')),
    # path('image/', include('image.urls', namespace='image')),
    # path('text/', include('text.urls', namespace='text')),
    # path('storage/', include('storage.urls', namespace='storage')),
    path('accounts/', include('django.contrib.auth.urls')), # new
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

