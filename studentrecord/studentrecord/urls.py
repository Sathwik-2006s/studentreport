from django.contrib import admin
from django.urls import path, include
app_name = "tasks"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('api/v1/', include(('tasks.urls', 'tasks'), namespace='v1')),
]
