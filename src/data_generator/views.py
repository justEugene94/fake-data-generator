from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.views.generic import ListView, CreateView

from data_generator.forms import SchemaForm, ColumnForm, BaseColumnFormSet
from data_generator.models import Schema


class HomePageView(LoginRequiredMixin, ListView):
    """ Home page """

    login_url = '/login/'

    model = Schema
    context_object_name = 'schemas'
    template_name = 'data_generator/home.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(HomePageView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        """get context data"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.username
        print(self.request.user.username)

        return context


class NewSchemaView(LoginRequiredMixin, CreateView):
    """ Add schema """

    login_url = '/login/'

    model = Schema
    context_object_name = 'schemas'
    template_name = 'data_generator/schema.html'
    form_class = SchemaForm
    # form_class = formset_factory(ColumnForm, BaseColumnFormSet)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        column_form_set = formset_factory(ColumnForm, BaseColumnFormSet)
        if self.request.POST:
            context['form'] = SchemaForm(self.request.POST)
            context['formset'] = column_form_set(self.request.POST)
        else:
            context['form'] = SchemaForm()
            context['formset'] = column_form_set()
            return context
