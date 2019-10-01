from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from workforceapi.models import *
from workforceapi.views import register_user, login_user
from workforceapi.views import Employees, Departments

# pylint: disable=invalid-name
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'departments', Departments, 'department')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth', obtain_auth_token),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
