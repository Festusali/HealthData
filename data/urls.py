from django.urls import path

from data.views import CreateDataView, DataDetailView, DataListView

urlpatterns = [
    path('', DataListView.as_view(), name='home'),
    path('add-data', CreateDataView.as_view(), name='create'),
    path('<int:pk>/data/', DataDetailView.as_view(), name='data-view'),
]