from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings

class StaticViewSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.5

    def items(self):
        return ['index', 'service_detail', 'portfolio_detail']

    def location(self, item):
        return f"{settings.PRODUCTION_URL}{reverse(item)}"