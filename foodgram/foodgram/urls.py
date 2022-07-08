
from django.contrib import admin
from django.urls import include, path
from users.views import get_jwt_token


urlpatterns = [
    path('api/', include('recipes.urls', namespace='recipes')),
    path('api/', include('users.urls', namespace='users')), 
    path('api/auth/token/', get_jwt_token, name='get_jwt_token'),),
    path('admin/', admin.site.urls),
]