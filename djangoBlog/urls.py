# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from djangoBlog.settings import MEDIA_ROOT, MEDIA_URL
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import Settings, settings
from articles.views import articles_list


app_name = "main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('', articles_list),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
