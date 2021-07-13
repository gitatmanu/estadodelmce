from django.views.generic import TemplateView
from estadodelmce.models import CommunistParty

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = CommunistParty.objects.all()
        return context

class CommunistPartiesView(TemplateView):
    template_name = "communistparty_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = CommunistParty.objects.all()
	contexto = 'jajaj'
	return contexto
