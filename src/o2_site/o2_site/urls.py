from rest_framework.routers import DefaultRouter
from django.urls.conf import include, path

from backend import views, viewsets


router = DefaultRouter()
router.register('getMap', viewsets.MapViewSet, basename='map')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/changeUsername/', views.ChangeUsernameView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),
    path('api/auth/', views.LoginView.as_view()),
    path('signup/', views.register_user)
]
