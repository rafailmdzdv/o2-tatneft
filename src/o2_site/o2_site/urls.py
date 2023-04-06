from rest_framework.routers import DefaultRouter
from django.urls.conf import include, path

from backend import views, viewsets


router = DefaultRouter()
router.register('getMap', viewsets.MapViewSet, basename='map')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/changeUsername/', views.ChangeUsernameView.as_view()),
    path('api/changeEmail/', views.ChangeEmailView.as_view()),
    path('api/changePassword/', views.ChangePasswordView.as_view()),
    path('changePasswordConfirm/', views.ChangePasswordConfirmView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),
    path('api/auth/', views.SigninView.as_view()),
    path('api/getAzsXls/', views.AzsListView.as_view()),
    path('signup/', views.signup_user)
]
