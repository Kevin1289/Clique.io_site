from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat import views
from Notifications import views as views_notif


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorize_main.urls')),
    path('posts/', include('posts_app.urls')),
    path('notifications/', include('Notifications.urls')),
    path('chat/', include('chat.urls')),
    path('friends/', include('friends.urls')),
    #debug
    #path('debug/delete_chat_model/', views.clear_all_chats, name='clearchat'),
    #path('debug/delete_user_keys/', views.clear_user_keys, name='clearkeys'),
    #path('debug/delete_all_notifications/', views_notif.delete_all_notifications, name='clearnotifications'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)