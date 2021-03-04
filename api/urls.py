from django.urls import path
from .views import ApiOverview, CreateView

urlpatterns = [
    path("", ApiOverview.as_view()),
    path('create/', CreateView.as_view())
]
