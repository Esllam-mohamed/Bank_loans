from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'mymodels', views.providerViewSet)
router.register(r'mymodels', views.loansViewSet)



urlpatterns = [
    path('', views.login,name='login'),
    path('customer/',include(router.urls)),
    path('provider/',include(router.urls)),
]

