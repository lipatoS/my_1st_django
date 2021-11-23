from django.urls import path
from currency.views import RegCreateViews
from currency.views import RegReadViews
from currency.views import RegUpdateViews
from currency.views import RegDeleteViews
from currency.views import RegDetailsViews


urlpatterns = [
    path('r_create/', RegCreateViews.as_view(), name="reg-create"),
    path('r_read/', RegReadViews.as_view(), name="reg-read"),
    path('r_read/update/<int:pk>', RegUpdateViews.as_view(), name="reg-update"),
    path('r_read/delete/<int:pk>', RegDeleteViews.as_view(), name="reg-delete"),
    path('r_read/details/<int:pk>', RegDetailsViews.as_view(), name="reg-info"),
]
