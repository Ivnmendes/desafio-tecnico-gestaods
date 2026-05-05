from django.urls import include, path
from rest_framework.routers import DefaultRouter

from estoque.infrastructure.django.containers import Container
from produto.infrastructure.django.viewsets.produto_viewset import ProdutoViewSet

container = Container()

container.wire(modules=["estoque.infrastructure.django.viewsets.item_estoque_viewsets"])


router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet, basename="produto")

urlpatterns = [
    path("", include(router.urls)),
]
