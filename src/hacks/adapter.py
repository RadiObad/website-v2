
import os

from allauth.account.adapter import DefaultAccountAdapter

from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.conf import settings


class MyAccountAdapter(DefaultAccountAdapter):

    def respond_email_verification_sent(self, request, user):
        return HttpResponseRedirect('')

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = "/confirm-account/{}".format(emailconfirmation.key)
        return os.environ.get('SPA_BASE_URL') + url
