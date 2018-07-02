from django.conf.urls import url
from . import views


# app_name='supplierList'
urlpatterns = [
    url(r'^processOrder/$', views.processOrder, name='processOrder'),
    url(r'^viewFinishedOrder/$', views.viewFinishedOrder, name='viewFinishedOrder'),
    # url(r'^info/([0-9]+)/$', views.info, name='info'),
    url(r'^processInvoice/$', views.processInvoice, name='processInvoice'),
    url(r'^updateOrder/$', views.updateOrder, name='updateOrder'),
    url(r'^updateInvoice/$', views.updateInvoice, name='updateInvoice'),
    url(r'^finishedInvoice/$', views.finishedInvoice, name='finishedInvoice'),
    # url(r'^infoOptional/([0-9]+)/$', views.infoOptional, name='infoOptional'),
    url(r'^receiveExcelOrder/$', views.receiveExcelOrder, name='receiveExcelOrder'),
    url(r'^receiveExcelInvoice/$', views.receiveExcelInvoice, name='receiveExcelInvoice'),
    url(r'^queryDelivery/$', views.queryDelivery, name='queryDelivery'),
    url(r'^queryOrder/$', views.queryOrder, name='queryOrder'),
    #url(r'^log_test/$', views.log_test, name='log_test'),

    url(r'^all/$', views.queryAll, name='queryAll'),
    url(r'^all2/$', views.queryAll2, name='queryAll2'),
]
