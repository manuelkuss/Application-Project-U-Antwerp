from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, ChartDataView, sequence_title
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("chart-data/", ChartDataView.as_view(), name="chart-data"),
    path("sequence/<int:id>/", sequence_title, name='sequence-title')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)