from django.db.models import Sum, Count, Prefetch
from django.db.models.functions import Coalesce
from django.views.generic import ListView

from mailer.models import Company, Contact


class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100

    def get_queryset(self):
        prefetched_contacts = Prefetch(
            'contacts',
            queryset=Contact.objects.prefetch_related('orders').annotate(
                get_order_count=Coalesce(Count('orders__id'), 0)))

        return Company.objects.prefetch_related(prefetched_contacts).annotate(
            get_order_count=Coalesce(Count('orders__id'), 0),
            get_order_sum=Coalesce(Sum('orders__total'), 0)).all()
