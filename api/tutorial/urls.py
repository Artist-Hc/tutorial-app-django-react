from rest_framework.routers import DefaultRouter
from .views import TutorialVeiw


router = DefaultRouter()
router.register('tutorials', TutorialVeiw)

urlpatterns = router.urls