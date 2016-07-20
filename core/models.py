# -*- coding: utf-8 -*-
from __future__ import division
from django.db import models

# Create your models here.


# from annoying.fields import AutoOneToOneField
from django_countries.fields import CountryField
# from django.core.urlresolvers import reverse

from django.db.models import Q

import datetime
# import logging

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# from django.conf import settings

from redactor.fields import RedactorField

from core import constants

# import hmac
# import time
# import base64
# import urllib
# import hashlib

# from taggit.managers import TaggableManager


class Http403(Exception):
    """ Custom error used to force Django to display 403.html as the error page
        if `raise Http403` is called in a view.
    """
    def __init__(self, message="User attempt to access entity foiled."):
        self.message = message


# Base classes, all abstract
class TimestampedBase(models.Model):
    """
    Timestamping features in an abstract class, for inheritance

    ALSO: we want to track the creating and last editing User, but because
    this is an abstract class, the FK relation won't work. Instead, we're
    denorming the relevant user ID and providing a convenient accessor
    which should work across all subclassing models.

    So, whenever saving a TimestampBased model, pass in the active user
    object as a kwarg to save(), eg:

    foo.save(user=request.user)

    """
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    creator_id = models.IntegerField(blank=True, null=True, editable=False)
    last_editor_id = models.IntegerField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True

    def _get_creator_or_editor(self, _id):
        try:
            return User.objects.get(id=_id)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    @property
    def creator(self):
        return self._get_creator_or_editor(self.creator_id)

    @property
    def last_editor(self):
        return self._get_creator_or_editor(self.last_editor_id)

    def save(self, *args, **kwargs):
        "Captures the acting user, via 'user' keyword argument"
        user = kwargs.pop('user', None)
        if user:
            self.last_editor_id = user.id
        if user and not self.creator_id:
            self.creator_id = user.id
        return super(TimestampedBase, self).save(*args, **kwargs)


class ActiveObjectsManager(models.Manager):
    """
    Custom manager that automatically filters to only show active objects
    """
    def get_queryset(self, *args, **kwargs):

        q = Q(status=constants.IS_ACTIVE)

        must_contain_id = kwargs.pop('must_contain_id', None)

        if must_contain_id:
            q.add(Q(id=must_contain_id), Q.OR)

        return super(ActiveObjectsManager, self).get_queryset().filter(q)

    def filter(self, *args, **kwargs):

        # Look for any specific object we must return, regardless of status
        must_contain_id = kwargs.pop('must_contain_id', None)
        # pop() here because we don't want to pass it to the
        # real filter() as must_contain_id

        # set up a default q
        q = Q(*args, **kwargs)  # start by filtering for the standard args

        # the call to filter() does't just ask for the args/kwargs filters, but
        # demands that the ORM returns the record with the specified id, too
        get_qs_kwargs = {'must_contain_id': must_contain_id}

        return self.get_queryset(**get_qs_kwargs).filter(q)


class RetiredObjectsManager(models.Manager):
    """
    Custom manager that automatically filters to only show retired objects
    """
    def get_queryset(self):
        return super(RetiredObjectsManager, self).get_queryset().filter(status=constants.IS_INACTIVE)


class StatusBase(models.Model):
    """
    Abstract base class that contains booleans for soft-deleting/retiring
    models, complete with a custom manager to pre-exclude inactive objects

    Important: see TimestampedBase code comments regarding use of save()

    """
    status = models.IntegerField(
        blank=False,
        null=False,
        choices=constants.BASE_STATUSES,
        default=constants.IS_ACTIVE
    )

    # in addition to the standard 'objects' manager, we now have...
    objects = models.Manager()
    active_objects = ActiveObjectsManager()
    retired_objects = RetiredObjectsManager()

    class Meta:
        abstract = True

    @property
    def is_retired(self):
        return self.status == constants.IS_INACTIVE

    def retire(self, **kwargs):
        user = kwargs.pop('user', None)
        # Inherited class may also inheirit from TimestampedBase
        # so need to pass along the user object as a keyword argument
        if not self.is_retired:
            self.status = constants.IS_INACTIVE
            self.save(user=user)


class NameAndSlugBase(models.Model):
    """
    Name and slug fields, with auto generation of the slug from the name
    """

    name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=255
    )

    slug = models.SlugField(
        # editable=False,
        help_text="Automatically generated",
        max_length=255
    )

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            # create a slug from the name
            self.slug = _generate_unique_slug(self, 'name')
        return super(NameAndSlugBase, self).save(*args, **kwargs)


# Utility methods
def _generate_unique_slug(instance, fieldname, offset=0):
    if offset == 0:
        slug = slugify(getattr(instance, fieldname))[:250]
    else:
        slug = slugify(getattr(instance, fieldname))[:250] + u"-%s" % (offset)
        # ie, foo-bar-1
    try:
        # It's okay for objects with the same id to have the same slug.
        instance.__class__.objects.exclude(id=instance.id).get(slug=slug)
    except instance.__class__.DoesNotExist:
        return slug
    except instance.__class__.MultipleObjectsReturned:
        pass  # fall through to generate a fresh slug
    return _generate_unique_slug(
        instance,
        fieldname,
        offset=offset + 1
    )


class Film(TimestampedBase, StatusBase, NameAndSlugBase):
    """
    The film object is related to a film that britdoc have in involvement with in some way - produced, or funded for example
    """

    YEAR_CHOICES = []
    for r in range(2005, (datetime.datetime.now().year + 6)):
        YEAR_CHOICES.append((r, r))

    # LOCATION_CHOICES = (
    #     ('LOCAL', 'Local'),
    #     ('AMAZON_S3', 'Amazon S3'),
    #     ('VIMEO', 'vimeo'),
    # )
    # LOCATION_LOCAL = 'LOCAL'
    # LOCATION_AMAZON_S3 = 'AMAZON_S3'
    # LOCATION_VIMEO = 'VIMEO'

    # ENCODING_CHOICES = (
    #     ('NONE', 'None / NA'),
    #     ('REQUIRED', 'Encoding Required'),
    #     ('PROCESSING', 'Encoding In Progress'),
    #     ('FAILED', 'Encoding Failed'),
    #     ('DONE', 'Encoding Complete'),
    # )
    # ENCODING_NONE = 'NONE'
    # ENCODING_REQUIRED = 'REQUIRED'
    # ENCODING_PROCESSING = 'PROCESSING'
    # ENCODING_FAILED = 'FAILED'
    # ENCODING_DONE = 'DONE'

    STAGE_CHOICES = (
        ('PRODUCTION', 'In Production'),
        ('COMPLETED', 'Completed')
    )
    STAGE_PRODUCTION = 'PRODUCTION'
    STAGE_COMPLETED = 'COMPLETED'

    # name is taken care of with name and slug base
    # name = models.CharField(verbose_name=u'Film Title', max_length=256, null=False, blank=False)
    year = models.IntegerField(verbose_name=u'Year of Completion', choices=YEAR_CHOICES, blank=True, null=True)
    synopsis = RedactorField(verbose_name=u'Synopsis', null=False, blank=False, max_length=65536)
    stage = models.CharField(verbose_name=u'Production Stage', max_length=20, choices=STAGE_CHOICES, default=STAGE_COMPLETED)
    runtime = models.IntegerField(verbose_name=u'Runtime in Minutes', null=True, blank=True)
    trailer = models.URLField(verbose_name=u'Film Trailer Link', null=False, blank=True)
    britdoc_help_development = models.BooleanField(verbose_name='Britdoc helped with DEVELOPMENT', default=False)
    britdoc_help_production = models.BooleanField(verbose_name='Britdoc helped in PRODUCTION', default=False)
    britdoc_help_outreach = models.BooleanField(verbose_name='Britdoc helped with OUTREACH', default=False)
    britdoc_help_goodpitch = models.BooleanField(verbose_name='Britdoc helped at GOODPITCH', default=False)
    featured = models.BooleanField(verbose_name='Featured - show in main index page or not', default=False)
    recommended = models.ManyToManyField('self', blank=True, verbose_name='Also Recommended')
    # TEMPORARY FIELDS
    temp_related_links = models.CharField(verbose_name='temporary copy of old related links field', blank=True, null=False, max_length=65536)
    temp_sales_contacts = models.CharField(verbose_name='temporary copy of old sales field', blank=True, null=False, max_length=65536)
    temp_according_to_filmmakers = models.CharField(verbose_name='temporary copy of old according to filmmakers', blank=True, null=False, max_length=65536)
    temp_quote_attribution = models.CharField(verbose_name='temporary copy of old quote attribution field', blank=True, null=False, max_length=65536)
    temp_quote_text = models.CharField(verbose_name='temporary copy of quote text field', blank=True, null=False, max_length=65536)
    temp_trailer_url = models.CharField(verbose_name='temporary copy of old trailer url field', blank=True, null=False, max_length=65536)

    @property
    def get_primary_image(self):
        """
        See if there is a primary film image and return it if so
        """
        try:
            img = FilmImage.active_objects.get(primary=True, film=self)
            return img
        except FilmImage.DoesNotExist:
            return False

    @property
    def get_other_image(self):
        """
        Return set of non primary images
        """
        return FilmImage.active_objects.filter(primary=False, film=self)

    @property
    def get_directors(self):
        return(Crew.active_objects.filter(role__icontains='Director', films=self))

    @property
    def get_director(self):
        dirs = Crew.active_objects.filter(role__icontains='Director', films=self).all()
        if dirs.count() > 0:
            return dirs[0]
        return None

    @property
    def get_producers(self):
        return(Crew.active_objects.filter(role__icontains='Producer', films=self))

    @property
    def get_display_string(self):
        """
        A string for the film display pages... name, directory, year, etc, nicely formatted
        """
        dirs = Crew.active_objects.filter(role__icontains='Director', films=self).all()
        if dirs.count() > 0 and self.year:
            result = "%s<br />%s, %s" % (self.name, dirs[0].name, self.year)
        elif dirs.count() > 0:
            result = "%s<br />%s" % (self.name, dirs[0].name)
        elif self.year:
            result = "%s<br />%s" % (self.name, self.year)
        else:
            result = "%s<br />" % (self.name)
        return result

    @property
    def get_twitter(self):
        return(ShareLink.active_objects.filter(name=ShareLink.SHARE_LINK_TYPE_TWITTER, film=self))

    @property
    def get_facebook(self):
        return(ShareLink.active_objects.filter(name=ShareLink.SHARE_LINK_TYPE_FACEBOOK, film=self))

    @property
    def get_website(self):
        return(ShareLink.active_objects.filter(name=ShareLink.SHARE_LINK_TYPE_WEBSITE, film=self))

    @property
    def get_docacademy(self):
        return(ShareLink.active_objects.filter(name=ShareLink.SHARE_LINK_TYPE_DOCACADEMY, film=self))

    def get_absolute_url(self):
        return "/films/display/%s" % self.slug

    @classmethod
    def years_with_films(cls):
        return(cls.active_objects.exclude(year=None).values_list('year', flat=True).order_by('year').distinct())

    def __unicode__(self):
        return u"%s" % self.name


class Laurel(TimestampedBase, StatusBase):
    """
    Film awards at festivals
    """
    award = models.CharField(max_length=128, verbose_name='Name of award')
    film = models.ForeignKey(Film)


class Fund(TimestampedBase, StatusBase, NameAndSlugBase):
    """
    For the different film funds available via britdoc
    """
    films = models.ManyToManyField(Film, related_name='funds')
    image_name = models.CharField(verbose_name='The name of the image used on site', max_length=128, blank=True, null=False)


class Subject(TimestampedBase, StatusBase, NameAndSlugBase):
    """
    For the different subjects for films
    """
    films = models.ManyToManyField(Film, related_name='subjects')


class FilmImage(TimestampedBase, StatusBase):
    """
    Multiple images associated with the film - one primary one uses for main site image
    """
    height = models.PositiveIntegerField(editable=False)
    width = models.PositiveIntegerField(editable=False)
    image = models.ImageField(upload_to='film', height_field='height', width_field='width')
    primary = models.BooleanField(default=False)
    film = models.ForeignKey(Film, related_name='images')


class Crew(TimestampedBase, StatusBase, NameAndSlugBase):
    """
    Directors and Producers for the film
    """
    image = models.ImageField(upload_to='crew', height_field='height', width_field='width', null=False, blank=True)
    height = models.PositiveIntegerField(editable=False, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True, blank=True)
    role = models.CharField(max_length=40, blank=False, null=False)
    about = RedactorField(verbose_name=u'About', null=False, blank=True, max_length=65536)
    films = models.ManyToManyField(Film, related_name='crew')

    class Meta:
        verbose_name_plural = "Crew"

class PurchaseLink(TimestampedBase, StatusBase):
    """
    Holds the url and associated data for a film link, associated with a film.
    """

    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Service - i.e. iTunes')
    title = models.CharField(max_length=128, blank=True, null=False, verbose_name='Longer name i.e. Watch this film on iTunes in the UK')
    url = models.URLField(max_length=256, blank=False, null=False, verbose_name='Link to view film.')
    country = CountryField(max_length=128, blank=False, verbose_name='Country')
    film = models.ForeignKey(Film, related_name='purchase_links')

    def __unicode__(self):
        return u"%s %s purchase link for %s" % (self.country, self.name, self.film.name)


class Review(TimestampedBase, StatusBase):
    """
    Holds a review associated with a film
    """

    body = RedactorField(max_length=65536, blank=False, null=False, verbose_name='Review Copy')
    attribution = models.CharField(max_length=128, blank=False, null=False, verbose_name='Review Attribution')
    film = models.ForeignKey(Film, related_name='reviews')


class ShareLink(TimestampedBase, StatusBase):
    """
    Holds the url and associated data for a sharing link, associated with a film.
    """

    SHARE_LINK_TYPES = (
        ('FACEBOOK', 'Facebook'),
        ('TWITTER', 'Twitter'),
        ('WEBSITE', 'Film Website'),
        ('DOCACADEMY', 'Docacademy Link'),
    )
    SHARE_LINK_TYPE_FACEBOOK = 'FACEBOOK'
    SHARE_LINK_TYPE_TWITTER = 'TWITTER'
    SHARE_LINK_TYPE_WEBSITE = 'WEBSITE'
    SHARE_LINK_TYPE_DOCACADEMY = 'DOCACADEMY'

    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Type of link', choices=SHARE_LINK_TYPES)
    text = models.CharField(max_length=128, blank=True, null=False, verbose_name='Optional text to use on link')
    url = models.URLField(max_length=128, blank=True, null=False, verbose_name='URL for link')
    film = models.ForeignKey(Film, related_name='share_links')

    def __unicode__(self):
        return u"%s share link for %s" % (self.name, self.film.name)


class Goodpitch(TimestampedBase, StatusBase):
    """
    Shows which goodpitches a film has been at
    """
    title = models.CharField(max_length=128, blank=False, null=False, verbose_name='Descriptive name for goodpitch event')
    slug = models.CharField(max_length=20, blank=False, unique=True, null=False, verbose_name='Slug on goodpitch site - e.g. gp2012eu')
    films = models.ManyToManyField(Film, related_name='goodpitches')

    class Meta:
        verbose_name_plural = "Goodpitches"

    def __unicode__(self):
        return u"%s - %s" % (self.slug, self.title)


class Staff(TimestampedBase, StatusBase, NameAndSlugBase):
    """
    People who work for britdoc or are on a board
    """

    STAFF_INVOLVEMENT_CHOICES = (
        ('STAFF', 'Staff'),
        ('FREELANCE', 'Freelance'),
        ('FOUNDATION', 'Foundation'),
        ('CHARITY', 'Charity'),
        ('BRITDOC_INC', 'Britdoc INC'),
        ('CONSULTANT', 'Consultant'),
    )

    STAFF_INVOLVEMENT_TYPE_STAFF = 'STAFF'
    STAFF_INVOLVEMENT_TYPE_FREELANCE = 'FREELANCE'
    STAFF_INVOLVEMENT_TYPE_FOUNDATION = 'FOUNDATION'
    STAFF_INVOLVEMENT_TYPE_CHARITY = 'CHARITY'
    STAFF_INVOLVEMENT_TYPE_BRITDOC_INC = 'BRITDOC_INC'
    STAFF_INVOLVEMENT_TYPE_CONSULTANT = 'CONSULTANT'

    image = models.ImageField(upload_to='staff', height_field='height', width_field='width', null=False, blank=True)
    height = models.PositiveIntegerField(editable=False, null=True, blank=True)
    width = models.PositiveIntegerField(editable=False, null=True, blank=True)
    role = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    about = RedactorField(verbose_name=u'About', null=False, blank=True, max_length=65536)
    involvement = models.CharField(max_length=128, blank=True, null=False, choices=STAFF_INVOLVEMENT_CHOICES)

    class Meta:
        verbose_name_plural = "Staff"

class MailoutSignup(TimestampedBase):
    """
    People who sign up for the britdoc mailout - here we need a task to a) process and send latest version and b) add to main mailout list ?
    """

    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=128, blank=True, null=False)
    last_name = models.CharField(max_length=128, blank=True, null=False)
    job_title = models.CharField(max_length=128, blank=False, null=False, choices=constants.JOB_ROLES)
    region = models.CharField(max_length=128, blank=False, null=False, choices=constants.REGIONS)


class ResourceCategory(TimestampedBase, NameAndSlugBase, StatusBase):
    description = RedactorField(verbose_name=u'Section Introduction', null=False, blank=True, max_length=65536)

    class Meta:
        verbose_name_plural = "Resource Categories"


class Resource(TimestampedBase, StatusBase, NameAndSlugBase):
    """
    Items to go in the resources section of the site 
    """

    category = models.ForeignKey('ResourceCategory')
    description = RedactorField(verbose_name=u'Description of resource', null=False, blank=True, max_length=65536)
    file = models.FileField(upload_to='resources',)
