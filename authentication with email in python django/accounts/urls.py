from django.urls import path, include
from . import views

from accounts.admin import CustomAdminSite  # Import the CustomAdminSite from your app

# admin.site = CustomAdminSite()  # Set the custom admin site
# admin.autodiscover()

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.logout_view, name='logout')
    # path('accounts/', include('accounts.urls')),
]