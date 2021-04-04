from django import forms
from django.forms import NumberInput, modelformset_factory, BaseModelFormSet

from data_generator.models import Column, Schema, Type


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

    name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-main', 'placeholder': 'column name',
               'label': 'Column name'}))
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, empty_label='Choose',
                                  widget=forms.Select(
                                      attrs={'autofocus': True, 'class': 'form-control formset-main type-selector'}))
    range_min = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-secondary input-visibility', 'placeholder': '0'}))
    range_max = forms.IntegerField(required=False, widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control formset-secondary input-visibility', 'placeholder': '0'}))

    class Meta:
        model = Column
        fields = ['name', 'type', 'range_min', 'range_max']


class BaseColumnFormSet(BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Column.objects.none()

    def clean(self):
        """ Adds validation to check that orders don't repeat """

        super(BaseColumnFormSet, self).clean()

        if any(self.errors):
            return

        # todo: Validation
        for form in self.forms:
            if form.cleaned_data.get('type') == Column.objects.get(name='Integer').pk \
                    or \
                    form.cleaned_data.get('type') == Column.objects.get(name='Text').pk:

                range_min = form.cleaned_data.get('range_min', None)
                range_max = form.cleaned_data.get('range_min', None)
                if not range_min:
                    raise forms.ValidationError('Range min is required here!')
                if not range_max:
                    raise forms.ValidationError('Range max is required here!')
        return self.cleaned_data

    def get_ordering_widget(self):
        return NumberInput(attrs={'class': 'form-control formset-secondary'})


ColumnModelFormSet = modelformset_factory(Column, fields=('name', 'type', 'range_min', 'range_max'), form=ColumnForm,
                                          formset=BaseColumnFormSet, min_num=0, can_order=True)
