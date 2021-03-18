from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

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
