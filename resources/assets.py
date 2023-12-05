import itertools
from mcresources import ResourceManager, ItemContext, BlockContext, block_states
from mcresources import utils, loot_tables

from constants import *



def generate(rm: ResourceManager):
    for crop, crop_data in CROPS.items():
        if crop_data.type == 'default' or crop_data.type == 'pickable' or crop_data.type == 'spreading':
            rm.block_model(('wild_crop', '%s' % crop), {'crop': 'tfc:block/crop/%s_wild' % crop}, parent='tfc:block/wild_crop/crop_bottom_alert')
        else:
            rm.block_model(('wild_crop', '%s_top' % crop), {'crop': 'tfc:block/crop/%s_wild_top' % crop}, parent='tfc:block/wild_crop/crop_top_alert')

    lifecycle_to_model = {'healthy': '', 'dormant': 'dry_', 'fruiting': 'fruiting_', 'flowering': 'flowering_'}
    for berry, data in BERRIES.items():
        if data.type == 'stationary' or data.type == 'waterlogged':
            for lifecycle, stage in itertools.product(lifecycle_to_model.values(), range(0, 3)):
                rm.block_model('plant/%s%s_bush_%d' % (lifecycle, berry, stage), parent='tfc:block/plant/stationary_bush_alert_%d' % stage, textures={'bush': 'tfc:block/berry_bush/' + lifecycle + '%s_bush' % berry})

    rm.domain = 'firmalife'
    for berry in STILL_BUSHES.keys():
        for lifecycle, stage in itertools.product(lifecycle_to_model.values(), range(0, 3)):
            rm.block_model('plant/%s%s_bush_%d' % (lifecycle, berry, stage), parent='tfc:block/plant/stationary_bush_alert_%d' % stage, textures={'bush': 'firmalife:block/berry_bush/' + lifecycle + '%s_bush' % berry})
