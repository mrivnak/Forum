from rest_framework import routers
from .api import UserViewSet, CategoryViewSet, BoardViewSet, PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'forumapp')
router.register('api/category', CategoryViewSet, 'forumapp')
router.register('api/board', BoardViewSet, 'forumapp')
router.register('api/post', PostViewSet, 'forumapp')
router.register('api/comment', CommentViewSet, 'forumapp')

urlpatterns = router.urls