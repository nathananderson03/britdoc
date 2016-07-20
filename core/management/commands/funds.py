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

        with open('data/import/films.json') as data_file:
            films = json.load(data_file)

        for of in films:
            print (of['title'])

            try:
                other_f = Film.objects.get(name=of['title'])
                # add crew
                if of['about_director'] or of['director']:
                    try:
                        c = Crew.objects.get(name=of['director'])
                    except Crew.DoesNotExist:
                        c = Crew(name=of['director'], about=of['about_director'])
                        c.save()
                    other_f.crew.add(c)
                    other_f.save()

                # funds
                if of['type'] == 'bertha_connect' or of['type'] == 'bertha_journalism_and_connect':
                    fund = Fund.objects.get(name='Bertha Connect')
                    other_f.funds.add(fund)
                    other_f.save()

                if of['type'] == 'bertha_journalism' or of['type'] == 'bertha_journalism_and_connect':
                    fund = Fund.objects.get(name='Bertha Journalism')
                    other_f.funds.add(fund)
                    other_f.save()

                if of['type'] == 'circle_fund':
                    fund = Fund.objects.get(name='Circle Fund')
                    other_f.funds.add(fund)
                    other_f.save()

                if of['type'] == 'foundation':
                    fund = Fund.objects.get(name='Foundation')
                    other_f.funds.add(fund)
                    other_f.save()

                if of['type'] == 'puma_catalyst' or of['type'] == 'puma_catalyst_and_mobility':
                    fund = Fund.objects.get(name='Puma Catalyst')
                    other_f.funds.add(fund)
                    other_f.save()

                if of['type'] == 'puma_mobility' or of['type'] == 'puma_catalyst_and_mobility':
                    fund = Fund.objects.get(name='Puma Mobility')
                    other_f.funds.add(fund)
                    other_f.save()


            except Film.DoesNotExist:
                pass

