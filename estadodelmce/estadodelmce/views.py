from django.views.generic import TemplateView
from estadodelmce.models import CommunistParty

class CommunistPartyView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = CommunistParty.objects.all()
        return context
