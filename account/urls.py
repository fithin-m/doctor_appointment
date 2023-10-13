from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('log/',lguview.as_view(),name='log'),
    path('reg/',userregview.as_view(),name="regg"),
    path('doc/',doctorview.as_view(),name='docs'),
    path('appo/',Appoimentview.as_view(),name='apppo'),
    path('payment/',paymentview.as_view(),name='pay'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)