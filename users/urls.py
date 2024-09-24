
from rest_framework.routers import DefaultRouter
from Blog_Users.users.views import BlogViewSet, CommentViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
