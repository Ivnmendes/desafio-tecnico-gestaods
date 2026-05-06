from django.urls import include, path
from rest_framework.routers import DefaultRouter

from produto.infrastructure.django.containers import Container
from produto.infrastructure.django.viewsets.produto_viewsets import ProdutoViewSet

container = Container()

container.wire(modules=["produto.infrastructure.django.viewsets.produto_viewsets"])


router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet, basename="produto")

urlpatterns = [
    path("", include(router.urls)),
]
