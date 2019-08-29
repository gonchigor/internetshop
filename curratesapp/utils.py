from django.views.generic.base import ContextMixin
from .functions import get_curr_rate


class RateContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usd_rate'] = get_curr_rate()
        return context
