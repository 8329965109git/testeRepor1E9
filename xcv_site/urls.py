from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.contrib.auth import views as auth
from .sitemaps import StaticViewSitemap
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Sitemap
sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns += [
    path('sitemap/', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap_xml'),
]
from .views import HomeView, ApplyView
urlpatterns += [
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('apply/', ApplyView.as_view(), name='apply'),
]

urlpatterns += [
     path('cars/', include('cars.urls')),
]