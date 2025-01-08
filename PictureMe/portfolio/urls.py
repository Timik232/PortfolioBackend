from django.urls import path

from portfolio.views import element_detail, photoreports, series

app_name = "portfolio"

urlpatterns = [
    path("series/", series, name="series"),
    path("series/<int:element_id>/", element_detail, name="series_element"),
    path("reports/", photoreports, name="reports"),
    path("reports/<int:element_id>/", element_detail, name="reports_element"),
]
