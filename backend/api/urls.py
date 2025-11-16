from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, ChartDataView, sequence_get, sequence_get_plotly_data
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("chart-data/", ChartDataView.as_view(), name="chart-data"),
    path("sequence/<int:id>/", sequence_get, name='sequence-title'),
    path("sequence-plotly-data/<int:id>/", sequence_get_plotly_data, name='sequence-plotly-data')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)