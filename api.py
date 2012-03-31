from tastypie import fields
from tastypie.resources import ModelResource
from gtdserver.models import *


class RegionResource(ModelResource):
    class Meta:
        queryset = Regions.objects.all()
        resource_name = 'regions'


class CountryResource(ModelResource):
    class Meta:
        queryset = Countries.objects.all()
        resource_name = 'countries'


class AlternativeResource(ModelResource):
    class Meta:
        queryset = Alternatives.objects.all()
        resource_name = 'alternatives'


class AttackTypeResource(ModelResource):
    class Meta:
        queryset = AttackTypes.objects.all()
        resource_name = 'attack_types'


class TargetTypeResource(ModelResource):
    class Meta:
        queryset = TargetTypes.objects.all()
        resource_name = 'targettypes'


class ClaimModeResource(ModelResource):
    class Meta:
        queryset = ClaimModes.objects.all()
        resource_name = 'claimmodes'


class WeaponTypeResource(ModelResource):
    class Meta:
        queryset = WeaponTypes.objects.all()
        resource_name = 'weapontypes'


class WeaponSubtypeResource(ModelResource):
    class Meta:
        queryset = WeaponSubtypes.objects.all()
        resource_name = 'weaponsubtypes'


class PropExtentResource(ModelResource):
    class Meta:
        queryset = Damage.objects.all()
        resource_name = 'propextents'


class HostageOutcomeResource(ModelResource):
    class Meta:
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

    class Meta:
        queryset = Gtd.objects.all()
        resource_name = 'attacks'
