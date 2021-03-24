from django import forms
from django.forms import BaseFormSet

from data_generator.models import Column, Schema


class SchemaForm(forms.ModelForm):
    """ Form for schema """

    ColumnSeparator = [
        (',', 'Comma (,)'),
        (':', 'Colon (:)'),
        ('-', 'Dash (-)'),
        (';', 'Semicolon (;)'),
        ('?', 'Question Mark (?)'),
    ]

    CharacterString = [
        ("'", "Single quote (')"),
        ('"', 'Double quote (")'),
    ]

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control w-50', 'placeholder': 'Name'}))
    column_separator = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control w-50'}),
                                         choices=ColumnSeparator)
    character_string = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control w-50'}),
                                         choices=CharacterString)

    class Meta:
        model = Schema
        fields = ['name', 'column_separator', 'character_string']


class ColumnForm(forms.ModelForm):
    """ Form for columns """

    Type = [
        ('FN', 'Full name'),
        ('J', 'Job'),
        ('E', 'Email'),
        ('DN', 'Domain name'),
        ('PN', 'Phone number'),
        ('T', 'Text'),
        ('I', 'Integer'),
        ('A', 'Address'),
        ('D', 'Data'),
    ]

    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-main', 'placeholder': 'column name', 'label': 'Column name'}))
    type = forms.ChoiceField(required=False, choices=Type, widget=forms.Select(
        attrs={'autofocus': True, 'class': 'form-control formset-main', 'placeholder': 'type'}))
    range_min = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-secondary', 'placeholder': '0'}))
    range_max = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-secondary', 'placeholder': '0'}))
    order = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-main', 'placeholder': 'order'}))

    class Meta:
        model = Column
        fields = ['name', 'type', 'range_min', 'range_max', 'order']


class BaseColumnFormSet(BaseFormSet):
    def clean(self):
        """ Adds validation to check that orders don't repeat """

        if any(self.errors):
            return

        orders = []
        repeat = False

        for form in self.forms:
            if form.cleaned_data:
                order = form.cleaned_data['order']
                if order in orders:
                    repeat = True

                orders.append(order)

        if repeat:
            raise forms.ValidationError('Order is repeated')
