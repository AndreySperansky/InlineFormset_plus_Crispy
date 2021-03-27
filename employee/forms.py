from django import forms
from .models import Collection, CollectionTitle
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, Row, HTML, ButtonHolder, Submit
from .custom_layout_object import Formset

import re


class CollectionTitleForm(forms.ModelForm):

    class Meta:
        model = CollectionTitle
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        print(kwargs.get('prefix', ''))
        # has_titles - 0


        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))
        # отбрасываем цифровую часть у префикса вместе с "-"  было  has_titles-1   стало has_titles
        print(formtag_prefix)
        # has_titles


        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Row(
                Field('name', css_class='col-md-11'),
                Field('language', css_class='col-md-12'),
                # Field('DELETE'),
                css_class='formset_row-{}'.format(formtag_prefix)
            )
        )


CollectionTitleFormSet = inlineformset_factory(
    Collection, CollectionTitle, form=CollectionTitleForm,
    fields=['name', 'language'], extra=1, can_delete=True
)


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        exclude = ['created_by', ]

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.disable_csrf = False
        self.helper.form_class = 'form-horizontal '
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('subject'),
                Field('owner'),
                Fieldset('Add titles',
                         Formset('title')),
                Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
            )
        )