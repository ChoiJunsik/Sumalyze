from django.urls import path
from . import views

app_name = 'text'

urlpatterns = [
    path('',views.index, name='index'),
    # path('<int:pk>/',views.post_detail, name='post_detail'),
    # path('new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    # path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
