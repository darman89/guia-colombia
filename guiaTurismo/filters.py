import django_filters
from guiaTurismo.models import Tour


class TourFilter(django_filters.FilterSet):
    lowest_price = django_filters.Filter(method='search_by_lowest_price')
    highest_price = django_filters.Filter(method='search_by_highest_price')
    idGuia = django_filters.Filter(method='search_by_guide_id')

    class Meta:
        model = Tour
        fields = ['id', 'guide__name', 'guide__facebook',
                  'guide__instagram', 'guide__email']

    def search_by_lowest_price(self, queryset, args, value):

        return queryset.filter(price__gte=value)

    def search_by_highest_price(self, queryset, args, value):
        return queryset.filter(price__lte=value)

    def search_by_guide_id(self, queryset, args, value):
        return queryset.filter(guide__id=value)
