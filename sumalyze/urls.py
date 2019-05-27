from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('video/', include('video.urls', namespace='video')),
    path('audio/', include('audio.urls', namespace='audio')),
    path('pdf/', include('pdf.urls', namespace='pdf')),
    # path('image/', include('image.urls', namespace='image')),
    path('text/', include('text.urls', namespace='text')),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('storage/', views.storage, name='storage'),
    path('result/pdf/<int:pk>/', views.pdfResult, name='pdfResult'),
    path('result/video/<int:pk>/', views.videoResult, name='videoResult'),
    path('result/audio/<int:pk>/', views.audioResult, name='audioResult'),
    path('result/text/<int:pk>/', views.textResult, name='textResult'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

