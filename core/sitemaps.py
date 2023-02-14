from django.contrib import sitemaps
from django.urls import reverse
from core.models import Services, Blog


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return ['home', 'contact', 'about', 'privacy']

    def location(self, item):
        return reverse(item)


class ServiceSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Services.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at