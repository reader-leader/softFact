from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_request/', views.logout_request, name="logout"),
    path('register_user/', views.register_user, name='register'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('contact_us/', views.contact_us, name='contact')
]
