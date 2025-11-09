from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, ChartDataView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("chart-data/", ChartDataView.as_view(), name="chart-data"),
]