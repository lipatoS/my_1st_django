from django.contrib import admin
from django.urls import path
from currency.views import index
from currency.views import hello_world
from currency.views import r_create
from currency.views import r_read
from currency.views import r_update
from currency.views import r_details
from currency.views import r_delete

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('r_create/', r_create),
    path('r_read/', r_read),
    path('r_update/', r_update),
    path('r_read/details/<int:reg_id>', r_details),
    path('r_read/update/<int:reg_id>', r_update),
    path('r_read/delete/<int:reg_id>', r_delete),
]
