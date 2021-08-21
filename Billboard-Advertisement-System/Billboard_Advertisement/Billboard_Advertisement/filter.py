import django_filters

from django import forms
from .models import PostAdvertiseTable, CurrentPriceUpdate


class billboardFilter(django_filters.FilterSet):
    location = django_filters.AllValuesFilter(label='Search by Location')
    size = django_filters.RangeFilter(label='Billboard Size ( in square feet )',
                                      widget=django_filters.widgets.RangeWidget(attrs={'placeholder': '0'}))
    class Meta:
        model = PostAdvertiseTable
        fields = ['size', 'location']


# class viewCurPriceByLoc(django_filters.FilterSet):
#     location = django_filters.AllValuesFilter(label='Location')
#
#     class Meta:
#         model = CurrentPriceUpdate
#         fields = ['location']









