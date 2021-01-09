from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addfriend', views.addfriend, name='addfriend'),
    path('friend_detail/<int:pk>', views.FriendDetailView.as_view(), name='friend_detail'),
    path('friend_update/<int:pk>', views.friend_update, name='friend_update'),
    path('remove_friend/<int:pk>', views.remove_friend, name='delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)