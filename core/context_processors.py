# for building the form on every page we need to do this in a context processor
from core.forms import MailoutSignupForm


def mailout_signup_form(request):
    return {
        'mailout_signup_form': MailoutSignupForm(),
    }
