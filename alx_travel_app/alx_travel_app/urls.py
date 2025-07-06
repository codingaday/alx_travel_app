from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', include('alx_travel_app.listings.urls')),
]
