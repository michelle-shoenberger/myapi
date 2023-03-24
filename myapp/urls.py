from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.contrib import admin

router = DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='drink')
router.register(r'food', FoodViewSet, basename='food')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
urlpatterns += [
    path('signup/', sign_up),
    path('login/', log_in),
    path('logout/', log_out),
    # path('api-token-auth/', UserAuthToken.as_view()),
    path('whoami/', who_am_i),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 


# re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)