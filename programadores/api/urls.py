from rest_framework.routers import DefaultRouter
from programadores.api.views import ProgrammerViewSet

router = DefaultRouter()
router.register('Programadores', ProgrammerViewSet, basename='programadores')

urlpatterns = router.urls

