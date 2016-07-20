from django.shortcuts import redirect

# from django.contrib.auth.decorators import login_required
from core.shortcuts import render_with_context
# from django.conf import settings
from django.http import JsonResponse
import json

import logging

from django.core.urlresolvers import reverse

# from django.http import (
#     Http404,
#     HttpResponse,
#     HttpResponseRedirect
# )

from core.models import Staff
from core.forms import MailoutSignupForm


def home(request, template_name="core/home.html"):
    staff_staff = Staff.active_objects \
        .filter(involvement=Staff.STAFF_INVOLVEMENT_TYPE_STAFF) \
        .order_by('name')
    staff_freelance = Staff.active_objects \
        .filter(involvement=Staff.STAFF_INVOLVEMENT_TYPE_FREELANCE) \
        .order_by('name')
    staff_foundation = Staff.active_objects \
        .filter(involvement=Staff.STAFF_INVOLVEMENT_TYPE_FOUNDATION) \
        .order_by('name')
    staff_charity = Staff.active_objects \
        .filter(involvement=Staff.STAFF_INVOLVEMENT_TYPE_CHARITY) \
        .order_by('name')
    staff_britdoc_inc = Staff.active_objects \
        .filter(involvement=Staff.STAFF_INVOLVEMENT_TYPE_BRITDOC_INC) \
        .order_by('name')
    staff_consultant = Staff.active_objects \
        .filter(involvement=Staff.STAFF_INVOLVEMENT_TYPE_CONSULTANT) \
        .order_by('name')

    return render_with_context(request, template_name, {
        'staff_staff': staff_staff,
        'staff_freelance': staff_freelance,
        'staff_foundation': staff_foundation,
        'staff_charity': staff_charity,
        'staff_britdoc_inc': staff_britdoc_inc,
        'staff_consultant': staff_consultant,
    })


def mailout_signup(request, template_name="core/mailout_signup.html"):
    logger = logging.getLogger(__name__)
    logger.error("Form view is called for signup")
    logger.info('hello')
    form = MailoutSignupForm(request.POST or None)

    if request.POST and request.is_ajax():
        logger.error("Form is posted and over ajax %s" % (form))
        for field, errors in form.errors.iteritems():
            logger.error('Form error in %s %s' % (field, errors))
        for field in form.fields:
            logger.error('Form data for %s %s' % (field, form.data[field]))

        if form.is_valid():
            logger.error("Allgood - saving form")
            form.save()
            response_data = {}
            response_data['success'] = True
            response_data['message'] = 'Added ok to mailout'
            return JsonResponse(response_data)
        else:
            logger.error("Bad - not saving form - sending error message")
            response_data = {}
            response_data['message'] = 'Errors adding to Mailout'
            response_data['success'] = False
            response_data['data'] = json.dumps(form.errors)
            logging.error(json.dumps(form.errors))
            return JsonResponse(response_data)

    elif request.POST:
        print("Form is posted  %s" % (form))
        for field, errors in form.errors.iteritems():
            logger.error('Form error in %s %s' % (field, errors))
        for field in form.fields:
            logger.error('Form data for %s %s' % (field, form.data[field]))
        if form.is_valid():
            form.save()
            # messages.success(request, "Thanks - signed up")
            return redirect(reverse('home'))
        # else reder as below
    else:
        pass

    return render_with_context(request, template_name, {
        'form': form,
    })


def mailout_preview(request, template_name="core/mailout_preview.html"):
    return render_with_context(request, template_name, {
    })


def contact(request, template_name="core/contact.html"):
    return render_with_context(request, template_name, {
    })


def projects(request, template_name="core/projects.html"):
    return render_with_context(request, template_name, {
    })


def funds(request, template_name="core/funds.html"):
    return render_with_context(request, template_name, {
    })


def berthaconnect(request, template_name="core/bertha-connect.html"):
    return render_with_context(request, template_name, {
    })


def berthajournalism(request, template_name="core/bertha-journalism.html"):
    return render_with_context(request, template_name, {
    })


def britdoccircle(request, template_name="core/britdoc-circle.html"):
    return render_with_context(request, template_name, {
    })


def resources(request, template_name="core/resources.html"):
    return render_with_context(request, template_name, {
    })
