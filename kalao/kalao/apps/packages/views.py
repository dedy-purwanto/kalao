# Create your views here.
from django.views.generic import TemplateView

from .models import Package

class PackageTableView(TemplateView):
    template_name = 'packages/table.html'

    def get_context_data(self, **kwargs):
        context = super(PackageTableView, self).get_context_data(**kwargs)

        package = Package.objects.get(pk=self.kwargs['pk'])

        context['package'] = package

        return context


