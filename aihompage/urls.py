from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'aihompage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^home/$', include('home.urls', namespace="home")),
    url(r'^admin/', include(admin.site.urls)),

]
