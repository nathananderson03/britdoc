from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404

import json
from django.core.serializers.json import DateTimeAwareJSONEncoder
from django.http import HttpResponse

def render_with_context(request, template, kwargs):
    """
    Wraps render_to_response() to use context processors with less syntax.

    Just pass in the request object, the template filename and any additional
    objects or values you want the template to have
    """
    return render_to_response(
        template,
        kwargs,
        context_instance=RequestContext(request)
    )


def json_response(request, content_dict, status_code=200):
    """
    Takes a dict of data and returns a NAMEDJSON-monickered HTTPResponse
    Based on JSONEmitter class in django-piston
    """

    _content_type = "application/json; charset=utf-8"
    _mime_type = "application/json"
    cb = request.GET.get('callback')

    seria = simplejson.dumps(
        content_dict,
        cls=DateTimeAwareJSONEncoder,
        ensure_ascii=False,
        indent=4
    )
    if cb:  # callback
        resp = HttpResponse('%s(%s)' % (cb, seria),
                    status=status_code,
                    content_type=_content_type,
                    mimetype=_mime_type)
    else:  # Non-callback
        resp = HttpResponse(
            seria,
            status=status_code,
            content_type=_content_type,
            mimetype=_mime_type
        )
    resp['If-Modified-Since'] = '0'  # stops IE caching GET requests
    resp['Cache-Control'] = 'no-cache'  # stops IE caching GET requests
    return resp


def get_active_object_or_404(model, **kwargs):
    try:
        return model.active_objects.get(**kwargs)
    except (model.DoesNotExist, model.MultipleObjectsReturned):
        raise Http404


def get_retired_object_or_404(model, **kwargs):
    try:
        return model.retired_objects.get(**kwargs)
    except (model.DoesNotExist, model.MultipleObjectsReturned):
        raise Http404
