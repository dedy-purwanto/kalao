# Create your views here.
from django.views.generic import TemplateView

from .models import Package

class PackageTableView(TemplateView):
    template_name = 'packages/table.html'

    def get_context_data(self, **kwargs):
        context = super(PackageTableView, self).get_context_data(**kwargs)

        pk = self.kwargs['pk']
        pks = self.request.GET.get('pks', None)

        pks = pks.split(',') if pks and len(pks) > 0 else [pk]

        packages = Package.objects.filter(pk__in=pks)

        context['packages'] = packages

        return context


