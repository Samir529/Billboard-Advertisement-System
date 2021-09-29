from urllib import request

import django_filters

from django import forms
from spyder.config import user

from .models import PostAdvertiseTable, CurrentPriceUpdate


class billboardFilter(django_filters.FilterSet):
    location = django_filters.AllValuesFilter(label='• Billboard Location',
                                              widget=forms.Select(
                                                  attrs={'style': 'width:210px'}))
    size = django_filters.RangeFilter(label='• Billboard Size (in square feet)',
                                      widget=django_filters.widgets.RangeWidget(
                                          attrs={'placeholder': ' 0', 'style': 'width:250px'}))
    price = django_filters.RangeFilter(label='• Billboard Price Range',
                                       widget=django_filters.widgets.RangeWidget(
                                           attrs={'placeholder': ' 0', 'style': 'width:250px'}))
    # author = django_filters.AllValuesFilter(field_name='author__username', lookup_expr='iexact')

    author = django_filters.CharFilter(field_name='author__username', lookup_expr='iexact',
                                       label='• Advertiser Username',
                                       widget=forms.TextInput(attrs={'placeholder': ' enter username', 'style': 'width:250px'}))

    class Meta:
        model = PostAdvertiseTable
        fields = ['size', 'price', 'location']



# class viewCurPriceByLoc(django_filters.FilterSet):
#     location = django_filters.AllValuesFilter(label='Location')
#
#     class Meta:
#         model = CurrentPriceUpdate
#         fields = ['location']



















