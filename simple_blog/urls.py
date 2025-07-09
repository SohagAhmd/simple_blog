from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    #webaplication endpoint
    path('students/', include('students.urls')),
    
    
    # API endpoint
    path('api/v1/', include('api.urls')),
]
