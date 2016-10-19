from django.conf.urls import url
from .views import GitLabHookView

app_name = 'discord'

urlpatterns = [
    url(r'^$', GitLabHookView.as_view()),
]
