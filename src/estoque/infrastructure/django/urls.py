from django.urls import include, path
from rest_framework.routers import DefaultRouter

from estoque.infrastructure.django.containers import Container
from estoque.infrastructure.django.viewsets.item_estoque_viewsets import (
    ItemEstoqueViewSet,
)

container = Container()

container.wire(modules=["estoque.infrastructure.django.viewsets.item_estoque_viewsets"])

router = DefaultRouter()
router.register(r"estoque", ItemEstoqueViewSet, basename="estoque")

urlpatterns = [
    path("", include(router.urls)),
]
