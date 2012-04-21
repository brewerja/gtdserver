# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field
# names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom
# [appname]'
# into your database.

from django.contrib.gis.db import models
from django.contrib.gis.geos import *

#class SpatialRefSys(models.Model):
#    srid = models.IntegerField(primary_key=True)
#    auth_name = models.CharField(max_length=256, blank=True)
#    auth_srid = models.IntegerField(null=True, blank=True)
#    srtext = models.CharField(max_length=2048, blank=True)
#    proj4text = models.CharField(max_length=2048, blank=True)
#    class Meta:
#        db_table = u'spatial_ref_sys'
#
#class GeometryColumns(models.Model):
#    f_table_catalog = models.CharField(max_length=256)
#    f_table_schema = models.CharField(max_length=256)
#    f_table_name = models.CharField(max_length=256)
#    f_geometry_column = models.CharField(max_length=256)
#    coord_dimension = models.IntegerField()
#    srid = models.IntegerField()
#    type = models.CharField(max_length=30)
#    class Meta:
#        db_table = u'geometry_columns'
#
#class GeographyColumns(models.Model):
#    f_table_catalog = models.TextField(blank=True)
#    f_table_schema = models.TextField(blank=True)
#    f_table_name = models.TextField(blank=True)
#    f_geography_column = models.TextField(blank=True)
#    coord_dimension = models.IntegerField(null=True, blank=True)
#    srid = models.IntegerField(null=True, blank=True)
#    type = models.TextField(blank=True)
#    class Meta:
#        db_table = u'geography_columns'

class Dbsources(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'dbsources'

class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)
    num_attacks_natlty1 = models.IntegerField(null=True, blank=True)
    num_attacks_natlty2 = models.IntegerField(null=True, blank=True)
    num_attacks_natlty3 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'countries'


class Alternatives(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'alternatives'


class HostageOutcomes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'hostage_outcomes'


class Damage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'damage'


class TargetTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)
    num_attacks_targtype1 = models.IntegerField(null=True, blank=True)
    num_attacks_targtype2 = models.IntegerField(null=True, blank=True)
    num_attacks_targtype3 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'target_types'


class WeaponSubtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)
    num_attacks_weapsubtype1 = models.IntegerField(null=True, blank=True)
    num_attacks_weapsubtype2 = models.IntegerField(null=True, blank=True)
    num_attacks_weapsubtype3 = models.IntegerField(null=True, blank=True)
    num_attacks_weapsubtype4 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'weapon_subtypes'


class Regions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'regions'


class WeaponTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)
    num_attacks_weaptype1 = models.IntegerField(null=True, blank=True)
    num_attacks_weaptype2 = models.IntegerField(null=True, blank=True)
    num_attacks_weaptype3 = models.IntegerField(null=True, blank=True)
    num_attacks_weaptype4 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'weapon_types'


class AttackTypes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)
    num_attacks_attacktype1 = models.IntegerField(null=True, blank=True)
    num_attacks_attacktype2 = models.IntegerField(null=True, blank=True)
    num_attacks_attacktype3 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'attack_types'


class ClaimModes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=35, blank=True)
    num_attacks = models.IntegerField(null=True, blank=True)
    num_attacks_claimmode = models.IntegerField(null=True, blank=True)
    num_attacks_claimmode2 = models.IntegerField(null=True, blank=True)
    num_attacks_claimmode3 = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'claim_modes'


class Gtd(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateField(null=True, blank=True)
    approxdate = models.CharField(max_length=100, blank=True)
    extended = models.NullBooleanField(null=True, blank=True)
    resolution = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Countries, null=True, db_column='country',
                                blank=True)
    region = models.ForeignKey(Regions, null=True, db_column='region',
                               blank=True)
    provstate = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    vicinity = models.NullBooleanField(null=True, blank=True)
    location = models.TextField(blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    summary = models.TextField(blank=True)
    crit1 = models.NullBooleanField(null=True, blank=True)
    crit2 = models.NullBooleanField(null=True, blank=True)
    crit3 = models.NullBooleanField(null=True, blank=True)
    doubtterr = models.NullBooleanField(null=True, blank=True)
    alternative = models.ForeignKey(Alternatives, null=True,
                                    db_column='alternative', blank=True)
    multiple = models.NullBooleanField(null=True, blank=True)
    conflict = models.NullBooleanField(null=True, blank=True)
    success = models.NullBooleanField(null=True, blank=True)
    suicide = models.NullBooleanField(null=True, blank=True)
    attacktype1 = models.ForeignKey(AttackTypes, null=True,
                                    db_column='attacktype1', blank=True,
                                    related_name='tt1')
    attacktype2 = models.ForeignKey(AttackTypes, null=True,
                                    db_column='attacktype2', blank=True,
                                    related_name='at2')
    attacktype3 = models.ForeignKey(AttackTypes, null=True,
                                    db_column='attacktype3', blank=True,
                                    related_name='at3')
    targtype1 = models.ForeignKey(TargetTypes, null=True,
                                  db_column='targtype1', blank=True,
                                  related_name='tt1')
    corp1 = models.CharField(max_length=200, blank=True)
    target1 = models.CharField(max_length=250, blank=True,)
    natlty1 = models.ForeignKey(Countries, null=True, db_column='natlty1',
                                blank=True, related_name='natlty1')
    targtype2 = models.ForeignKey(TargetTypes, null=True,
                                  db_column='targtype2', blank=True,
                                  related_name='tt2')
    corp2 = models.CharField(max_length=200, blank=True)
    target2 = models.CharField(max_length=200, blank=True)
    natlty2 = models.ForeignKey(Countries, null=True, db_column='natlty2',
                                blank=True, related_name='natlty2')
    targtype3 = models.ForeignKey(TargetTypes, null=True,
                                  db_column='targtype3', blank=True,
                                  related_name='tt3')
    corp3 = models.CharField(max_length=200, blank=True)
    target3 = models.CharField(max_length=150, blank=True)
    natlty3 = models.ForeignKey(Countries, null=True, db_column='natlty3',
                                blank=True, related_name='natlty3')
    gname = models.CharField(max_length=150, blank=True)
    gsubname = models.CharField(max_length=100, blank=True)
    gname2 = models.CharField(max_length=100, blank=True)
    gsubname2 = models.CharField(max_length=100, blank=True)
    gname3 = models.CharField(max_length=100, blank=True)
    gsubname3 = models.CharField(max_length=100, blank=True)
    motive = models.TextField(blank=True)
    guncertain1 = models.NullBooleanField(null=True, blank=True)
    guncertain2 = models.NullBooleanField(null=True, blank=True)
    guncertain3 = models.NullBooleanField(null=True, blank=True)
    nperps = models.IntegerField(null=True, blank=True)
    nperpcap = models.IntegerField(null=True, blank=True)
    claimed = models.NullBooleanField(null=True, blank=True)
    claimmode = models.ForeignKey(ClaimModes, null=True, db_column='claimmode',
                                  blank=True, related_name='cm1')
    claimconf = models.NullBooleanField(null=True, blank=True)
    claim2 = models.NullBooleanField(null=True, blank=True)
    claimmode2 = models.ForeignKey(ClaimModes, null=True,
                                   db_column='claimmode2', blank=True,
                                   related_name='cm2')
    claimconf2 = models.NullBooleanField(null=True, blank=True)
    claim3 = models.NullBooleanField(null=True, blank=True)
    claimmode3 = models.ForeignKey(ClaimModes, null=True,
                                   db_column='claimmode3', blank=True,
                                   related_name='cm3')
    claimconf3 = models.NullBooleanField(null=True, blank=True)
    compclaim = models.NullBooleanField(null=True, blank=True)
    weaptype1 = models.ForeignKey(WeaponTypes, null=True,
                                  db_column='weaptype1', blank=True,
                                  related_name='wt1')
    weapsubtype1 = models.ForeignKey(WeaponSubtypes, null=True,
                                     db_column='weapsubtype1', blank=True,
                                     related_name='wst1')
    weaptype2 = models.ForeignKey(WeaponTypes, null=True,
                                  db_column='weaptype2', blank=True,
                                  related_name='wt2')
    weapsubtype2 = models.ForeignKey(WeaponSubtypes, null=True,
                                     db_column='weapsubtype2', blank=True,
                                     related_name='wst2')
    weaptype3 = models.ForeignKey(WeaponTypes, null=True,
                                  db_column='weaptype3', blank=True,
                                  related_name='wt3')
    weapsubtype3 = models.ForeignKey(WeaponSubtypes, null=True,
                                     db_column='weapsubtype3', blank=True,
                                     related_name='wst3')
    weaptype4 = models.ForeignKey(WeaponTypes, null=True,
                                  db_column='weaptype4', blank=True,
                                  related_name='wt4')
    weapsubtype4 = models.ForeignKey(WeaponSubtypes, null=True,
                                     db_column='weapsubtype4', blank=True,
                                     related_name='wst4')
    weapdetail = models.CharField(max_length=800, blank=True)
    nkill = models.FloatField(null=True, blank=True)
    nkillus = models.FloatField(null=True, blank=True)
    nkillter = models.FloatField(null=True, blank=True)
    nwound = models.FloatField(null=True, blank=True)
    nwoundus = models.FloatField(null=True, blank=True)
    nwoundter = models.FloatField(null=True, blank=True)
    property = models.NullBooleanField(null=True, blank=True)
    propextent = models.ForeignKey(Damage, null=True, db_column='propextent',
                                   blank=True)
    propvalue = models.FloatField(null=True, blank=True)
    propcomment = models.CharField(max_length=1000, blank=True)
    ishostkid = models.NullBooleanField(null=True, blank=True)
    nhostkid = models.FloatField(null=True, blank=True)
    nhostkidus = models.FloatField(null=True, blank=True)
    nhours = models.FloatField(null=True, blank=True)
    ndays = models.IntegerField(null=True, blank=True)
    divert = models.CharField(max_length=100, blank=True)
    kidhijcountry = models.CharField(max_length=100, blank=True)
    ransom = models.NullBooleanField(null=True, blank=True)
    ransomamt = models.FloatField(null=True, blank=True)
    ransomamtus = models.FloatField(null=True, blank=True)
    ransompaid = models.FloatField(null=True, blank=True)
    ransompaidus = models.FloatField(null=True, blank=True)
    ransomnote = models.TextField(blank=True)
    hostkidoutcome = models.ForeignKey(HostageOutcomes, null=True,
                                       db_column='hostkidoutcome', blank=True)
    nreleased = models.FloatField(null=True, blank=True)
    addnotes = models.TextField(blank=True)
    scite1 = models.CharField(max_length=500, blank=True)
    scite2 = models.CharField(max_length=500, blank=True)
    scite3 = models.CharField(max_length=500, blank=True)
    dbsource = models.ForeignKey(Dbsources, db_column='dbsource')
    geom = models.PointField(srid=2163, null=True, blank=True)
    geog = models.PointField(blank=True, null=True, geography=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.summary

    class Meta:
        db_table = u'gtd'
