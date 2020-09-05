from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from data.models import Data
from data.forms import DataForm


class DataListView(ListView):
    """Return list of data in the database."""

    model = Data
    template_name = 'data/data_list.html'
    context_object_name = 'data_list'


class CreateDataView(CreateView):
    """Create and save data."""

    model = Data
    form_class = DataForm
    # template_name = "data/create"


class DataDetailView(DetailView):
    """For displaying individual data."""

    model = Data
    template_name = 'data/data_detail.html'
    context_object_name = 'data'
