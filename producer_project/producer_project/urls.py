from django.contrib import admin
from django.urls import path, include

# URL patterns for the entire Django project
urlpatterns = [
    # Admin site URL pattern
    path('admin/', admin.site.urls),

    # Include URL patterns from the 'producer_app' app under the 'api/' 
    path('api/', include('producer_app.urls')),  
]
