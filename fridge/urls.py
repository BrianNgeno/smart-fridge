from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
    url(r'^$',views.home, name='fridgehome'), 
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^add/(?P<id>\d+)/',views.add_to_cart,name='add'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^remove/(?P<id>\d+)',views.delete_cart,name='delete'),
    url(r'^empty',views.empty,name='empty')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    