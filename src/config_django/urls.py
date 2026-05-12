from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("produto.infrastructure.django.urls")),
    path("api/", include("estoque.infrastructure.django.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/docs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc")
]
