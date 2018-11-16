from django.conf.urls import url

from crashstats.api import views


app_name = 'api'
urlpatterns = [
    url(r'^$', views.documentation, name='documentation'),
    url(r'^CrashVerify/$',
        views.crash_verify,
        name='crash_verify'),
    url(r'^(?P<model_name>\w+)/$',
        views.model_wrapper,
        name='model_wrapper'),
]
