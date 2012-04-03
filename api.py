from tastypie import fields
from tastypie.contrib.gis.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from gtdserver.models import *


class DBSourceResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = DBSources.objects.all()
        resource_name = 'dbsources'


class RegionResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = Regions.objects.all()
        resource_name = 'regions'


class CountryResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = Countries.objects.all()
        resource_name = 'countries'


class AlternativeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = Alternatives.objects.all()
        resource_name = 'alternatives'


class AttackTypeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = AttackTypes.objects.all()
        resource_name = 'attack_types'


class TargetTypeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = TargetTypes.objects.all()
        resource_name = 'targettypes'


class ClaimModeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = ClaimModes.objects.all()
        resource_name = 'claimmodes'


class WeaponTypeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = WeaponTypes.objects.all()
        resource_name = 'weapontypes'


class WeaponSubtypeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = WeaponSubtypes.objects.all()
        resource_name = 'weaponsubtypes'


class PropExtentResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = Damage.objects.all()
        resource_name = 'propextents'


class HostageOutcomeResource(ModelResource):
    class Meta:
        filtering = {'id': ALL, 'name': ALL}
        allowed_methods = ['get']
        queryset = HostageOutcomes.objects.all()
        resource_name = 'hostageoutcomes'


class GtdResource(ModelResource):
    region = fields.ForeignKey(RegionResource, 'region', full=True)
    country = fields.ForeignKey(CountryResource, 'country', full=True)
    alternative = fields.ForeignKey(AlternativeResource, 'alternative',
                                    null=True)
    attacktype1 = fields.ForeignKey(AttackTypeResource, 'attacktype1',
                                    null=True)
    attacktype2 = fields.ForeignKey(AttackTypeResource, 'attacktype2',
                                    null=True)
    attacktype3 = fields.ForeignKey(AttackTypeResource, 'attacktype3',
                                    null=True)
    targtype1 = fields.ForeignKey(TargetTypeResource, 'targtype1', null=True)
    targtype2 = fields.ForeignKey(TargetTypeResource, 'targtype2', null=True)
    targtype3 = fields.ForeignKey(TargetTypeResource, 'targtype3', null=True)
    claimmode = fields.ForeignKey(ClaimModeResource, 'claimmode', null=True)
    claimmode2 = fields.ForeignKey(ClaimModeResource, 'claimmode2', null=True)
    claimmode3 = fields.ForeignKey(ClaimModeResource, 'claimmode3', null=True)
    weapontype1 = fields.ForeignKey(WeaponTypeResource, 'weaptype1', null=True)
    weapontype2 = fields.ForeignKey(WeaponTypeResource, 'weaptype2', null=True)
    weapontype3 = fields.ForeignKey(WeaponTypeResource, 'weaptype3', null=True)
    weapontype4 = fields.ForeignKey(WeaponTypeResource, 'weaptype4', null=True)
    weaponsubtype1 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype1',
                                       null=True)
    weaponsubtype2 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype2',
                                       null=True)
    weaponsubtype3 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype3',
                                       null=True)
    weaponsubtype4 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype4',
                                       null=True)
    propextent = fields.ForeignKey(PropExtentResource, 'propextent', null=True)
    hostkidoutcome = fields.ForeignKey(HostageOutcomeResource,
                                       'hostkidoutcome', blank=True, null=True)
    dbsource = fields.ForeignKey(DBSourceResource, 'dbsource', blank=True,
                                 null=True)

    class Meta:
        filtering = {
            'id': ALL,
            'date': ALL,
            'extended': ALL,
            'resolution': ALL,
            'region': ALL_WITH_RELATIONS,
            'country': ALL_WITH_RELATIONS,
            'provstate': ALL,
            'city': ALL,
            'vicinity': ALL,
            'location': ALL,
            'crit1': ALL,
            'crit2': ALL,
            'crit3': ALL,
            'doubtterr': ALL,
            'alternative': ALL_WITH_RELATIONS,
            'multiple': ALL,
            'conflict': ALL,
            'success': ALL,
            'suicide': ALL,
            'attacktype1': ALL_WITH_RELATIONS,
            'attacktype2': ALL_WITH_RELATIONS,
            'attacktype3': ALL_WITH_RELATIONS,
            'targtype1': ALL_WITH_RELATIONS,
            'natlty1': ALL,
            'targtype2': ALL_WITH_RELATIONS,
            'natlty2': ALL,
            'targtype3': ALL_WITH_RELATIONS,
            'natlty3': ALL,
            'guncertain1': ALL,
            'guncertain2': ALL,
            'guncertain3': ALL,
            'nperps': ALL,
            'nperpcap': ALL,
            'claimed': ALL,
            'claimmode': ALL_WITH_RELATIONS,
            'claimconf': ALL,
            'claim2': ALL,
            'claimmode2': ALL_WITH_RELATIONS,
            'claimconf2': ALL,
            'claim3': ALL,
            'claimmode3': ALL_WITH_RELATIONS,
            'claimconf3': ALL,
            'compclaim': ALL,
            'weapontype1': ALL_WITH_RELATIONS,
            'weaponsubtype1': ALL_WITH_RELATIONS,
            'weapontype2': ALL_WITH_RELATIONS,
            'weaponsubtype2': ALL_WITH_RELATIONS,
            'weapontype3': ALL_WITH_RELATIONS,
            'weaponsubtype3': ALL_WITH_RELATIONS,
            'weapontype4': ALL_WITH_RELATIONS,
            'weaponsubtype4': ALL_WITH_RELATIONS,
            'nkill': ALL,
            'nkillus': ALL,
            'nkillter': ALL,
            'nwound': ALL,
            'nwoundus': ALL,
            'nwoundter': ALL,
            'property': ALL,
            'propextent': ALL,
            'propvalue': ALL,
            'propextent': ALL_WITH_RELATIONS,
            'ishostkid': ALL,
            'nhostkid': ALL,
            'nhostkidus': ALL,
            'nhours': ALL,
            'ndays': ALL,
            'kidhijcountry': ALL,
            'ransom': ALL,
            'ransomamt': ALL,
            'ransomamtus': ALL,
            'ransompaid': ALL,
            'ransompaidus': ALL,
            'hostkidoutcome': ALL_WITH_RELATIONS,
            'nreleased': ALL,
            'dbsource': ALL_WITH_RELATIONS
        }
        allowed_methods = ['get']
        queryset = Gtd.objects.all()
        resource_name = 'attacks'

