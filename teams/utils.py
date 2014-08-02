
import logging
from django.utils.importlib import import_module


FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger('Models')

def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = import_module( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m


def get_base_model(BASE_MODEL):
    """Determine the base Model to inherit in the
    Entry Model, this allows to overload it."""

    dot = BASE_MODEL.rindex('.')
    module_name = BASE_MODEL[:dot]
    class_name = BASE_MODEL[dot + 1:]
    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except (ImportError, AttributeError):
        log.warning('%s cannot be imported' % BASE_MODEL)
    return get_class(BASE_MODEL)