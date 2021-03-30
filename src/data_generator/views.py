from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView

from data_generator.forms import SchemaForm, ColumnModelFormSet
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = SchemaForm()
        context['formset'] = ColumnModelFormSet()

        return context

    def post(self, request, *args, **kwargs):
        schema_form = SchemaForm(self.request.POST)
        column_model_formset = ColumnModelFormSet(self.request.POST)

        if schema_form.is_valid() and column_model_formset.is_valid():
            return self.form_valid(schema_form, column_model_formset)

    def form_valid(self, schema_form, column_model_formset):
        """ Saving models """

        schema = schema_form.save(commit=False)
        schema.user = self.request.user
        schema.save()

        instances = column_model_formset.save(commit=False)
        for instance in instances:
            instance.schema = schema
            instance.save()
        return HttpResponseRedirect('/')