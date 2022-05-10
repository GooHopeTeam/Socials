from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from dialogs.views import DialogsViewSet, MessageViewSet
from content.views import IllustrationViewSet, VideoViewSet, NewsViewSet, ReviewViewSet
from society.views import ProfileViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'dialogs', DialogsViewSet, basename='dialogs')
router.register(r'dialogs/(?P<dialog_id>.*)/messages', MessageViewSet, basename='messages')
router.register(r'illustration', IllustrationViewSet, basename='illustrations')
router.register(r'video', VideoViewSet, basename='video')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
