from django.contrib import admin
from django.urls import path, include
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
]
