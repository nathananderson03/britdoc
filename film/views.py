# from django.shortcuts import render

from core.shortcuts import get_active_object_or_404
# from django.contrib.auth.decorators import login_required
from core.shortcuts import render_with_context
# from django.conf import settings

# import logging
import string

from core.models import (
    Film,
    Fund,
    Subject,
)

# from django.core.urlresolvers import reverse

from django.http import (
    Http404,
    # HttpResponse,
    # HttpResponseRedirect
)


def index(request, template_name="film/index.html"):
    funds = Fund.active_objects.all()
    subjects = Subject.active_objects.all()
    year_list = Film.years_with_films()
    alpha_list = [i[0] for i in string.ascii_uppercase]

    films = Film.active_objects.filter(featured=True)

    return render_with_context(request, template_name, {
        'films': films,
        'funds': funds,
        'year_list': year_list,
        'alpha_list': alpha_list,
        'subjects': subjects,
    })


def fund(request, slug, template_name="film/fund.html"):
    subjects = Subject.active_objects.all()
    funds = Fund.active_objects.all()
    year_list = Film.years_with_films()
    alpha_list = [i[0] for i in string.ascii_uppercase]

    fund = get_active_object_or_404(Fund, slug=slug)
    films = Film.active_objects.filter(funds=fund)

    return render_with_context(request, template_name, {
        'films': films,
        'fund': fund,
        'funds': funds,
        'year_list': year_list,
        'alpha_list': alpha_list,
        'subjects': subjects,
    })


def year(request, year, template_name="film/year.html"):
    subjects = Subject.active_objects.all()
    funds = Fund.active_objects.all()
    year_list = Film.years_with_films()
    alpha_list = [i[0] for i in string.ascii_uppercase]

    films = Film.active_objects.filter(year=year)

    return render_with_context(request, template_name, {
        'films': films,
        'year': year,
        'funds': funds,
        'year_list': year_list,
        'alpha_list': alpha_list,
        'subjects': subjects,
    })


def alpha(request, alpha, template_name="film/alpha.html"):
    subjects = Subject.active_objects.all()
    funds = Fund.active_objects.all()
    year_list = Film.years_with_films()
    alpha_list = [i[0] for i in string.ascii_uppercase]

    if alpha in string.ascii_uppercase:
        films = Film.active_objects.filter(name__istartswith=alpha)
    else:
        raise Http404

    return render_with_context(request, template_name, {
        'films': films,
        'alpha': alpha,
        'funds': funds,
        'year_list': year_list,
        'alpha_list': alpha_list,
        'subjects': subjects,
    })


def subject(request, slug, template_name="film/subject.html"):
    subjects = Subject.active_objects.all()
    funds = Fund.active_objects.all()
    year_list = Film.years_with_films()
    alpha_list = [i[0] for i in string.ascii_uppercase]

    subject = get_active_object_or_404(Subject, slug=slug)
    films = Film.active_objects.filter(subjects=subject)

    return render_with_context(request, template_name, {
        'films': films,
        'alpha': alpha,
        'funds': funds,
        'year_list': year_list,
        'alpha_list': alpha_list,
        'subjects': subjects,
        'subject': subject,
    })


def display(request, slug, template_name="film/display.html"):
    subjects = Subject.active_objects.all()
    funds = Fund.active_objects.all()
    year_list = Film.years_with_films()
    alpha_list = [i[0] for i in string.ascii_uppercase]

    film = get_active_object_or_404(Film, slug=slug)
    return render_with_context(request, template_name, {
        'film': film,
        'funds': funds,
        'year_list': year_list,
        'alpha_list': alpha_list,
        'subjects': subjects,
    })
