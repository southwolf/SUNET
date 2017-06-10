# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.38
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_CRFPP', [dirname(__file__)])
            _mod = imp.load_module('_CRFPP', fp, pathname, description)
        finally:
            if fp is not None: fp.close()
        return _mod
    _CRFPP = swig_import_helper()
    del swig_import_helper
else:
    import _CRFPP
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Tagger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tagger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tagger, name)
    __repr__ = _swig_repr
    def set_vlevel(self, *args): return _CRFPP.Tagger_set_vlevel(self, *args)
    def vlevel(self): return _CRFPP.Tagger_vlevel(self)
    def set_cost_factor(self, *args): return _CRFPP.Tagger_set_cost_factor(self, *args)
    def cost_factor(self): return _CRFPP.Tagger_cost_factor(self)
    def set_nbest(self, *args): return _CRFPP.Tagger_set_nbest(self, *args)
    def nbest(self): return _CRFPP.Tagger_nbest(self)
    def add(self, *args): return _CRFPP.Tagger_add(self, *args)
    def size(self): return _CRFPP.Tagger_size(self)
    def xsize(self): return _CRFPP.Tagger_xsize(self)
    def dsize(self): return _CRFPP.Tagger_dsize(self)
    def result(self, *args): return _CRFPP.Tagger_result(self, *args)
    def answer(self, *args): return _CRFPP.Tagger_answer(self, *args)
    def y(self, *args): return _CRFPP.Tagger_y(self, *args)
    def y2(self, *args): return _CRFPP.Tagger_y2(self, *args)
    def yname(self, *args): return _CRFPP.Tagger_yname(self, *args)
    def x(self, *args): return _CRFPP.Tagger_x(self, *args)
    def ysize(self): return _CRFPP.Tagger_ysize(self)
    def prob(self, *args): return _CRFPP.Tagger_prob(self, *args)
    def alpha(self, *args): return _CRFPP.Tagger_alpha(self, *args)
    def beta(self, *args): return _CRFPP.Tagger_beta(self, *args)
    def emission_cost(self, *args): return _CRFPP.Tagger_emission_cost(self, *args)
    def next_transition_cost(self, *args): return _CRFPP.Tagger_next_transition_cost(self, *args)
    def prev_transition_cost(self, *args): return _CRFPP.Tagger_prev_transition_cost(self, *args)
    def best_cost(self, *args): return _CRFPP.Tagger_best_cost(self, *args)
    def Z(self): return _CRFPP.Tagger_Z(self)
    def empty(self): return _CRFPP.Tagger_empty(self)
    def clear(self): return _CRFPP.Tagger_clear(self)
    def next(self): return _CRFPP.Tagger_next(self)
    def parse(self, *args): return _CRFPP.Tagger_parse(self, *args)
    def what(self): return _CRFPP.Tagger_what(self)
    __swig_destroy__ = _CRFPP.delete_Tagger
    __del__ = lambda self : None;
    def __init__(self, *args): 
        this = _CRFPP.new_Tagger(*args)
        try: self.this.append(this)
        except: self.this = this
Tagger_swigregister = _CRFPP.Tagger_swigregister
Tagger_swigregister(Tagger)

VERSION = _CRFPP.VERSION


