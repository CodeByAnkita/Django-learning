# Core/Core/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from vege.views import login_user, register_user, receipes, delete_receipe, update_receipe, about, success_page, confirm_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', receipes, name="receipes"),  # Default route points to the recipe page
    path('login/', login_user, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('confirm-logout/', confirm_logout, name="confirm_logout"),
    path('delete-receipe/<int:id>/', delete_receipe, name="delete_receipe"),
    path('update-receipe/<int:id>/', update_receipe, name="update_receipe"),
    path('about/', about, name="about"),
    path('success_page/', success_page, name="success_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

