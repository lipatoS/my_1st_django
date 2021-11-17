from django.contrib import admin
from django.urls import path
from currency.views import index
from currency.views import hello_world
from currency.views import r_create
from currency.views import r_read
from currency.views import r_update
from currency.views import r_details
from currency.views import r_delete
from currency.views import random_logins
from currency.views import clear_regs

import debug_toolbar
from django.urls import include, path

urlpatterns = [
    path('', index),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('r_create/', r_create),
    path('r_read/', r_read),
    path('r_update/', r_update),
    path('r_read/details/<int:reg_id>', r_details),
    path('r_read/update/<int:reg_id>', r_update),
    path('r_read/delete/<int:reg_id>', r_delete),
    path('logins_gen/', random_logins),
    path('delete_base/', clear_regs),
]
