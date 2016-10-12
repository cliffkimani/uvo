from django.conf.urls import url, include
import users


urlpatterns = [
    url(r'^$', users.views.index_view),
]
