from django.urls import include, path
from rest_framework.routers import DefaultRouter

from produto.infrastructure.django.viewsets.produto_viewset import ProdutoViewSet

router = DefaultRouter()
router.register(r"produtos", ProdutoViewSet, basename="produto")

urlpatterns = [
    path("", include(router.urls)),
]
