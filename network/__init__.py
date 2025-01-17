from .resnet101_baseline import get_resnet101_baseline_dsn
from .resnet101_base_oc import get_resnet101_base_oc_dsn
from .resnet101_base_gc import get_resnet101_base_gc_dsn
from .resnet101_base_nl import get_resnet101_base_nl_dsn
from .resnet101_pyramid_oc import get_resnet101_pyramid_oc_dsn
from .resnet101_asp_oc import get_resnet101_asp_oc_dsn


networks = {
    'resnet101_baseline_dsn': get_resnet101_baseline_dsn,
    'resnet101_base_oc_dsn': get_resnet101_base_oc_dsn,
    'resnet101_base_gc_dsn': get_resnet101_base_gc_dsn,
    'resnet101_base_nl_dsn': get_resnet101_base_nl_dsn,
    'resnet101_pyramid_oc_dsn': get_resnet101_pyramid_oc_dsn,
    'resnet101_asp_oc_dsn': get_resnet101_asp_oc_dsn,
}

def get_segmentation_model(name, **kwargs):
    return networks[name.lower()](**kwargs)