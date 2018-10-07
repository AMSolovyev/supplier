from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.suppliers_table, name='suppliers_table'),
]