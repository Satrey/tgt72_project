from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import login_user, logout_user, main, CustomUserListView, UserDetailView

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('main/', main, name='main'),
    path('user_list/', CustomUserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
