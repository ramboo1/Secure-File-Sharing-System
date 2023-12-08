from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, FileViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet, basename='user-profiles')
router.register(r'files', FileViewSet, basename='files')

urlpatterns = [
    path('user-profiles/signup/', UserProfileViewSet.as_view({'post': 'signup'}), name='signup'),
    path('user-profiles/email-verify/', UserProfileViewSet.as_view({'post': 'email_verify'}), name='email-verify'),
    path('user-profiles/login/', UserProfileViewSet.as_view({'post': 'login'}), name='login'),
    path('files/', FileViewSet.as_view({'post': 'create', 'get': 'list'}), name='file-list'),
    path('files/<int:pk>/', FileViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='file-detail'),
    path('files/<int:pk>/download/', FileViewSet.as_view({'get': 'download'}), name='file-download'),
]