from django.urls import include, path
from rest_framework.routers import DefaultRouter

from estoque.infrastructure.django.views.item_estoque_viewsets import ItemEstoqueViewSet

router = DefaultRouter()
router.register(r"estoque", ItemEstoqueViewSet, basename="estoque")

urlpatterns = [
    path("", include(router.urls)),
]
