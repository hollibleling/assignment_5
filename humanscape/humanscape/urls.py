from django.urls import path
from rest_framework.routers import DefaultRouter
from api.develope.views import ResearchInformationViewset

route = DefaultRouter(trailing_slash=False)
route.register('list', ResearchInformationViewset, basename='list')
route.register('trials', ResearchInformationViewset, basename='trials')
urlpatterns = route.urls