from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register(r'api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    *router.urls
]
