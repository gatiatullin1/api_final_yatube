from rest_framework import routers

from django.urls import include, path

from .views import (PostViewSet, GroupViewSet,
                    CommentViewSet, FollowViewSet)

router = routers.DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'follow', FollowViewSet,
                basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
