from django.urls import path, include

from rest_framework import routers

from . import views
from . import viewset

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'users', viewset.UserViewSet)
router.register(r'provinces', viewset.ProvinceViewSet, base_name='provinces-list')
router.register(r'province-data', viewset.ProvinceDataViewSet, base_name='provinces-data')
router.register(r'districts', viewset.DistrictViewSet, base_name='provinces-district-list')
router.register(r'districts-spending', viewset.DistrictSpendingViewSet, base_name='district-spending')
router.register(r'programmes', viewset.ProgramViewSet, base_name='programmes-list')
router.register(r'indicators', viewset.IndicatorViewSet, base_name='indicators-list')
router.register(r'indicator-data', viewset.IndicatorDataViewSet, base_name='indicator-data-list')
router.register(r'sectors', viewset.SectorViewSet, base_name='sectors-list')
router.register(r'province-info', viewset.ProvinceInfoViewSet, base_name='province-info-list')
router.register(r'programme-data', viewset.ProgramDataViewSet, base_name='program-data-list')
router.register(r'country-data', viewset.CountryDataViewSet, base_name='country-data-list')
router.register(r'layer-data', viewset.LayerDataViewSet, base_name='layer')
router.register(r'dataset', viewset.DatasetViewSet, base_name='dataset')
router.register(r'partners', viewset.PartnerViewSet, base_name='partner-list')
router.register(r'municipalities', viewset.AreaViewSet, base_name='municipalities')
router.register(r'glossary-data', viewset.GlossaryDataViewSet, base_name='glossary-data')
router.register(r'explore', viewset.PdfViewSet, base_name='explore')
router.register(r'poverty-literacy', viewset.PovertyViewSet, base_name='poverty')
# router.register(r'program-spend-allocation', viewset.ProgramSpendAllocationViewSet, base_name='program-spend')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.token),
    # path('geojson/country/', views.country_geojson),
    # path('geojson/municipalities/', views.municipalities_geojson),
    # path('geojson/ipssj/', views.ipssj_geojson),
    # path('geojson/province/<province_id>/', views.province_geojson),
    path('about/', viewset.AboutViewSet.as_view({'get': 'list'})),
    path('layer-data-file/<int:pk>/', views.LayerDatafileView.as_view()),
    path('municipality-update/<int:pk>/', views.AreaUpdateView.as_view()),
    path('municipality-list/', views.AreaListView.as_view(), name="area_list"),
    path('pdf-create/', views.PdfFormView.as_view(), name="pdf_form"),
    path('pdf-list/', views.PdfListView.as_view(), name="pdf_list"),
    path('partner-update/<int:pk>/', views.PartnerUpdateView.as_view()),
    path('partner-list/', views.PartnerListView.as_view(), name="partner_list"),

]