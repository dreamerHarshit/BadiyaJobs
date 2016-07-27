from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from bj import views
urlpatterns = [
    url(r'^bj/', include('bj.urls',namespace="bj")),
    url(r'^admin/', include(admin.site.urls)),
]
#urlpatterns=format_suffix_patterns(urlpatterns)