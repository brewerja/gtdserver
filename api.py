from tastypie import fields
from tastypie.contrib.gis.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.cache import SimpleCache
from gtdserver.models import *
import tastypie.resources


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
    region = fields.ForeignKey(RegionResource, 'region')
    country = fields.ForeignKey(CountryResource, 'country')
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
    weaptype1 = fields.ForeignKey(WeaponTypeResource, 'weaptype1', null=True)
    weaptype2 = fields.ForeignKey(WeaponTypeResource, 'weaptype2', null=True)
    weaptype3 = fields.ForeignKey(WeaponTypeResource, 'weaptype3', null=True)
    weaptype4 = fields.ForeignKey(WeaponTypeResource, 'weaptype4', null=True)
    weapsubtype1 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype1',
                                       null=True)
    weapsubtype2 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype2',
                                       null=True)
    weapsubtype3 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype3',
                                       null=True)
    weapsubtype4 = fields.ForeignKey(WeaponSubtypeResource, 'weapsubtype4',
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
        cache = SimpleCache()

    def dehydrate(self, bundle):
        """Reference all foreign keys' names."""
        data = bundle.data
        obj = bundle.obj
        data['geog'] = [obj.geog.x, obj.geog.y]
        data['geom'] = [obj.geom.x, obj.geom.y]
        data['region'] = obj.region.name
        data['country'] = obj.country.name
        if obj.alternative:
            data['alternative'] = obj.alternative.name
        if obj.attacktype1:
            data['attacktype1'] = obj.attacktype1.name
        if obj.attacktype2:
            data['attacktype2'] = obj.attacktype1.name
        if obj.attacktype3:
            data['attacktype3'] = obj.attacktype1.name
        if obj.targtype1:
            data['targtype1'] = obj.targtype1.name
        if obj.targtype2:
            data['targtype2'] = obj.targtype2.name
        if obj.targtype3:
            data['targtype3'] = obj.targtype3.name
        if obj.claimmode:
            data['claimmode'] = obj.claimmode.name
        if obj.claimmode2:
            data['claimmode2'] = obj.claimmode2.name
        if obj.claimmode3:
            data['claimmode3'] = obj.claimmode3.name
        if obj.weaptype1:
            data['weaptype1'] = obj.weaptype1.name
        if obj.weaptype2:
            data['weaptype2'] = obj.weaptype2.name
        if obj.weaptype3:
            data['weaptype3'] = obj.weaptype3.name
        if obj.weaptype4:
            data['weaptype4'] = obj.weaptype4.name
        if obj.weapsubtype1:
            data['weapsubtype1'] = obj.weapsubtype1.name
        if obj.weapsubtype2:
            data['weapsubtype2'] = obj.weapsubtype2.name
        if obj.weapsubtype3:
            data['weapsubtype3'] = obj.weapsubtype3.name
        if obj.weapsubtype4:
            data['weapsubtype4'] = obj.weapsubtype4.name
        if obj.propextent:
            data['propextent'] = obj.propextent.name
        if obj.hostkidoutcome:
            data['hostkidoutcome'] = obj.hostkidoutcome.name
        if obj.dbsource:
            data['dbsource'] = obj.dbsource.name
        return bundle
