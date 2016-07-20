from django.forms import ModelForm

from core.models import MailoutSignup

from django import forms
import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *


class MailoutSignupForm(ModelForm):
    class Meta:
        model = MailoutSignup
        fields = [
            'email',
            'job_title',
            'region',
            'first_name',
            'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super(MailoutSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_class = 'form-horizontal'
        # self.helper.form_id = 'mailout_signup_form'
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'POST'
        self.helper.form_action = '/mailout_signup/'
        self.helper.layout = Layout(
            Field('email',),
            Field('job_title',),
            Field('region',),
            Field('first_name',),
            Field('last_name'),
            FormActions(Submit('submit', "Submit", css_class='btn'))
        )
        self.fields['email'].required = True
        self.fields['job_title'].required = True
        self.fields['region'].required = True

    # def save(self, commit=True):
    #     inst = super(FilmForm, self).save(commit=False)
    #     inst.user = self._user
    #     if commit:
    #         inst.save()
    #         self.save_m2m()
    #     return inst
