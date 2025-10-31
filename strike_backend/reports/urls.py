from rest_framework.routers import DefaultRouter
from .views import StrikeReportViewSet

router = DefaultRouter()
router.register(r"reports", StrikeReportViewSet)

urlpatterns = router.urls
