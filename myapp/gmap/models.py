from django.db import models

# Create your models here.

class Country(models.Model):
    class Meta:
        db_table = 'country'

    countryid          = models.CharField('countryid', primary_key=True, max_length=255)
    country            = models.CharField('country', max_length=255)
    fips104            = models.CharField('fips104', max_length=255)
    iso2               = models.CharField('iso2', max_length=255)
    iso3               = models.CharField('iso3', max_length=255)
    ison               = models.CharField('ison', max_length=255)
    internet           = models.CharField('internet', max_length=255)
    capital            = models.CharField('capital', max_length=255)
    mapreference       = models.CharField('mapreference', max_length=255)
    nationalitysingular= models.CharField('nationalitysingular', max_length=255)
    nationalityplural  = models.CharField('nationalityplural', max_length=255)
    currency           = models.CharField('currency', max_length=255)
    currencycode       = models.CharField('currencycode', max_length=255)
    population         = models.CharField('population', max_length=255)
    title              = models.CharField('title', max_length=255)
    comment            = models.CharField('comment', max_length=255)

class State(models.Model):
    class Meta:
        db_table = 'states'

    regionid  = models.CharField('regionid', primary_key=True, max_length=255)
    country = models.ForeignKey(Country, db_column='countryid', max_length=255)
    region    = models.CharField('region', max_length=255)
    code      = models.CharField('code', max_length=255)
    adm1code  = models.CharField('adm1code', max_length=255)


class City(models.Model):
    class Meta:
        db_table = 'cities'

    cityid    = models.CharField('CityId', primary_key=True, max_length=255)
    country   = models.ForeignKey(Country, db_column='CountryID', max_length=255)
    regionid  = models.CharField('RegionID', max_length=255)
    city      = models.CharField('City', max_length=255)
    latitude  = models.CharField('Latitude', max_length=255)
    longitude = models.CharField('Longitude', max_length=255)
    timezone  = models.CharField('TimeZone', max_length=255)
    dmaid     = models.CharField('DmaId', max_length=255)
    code      = models.CharField('Code', max_length=255)
