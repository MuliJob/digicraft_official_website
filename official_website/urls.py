from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemap_dict = {
    'static': StaticViewSitemap(),
}

urlpatterns = [
  path('', views.index, name='index'),
  path('sitemap.xml', sitemap, {'sitemaps': sitemap_dict}, name='django_sitemap'),
  path('services-details', views.service_detail, name='service_detail'),
  path('portfolio-details', views.portfolio_detail, name='portfolio_detail')
]