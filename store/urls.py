from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import api,views

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    url(r'^$',views.home_page, name='home'),
    url(r'^order$',views.order, name='order'),
    url(r'^notify$', api.realtime_notify),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)