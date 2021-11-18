import debug_toolbar
from django.urls import include, path
from django.contrib import admin
from currency.views import RegIndexViews
from currency.views import RegCreateViews
from currency.views import RegReadViews
from currency.views import RegUpdateViews
from currency.views import RegDeleteViews
from currency.views import RegDetailsViews
from currency.views import RandomLoginsViews
from currency.views import ClearRegsViews


urlpatterns = [
    path('', RegIndexViews.as_view()),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('r_create/', RegCreateViews.as_view()),
    path('r_read/', RegReadViews.as_view()),
    path('r_read/update/<int:pk>', RegUpdateViews.as_view()),
    path('r_read/delete/<int:pk>', RegDeleteViews.as_view()),
    path('r_read/details/<int:pk>', RegDetailsViews.as_view()),
    path('logins_gen/', RandomLoginsViews.as_view()),
    path('delete_base/', ClearRegsViews.as_view()),
]
