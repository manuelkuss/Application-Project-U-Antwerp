from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, ChartDataView, mgf_file_get_info, MgfFileViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'mgf-files', MgfFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("chart-data/", ChartDataView.as_view(), name="chart-data"),
    # path("sequence/<int:id>/", sequence_get, name='sequence-title'),
    # path("sequence-plotly-data/<int:id>/", sequence_get_plotly_data, name='sequence-plotly-data'),
    path("mgf-file-info/<str:name>", mgf_file_get_info, name='mgf-file-info')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

