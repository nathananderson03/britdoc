from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from core.models import Film, FilmImage, Fund, Crew
from django.core.files import File
# import sys

import json
import urllib
import re
# from pprint import pprint


class Command(BaseCommand):
    help = 'Import film data from old site'

    def handle(self, *args, **options):

        for c in Crew.objects.all():
            c.delete()

        for f in Film.objects.all():
            f.delete()

        for fund in Fund.objects.all():
            fund.delete()

        # make the 6 initial funds
        fund = Fund(name='Bertha Connect')
        fund.save()
        fund = Fund(name='Bertha Journalism')
        fund.save()
        fund = Fund(name='Circle Fund')
        fund.save()
        fund = Fund(name='Foundation')
        fund.save()
        fund = Fund(name='Puma Catalyst')
        fund.save()
        fund = Fund(name='Puma Mobility')
        fund.save()

        for fimg in FilmImage.objects.all():
            fimg.delete()

        with open('data/import/films.json') as data_file:
            films = json.load(data_file)

        for of in films:
            if of['year'] != '':
                year = int(of['year'])
            else:
                year = '0'

            of['length'] = re.sub(r'\s*min[s]*\s*', '', of['length'], flags=re.IGNORECASE)

            if of['length'] != '':
                runtime = int(of['length'])
            else:
                runtime = '0'

            print (of['title'])

            try:
                other_f = Film.objects.get(name=of['title'])
                if other_f:
                    of['title'] = of['title'] + " DUPLICATE"
                    print ("Using %s " % of['title'])
            except Film.DoesNotExist:
                pass

            try:
                other_f = Film.objects.get(name=of['title'])
                if other_f:
                    of['title'] = of['title'] + " DUPLICATE"
                    print ("Using %s " % of['title'])
            except Film.DoesNotExist:
                pass

            f = Film(
                name=of['title'],
                synopsis=of['synopsis'],
                runtime=runtime,
                year=year,
                temp_related_links=of['related_links'],
                temp_sales_contacts=of['sales_contact'],
                temp_according_to_filmmakers=of['according_to_filmmakers'],
                temp_quote_attribution=of['quote_attribution'],
                temp_quote_text=of['quote_text'],
                temp_trailer_url=of['trailer_url'],
            )
            f.save()

            # add crew
            if of['about_director'] or of['director']:
                try:
                    c = Crew.objects.get(name=of['director'])
                except Crew.DoesNotExist:
                    c = Crew(name=of['director'], about=of['about_director'])
                    c.save()
                f.crew.add(c)
                f.save()

            # funds
            if of['type'] == 'bertha_connect' or of['type'] == 'bertha_journalism_and_connect':
                fund = Fund.objects.get(name='Bertha Connect')
                f.funds.add(fund)
                f.save()

            if of['type'] == 'bertha_journalism' or of['type'] == 'bertha_journalism_and_connect':
                fund = Fund.objects.get(name='Bertha Journalism')
                f.funds.add(fund)
                f.save()

            if of['type'] == 'circle_fund':
                fund = Fund.objects.get(name='Circle Fund')
                f.funds.add(fund)
                f.save()

            if of['type'] == 'foundation':
                fund = Fund.objects.get(name='Foundation')
                f.funds.add(fund)
                f.save()

            if of['type'] == 'puma_catalyst' or of['type'] == 'puma_catalyst_and_mobility':
                fund = Fund.objects.get(name='Puma Catalyst')
                f.funds.add(fund)
                f.save()

            if of['type'] == 'puma_mobility' or of['type'] == 'puma_catalyst_and_mobility':
                fund = Fund.objects.get(name='Puma Mobility')
                f.funds.add(fund)
                f.save()

            img = urllib.urlretrieve(of['img'], "media/film/%s.imported.jpg" % f.slug)

            fi = FilmImage()
            fi.image = "film/%s.imported.jpg" % f.slug
            fi.film = f
            fi.primary = True
            fi.save()
