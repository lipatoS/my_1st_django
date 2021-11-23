import debug_toolbar
from django.urls import include, path
from django.contrib import admin
from currency.views import RegIndexViews
from currency.views import RandomLoginsViews
from currency.views import ClearRegsViews

urlpatterns = [
    path('', RegIndexViews.as_view(),name="reg-home"),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('regs/',include("currency.urls")),
    path('logins_gen/', RandomLoginsViews.as_view(), name="log-gen"),
    path('delete_base/', ClearRegsViews.as_view(), name="del-base-reg"),
]
