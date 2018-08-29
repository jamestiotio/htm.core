# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013-2017, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_math', [dirname(__file__)])
        except ImportError:
            import _math
            return _math
        if fp is not None:
            try:
                _mod = imp.load_module('_math', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _math = swig_import_helper()
    del swig_import_helper
else:
    import _math
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
    if (not static):
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


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


_MATH = _math

NTA_BasicType_Byte = _math.NTA_BasicType_Byte
NTA_BasicType_Int16 = _math.NTA_BasicType_Int16
NTA_BasicType_UInt16 = _math.NTA_BasicType_UInt16
NTA_BasicType_Int32 = _math.NTA_BasicType_Int32
NTA_BasicType_UInt32 = _math.NTA_BasicType_UInt32
NTA_BasicType_Int64 = _math.NTA_BasicType_Int64
NTA_BasicType_UInt64 = _math.NTA_BasicType_UInt64
NTA_BasicType_Real32 = _math.NTA_BasicType_Real32
NTA_BasicType_Real64 = _math.NTA_BasicType_Real64
NTA_BasicType_Handle = _math.NTA_BasicType_Handle
NTA_BasicType_Bool = _math.NTA_BasicType_Bool
NTA_BasicType_Last = _math.NTA_BasicType_Last
NTA_BasicType_Real = _math.NTA_BasicType_Real
NTA_REAL_TYPE_STRING = _math.NTA_REAL_TYPE_STRING
NTA_LogLevel_None = _math.NTA_LogLevel_None
NTA_LogLevel_Minimal = _math.NTA_LogLevel_Minimal
NTA_LogLevel_Normal = _math.NTA_LogLevel_Normal
NTA_LogLevel_Verbose = _math.NTA_LogLevel_Verbose
LogLevel_None = _math.LogLevel_None
LogLevel_Minimal = _math.LogLevel_Minimal
LogLevel_Normal = _math.LogLevel_Normal
LogLevel_Verbose = _math.LogLevel_Verbose
class SwigPyIterator(object):
    """Proxy of C++ swig::SwigPyIterator class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _math.delete_SwigPyIterator
    def value(self):
        """value(self) -> PyObject *"""
        return _math.SwigPyIterator_value(self)

    def incr(self, n=1):
        """incr(self, n=1) -> SwigPyIterator"""
        return _math.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        """decr(self, n=1) -> SwigPyIterator"""
        return _math.SwigPyIterator_decr(self, n)

    def distance(self, *args, **kwargs):
        """distance(self, x) -> ptrdiff_t"""
        return _math.SwigPyIterator_distance(self, *args, **kwargs)

    def equal(self, *args, **kwargs):
        """equal(self, x) -> bool"""
        return _math.SwigPyIterator_equal(self, *args, **kwargs)

    def copy(self):
        """copy(self) -> SwigPyIterator"""
        return _math.SwigPyIterator_copy(self)

    def next(self):
        """next(self) -> PyObject *"""
        return _math.SwigPyIterator_next(self)

    def __next__(self):
        """__next__(self) -> PyObject *"""
        return _math.SwigPyIterator___next__(self)

    def previous(self):
        """previous(self) -> PyObject *"""
        return _math.SwigPyIterator_previous(self)

    def advance(self, *args, **kwargs):
        """advance(self, n) -> SwigPyIterator"""
        return _math.SwigPyIterator_advance(self, *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, x) -> bool"""
        return _math.SwigPyIterator___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, x) -> bool"""
        return _math.SwigPyIterator___ne__(self, *args, **kwargs)

    def __iadd__(self, *args, **kwargs):
        """__iadd__(self, n) -> SwigPyIterator"""
        return _math.SwigPyIterator___iadd__(self, *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        """__isub__(self, n) -> SwigPyIterator"""
        return _math.SwigPyIterator___isub__(self, *args, **kwargs)

    def __add__(self, *args, **kwargs):
        """__add__(self, n) -> SwigPyIterator"""
        return _math.SwigPyIterator___add__(self, *args, **kwargs)

    def __sub__(self, *args):
        """
        __sub__(self, n) -> SwigPyIterator
        __sub__(self, x) -> ptrdiff_t
        """
        return _math.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self
SwigPyIterator_swigregister = _math.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class VectorOfInt32(object):
    """Proxy of C++ std::vector<(NTA_Int32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfInt32_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfInt32___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfInt32___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< int >::size_type"""
        return _math.VectorOfInt32___len__(self)

    def pop(self):
        """pop(self) -> std::vector< int >::value_type"""
        return _math.VectorOfInt32_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfInt32"""
        return _math.VectorOfInt32___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< int,std::allocator< int > >())"""
        return _math.VectorOfInt32___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfInt32___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfInt32___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfInt32
        __getitem__(self, i) -> std::vector< int >::value_type const &
        """
        return _math.VectorOfInt32___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfInt32___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfInt32_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfInt32_empty(self)

    def size(self):
        """size(self) -> std::vector< int >::size_type"""
        return _math.VectorOfInt32_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfInt32_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfInt32_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< int >::allocator_type"""
        return _math.VectorOfInt32_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< int >::iterator"""
        return _math.VectorOfInt32_begin(self)

    def end(self):
        """end(self) -> std::vector< int >::iterator"""
        return _math.VectorOfInt32_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< int >::reverse_iterator"""
        return _math.VectorOfInt32_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< int >::reverse_iterator"""
        return _math.VectorOfInt32_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfInt32_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< int >::iterator
        erase(self, first, last) -> std::vector< int >::iterator
        """
        return _math.VectorOfInt32_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfInt32
        __init__(self, arg2) -> VectorOfInt32
        __init__(self, size) -> VectorOfInt32
        __init__(self, size, value) -> VectorOfInt32
        """
        this = _math.new_VectorOfInt32(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfInt32_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< int >::value_type const &"""
        return _math.VectorOfInt32_front(self)

    def back(self):
        """back(self) -> std::vector< int >::value_type const &"""
        return _math.VectorOfInt32_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfInt32_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfInt32_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< int >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfInt32_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfInt32_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< int >::size_type"""
        return _math.VectorOfInt32_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfInt32
VectorOfInt32_swigregister = _math.VectorOfInt32_swigregister
VectorOfInt32_swigregister(VectorOfInt32)

class VectorOfInt64(object):
    """Proxy of C++ std::vector<(NTA_Int64)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfInt64_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfInt64___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfInt64___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< long >::size_type"""
        return _math.VectorOfInt64___len__(self)

    def pop(self):
        """pop(self) -> std::vector< long >::value_type"""
        return _math.VectorOfInt64_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfInt64"""
        return _math.VectorOfInt64___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< long,std::allocator< long > >())"""
        return _math.VectorOfInt64___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfInt64___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfInt64___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfInt64
        __getitem__(self, i) -> std::vector< long >::value_type const &
        """
        return _math.VectorOfInt64___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfInt64___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfInt64_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfInt64_empty(self)

    def size(self):
        """size(self) -> std::vector< long >::size_type"""
        return _math.VectorOfInt64_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfInt64_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfInt64_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< long >::allocator_type"""
        return _math.VectorOfInt64_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< long >::iterator"""
        return _math.VectorOfInt64_begin(self)

    def end(self):
        """end(self) -> std::vector< long >::iterator"""
        return _math.VectorOfInt64_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< long >::reverse_iterator"""
        return _math.VectorOfInt64_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< long >::reverse_iterator"""
        return _math.VectorOfInt64_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfInt64_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< long >::iterator
        erase(self, first, last) -> std::vector< long >::iterator
        """
        return _math.VectorOfInt64_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfInt64
        __init__(self, arg2) -> VectorOfInt64
        __init__(self, size) -> VectorOfInt64
        __init__(self, size, value) -> VectorOfInt64
        """
        this = _math.new_VectorOfInt64(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfInt64_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< long >::value_type const &"""
        return _math.VectorOfInt64_front(self)

    def back(self):
        """back(self) -> std::vector< long >::value_type const &"""
        return _math.VectorOfInt64_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfInt64_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfInt64_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< long >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfInt64_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfInt64_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< long >::size_type"""
        return _math.VectorOfInt64_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfInt64
VectorOfInt64_swigregister = _math.VectorOfInt64_swigregister
VectorOfInt64_swigregister(VectorOfInt64)

class VectorOfUInt32(object):
    """Proxy of C++ std::vector<(NTA_UInt32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfUInt32_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfUInt32___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfUInt32___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< unsigned int >::size_type"""
        return _math.VectorOfUInt32___len__(self)

    def pop(self):
        """pop(self) -> std::vector< unsigned int >::value_type"""
        return _math.VectorOfUInt32_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfUInt32"""
        return _math.VectorOfUInt32___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< unsigned int,std::allocator< unsigned int > >())"""
        return _math.VectorOfUInt32___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfUInt32___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfUInt32___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfUInt32
        __getitem__(self, i) -> std::vector< unsigned int >::value_type const &
        """
        return _math.VectorOfUInt32___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfUInt32___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfUInt32_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfUInt32_empty(self)

    def size(self):
        """size(self) -> std::vector< unsigned int >::size_type"""
        return _math.VectorOfUInt32_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfUInt32_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfUInt32_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< unsigned int >::allocator_type"""
        return _math.VectorOfUInt32_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< unsigned int >::iterator"""
        return _math.VectorOfUInt32_begin(self)

    def end(self):
        """end(self) -> std::vector< unsigned int >::iterator"""
        return _math.VectorOfUInt32_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< unsigned int >::reverse_iterator"""
        return _math.VectorOfUInt32_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< unsigned int >::reverse_iterator"""
        return _math.VectorOfUInt32_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfUInt32_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< unsigned int >::iterator
        erase(self, first, last) -> std::vector< unsigned int >::iterator
        """
        return _math.VectorOfUInt32_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfUInt32
        __init__(self, arg2) -> VectorOfUInt32
        __init__(self, size) -> VectorOfUInt32
        __init__(self, size, value) -> VectorOfUInt32
        """
        this = _math.new_VectorOfUInt32(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfUInt32_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< unsigned int >::value_type const &"""
        return _math.VectorOfUInt32_front(self)

    def back(self):
        """back(self) -> std::vector< unsigned int >::value_type const &"""
        return _math.VectorOfUInt32_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfUInt32_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfUInt32_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< unsigned int >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfUInt32_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfUInt32_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< unsigned int >::size_type"""
        return _math.VectorOfUInt32_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfUInt32
VectorOfUInt32_swigregister = _math.VectorOfUInt32_swigregister
VectorOfUInt32_swigregister(VectorOfUInt32)

class VectorOfUInt64(object):
    """Proxy of C++ std::vector<(NTA_UInt64)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfUInt64_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfUInt64___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfUInt64___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< unsigned long >::size_type"""
        return _math.VectorOfUInt64___len__(self)

    def pop(self):
        """pop(self) -> std::vector< unsigned long >::value_type"""
        return _math.VectorOfUInt64_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfUInt64"""
        return _math.VectorOfUInt64___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< unsigned long,std::allocator< unsigned long > >())"""
        return _math.VectorOfUInt64___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfUInt64___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfUInt64___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfUInt64
        __getitem__(self, i) -> std::vector< unsigned long >::value_type const &
        """
        return _math.VectorOfUInt64___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfUInt64___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfUInt64_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfUInt64_empty(self)

    def size(self):
        """size(self) -> std::vector< unsigned long >::size_type"""
        return _math.VectorOfUInt64_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfUInt64_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfUInt64_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< unsigned long >::allocator_type"""
        return _math.VectorOfUInt64_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< unsigned long >::iterator"""
        return _math.VectorOfUInt64_begin(self)

    def end(self):
        """end(self) -> std::vector< unsigned long >::iterator"""
        return _math.VectorOfUInt64_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< unsigned long >::reverse_iterator"""
        return _math.VectorOfUInt64_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< unsigned long >::reverse_iterator"""
        return _math.VectorOfUInt64_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfUInt64_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< unsigned long >::iterator
        erase(self, first, last) -> std::vector< unsigned long >::iterator
        """
        return _math.VectorOfUInt64_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfUInt64
        __init__(self, arg2) -> VectorOfUInt64
        __init__(self, size) -> VectorOfUInt64
        __init__(self, size, value) -> VectorOfUInt64
        """
        this = _math.new_VectorOfUInt64(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfUInt64_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< unsigned long >::value_type const &"""
        return _math.VectorOfUInt64_front(self)

    def back(self):
        """back(self) -> std::vector< unsigned long >::value_type const &"""
        return _math.VectorOfUInt64_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfUInt64_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfUInt64_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< unsigned long >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfUInt64_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfUInt64_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< unsigned long >::size_type"""
        return _math.VectorOfUInt64_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfUInt64
VectorOfUInt64_swigregister = _math.VectorOfUInt64_swigregister
VectorOfUInt64_swigregister(VectorOfUInt64)

class FloatVector(object):
    """Proxy of C++ std::vector<(NTA_Real32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.FloatVector_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.FloatVector___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.FloatVector___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< float >::size_type"""
        return _math.FloatVector___len__(self)

    def pop(self):
        """pop(self) -> std::vector< float >::value_type"""
        return _math.FloatVector_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> FloatVector"""
        return _math.FloatVector___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< float,std::allocator< float > >())"""
        return _math.FloatVector___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.FloatVector___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.FloatVector___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> FloatVector
        __getitem__(self, i) -> std::vector< float >::value_type const &
        """
        return _math.FloatVector___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.FloatVector___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.FloatVector_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.FloatVector_empty(self)

    def size(self):
        """size(self) -> std::vector< float >::size_type"""
        return _math.FloatVector_size(self)

    def clear(self):
        """clear(self)"""
        return _math.FloatVector_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.FloatVector_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< float >::allocator_type"""
        return _math.FloatVector_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< float >::iterator"""
        return _math.FloatVector_begin(self)

    def end(self):
        """end(self) -> std::vector< float >::iterator"""
        return _math.FloatVector_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< float >::reverse_iterator"""
        return _math.FloatVector_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< float >::reverse_iterator"""
        return _math.FloatVector_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.FloatVector_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< float >::iterator
        erase(self, first, last) -> std::vector< float >::iterator
        """
        return _math.FloatVector_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> FloatVector
        __init__(self, arg2) -> FloatVector
        __init__(self, size) -> FloatVector
        __init__(self, size, value) -> FloatVector
        """
        this = _math.new_FloatVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.FloatVector_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< float >::value_type const &"""
        return _math.FloatVector_front(self)

    def back(self):
        """back(self) -> std::vector< float >::value_type const &"""
        return _math.FloatVector_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.FloatVector_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.FloatVector_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< float >::iterator
        insert(self, pos, n, x)
        """
        return _math.FloatVector_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.FloatVector_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< float >::size_type"""
        return _math.FloatVector_capacity(self)

    __swig_destroy__ = _math.delete_FloatVector
FloatVector_swigregister = _math.FloatVector_swigregister
FloatVector_swigregister(FloatVector)

class DoubleVector(object):
    """Proxy of C++ std::vector<(NTA_Real64)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.DoubleVector_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.DoubleVector___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.DoubleVector___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< double >::size_type"""
        return _math.DoubleVector___len__(self)

    def pop(self):
        """pop(self) -> std::vector< double >::value_type"""
        return _math.DoubleVector_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> DoubleVector"""
        return _math.DoubleVector___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< double,std::allocator< double > >())"""
        return _math.DoubleVector___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.DoubleVector___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> DoubleVector
        __getitem__(self, i) -> std::vector< double >::value_type const &
        """
        return _math.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.DoubleVector___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.DoubleVector_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.DoubleVector_empty(self)

    def size(self):
        """size(self) -> std::vector< double >::size_type"""
        return _math.DoubleVector_size(self)

    def clear(self):
        """clear(self)"""
        return _math.DoubleVector_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.DoubleVector_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< double >::allocator_type"""
        return _math.DoubleVector_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< double >::iterator"""
        return _math.DoubleVector_begin(self)

    def end(self):
        """end(self) -> std::vector< double >::iterator"""
        return _math.DoubleVector_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< double >::reverse_iterator"""
        return _math.DoubleVector_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< double >::reverse_iterator"""
        return _math.DoubleVector_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.DoubleVector_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< double >::iterator
        erase(self, first, last) -> std::vector< double >::iterator
        """
        return _math.DoubleVector_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> DoubleVector
        __init__(self, arg2) -> DoubleVector
        __init__(self, size) -> DoubleVector
        __init__(self, size, value) -> DoubleVector
        """
        this = _math.new_DoubleVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.DoubleVector_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< double >::value_type const &"""
        return _math.DoubleVector_front(self)

    def back(self):
        """back(self) -> std::vector< double >::value_type const &"""
        return _math.DoubleVector_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.DoubleVector_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.DoubleVector_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< double >::iterator
        insert(self, pos, n, x)
        """
        return _math.DoubleVector_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.DoubleVector_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< double >::size_type"""
        return _math.DoubleVector_capacity(self)

    __swig_destroy__ = _math.delete_DoubleVector
DoubleVector_swigregister = _math.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)

class StringVector(object):
    """Proxy of C++ std::vector<(std::string)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.StringVector_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.StringVector___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.StringVector___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::string >::size_type"""
        return _math.StringVector___len__(self)

    def pop(self):
        """pop(self) -> std::vector< std::string >::value_type"""
        return _math.StringVector_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> StringVector"""
        return _math.StringVector___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::string,std::allocator< std::string > >())"""
        return _math.StringVector___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.StringVector___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> StringVector
        __getitem__(self, i) -> std::vector< std::string >::value_type const &
        """
        return _math.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.StringVector___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.StringVector_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.StringVector_empty(self)

    def size(self):
        """size(self) -> std::vector< std::string >::size_type"""
        return _math.StringVector_size(self)

    def clear(self):
        """clear(self)"""
        return _math.StringVector_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.StringVector_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::string >::allocator_type"""
        return _math.StringVector_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::string >::iterator"""
        return _math.StringVector_begin(self)

    def end(self):
        """end(self) -> std::vector< std::string >::iterator"""
        return _math.StringVector_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::string >::reverse_iterator"""
        return _math.StringVector_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::string >::reverse_iterator"""
        return _math.StringVector_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.StringVector_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::string >::iterator
        erase(self, first, last) -> std::vector< std::string >::iterator
        """
        return _math.StringVector_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> StringVector
        __init__(self, arg2) -> StringVector
        __init__(self, size) -> StringVector
        __init__(self, size, value) -> StringVector
        """
        this = _math.new_StringVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.StringVector_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::vector< std::string >::value_type const &"""
        return _math.StringVector_front(self)

    def back(self):
        """back(self) -> std::vector< std::string >::value_type const &"""
        return _math.StringVector_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.StringVector_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.StringVector_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::string >::iterator
        insert(self, pos, n, x)
        """
        return _math.StringVector_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.StringVector_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::string >::size_type"""
        return _math.StringVector_capacity(self)

    __swig_destroy__ = _math.delete_StringVector
StringVector_swigregister = _math.StringVector_swigregister
StringVector_swigregister(StringVector)

class StringList(object):
    """Proxy of C++ std::list<(std::string)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.StringList_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.StringList___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.StringList___bool__(self)

    def __len__(self):
        """__len__(self) -> std::list< std::string >::size_type"""
        return _math.StringList___len__(self)

    def pop(self):
        """pop(self) -> std::list< std::string >::value_type"""
        return _math.StringList_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> StringList"""
        return _math.StringList___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::list< std::string,std::allocator< std::string > >())"""
        return _math.StringList___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.StringList___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.StringList___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> StringList
        __getitem__(self, i) -> std::list< std::string >::value_type const &
        """
        return _math.StringList___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.StringList___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.StringList_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.StringList_empty(self)

    def size(self):
        """size(self) -> std::list< std::string >::size_type"""
        return _math.StringList_size(self)

    def clear(self):
        """clear(self)"""
        return _math.StringList_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.StringList_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::list< std::string >::allocator_type"""
        return _math.StringList_get_allocator(self)

    def begin(self):
        """begin(self) -> std::list< std::string >::iterator"""
        return _math.StringList_begin(self)

    def end(self):
        """end(self) -> std::list< std::string >::iterator"""
        return _math.StringList_end(self)

    def rbegin(self):
        """rbegin(self) -> std::list< std::string >::reverse_iterator"""
        return _math.StringList_rbegin(self)

    def rend(self):
        """rend(self) -> std::list< std::string >::reverse_iterator"""
        return _math.StringList_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.StringList_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::list< std::string >::iterator
        erase(self, first, last) -> std::list< std::string >::iterator
        """
        return _math.StringList_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> StringList
        __init__(self, arg2) -> StringList
        __init__(self, size) -> StringList
        __init__(self, size, value) -> StringList
        """
        this = _math.new_StringList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.StringList_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> std::list< std::string >::value_type const &"""
        return _math.StringList_front(self)

    def back(self):
        """back(self) -> std::list< std::string >::value_type const &"""
        return _math.StringList_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.StringList_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.StringList_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::list< std::string >::iterator
        insert(self, pos, n, x)
        """
        return _math.StringList_insert(self, *args)

    def pop_front(self):
        """pop_front(self)"""
        return _math.StringList_pop_front(self)

    def push_front(self, *args, **kwargs):
        """push_front(self, x)"""
        return _math.StringList_push_front(self, *args, **kwargs)

    def reverse(self):
        """reverse(self)"""
        return _math.StringList_reverse(self)

    __swig_destroy__ = _math.delete_StringList
StringList_swigregister = _math.StringList_swigregister
StringList_swigregister(StringList)

class StringSet(object):
    """Proxy of C++ std::set<(std::string)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.StringSet_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.StringSet___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.StringSet___bool__(self)

    def __len__(self):
        """__len__(self) -> std::set< std::string >::size_type"""
        return _math.StringSet___len__(self)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.StringSet_append(self, *args, **kwargs)

    def __contains__(self, *args, **kwargs):
        """__contains__(self, x) -> bool"""
        return _math.StringSet___contains__(self, *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        """__getitem__(self, i) -> std::set< std::string >::value_type"""
        return _math.StringSet___getitem__(self, *args, **kwargs)

    def add(self, *args, **kwargs):
        """add(self, x)"""
        return _math.StringSet_add(self, *args, **kwargs)

    def discard(self, *args, **kwargs):
        """discard(self, x)"""
        return _math.StringSet_discard(self, *args, **kwargs)

    def __init__(self, *args): 
        """
        __init__(self, arg2) -> StringSet
        __init__(self) -> StringSet
        __init__(self, arg2) -> StringSet
        """
        this = _math.new_StringSet(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self):
        """empty(self) -> bool"""
        return _math.StringSet_empty(self)

    def size(self):
        """size(self) -> std::set< std::string >::size_type"""
        return _math.StringSet_size(self)

    def clear(self):
        """clear(self)"""
        return _math.StringSet_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.StringSet_swap(self, *args, **kwargs)

    def count(self, *args, **kwargs):
        """count(self, x) -> std::set< std::string >::size_type"""
        return _math.StringSet_count(self, *args, **kwargs)

    def begin(self):
        """begin(self) -> std::set< std::string >::iterator"""
        return _math.StringSet_begin(self)

    def end(self):
        """end(self) -> std::set< std::string >::iterator"""
        return _math.StringSet_end(self)

    def rbegin(self):
        """rbegin(self) -> std::set< std::string >::reverse_iterator"""
        return _math.StringSet_rbegin(self)

    def rend(self):
        """rend(self) -> std::set< std::string >::reverse_iterator"""
        return _math.StringSet_rend(self)

    def erase(self, *args):
        """
        erase(self, x) -> std::set< std::string >::size_type
        erase(self, pos)
        erase(self, first, last)
        """
        return _math.StringSet_erase(self, *args)

    def find(self, *args, **kwargs):
        """find(self, x) -> std::set< std::string >::iterator"""
        return _math.StringSet_find(self, *args, **kwargs)

    def lower_bound(self, *args, **kwargs):
        """lower_bound(self, x) -> std::set< std::string >::iterator"""
        return _math.StringSet_lower_bound(self, *args, **kwargs)

    def upper_bound(self, *args, **kwargs):
        """upper_bound(self, x) -> std::set< std::string >::iterator"""
        return _math.StringSet_upper_bound(self, *args, **kwargs)

    def equal_range(self, *args, **kwargs):
        """equal_range(self, x) -> std::pair< std::set< std::string >::iterator,std::set< std::string >::iterator >"""
        return _math.StringSet_equal_range(self, *args, **kwargs)

    def insert(self, *args, **kwargs):
        """insert(self, __x) -> std::pair< std::set< std::string >::iterator,bool >"""
        return _math.StringSet_insert(self, *args, **kwargs)

    __swig_destroy__ = _math.delete_StringSet
StringSet_swigregister = _math.StringSet_swigregister
StringSet_swigregister(StringSet)

class StringMap(object):
    """Proxy of C++ std::map<(std::string,std::string)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.StringMap_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.StringMap___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.StringMap___bool__(self)

    def __len__(self):
        """__len__(self) -> std::map< std::string,std::string >::size_type"""
        return _math.StringMap___len__(self)

    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args, **kwargs):
        """__getitem__(self, key) -> std::map< std::string,std::string >::mapped_type const &"""
        return _math.StringMap___getitem__(self, *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        """__delitem__(self, key)"""
        return _math.StringMap___delitem__(self, *args, **kwargs)

    def has_key(self, *args, **kwargs):
        """has_key(self, key) -> bool"""
        return _math.StringMap_has_key(self, *args, **kwargs)

    def keys(self):
        """keys(self) -> PyObject *"""
        return _math.StringMap_keys(self)

    def values(self):
        """values(self) -> PyObject *"""
        return _math.StringMap_values(self)

    def items(self):
        """items(self) -> PyObject *"""
        return _math.StringMap_items(self)

    def __contains__(self, *args, **kwargs):
        """__contains__(self, key) -> bool"""
        return _math.StringMap___contains__(self, *args, **kwargs)

    def key_iterator(self):
        """key_iterator(self) -> SwigPyIterator"""
        return _math.StringMap_key_iterator(self)

    def value_iterator(self):
        """value_iterator(self) -> SwigPyIterator"""
        return _math.StringMap_value_iterator(self)

    def __setitem__(self, *args):
        """
        __setitem__(self, key)
        __setitem__(self, key, x)
        """
        return _math.StringMap___setitem__(self, *args)

    def asdict(self):
        """asdict(self) -> PyObject *"""
        return _math.StringMap_asdict(self)

    def __init__(self, *args): 
        """
        __init__(self, arg2) -> StringMap
        __init__(self) -> StringMap
        __init__(self, arg2) -> StringMap
        """
        this = _math.new_StringMap(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self):
        """empty(self) -> bool"""
        return _math.StringMap_empty(self)

    def size(self):
        """size(self) -> std::map< std::string,std::string >::size_type"""
        return _math.StringMap_size(self)

    def clear(self):
        """clear(self)"""
        return _math.StringMap_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.StringMap_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::map< std::string,std::string >::allocator_type"""
        return _math.StringMap_get_allocator(self)

    def begin(self):
        """begin(self) -> std::map< std::string,std::string >::iterator"""
        return _math.StringMap_begin(self)

    def end(self):
        """end(self) -> std::map< std::string,std::string >::iterator"""
        return _math.StringMap_end(self)

    def rbegin(self):
        """rbegin(self) -> std::map< std::string,std::string >::reverse_iterator"""
        return _math.StringMap_rbegin(self)

    def rend(self):
        """rend(self) -> std::map< std::string,std::string >::reverse_iterator"""
        return _math.StringMap_rend(self)

    def count(self, *args, **kwargs):
        """count(self, x) -> std::map< std::string,std::string >::size_type"""
        return _math.StringMap_count(self, *args, **kwargs)

    def erase(self, *args):
        """
        erase(self, x) -> std::map< std::string,std::string >::size_type
        erase(self, position)
        erase(self, first, last)
        """
        return _math.StringMap_erase(self, *args)

    def find(self, *args, **kwargs):
        """find(self, x) -> std::map< std::string,std::string >::iterator"""
        return _math.StringMap_find(self, *args, **kwargs)

    def lower_bound(self, *args, **kwargs):
        """lower_bound(self, x) -> std::map< std::string,std::string >::iterator"""
        return _math.StringMap_lower_bound(self, *args, **kwargs)

    def upper_bound(self, *args, **kwargs):
        """upper_bound(self, x) -> std::map< std::string,std::string >::iterator"""
        return _math.StringMap_upper_bound(self, *args, **kwargs)

    __swig_destroy__ = _math.delete_StringMap
StringMap_swigregister = _math.StringMap_swigregister
StringMap_swigregister(StringMap)

class StringStringPair(object):
    """Proxy of C++ std::pair<(std::string,std::string)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> StringStringPair
        __init__(self, first, second) -> StringStringPair
        __init__(self, p) -> StringStringPair
        """
        this = _math.new_StringStringPair(*args)
        try: self.this.append(this)
        except: self.this = this
    first = _swig_property(_math.StringStringPair_first_get, _math.StringStringPair_first_set)
    second = _swig_property(_math.StringStringPair_second_get, _math.StringStringPair_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _math.delete_StringStringPair
StringStringPair_swigregister = _math.StringStringPair_swigregister
StringStringPair_swigregister(StringStringPair)

class StringStringList(object):
    """Proxy of C++ std::vector<(std::pair<(std::string,std::string)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.StringStringList_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.StringStringList___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.StringStringList___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::pair< std::string,std::string > >::size_type"""
        return _math.StringStringList___len__(self)

    def pop(self):
        """pop(self) -> StringStringPair"""
        return _math.StringStringList_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> StringStringList"""
        return _math.StringStringList___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::pair< std::string,std::string >,std::allocator< std::pair< std::string,std::string > > >())"""
        return _math.StringStringList___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.StringStringList___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.StringStringList___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> StringStringList
        __getitem__(self, i) -> StringStringPair
        """
        return _math.StringStringList___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.StringStringList___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.StringStringList_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.StringStringList_empty(self)

    def size(self):
        """size(self) -> std::vector< std::pair< std::string,std::string > >::size_type"""
        return _math.StringStringList_size(self)

    def clear(self):
        """clear(self)"""
        return _math.StringStringList_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.StringStringList_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::pair< std::string,std::string > >::allocator_type"""
        return _math.StringStringList_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::pair< std::string,std::string > >::iterator"""
        return _math.StringStringList_begin(self)

    def end(self):
        """end(self) -> std::vector< std::pair< std::string,std::string > >::iterator"""
        return _math.StringStringList_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::pair< std::string,std::string > >::reverse_iterator"""
        return _math.StringStringList_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::pair< std::string,std::string > >::reverse_iterator"""
        return _math.StringStringList_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.StringStringList_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::pair< std::string,std::string > >::iterator
        erase(self, first, last) -> std::vector< std::pair< std::string,std::string > >::iterator
        """
        return _math.StringStringList_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> StringStringList
        __init__(self, arg2) -> StringStringList
        __init__(self, size) -> StringStringList
        __init__(self, size, value) -> StringStringList
        """
        this = _math.new_StringStringList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.StringStringList_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> StringStringPair"""
        return _math.StringStringList_front(self)

    def back(self):
        """back(self) -> StringStringPair"""
        return _math.StringStringList_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.StringStringList_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.StringStringList_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::pair< std::string,std::string > >::iterator
        insert(self, pos, n, x)
        """
        return _math.StringStringList_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.StringStringList_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::pair< std::string,std::string > >::size_type"""
        return _math.StringStringList_capacity(self)

    __swig_destroy__ = _math.delete_StringStringList
StringStringList_swigregister = _math.StringStringList_swigregister
StringStringList_swigregister(StringStringList)

class StringMapList(object):
    """Proxy of C++ std::vector<(std::map<(std::string,std::string)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.StringMapList_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.StringMapList___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.StringMapList___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::map< std::string,std::string > >::size_type"""
        return _math.StringMapList___len__(self)

    def pop(self):
        """pop(self) -> StringMap"""
        return _math.StringMapList_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> StringMapList"""
        return _math.StringMapList___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > >,std::allocator< std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > > > >())"""
        return _math.StringMapList___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.StringMapList___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.StringMapList___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> StringMapList
        __getitem__(self, i) -> StringMap
        """
        return _math.StringMapList___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.StringMapList___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.StringMapList_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.StringMapList_empty(self)

    def size(self):
        """size(self) -> std::vector< std::map< std::string,std::string > >::size_type"""
        return _math.StringMapList_size(self)

    def clear(self):
        """clear(self)"""
        return _math.StringMapList_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.StringMapList_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::map< std::string,std::string > >::allocator_type"""
        return _math.StringMapList_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::map< std::string,std::string > >::iterator"""
        return _math.StringMapList_begin(self)

    def end(self):
        """end(self) -> std::vector< std::map< std::string,std::string > >::iterator"""
        return _math.StringMapList_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::map< std::string,std::string > >::reverse_iterator"""
        return _math.StringMapList_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::map< std::string,std::string > >::reverse_iterator"""
        return _math.StringMapList_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.StringMapList_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::map< std::string,std::string > >::iterator
        erase(self, first, last) -> std::vector< std::map< std::string,std::string > >::iterator
        """
        return _math.StringMapList_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> StringMapList
        __init__(self, arg2) -> StringMapList
        __init__(self, size) -> StringMapList
        __init__(self, size, value) -> StringMapList
        """
        this = _math.new_StringMapList(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.StringMapList_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> StringMap"""
        return _math.StringMapList_front(self)

    def back(self):
        """back(self) -> StringMap"""
        return _math.StringMapList_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.StringMapList_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.StringMapList_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::map< std::string,std::string > >::iterator
        insert(self, pos, n, x)
        """
        return _math.StringMapList_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.StringMapList_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::map< std::string,std::string > >::size_type"""
        return _math.StringMapList_capacity(self)

    __swig_destroy__ = _math.delete_StringMapList
StringMapList_swigregister = _math.StringMapList_swigregister
StringMapList_swigregister(StringMapList)

class StringIntPair(object):
    """Proxy of C++ std::pair<(std::string,NTA_Int32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> StringIntPair
        __init__(self, first, second) -> StringIntPair
        __init__(self, p) -> StringIntPair
        """
        this = _math.new_StringIntPair(*args)
        try: self.this.append(this)
        except: self.this = this
    first = _swig_property(_math.StringIntPair_first_get, _math.StringIntPair_first_set)
    second = _swig_property(_math.StringIntPair_second_get, _math.StringIntPair_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _math.delete_StringIntPair
StringIntPair_swigregister = _math.StringIntPair_swigregister
StringIntPair_swigregister(StringIntPair)

class PairOfUInt32(object):
    """Proxy of C++ std::pair<(nupic::UInt32,nupic::UInt32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PairOfUInt32
        __init__(self, first, second) -> PairOfUInt32
        __init__(self, p) -> PairOfUInt32
        """
        this = _math.new_PairOfUInt32(*args)
        try: self.this.append(this)
        except: self.this = this
    first = _swig_property(_math.PairOfUInt32_first_get, _math.PairOfUInt32_first_set)
    second = _swig_property(_math.PairOfUInt32_second_get, _math.PairOfUInt32_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _math.delete_PairOfUInt32
PairOfUInt32_swigregister = _math.PairOfUInt32_swigregister
PairOfUInt32_swigregister(PairOfUInt32)

class VectorOfPairsOfUInt32(object):
    """Proxy of C++ std::vector<(std::pair<(nupic::UInt32,nupic::UInt32)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfPairsOfUInt32_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfPairsOfUInt32___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfPairsOfUInt32___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::pair< unsigned int,unsigned int > >::size_type"""
        return _math.VectorOfPairsOfUInt32___len__(self)

    def pop(self):
        """pop(self) -> PairOfUInt32"""
        return _math.VectorOfPairsOfUInt32_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfPairsOfUInt32"""
        return _math.VectorOfPairsOfUInt32___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::pair< nupic::UInt32,nupic::UInt32 >,std::allocator< std::pair< nupic::UInt32,nupic::UInt32 > > >())"""
        return _math.VectorOfPairsOfUInt32___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfPairsOfUInt32___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfPairsOfUInt32___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfPairsOfUInt32
        __getitem__(self, i) -> PairOfUInt32
        """
        return _math.VectorOfPairsOfUInt32___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfPairsOfUInt32___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfPairsOfUInt32_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfPairsOfUInt32_empty(self)

    def size(self):
        """size(self) -> std::vector< std::pair< unsigned int,unsigned int > >::size_type"""
        return _math.VectorOfPairsOfUInt32_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfPairsOfUInt32_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfPairsOfUInt32_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::pair< unsigned int,unsigned int > >::allocator_type"""
        return _math.VectorOfPairsOfUInt32_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::pair< unsigned int,unsigned int > >::iterator"""
        return _math.VectorOfPairsOfUInt32_begin(self)

    def end(self):
        """end(self) -> std::vector< std::pair< unsigned int,unsigned int > >::iterator"""
        return _math.VectorOfPairsOfUInt32_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::pair< unsigned int,unsigned int > >::reverse_iterator"""
        return _math.VectorOfPairsOfUInt32_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::pair< unsigned int,unsigned int > >::reverse_iterator"""
        return _math.VectorOfPairsOfUInt32_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfPairsOfUInt32_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::pair< unsigned int,unsigned int > >::iterator
        erase(self, first, last) -> std::vector< std::pair< unsigned int,unsigned int > >::iterator
        """
        return _math.VectorOfPairsOfUInt32_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfPairsOfUInt32
        __init__(self, arg2) -> VectorOfPairsOfUInt32
        __init__(self, size) -> VectorOfPairsOfUInt32
        __init__(self, size, value) -> VectorOfPairsOfUInt32
        """
        this = _math.new_VectorOfPairsOfUInt32(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfPairsOfUInt32_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> PairOfUInt32"""
        return _math.VectorOfPairsOfUInt32_front(self)

    def back(self):
        """back(self) -> PairOfUInt32"""
        return _math.VectorOfPairsOfUInt32_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfPairsOfUInt32_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfPairsOfUInt32_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::pair< unsigned int,unsigned int > >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfPairsOfUInt32_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfPairsOfUInt32_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::pair< unsigned int,unsigned int > >::size_type"""
        return _math.VectorOfPairsOfUInt32_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfPairsOfUInt32
VectorOfPairsOfUInt32_swigregister = _math.VectorOfPairsOfUInt32_swigregister
VectorOfPairsOfUInt32_swigregister(VectorOfPairsOfUInt32)

class VectorOfVectorsOfPairsOfUInt32(object):
    """Proxy of C++ std::vector<(std::vector<(std::pair<(nupic::UInt32,nupic::UInt32)>)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfVectorsOfPairsOfUInt32_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfVectorsOfPairsOfUInt32___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfVectorsOfPairsOfUInt32___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::size_type"""
        return _math.VectorOfVectorsOfPairsOfUInt32___len__(self)

    def pop(self):
        """pop(self) -> VectorOfPairsOfUInt32"""
        return _math.VectorOfVectorsOfPairsOfUInt32_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfVectorsOfPairsOfUInt32"""
        return _math.VectorOfVectorsOfPairsOfUInt32___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::vector< std::pair< nupic::UInt32,nupic::UInt32 >,std::allocator< std::pair< nupic::UInt32,nupic::UInt32 > > >,std::allocator< std::vector< std::pair< nupic::UInt32,nupic::UInt32 >,std::allocator< std::pair< nupic::UInt32,nupic::UInt32 > > > > >())"""
        return _math.VectorOfVectorsOfPairsOfUInt32___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfVectorsOfPairsOfUInt32___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfVectorsOfPairsOfUInt32___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfVectorsOfPairsOfUInt32
        __getitem__(self, i) -> VectorOfPairsOfUInt32
        """
        return _math.VectorOfVectorsOfPairsOfUInt32___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfVectorsOfPairsOfUInt32___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfVectorsOfPairsOfUInt32_empty(self)

    def size(self):
        """size(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::size_type"""
        return _math.VectorOfVectorsOfPairsOfUInt32_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::allocator_type"""
        return _math.VectorOfVectorsOfPairsOfUInt32_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::iterator"""
        return _math.VectorOfVectorsOfPairsOfUInt32_begin(self)

    def end(self):
        """end(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::iterator"""
        return _math.VectorOfVectorsOfPairsOfUInt32_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::reverse_iterator"""
        return _math.VectorOfVectorsOfPairsOfUInt32_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::reverse_iterator"""
        return _math.VectorOfVectorsOfPairsOfUInt32_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::iterator
        erase(self, first, last) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::iterator
        """
        return _math.VectorOfVectorsOfPairsOfUInt32_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfVectorsOfPairsOfUInt32
        __init__(self, arg2) -> VectorOfVectorsOfPairsOfUInt32
        __init__(self, size) -> VectorOfVectorsOfPairsOfUInt32
        __init__(self, size, value) -> VectorOfVectorsOfPairsOfUInt32
        """
        this = _math.new_VectorOfVectorsOfPairsOfUInt32(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> VectorOfPairsOfUInt32"""
        return _math.VectorOfVectorsOfPairsOfUInt32_front(self)

    def back(self):
        """back(self) -> VectorOfPairsOfUInt32"""
        return _math.VectorOfVectorsOfPairsOfUInt32_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfVectorsOfPairsOfUInt32_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfVectorsOfPairsOfUInt32_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfVectorsOfPairsOfUInt32_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::vector< std::pair< unsigned int,unsigned int > > >::size_type"""
        return _math.VectorOfVectorsOfPairsOfUInt32_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfVectorsOfPairsOfUInt32
VectorOfVectorsOfPairsOfUInt32_swigregister = _math.VectorOfVectorsOfPairsOfUInt32_swigregister
VectorOfVectorsOfPairsOfUInt32_swigregister(VectorOfVectorsOfPairsOfUInt32)

class PairUInt32Real32(object):
    """Proxy of C++ std::pair<(nupic::UInt32,nupic::Real32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PairUInt32Real32
        __init__(self, first, second) -> PairUInt32Real32
        __init__(self, p) -> PairUInt32Real32
        """
        this = _math.new_PairUInt32Real32(*args)
        try: self.this.append(this)
        except: self.this = this
    first = _swig_property(_math.PairUInt32Real32_first_get, _math.PairUInt32Real32_first_set)
    second = _swig_property(_math.PairUInt32Real32_second_get, _math.PairUInt32Real32_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _math.delete_PairUInt32Real32
PairUInt32Real32_swigregister = _math.PairUInt32Real32_swigregister
PairUInt32Real32_swigregister(PairUInt32Real32)

class PairUInt32Real64(object):
    """Proxy of C++ std::pair<(nupic::UInt32,nupic::Real64)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PairUInt32Real64
        __init__(self, first, second) -> PairUInt32Real64
        __init__(self, p) -> PairUInt32Real64
        """
        this = _math.new_PairUInt32Real64(*args)
        try: self.this.append(this)
        except: self.this = this
    first = _swig_property(_math.PairUInt32Real64_first_get, _math.PairUInt32Real64_first_set)
    second = _swig_property(_math.PairUInt32Real64_second_get, _math.PairUInt32Real64_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _math.delete_PairUInt32Real64
PairUInt32Real64_swigregister = _math.PairUInt32Real64_swigregister
PairUInt32Real64_swigregister(PairUInt32Real64)

class VectorOfPairsUInt32Real32(object):
    """Proxy of C++ std::vector<(std::pair<(nupic::UInt32,nupic::Real32)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfPairsUInt32Real32_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfPairsUInt32Real32___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfPairsUInt32Real32___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::pair< unsigned int,float > >::size_type"""
        return _math.VectorOfPairsUInt32Real32___len__(self)

    def pop(self):
        """pop(self) -> PairUInt32Real32"""
        return _math.VectorOfPairsUInt32Real32_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfPairsUInt32Real32"""
        return _math.VectorOfPairsUInt32Real32___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::pair< nupic::UInt32,nupic::Real32 >,std::allocator< std::pair< nupic::UInt32,nupic::Real32 > > >())"""
        return _math.VectorOfPairsUInt32Real32___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfPairsUInt32Real32___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfPairsUInt32Real32___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfPairsUInt32Real32
        __getitem__(self, i) -> PairUInt32Real32
        """
        return _math.VectorOfPairsUInt32Real32___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfPairsUInt32Real32___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfPairsUInt32Real32_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfPairsUInt32Real32_empty(self)

    def size(self):
        """size(self) -> std::vector< std::pair< unsigned int,float > >::size_type"""
        return _math.VectorOfPairsUInt32Real32_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfPairsUInt32Real32_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfPairsUInt32Real32_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::pair< unsigned int,float > >::allocator_type"""
        return _math.VectorOfPairsUInt32Real32_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::pair< unsigned int,float > >::iterator"""
        return _math.VectorOfPairsUInt32Real32_begin(self)

    def end(self):
        """end(self) -> std::vector< std::pair< unsigned int,float > >::iterator"""
        return _math.VectorOfPairsUInt32Real32_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::pair< unsigned int,float > >::reverse_iterator"""
        return _math.VectorOfPairsUInt32Real32_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::pair< unsigned int,float > >::reverse_iterator"""
        return _math.VectorOfPairsUInt32Real32_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfPairsUInt32Real32_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::pair< unsigned int,float > >::iterator
        erase(self, first, last) -> std::vector< std::pair< unsigned int,float > >::iterator
        """
        return _math.VectorOfPairsUInt32Real32_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfPairsUInt32Real32
        __init__(self, arg2) -> VectorOfPairsUInt32Real32
        __init__(self, size) -> VectorOfPairsUInt32Real32
        __init__(self, size, value) -> VectorOfPairsUInt32Real32
        """
        this = _math.new_VectorOfPairsUInt32Real32(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfPairsUInt32Real32_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> PairUInt32Real32"""
        return _math.VectorOfPairsUInt32Real32_front(self)

    def back(self):
        """back(self) -> PairUInt32Real32"""
        return _math.VectorOfPairsUInt32Real32_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfPairsUInt32Real32_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfPairsUInt32Real32_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::pair< unsigned int,float > >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfPairsUInt32Real32_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfPairsUInt32Real32_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::pair< unsigned int,float > >::size_type"""
        return _math.VectorOfPairsUInt32Real32_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfPairsUInt32Real32
VectorOfPairsUInt32Real32_swigregister = _math.VectorOfPairsUInt32Real32_swigregister
VectorOfPairsUInt32Real32_swigregister(VectorOfPairsUInt32Real32)

class VectorOfPairsUInt32Real64(object):
    """Proxy of C++ std::vector<(std::pair<(nupic::UInt32,nupic::Real64)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def iterator(self):
        """iterator(self) -> SwigPyIterator"""
        return _math.VectorOfPairsUInt32Real64_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """__nonzero__(self) -> bool"""
        return _math.VectorOfPairsUInt32Real64___nonzero__(self)

    def __bool__(self):
        """__bool__(self) -> bool"""
        return _math.VectorOfPairsUInt32Real64___bool__(self)

    def __len__(self):
        """__len__(self) -> std::vector< std::pair< unsigned int,double > >::size_type"""
        return _math.VectorOfPairsUInt32Real64___len__(self)

    def pop(self):
        """pop(self) -> PairUInt32Real64"""
        return _math.VectorOfPairsUInt32Real64_pop(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfPairsUInt32Real64"""
        return _math.VectorOfPairsUInt32Real64___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, v=std::vector< std::pair< nupic::UInt32,nupic::Real64 >,std::allocator< std::pair< nupic::UInt32,nupic::Real64 > > >())"""
        return _math.VectorOfPairsUInt32Real64___setslice__(self, *args, **kwargs)

    def __delslice__(self, *args, **kwargs):
        """__delslice__(self, i, j)"""
        return _math.VectorOfPairsUInt32Real64___delslice__(self, *args, **kwargs)

    def __delitem__(self, *args):
        """
        __delitem__(self, i)
        __delitem__(self, slice)
        """
        return _math.VectorOfPairsUInt32Real64___delitem__(self, *args)

    def __getitem__(self, *args):
        """
        __getitem__(self, slice) -> VectorOfPairsUInt32Real64
        __getitem__(self, i) -> PairUInt32Real64
        """
        return _math.VectorOfPairsUInt32Real64___getitem__(self, *args)

    def __setitem__(self, *args):
        """
        __setitem__(self, slice, v)
        __setitem__(self, slice)
        __setitem__(self, i, x)
        """
        return _math.VectorOfPairsUInt32Real64___setitem__(self, *args)

    def append(self, *args, **kwargs):
        """append(self, x)"""
        return _math.VectorOfPairsUInt32Real64_append(self, *args, **kwargs)

    def empty(self):
        """empty(self) -> bool"""
        return _math.VectorOfPairsUInt32Real64_empty(self)

    def size(self):
        """size(self) -> std::vector< std::pair< unsigned int,double > >::size_type"""
        return _math.VectorOfPairsUInt32Real64_size(self)

    def clear(self):
        """clear(self)"""
        return _math.VectorOfPairsUInt32Real64_clear(self)

    def swap(self, *args, **kwargs):
        """swap(self, v)"""
        return _math.VectorOfPairsUInt32Real64_swap(self, *args, **kwargs)

    def get_allocator(self):
        """get_allocator(self) -> std::vector< std::pair< unsigned int,double > >::allocator_type"""
        return _math.VectorOfPairsUInt32Real64_get_allocator(self)

    def begin(self):
        """begin(self) -> std::vector< std::pair< unsigned int,double > >::iterator"""
        return _math.VectorOfPairsUInt32Real64_begin(self)

    def end(self):
        """end(self) -> std::vector< std::pair< unsigned int,double > >::iterator"""
        return _math.VectorOfPairsUInt32Real64_end(self)

    def rbegin(self):
        """rbegin(self) -> std::vector< std::pair< unsigned int,double > >::reverse_iterator"""
        return _math.VectorOfPairsUInt32Real64_rbegin(self)

    def rend(self):
        """rend(self) -> std::vector< std::pair< unsigned int,double > >::reverse_iterator"""
        return _math.VectorOfPairsUInt32Real64_rend(self)

    def pop_back(self):
        """pop_back(self)"""
        return _math.VectorOfPairsUInt32Real64_pop_back(self)

    def erase(self, *args):
        """
        erase(self, pos) -> std::vector< std::pair< unsigned int,double > >::iterator
        erase(self, first, last) -> std::vector< std::pair< unsigned int,double > >::iterator
        """
        return _math.VectorOfPairsUInt32Real64_erase(self, *args)

    def __init__(self, *args): 
        """
        __init__(self) -> VectorOfPairsUInt32Real64
        __init__(self, arg2) -> VectorOfPairsUInt32Real64
        __init__(self, size) -> VectorOfPairsUInt32Real64
        __init__(self, size, value) -> VectorOfPairsUInt32Real64
        """
        this = _math.new_VectorOfPairsUInt32Real64(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args, **kwargs):
        """push_back(self, x)"""
        return _math.VectorOfPairsUInt32Real64_push_back(self, *args, **kwargs)

    def front(self):
        """front(self) -> PairUInt32Real64"""
        return _math.VectorOfPairsUInt32Real64_front(self)

    def back(self):
        """back(self) -> PairUInt32Real64"""
        return _math.VectorOfPairsUInt32Real64_back(self)

    def assign(self, *args, **kwargs):
        """assign(self, n, x)"""
        return _math.VectorOfPairsUInt32Real64_assign(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, new_size)
        resize(self, new_size, x)
        """
        return _math.VectorOfPairsUInt32Real64_resize(self, *args)

    def insert(self, *args):
        """
        insert(self, pos, x) -> std::vector< std::pair< unsigned int,double > >::iterator
        insert(self, pos, n, x)
        """
        return _math.VectorOfPairsUInt32Real64_insert(self, *args)

    def reserve(self, *args, **kwargs):
        """reserve(self, n)"""
        return _math.VectorOfPairsUInt32Real64_reserve(self, *args, **kwargs)

    def capacity(self):
        """capacity(self) -> std::vector< std::pair< unsigned int,double > >::size_type"""
        return _math.VectorOfPairsUInt32Real64_capacity(self)

    __swig_destroy__ = _math.delete_VectorOfPairsUInt32Real64
VectorOfPairsUInt32Real64_swigregister = _math.VectorOfPairsUInt32Real64_swigregister
VectorOfPairsUInt32Real64_swigregister(VectorOfPairsUInt32Real64)


def GetBasicTypeFromName(*args, **kwargs):
  """
    GetBasicTypeFromName(type) -> NTA_BasicType

    GetBasicTypeFromName(typeName) -> int

    Internal use.
    Finds a base type enumeration given a type name.

    """
  return _math.GetBasicTypeFromName(*args, **kwargs)

def GetBasicTypeSize(*args, **kwargs):
  """
    GetBasicTypeSize(type) -> size_t

    GetBasicTypeFromName(typeName) -> int

    Internal use.
    Gets the number of bytes use to specify the named
    type in C code.

    """
  return _math.GetBasicTypeSize(*args, **kwargs)
import numpy
def GetNumpyDataType(typeName):
  """Gets the numpy dtype associated with a particular NuPIC 
  base type name. The only supported type name is 
  'NTA_Real', which returns a numpy dtype of numpy.float32.
  The returned value can be used with numpy functions like
  numpy.array(..., dtype=dtype) and numpy.astype(..., dtype=dtype).
  """
  if typeName == "NTA_Real": return numpy.float32
  elif typeName == "NTA_Real32": return numpy.float32
  elif typeName == "NTA_Real64": return numpy.float64
  else: raise RuntimeError("Unsupported type name: {}".format(typeName))

def GetNTARealType():
  """Gets the name of the NuPIC floating point base type, 
  which is used for most internal calculations.
  This base type name can be used with GetBasicTypeFromName(),
  GetBasicTypeSize(), and GetNumpyDataType().
  """
  return "NTA_Real"
def GetNTAReal():
  """Gets the numpy dtype of the NuPIC floating point base type,
  which is used for most internal calculations.
  The returned value can be used with numpy functions like
  numpy.array(..., dtype=dtype) and numpy.astype(..., dtype=dtype).
  """
  return GetNumpyDataType(GetNTARealType())

import numbers



def getGlobalEpsilon():
  """getGlobalEpsilon() -> nupic::Real"""
  return _math.getGlobalEpsilon()

def INVARIANT(*args, **kwargs):
  """INVARIANT(cond, msg) -> bool"""
  return _math.INVARIANT(*args, **kwargs)

def emod(*args, **kwargs):
  """emod(x, m) -> int"""
  return _math.emod(*args, **kwargs)
class SparseMatrixAlgorithms(object):
    """Proxy of C++ nupic::SparseMatrixAlgorithms class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(self) -> SparseMatrixAlgorithms"""
        this = _math.new_SparseMatrixAlgorithms()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _math.delete_SparseMatrixAlgorithms
SparseMatrixAlgorithms_swigregister = _math.SparseMatrixAlgorithms_swigregister
SparseMatrixAlgorithms_swigregister(SparseMatrixAlgorithms)
cvar = _math.cvar
Epsilon = cvar.Epsilon

class LogSumApprox(object):
    """Proxy of C++ nupic::LogSumApprox class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, n_=5000000, min_a_=-28, max_a_=28, trace_=False) -> LogSumApprox"""
        this = _math.new_LogSumApprox(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def compute_table(self):
        """compute_table(self)"""
        return _math.LogSumApprox_compute_table(self)

    def index(self, *args, **kwargs):
        """index(self, a, b) -> int"""
        return _math.LogSumApprox_index(self, *args, **kwargs)

    def fast_sum_of_logs(self, *args, **kwargs):
        """fast_sum_of_logs(self, a, b) -> nupic::LogSumApprox::value_type"""
        return _math.LogSumApprox_fast_sum_of_logs(self, *args, **kwargs)

    def sum_of_logs(self, *args, **kwargs):
        """sum_of_logs(self, a, b) -> nupic::LogSumApprox::value_type"""
        return _math.LogSumApprox_sum_of_logs(self, *args, **kwargs)

    def logSum(self, *args, **kwargs):
        """logSum(self, x, y) -> nupic::Real32"""
        return _math.LogSumApprox_logSum(self, *args, **kwargs)

    def fastLogSum(self, *args, **kwargs):
        """fastLogSum(self, x, y) -> nupic::Real32"""
        return _math.LogSumApprox_fastLogSum(self, *args, **kwargs)

    __swig_destroy__ = _math.delete_LogSumApprox
LogSumApprox_swigregister = _math.LogSumApprox_swigregister
LogSumApprox_swigregister(LogSumApprox)

class LogDiffApprox(object):
    """Proxy of C++ nupic::LogDiffApprox class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, n_=5000000, min_a_=1e-10, max_a_=28, trace_=False): 
        """__init__(self, n_=5000000, min_a_=1e-10, max_a_=28, trace_=False) -> LogDiffApprox"""
        this = _math.new_LogDiffApprox(n_, min_a_, max_a_, trace_)
        try: self.this.append(this)
        except: self.this = this
    def compute_table(self):
        """compute_table(self)"""
        return _math.LogDiffApprox_compute_table(self)

    def index(self, *args, **kwargs):
        """index(self, a, b) -> int"""
        return _math.LogDiffApprox_index(self, *args, **kwargs)

    def fast_diff_of_logs(self, *args, **kwargs):
        """fast_diff_of_logs(self, a, b) -> nupic::LogDiffApprox::value_type"""
        return _math.LogDiffApprox_fast_diff_of_logs(self, *args, **kwargs)

    def diff_of_logs(self, *args, **kwargs):
        """diff_of_logs(self, a, b) -> nupic::LogDiffApprox::value_type"""
        return _math.LogDiffApprox_diff_of_logs(self, *args, **kwargs)

    def logDiff(self, *args, **kwargs):
        """logDiff(self, x, y) -> nupic::Real32"""
        return _math.LogDiffApprox_logDiff(self, *args, **kwargs)

    def fastLogDiff(self, *args, **kwargs):
        """fastLogDiff(self, x, y) -> nupic::Real32"""
        return _math.LogDiffApprox_fastLogDiff(self, *args, **kwargs)

    __swig_destroy__ = _math.delete_LogDiffApprox
LogDiffApprox_swigregister = _math.LogDiffApprox_swigregister
LogDiffApprox_swigregister(LogDiffApprox)

class _Domain32(object):
    """Proxy of C++ nupic::Domain<(nupic::UInt32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, o) -> _Domain32"""
        this = _math.new__Domain32(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def rank(self):
        """rank(self) -> unsigned int"""
        return _math._Domain32_rank(self)

    def empty(self):
        """empty(self) -> bool"""
        return _math._Domain32_empty(self)

    def size_elts(self):
        """size_elts(self) -> unsigned int"""
        return _math._Domain32_size_elts(self)

    def getNOpenDims(self):
        """getNOpenDims(self) -> unsigned int"""
        return _math._Domain32_getNOpenDims(self)

    def hasClosedDims(self):
        """hasClosedDims(self) -> bool"""
        return _math._Domain32_hasClosedDims(self)

    def getNClosedDims(self):
        """getNClosedDims(self) -> unsigned int"""
        return _math._Domain32_getNClosedDims(self)

    def includes(self, *args, **kwargs):
        """includes(self, d) -> bool"""
        return _math._Domain32_includes(self, *args, **kwargs)

    __swig_destroy__ = _math.delete__Domain32
_Domain32_swigregister = _math._Domain32_swigregister
_Domain32_swigregister(_Domain32)

class _Domain2D32(_Domain32):
    """Proxy of C++ nupic::Domain2D<(nupic::UInt32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, first_row, row_end, first_col, col_end) -> _Domain2D32"""
        this = _math.new__Domain2D32(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def getFirstRow(self):
        """getFirstRow(self) -> unsigned int"""
        return _math._Domain2D32_getFirstRow(self)

    def getRowEnd(self):
        """getRowEnd(self) -> unsigned int"""
        return _math._Domain2D32_getRowEnd(self)

    def getFirstCol(self):
        """getFirstCol(self) -> unsigned int"""
        return _math._Domain2D32_getFirstCol(self)

    def getColEnd(self):
        """getColEnd(self) -> unsigned int"""
        return _math._Domain2D32_getColEnd(self)

    __swig_destroy__ = _math.delete__Domain2D32
_Domain2D32_swigregister = _math._Domain2D32_swigregister
_Domain2D32_swigregister(_Domain2D32)

class _DistanceToZero32(object):
    """Proxy of C++ nupic::DistanceToZero<(nupic::Real32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __call__(self, *args, **kwargs):
        """__call__(self, x) -> float"""
        return _math._DistanceToZero32___call__(self, *args, **kwargs)

    def __init__(self): 
        """__init__(self) -> _DistanceToZero32"""
        this = _math.new__DistanceToZero32()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _math.delete__DistanceToZero32
_DistanceToZero32_swigregister = _math._DistanceToZero32_swigregister
_DistanceToZero32_swigregister(_DistanceToZero32)

class _SparseMatrix32(object):
    """Proxy of C++ nupic::SparseMatrix<(nupic::UInt32,nupic::Real32,nupic::Int32,nupic::Real64,nupic::DistanceToZero<(nupic::Real32)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> _SparseMatrix32
        __init__(self, nrows, ncols) -> _SparseMatrix32
        __init__(self, inStream) -> _SparseMatrix32
        __init__(self, other) -> _SparseMatrix32
        """
        this = _math.new__SparseMatrix32(*args)
        try: self.this.append(this)
        except: self.this = this
    def initializeWithFixedNNZR(self, *args, **kwargs):
        """initializeWithFixedNNZR(self, nnzr, v=1, mode=0, seed=42)"""
        return _math._SparseMatrix32_initializeWithFixedNNZR(self, *args, **kwargs)

    __swig_destroy__ = _math.delete__SparseMatrix32
    def isZero(self):
        """isZero(self) -> bool"""
        return _math._SparseMatrix32_isZero(self)

    def getIsNearlyZeroFunction(self):
        """getIsNearlyZeroFunction(self) -> nupic::IsNearlyZero< nupic::DistanceToZero< nupic::Real32 > > const &"""
        return _math._SparseMatrix32_getIsNearlyZeroFunction(self)

    def isCompact(self):
        """isCompact(self) -> bool"""
        return _math._SparseMatrix32_isCompact(self)

    def nRows(self):
        """nRows(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nRows(self)

    def nCols(self):
        """nCols(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nCols(self)

    def nBytes(self):
        """nBytes(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nBytes(self)

    def nNonZerosOnRow(self, *args, **kwargs):
        """nNonZerosOnRow(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZerosOnRow(self, *args, **kwargs)

    def nNonZerosOnCol(self, *args, **kwargs):
        """nNonZerosOnCol(self, col) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZerosOnCol(self, *args, **kwargs)

    def nNonZeros(self):
        """nNonZeros(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZeros(self)

    def isRowZero(self, *args, **kwargs):
        """isRowZero(self, row) -> bool"""
        return _math._SparseMatrix32_isRowZero(self, *args, **kwargs)

    def isColZero(self, *args, **kwargs):
        """isColZero(self, col) -> bool"""
        return _math._SparseMatrix32_isColZero(self, *args, **kwargs)

    def nNonZeroRows(self):
        """nNonZeroRows(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZeroRows(self)

    def nNonZeroCols(self):
        """nNonZeroCols(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZeroCols(self)

    def nZeroRows(self):
        """nZeroRows(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nZeroRows(self)

    def nZeroCols(self):
        """nZeroCols(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nZeroCols(self)

    def firstNonZeroOnRow(self, *args, **kwargs):
        """firstNonZeroOnRow(self, row) -> PairUInt32Real32"""
        return _math._SparseMatrix32_firstNonZeroOnRow(self, *args, **kwargs)

    def lastNonZeroOnRow(self, *args, **kwargs):
        """lastNonZeroOnRow(self, row) -> PairUInt32Real32"""
        return _math._SparseMatrix32_lastNonZeroOnRow(self, *args, **kwargs)

    def rowBandwidth(self, *args, **kwargs):
        """rowBandwidth(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_rowBandwidth(self, *args, **kwargs)

    def firstNonZeroOnCol(self, *args, **kwargs):
        """firstNonZeroOnCol(self, col) -> PairUInt32Real32"""
        return _math._SparseMatrix32_firstNonZeroOnCol(self, *args, **kwargs)

    def lastNonZeroOnCol(self, *args, **kwargs):
        """lastNonZeroOnCol(self, col) -> PairUInt32Real32"""
        return _math._SparseMatrix32_lastNonZeroOnCol(self, *args, **kwargs)

    def colBandwidth(self, *args, **kwargs):
        """colBandwidth(self, col) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_colBandwidth(self, *args, **kwargs)

    def nonZerosInRowRange(self, *args, **kwargs):
        """nonZerosInRowRange(self, row, col_begin, col_end) -> bool"""
        return _math._SparseMatrix32_nonZerosInRowRange(self, *args, **kwargs)

    def nNonZerosInRowRange(self, *args, **kwargs):
        """nNonZerosInRowRange(self, row, col_begin, col_end) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZerosInRowRange(self, *args, **kwargs)

    def nNonZerosInBox(self, *args, **kwargs):
        """nNonZerosInBox(self, row_begin, row_end, col_begin, col_end) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_nNonZerosInBox(self, *args, **kwargs)

    def isSymmetric(self):
        """isSymmetric(self) -> bool"""
        return _math._SparseMatrix32_isSymmetric(self)

    def isBinary(self):
        """isBinary(self) -> bool"""
        return _math._SparseMatrix32_isBinary(self)

    def equals(self, *args, **kwargs):
        """equals(self, B) -> bool"""
        return _math._SparseMatrix32_equals(self, *args, **kwargs)

    def sameRowNonZeroIndices(self, *args, **kwargs):
        """sameRowNonZeroIndices(self, row, B) -> bool"""
        return _math._SparseMatrix32_sameRowNonZeroIndices(self, *args, **kwargs)

    def sameNonZeroIndices(self, *args, **kwargs):
        """sameNonZeroIndices(self, B) -> bool"""
        return _math._SparseMatrix32_sameNonZeroIndices(self, *args, **kwargs)

    def nonZeroIndicesIncluded(self, *args):
        """
        nonZeroIndicesIncluded(self, row, B) -> bool
        nonZeroIndicesIncluded(self, B) -> bool
        """
        return _math._SparseMatrix32_nonZeroIndicesIncluded(self, *args)

    def compact(self):
        """compact(self)"""
        return _math._SparseMatrix32_compact(self)

    def decompact(self):
        """decompact(self)"""
        return _math._SparseMatrix32_decompact(self)

    def CSRSize(self):
        """CSRSize(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_CSRSize(self)

    def fromCSR(self, *args, **kwargs):
        """fromCSR(self, inStreamParam, zero_permissive=False) -> std::istream &"""
        return _math._SparseMatrix32_fromCSR(self, *args, **kwargs)

    def toCSR(self, *args, **kwargs):
        """toCSR(self, out) -> std::ostream &"""
        return _math._SparseMatrix32_toCSR(self, *args, **kwargs)

    def fromBinary(self, *args, **kwargs):
        """fromBinary(self, inStream)"""
        return _math._SparseMatrix32_fromBinary(self, *args, **kwargs)

    def toBinary(self, *args, **kwargs):
        """toBinary(self, outStream)"""
        return _math._SparseMatrix32_toBinary(self, *args, **kwargs)

    def resize(self, *args, **kwargs):
        """resize(self, new_nrows, new_ncols, setToZero=False)"""
        return _math._SparseMatrix32_resize(self, *args, **kwargs)

    def reshape(self, *args, **kwargs):
        """reshape(self, new_nrows, new_ncols)"""
        return _math._SparseMatrix32_reshape(self, *args, **kwargs)

    def deleteRow(self, *args, **kwargs):
        """deleteRow(self, del_row)"""
        return _math._SparseMatrix32_deleteRow(self, *args, **kwargs)

    def deleteCol(self, *args, **kwargs):
        """deleteCol(self, del_col)"""
        return _math._SparseMatrix32_deleteCol(self, *args, **kwargs)

    def append(self, *args, **kwargs):
        """append(self, other, zero_permissive=False)"""
        return _math._SparseMatrix32_append(self, *args, **kwargs)

    def duplicateRow(self, *args, **kwargs):
        """duplicateRow(self, row)"""
        return _math._SparseMatrix32_duplicateRow(self, *args, **kwargs)

    def setZero(self, *args, **kwargs):
        """setZero(self, row, col, resizeYesNo=False)"""
        return _math._SparseMatrix32_setZero(self, *args, **kwargs)

    def setDiagonalToZero(self):
        """setDiagonalToZero(self)"""
        return _math._SparseMatrix32_setDiagonalToZero(self)

    def setDiagonalToVal(self, *args, **kwargs):
        """setDiagonalToVal(self, val)"""
        return _math._SparseMatrix32_setDiagonalToVal(self, *args, **kwargs)

    def setNonZero(self, *args, **kwargs):
        """setNonZero(self, i, j, val, resizeYesNo=False)"""
        return _math._SparseMatrix32_setNonZero(self, *args, **kwargs)

    def set(self, *args, **kwargs):
        """set(self, i, j, val, resizeYesNo=False)"""
        return _math._SparseMatrix32_set(self, *args, **kwargs)

    def setBoxToZero(self, *args, **kwargs):
        """setBoxToZero(self, row_begin, row_end, col_begin, col_end)"""
        return _math._SparseMatrix32_setBoxToZero(self, *args, **kwargs)

    def setBox(self, *args, **kwargs):
        """setBox(self, row_begin, row_end, col_begin, col_end, val)"""
        return _math._SparseMatrix32_setBox(self, *args, **kwargs)

    def increment(self, *args, **kwargs):
        """increment(self, i, j, delta=1, resizeYesNo=False)"""
        return _math._SparseMatrix32_increment(self, *args, **kwargs)

    def incrementWNZ(self, *args, **kwargs):
        """incrementWNZ(self, i, j, delta=1, resizeYesNo=False)"""
        return _math._SparseMatrix32_incrementWNZ(self, *args, **kwargs)

    def get(self, *args, **kwargs):
        """get(self, row, col) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_get(self, *args, **kwargs)

    def row_nz_index_begin(self, *args, **kwargs):
        """row_nz_index_begin(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::const_row_nz_index_iterator"""
        return _math._SparseMatrix32_row_nz_index_begin(self, *args, **kwargs)

    def row_nz_index_end(self, *args, **kwargs):
        """row_nz_index_end(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::const_row_nz_index_iterator"""
        return _math._SparseMatrix32_row_nz_index_end(self, *args, **kwargs)

    def row_nz_value_begin(self, *args, **kwargs):
        """row_nz_value_begin(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::const_row_nz_value_iterator"""
        return _math._SparseMatrix32_row_nz_value_begin(self, *args, **kwargs)

    def row_nz_value_end(self, *args, **kwargs):
        """row_nz_value_end(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::const_row_nz_value_iterator"""
        return _math._SparseMatrix32_row_nz_value_end(self, *args, **kwargs)

    def setRowToZero(self, *args, **kwargs):
        """setRowToZero(self, row)"""
        return _math._SparseMatrix32_setRowToZero(self, *args, **kwargs)

    def setRowToVal(self, *args, **kwargs):
        """setRowToVal(self, row, val)"""
        return _math._SparseMatrix32_setRowToVal(self, *args, **kwargs)

    def setColToZero(self, *args, **kwargs):
        """setColToZero(self, col)"""
        return _math._SparseMatrix32_setColToZero(self, *args, **kwargs)

    def setColToVal(self, *args, **kwargs):
        """setColToVal(self, col, val)"""
        return _math._SparseMatrix32_setColToVal(self, *args, **kwargs)

    def setToZero(self):
        """setToZero(self)"""
        return _math._SparseMatrix32_setToZero(self)

    def setFromOuter(self, *args, **kwargs):
        """setFromOuter(self, x, y, keepMemory=False)"""
        return _math._SparseMatrix32_setFromOuter(self, *args, **kwargs)

    def setFromElementMultiplyWithOuter(self, *args, **kwargs):
        """setFromElementMultiplyWithOuter(self, x, y, b)"""
        return _math._SparseMatrix32_setFromElementMultiplyWithOuter(self, *args, **kwargs)

    def setRowFromDense(self, *args, **kwargs):
        """setRowFromDense(self, row, x)"""
        return _math._SparseMatrix32_setRowFromDense(self, *args, **kwargs)

    def getRowToDense(self, *args, **kwargs):
        """getRowToDense(self, row, dense)"""
        return _math._SparseMatrix32_getRowToDense(self, *args, **kwargs)

    def copyRow(self, *args, **kwargs):
        """copyRow(self, dst_row, src_row, other)"""
        return _math._SparseMatrix32_copyRow(self, *args, **kwargs)

    def getColToDense(self, *args, **kwargs):
        """getColToDense(self, col, dense)"""
        return _math._SparseMatrix32_getColToDense(self, *args, **kwargs)

    def setColFromDense(self, *args, **kwargs):
        """setColFromDense(self, col, x)"""
        return _math._SparseMatrix32_setColFromDense(self, *args, **kwargs)

    def shiftRows(self, *args, **kwargs):
        """shiftRows(self, n)"""
        return _math._SparseMatrix32_shiftRows(self, *args, **kwargs)

    def shiftCols(self, *args, **kwargs):
        """shiftCols(self, n)"""
        return _math._SparseMatrix32_shiftCols(self, *args, **kwargs)

    def transpose(self, *args):
        """
        transpose(self, tr)
        transpose(self)
        """
        return _math._SparseMatrix32_transpose(self, *args)

    def addToTranspose(self, *args):
        """
        addToTranspose(self, sm)
        addToTranspose(self)
        """
        return _math._SparseMatrix32_addToTranspose(self, *args)

    def thresholdRow(self, *args, **kwargs):
        """thresholdRow(self, row, threshold=Epsilon)"""
        return _math._SparseMatrix32_thresholdRow(self, *args, **kwargs)

    def thresholdCol(self, *args, **kwargs):
        """thresholdCol(self, col, threshold=Epsilon)"""
        return _math._SparseMatrix32_thresholdCol(self, *args, **kwargs)

    def clipRow(self, *args, **kwargs):
        """clipRow(self, row, val, above=True)"""
        return _math._SparseMatrix32_clipRow(self, *args, **kwargs)

    def clipRowBelowAndAbove(self, *args, **kwargs):
        """clipRowBelowAndAbove(self, row, a, b)"""
        return _math._SparseMatrix32_clipRowBelowAndAbove(self, *args, **kwargs)

    def clipCol(self, *args, **kwargs):
        """clipCol(self, col, val, above=True)"""
        return _math._SparseMatrix32_clipCol(self, *args, **kwargs)

    def clipColBelowAndAbove(self, *args, **kwargs):
        """clipColBelowAndAbove(self, col, a, b)"""
        return _math._SparseMatrix32_clipColBelowAndAbove(self, *args, **kwargs)

    def clip(self, *args, **kwargs):
        """clip(self, val, above=True)"""
        return _math._SparseMatrix32_clip(self, *args, **kwargs)

    def clipBelowAndAbove(self, *args, **kwargs):
        """clipBelowAndAbove(self, a, b)"""
        return _math._SparseMatrix32_clipBelowAndAbove(self, *args, **kwargs)

    def countWhereEqual(self, *args, **kwargs):
        """countWhereEqual(self, begin_row, end_row, begin_col, end_col, value) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_countWhereEqual(self, *args, **kwargs)

    def countWhereGreater(self, *args, **kwargs):
        """countWhereGreater(self, begin_row, end_row, begin_col, end_col, value) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_countWhereGreater(self, *args, **kwargs)

    def countWhereGreaterEqual(self, *args, **kwargs):
        """countWhereGreaterEqual(self, begin_row, end_row, begin_col, end_col, value) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::size_type"""
        return _math._SparseMatrix32_countWhereGreaterEqual(self, *args, **kwargs)

    def argmax(self):
        """argmax(self) -> PairOfUInt32"""
        return _math._SparseMatrix32_argmax(self)

    def argmin(self):
        """argmin(self) -> PairOfUInt32"""
        return _math._SparseMatrix32_argmin(self)

    def normalizeRow(self, *args, **kwargs):
        """normalizeRow(self, row, val=1.0, exact=False) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_normalizeRow(self, *args, **kwargs)

    def normalizeCol(self, *args, **kwargs):
        """normalizeCol(self, col, val=1.0, exact=False) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_normalizeCol(self, *args, **kwargs)

    def normalizeRows(self, val=1.0, exact=False):
        """normalizeRows(self, val=1.0, exact=False)"""
        return _math._SparseMatrix32_normalizeRows(self, val, exact)

    def normalizeCols(self, val=1.0, exact=False):
        """normalizeCols(self, val=1.0, exact=False)"""
        return _math._SparseMatrix32_normalizeCols(self, val, exact)

    def normalize(self, val=1.0, exact=False):
        """normalize(self, val=1.0, exact=False)"""
        return _math._SparseMatrix32_normalize(self, val, exact)

    def normalize_max(self, val=1.0):
        """normalize_max(self, val=1.0)"""
        return _math._SparseMatrix32_normalize_max(self, val)

    def rowSum(self, *args, **kwargs):
        """rowSum(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_rowSum(self, *args, **kwargs)

    def rowProd(self, *args, **kwargs):
        """rowProd(self, row) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_rowProd(self, *args, **kwargs)

    def colSum(self, *args, **kwargs):
        """colSum(self, col) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_colSum(self, *args, **kwargs)

    def colProd(self, *args, **kwargs):
        """colProd(self, col) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_colProd(self, *args, **kwargs)

    def sum(self):
        """sum(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_sum(self)

    def prod(self):
        """prod(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_prod(self)

    def lerp(self, *args, **kwargs):
        """lerp(self, a, b, B)"""
        return _math._SparseMatrix32_lerp(self, *args, **kwargs)

    def addTwoRows(self, *args, **kwargs):
        """addTwoRows(self, src_row, dst_row)"""
        return _math._SparseMatrix32_addTwoRows(self, *args, **kwargs)

    def addTwoCols(self, *args, **kwargs):
        """addTwoCols(self, src_col, dst_col)"""
        return _math._SparseMatrix32_addTwoCols(self, *args, **kwargs)

    def map(self, *args, **kwargs):
        """map(self, B, C)"""
        return _math._SparseMatrix32_map(self, *args, **kwargs)

    def incrementWithOuterProduct(self, *args, **kwargs):
        """incrementWithOuterProduct(self, x, y)"""
        return _math._SparseMatrix32_incrementWithOuterProduct(self, *args, **kwargs)

    def incrementOnOuterProductVal(self, *args, **kwargs):
        """incrementOnOuterProductVal(self, rows, cols, val=1.0)"""
        return _math._SparseMatrix32_incrementOnOuterProductVal(self, *args, **kwargs)

    def sortRowsAscendingNNZ(self):
        """sortRowsAscendingNNZ(self)"""
        return _math._SparseMatrix32_sortRowsAscendingNNZ(self)

    def replaceNZ(self, val=1.0):
        """replaceNZ(self, val=1.0)"""
        return _math._SparseMatrix32_replaceNZ(self, val)

    def diagNZProd(self):
        """diagNZProd(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_diagNZProd(self)

    def diagSum(self):
        """diagSum(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_diagSum(self)

    def diagNZLogSum(self):
        """diagNZLogSum(self) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type"""
        return _math._SparseMatrix32_diagNZLogSum(self)

    def rowNegate(self, *args, **kwargs):
        """rowNegate(self, idx)"""
        return _math._SparseMatrix32_rowNegate(self, *args, **kwargs)

    def colNegate(self, *args, **kwargs):
        """colNegate(self, idx)"""
        return _math._SparseMatrix32_colNegate(self, *args, **kwargs)

    def negate(self):
        """negate(self)"""
        return _math._SparseMatrix32_negate(self)

    def rowAbs(self, *args, **kwargs):
        """rowAbs(self, idx)"""
        return _math._SparseMatrix32_rowAbs(self, *args, **kwargs)

    def colAbs(self, *args, **kwargs):
        """colAbs(self, idx)"""
        return _math._SparseMatrix32_colAbs(self, *args, **kwargs)

    def abs(self):
        """abs(self)"""
        return _math._SparseMatrix32_abs(self)

    def elementRowSquare(self, *args, **kwargs):
        """elementRowSquare(self, idx)"""
        return _math._SparseMatrix32_elementRowSquare(self, *args, **kwargs)

    def elementColSquare(self, *args, **kwargs):
        """elementColSquare(self, idx)"""
        return _math._SparseMatrix32_elementColSquare(self, *args, **kwargs)

    def elementSquare(self):
        """elementSquare(self)"""
        return _math._SparseMatrix32_elementSquare(self)

    def elementRowCube(self, *args, **kwargs):
        """elementRowCube(self, idx)"""
        return _math._SparseMatrix32_elementRowCube(self, *args, **kwargs)

    def elementColCube(self, *args, **kwargs):
        """elementColCube(self, idx)"""
        return _math._SparseMatrix32_elementColCube(self, *args, **kwargs)

    def elementCube(self):
        """elementCube(self)"""
        return _math._SparseMatrix32_elementCube(self)

    def elementRowNZInverse(self, *args, **kwargs):
        """elementRowNZInverse(self, idx)"""
        return _math._SparseMatrix32_elementRowNZInverse(self, *args, **kwargs)

    def elementColNZInverse(self, *args, **kwargs):
        """elementColNZInverse(self, idx)"""
        return _math._SparseMatrix32_elementColNZInverse(self, *args, **kwargs)

    def elementNZInverse(self):
        """elementNZInverse(self)"""
        return _math._SparseMatrix32_elementNZInverse(self)

    def elementRowSqrt(self, *args, **kwargs):
        """elementRowSqrt(self, idx)"""
        return _math._SparseMatrix32_elementRowSqrt(self, *args, **kwargs)

    def elementColSqrt(self, *args, **kwargs):
        """elementColSqrt(self, idx)"""
        return _math._SparseMatrix32_elementColSqrt(self, *args, **kwargs)

    def elementSqrt(self):
        """elementSqrt(self)"""
        return _math._SparseMatrix32_elementSqrt(self)

    def elementRowNZLog(self, *args, **kwargs):
        """elementRowNZLog(self, idx)"""
        return _math._SparseMatrix32_elementRowNZLog(self, *args, **kwargs)

    def elementColNZLog(self, *args, **kwargs):
        """elementColNZLog(self, idx)"""
        return _math._SparseMatrix32_elementColNZLog(self, *args, **kwargs)

    def elementNZLog(self):
        """elementNZLog(self)"""
        return _math._SparseMatrix32_elementNZLog(self)

    def elementRowNZExp(self, *args, **kwargs):
        """elementRowNZExp(self, idx)"""
        return _math._SparseMatrix32_elementRowNZExp(self, *args, **kwargs)

    def elementColNZExp(self, *args, **kwargs):
        """elementColNZExp(self, idx)"""
        return _math._SparseMatrix32_elementColNZExp(self, *args, **kwargs)

    def elementNZExp(self):
        """elementNZExp(self)"""
        return _math._SparseMatrix32_elementNZExp(self)

    def multiply(self, *args):
        """
        multiply(self, B, C)
        multiply(self, val)
        """
        return _math._SparseMatrix32_multiply(self, *args)

    def divide(self, *args, **kwargs):
        """divide(self, val)"""
        return _math._SparseMatrix32_divide(self, *args, **kwargs)

    def elementRowNZPow(self, *args, **kwargs):
        """elementRowNZPow(self, idx, val)"""
        return _math._SparseMatrix32_elementRowNZPow(self, *args, **kwargs)

    def elementColNZPow(self, *args, **kwargs):
        """elementColNZPow(self, idx, val)"""
        return _math._SparseMatrix32_elementColNZPow(self, *args, **kwargs)

    def elementNZPow(self, *args, **kwargs):
        """elementNZPow(self, val)"""
        return _math._SparseMatrix32_elementNZPow(self, *args, **kwargs)

    def elementRowNZLogk(self, *args, **kwargs):
        """elementRowNZLogk(self, idx, val)"""
        return _math._SparseMatrix32_elementRowNZLogk(self, *args, **kwargs)

    def elementColNZLogk(self, *args, **kwargs):
        """elementColNZLogk(self, idx, val)"""
        return _math._SparseMatrix32_elementColNZLogk(self, *args, **kwargs)

    def elementNZLogk(self, *args, **kwargs):
        """elementNZLogk(self, val)"""
        return _math._SparseMatrix32_elementNZLogk(self, *args, **kwargs)

    def rowAdd(self, *args, **kwargs):
        """rowAdd(self, idx, val)"""
        return _math._SparseMatrix32_rowAdd(self, *args, **kwargs)

    def colAdd(self, *args, **kwargs):
        """colAdd(self, idx, val)"""
        return _math._SparseMatrix32_colAdd(self, *args, **kwargs)

    def add(self, *args):
        """
        add(self, other)
        add(self, val)
        """
        return _math._SparseMatrix32_add(self, *args)

    def elementNZAdd(self, *args, **kwargs):
        """elementNZAdd(self, val)"""
        return _math._SparseMatrix32_elementNZAdd(self, *args, **kwargs)

    def rowSubtract(self, *args, **kwargs):
        """rowSubtract(self, idx, val)"""
        return _math._SparseMatrix32_rowSubtract(self, *args, **kwargs)

    def colSubtract(self, *args, **kwargs):
        """colSubtract(self, idx, val)"""
        return _math._SparseMatrix32_colSubtract(self, *args, **kwargs)

    def elementNZMultiply(self, *args, **kwargs):
        """elementNZMultiply(self, other)"""
        return _math._SparseMatrix32_elementNZMultiply(self, *args, **kwargs)

    def elementNZDivide(self, *args, **kwargs):
        """elementNZDivide(self, other)"""
        return _math._SparseMatrix32_elementNZDivide(self, *args, **kwargs)

    def subtract(self, *args):
        """
        subtract(self, val)
        subtract(self, other)
        """
        return _math._SparseMatrix32_subtract(self, *args)

    def __iadd__(self, *args, **kwargs):
        """__iadd__(self, val)"""
        return _math._SparseMatrix32___iadd__(self, *args, **kwargs)

    def __isub__(self, *args, **kwargs):
        """__isub__(self, val)"""
        return _math._SparseMatrix32___isub__(self, *args, **kwargs)

    def __imul__(self, *args, **kwargs):
        """__imul__(self, val)"""
        return _math._SparseMatrix32___imul__(self, *args, **kwargs)

    def __idiv__(self, *args, **kwargs):
        """__idiv__(self, val)"""
        return _math._SparseMatrix32___idiv__(self, *args, **kwargs)

    allowed_scalar_types = ['int', 'float', 'float32', 'float64', 'float128']

    def __init__(self, *args):
      """
      Constructs a new SparseMatrix from the following available arguments:
                    SparseMatrix(): An empty sparse matrix with 0 rows and columns.
        SparseMatrix(nrows, ncols): A zero sparse matrix with the
                                    specified rows and columns.
        SparseMatrix(SparseMatrix): Copies an existing sparse matrix.
              SparseMatrix(string): Loads a SparseMatrix from its serialized form.
         SparseMatrix(numpy.array): Loads a SparseMatrix from a numpy array.
         SparseMatrix([[...],[...]]): Creates an array from a list of lists.
      """
      serialized,dense,from01,fromstr3f = None,None,False,False
      fromSpecRowCols = False

      if (len(args) == 3) and isinstance(args[0], _SparseMatrix32):
        fromSpecRowCols = True

      if (len(args) == 1):
        if isinstance(args[0], basestring):
          serialized = args[0]
          args = tuple()
        elif isinstance(args[0], numpy.ndarray):
          dense = args[0]
          args = tuple()
        elif hasattr(args[0], '__iter__'):
          dense = args[0]
          args = tuple()
        elif isinstance(args[0], _SM_01_32_32):#or isinstance(args[0], _SM_01_32_16):
          from01 = True

      if from01 or fromSpecRowCols:
        this = _MATH.new__SparseMatrix32(1,1)
      else:
        this = _MATH.new__SparseMatrix32(*args)

      try:
        self.this.append(this)
      except:
        self.this = this

      if serialized is not None:
        s = serialized.split(None, 1)
        self.fromPyString(serialized)

      elif dense is not None:
        self.fromDense(numpy.asarray(dense,dtype=GetNumpyDataType('NTA_Real' +"32")))

      elif from01:
        nz_i,nz_j = args[0].getAllNonZeros(True)
        nz_ones = numpy.ones((len(nz_i)))
        self.setAllNonZeros(args[0].nRows(), args[0].nCols(), nz_i, nz_j, nz_ones)

      elif fromstr3f:
        nz_i,nz_j,nz_v = args[1].getAllNonZeros(args[0], True)
        self.setAllNonZeros(args[1].nRows(), args[1].nCols(), nz_i,nz_j,nz_v)

      elif fromSpecRowCols:
        if args[2] == 0:
          self.__initializeWithRows(args[0], args[1])
        elif args[2] == 1:
          self.__initializeWithCols(args[0], args[1])

    #def _fixSlice(self, dim, ub):
    #"""Used internally to fill out blank fields in slicing records."""
    #start = dim.start
    #if start is None: start = 0
    #elif start < 0: start += ub
    #stop = dim.stop
    #if stop is None: stop = ub
    #elif stop < 0: stop += ub
    #return slice(start, stop, 1)

    #def _getDomain(self, key, bounds):
    #"""Used internally to convert a list of slices to a valid Domain."""
    #slices = [None] * len(bounds)
    #cur = 0
    #hasEllipsis = False
    #for dim in key:
    #if dim is Ellipsis:
    #hasEllipsis = True
    #toFill = len(bounds) - len(key) + 1
    #if toFill > 0:
    #for j in xrange(toFill-1):
    #slices[cur] = slice(0, bounds[cur], 1)
    #cur += 1
    #slices[cur] = slice(0, bounds[cur], 1)
    #elif isinstance(dim, slice):
    #slices[cur] = self._fixSlice(dim, bounds[cur])
    #else: slices[cur] = slice(dim, dim, 0)
    #cur += 1
    #return Domain([x.start for x in slices], [x.stop for x in slices])

    #def getSliceWrap(self, key):
    #bounds = [ self.nRows(), self.nCols() ]                                                    d = self._getDomain(key, bounds)
    #return self.getSlice(d[0].getLB(), d[0].getUB(), d[1].getLB(), d[1].getUB())

    #def setSliceWrap(self, key, value):
    #bounds = [ self.nRows(), self.nCols() ]                                                    d = self._getDomain(key, bounds)
    #return self.setSlice(d[0].getLB(), d[1].getLB(), value)

    #def __getitem__(self, key):
    #if isinstance(key, tuple):
    #hasSlices = False
    #for dim in key:
    #if (dim is Ellipsis) or isinstance(dim, slice):
    #hasSlices = True
    #break
    #if hasSlices: return self.getSliceWrap(key)
    #else: return _MATH.SparseMatrixN2_get(self, key)
    #elif (key is Ellipsis) or isinstance(key, slice):
    #return self.getSliceWrap((key,))
    #else:
    #return _MATH.SparseMatrixN2_get(self, (key,))

    #def __setitem__(self, key, value):
    #if isinstance(key, tuple):
    #hasSlices = False
    #for dim in key:
    #if isinstance(dim, slice): hasSlices = True
    #if hasSlices: return self.setSliceWrap(key, value)
    #else: return _MATH.SparseMatrixN2_set(self, key, value)
    #elif (key is Ellipsis) or isinstance(key, slice):
    #return self.setSliceWrap((key,), value)
    #else:
    #return _MATH.SparseMatrixN2_set(self, (key,), value)

    def setRowFromDense(self, row, x):
      self._setRowFromDense(row, x)

    def __getitem__(self, index):
      return numpy.float32(self.get(index[0], index[1]))

    def __setitem__(self, index, value):
      self.set(index[0], index[1], value)

    def __getstate__(self):
      """
      Used by the pickling mechanism to get state that will be saved.
      """
      return (self.toPyString(),)

    def __setstate__(self,tup):
      """
      Used by the pickling mechanism to restore state that was saved.
      """
      self.this = _MATH.new__SparseMatrix32(1, 1)
      self.thisown = 1
      self.fromPyString(tup[0])

    def __str__(self):
      return self.toDense().__str__()

    def _setShape(self, *args):
      if len(args) == 1:
        self.resize(*(args[0]))
      elif len(args) == 2:
        self.resize(*args)
      else:
        raise RuntimeError("Error: setShape(rows, cols) or setShape((rows, cols))")
    shape = property(fget=lambda self: (self.nRows(), self.nCols()), fset=_setShape,
        doc="rows, cols")

    def getTransposed(self):
      result = self.__class__()
      self.transpose(result)
      return result

    def __neg__(self):
      result = _SparseMatrix32(self)
      result.negate()
      return result

    def __abs__(self):
      result = _SparseMatrix32(self)
      result.abs()
      return result

    def __iadd__(self, other):
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        self.__add(other)
      elif t == 'ndarray':
        self.add(_SparseMatrix32(other))
      elif t == '_SparseMatrix' +"32":
        self.add(other)
      else:
        raise Exception("Can't use type: " + t)
      return self

    def __add__(self, other):
      arg = None
      result = _SparseMatrix32(self)
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        result.__add(other)
      elif t == 'ndarray':
        result.add(_SparseMatrix32(other))
      elif t == '_SparseMatrix' +"32":
        result.add(other)
      else:
        raise Exception("Can't use type: " + t)
      return result

    def __radd__(self, other):
      return self.__add__(other)

    def __isub__(self, other):
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        self.__subtract(other)
      elif t == 'ndarray':
        self.subtract(_SparseMatrix32(other))
      elif t == '_SparseMatrix' +"32":
        self.subtract(other)
      else:
        raise Exception("Can't use type: " + t)
      return self

    def __sub__(self, other):
      result = _SparseMatrix32(self)
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        result.__subtract(other)
      elif t == 'ndarray':
        result.subtract(_SparseMatrix32(other))
      elif t == '_SparseMatrix' +"32":
        result.subtract(other)
      else:
        raise Exception("Can't use type: " + t)
      return result

    def __rsub__(self, other):
      return self.__sub__(other)

    def __imul__(self, other):
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        self.__multiply(other)
      elif t == '_SparseMatrix' +"32":
        self.multiply(other)
      else:
        raise Exception("Can't use type: " + t)
      return self

    def __mul__(self, other):
      t = type(other).__name__
      arg = other
      result = None
      if t in self.allowed_scalar_types:
        result = _SparseMatrix32(self)
        result.__multiply(arg)
      elif t == 'ndarray':
        if arg.ndim == 1:
          result = numpy.array(self.rightVecProd(arg))
        elif arg.ndim == 2:
          arg = _SparseMatrix32(other)
          result = _SparseMatrix32()
          self.multiply(arg, result)
        else:
          raise Exception("Wrong ndim: " + str(arg.ndim))
      elif t == '_SparseMatrix' +"32":
        if other.nCols() == 1:
          if self.nRows() == 1:
            result = self.rightVecProd(other.getCol(0))[0]
          else:
            result_list = self.rightVecProd(other.getCol(0))
            result = _SparseMatrix32(self.nRows(), 0)
            result.addCol(result_list)
        else:
          result = _SparseMatrix32()
          self.multiply(arg, result)
      else:
        raise Exception("Can't use type: " + t + " for multiplication")
      return result

    def __rmul__(self, other):
      t = type(other).__name__
      arg = other
      result = None
      if t in self.allowed_scalar_types:
        result = _SparseMatrix32(self)
        result.__multiply(arg)
      elif t == 'ndarray':
        if arg.ndim == 1:
          result = numpy.array(self.leftVecProd(arg))
        elif arg.ndim == 2:
          arg = _SparseMatrix32(other)
          result = _SparseMatrix32()
          arg.multiply(self, result)
        else:
          raise Exception("Wrong ndim: " + str(arg.ndim))
      elif t == '_SparseMatrix' +"32":
        if other.nRows() == 1:
          if self.nCols() == 1:
            result = self.leftVecProd(other.getRow(0))[0]
          else:
            result_list = self.leftVecProd(other.getRow(0))
            result = _SparseMatrix32(self.nCols(), 0)
            result.addRow(result_list)
        else:
          result = _SparseMatrix32()
          arg.multiply(self, result)
      else:
        raise Exception("Can't use type: " + t + " for multiplication")
      return result

    def __idiv__(self, other):
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        self.__divide(other)
      else:
        raise Exception("Can't use type: " + t)
      return self

    def __div__(self, other):
      t = type(other).__name__
      if t in self.allowed_scalar_types:
        result = _SparseMatrix32(self)
        result.__divide(other)
        return result
      else:
        raise Exception("Can't use type: " + t)


    @classmethod
    def getSchema(cls):
      """ Get Cap'n Proto schema. 
      :return: Cap'n Proto schema
      """
      return SparseMatrixProto


    def __initializeWithRows(self, *args, **kwargs):
        """__initializeWithRows(self, other, py_take)"""
        return _math._SparseMatrix32___initializeWithRows(self, *args, **kwargs)

    def __initializeWithCols(self, *args, **kwargs):
        """__initializeWithCols(self, other, py_take)"""
        return _math._SparseMatrix32___initializeWithCols(self, *args, **kwargs)

    def __add(self, *args, **kwargs):
        """__add(self, val)"""
        return _math._SparseMatrix32___add(self, *args, **kwargs)

    def __multiply(self, *args, **kwargs):
        """__multiply(self, val)"""
        return _math._SparseMatrix32___multiply(self, *args, **kwargs)

    def __subtract(self, *args, **kwargs):
        """__subtract(self, val)"""
        return _math._SparseMatrix32___subtract(self, *args, **kwargs)

    def __divide(self, *args, **kwargs):
        """__divide(self, val)"""
        return _math._SparseMatrix32___divide(self, *args, **kwargs)

    def copy(self, *args, **kwargs):
        """copy(self, other)"""
        return _math._SparseMatrix32_copy(self, *args, **kwargs)

    def fromDense(self, *args, **kwargs):
        """fromDense(self, matrix)"""
        return _math._SparseMatrix32_fromDense(self, *args, **kwargs)

    def toDense(self):
        """toDense(self) -> PyObject *"""
        return _math._SparseMatrix32_toDense(self)

    def _setRowFromDense(self, *args, **kwargs):
        """_setRowFromDense(self, row, py_row)"""
        return _math._SparseMatrix32__setRowFromDense(self, *args, **kwargs)

    def setRowFromSparse(self, *args, **kwargs):
        """setRowFromSparse(self, row, py_ind, py_nz)"""
        return _math._SparseMatrix32_setRowFromSparse(self, *args, **kwargs)

    def binarySaveToFile(self, *args, **kwargs):
        """binarySaveToFile(self, filename)"""
        return _math._SparseMatrix32_binarySaveToFile(self, *args, **kwargs)

    def binaryLoadFromFile(self, *args, **kwargs):
        """binaryLoadFromFile(self, filename)"""
        return _math._SparseMatrix32_binaryLoadFromFile(self, *args, **kwargs)

    def addRow(self, *args, **kwargs):
        """addRow(self, row)"""
        return _math._SparseMatrix32_addRow(self, *args, **kwargs)

    def addRowNZ(self, *args, **kwargs):
        """addRowNZ(self, ind, nz, zero_permissive=False)"""
        return _math._SparseMatrix32_addRowNZ(self, *args, **kwargs)

    def addCol(self, *args, **kwargs):
        """addCol(self, col)"""
        return _math._SparseMatrix32_addCol(self, *args, **kwargs)

    def addColNZ(self, *args, **kwargs):
        """addColNZ(self, ind, nz)"""
        return _math._SparseMatrix32_addColNZ(self, *args, **kwargs)

    def deleteRows(self, *args, **kwargs):
        """deleteRows(self, rowIndices)"""
        return _math._SparseMatrix32_deleteRows(self, *args, **kwargs)

    def deleteCols(self, *args, **kwargs):
        """deleteCols(self, colIndices)"""
        return _math._SparseMatrix32_deleteCols(self, *args, **kwargs)

    def getRow(self, *args, **kwargs):
        """getRow(self, row) -> PyObject *"""
        return _math._SparseMatrix32_getRow(self, *args, **kwargs)

    def getCol(self, *args, **kwargs):
        """getCol(self, col) -> PyObject *"""
        return _math._SparseMatrix32_getCol(self, *args, **kwargs)

    def getDiagonal(self):
        """getDiagonal(self) -> PyObject *"""
        return _math._SparseMatrix32_getDiagonal(self)

    def rowNonZeros(self, *args, **kwargs):
        """rowNonZeros(self, row) -> PyObject *"""
        return _math._SparseMatrix32_rowNonZeros(self, *args, **kwargs)

    def rowNonZeroIndices(self, *args, **kwargs):
        """rowNonZeroIndices(self, row) -> PyObject *"""
        return _math._SparseMatrix32_rowNonZeroIndices(self, *args, **kwargs)

    def colNonZeros(self, *args, **kwargs):
        """colNonZeros(self, col) -> PyObject *"""
        return _math._SparseMatrix32_colNonZeros(self, *args, **kwargs)

    def nonZeroRows(self):
        """nonZeroRows(self) -> PyObject *"""
        return _math._SparseMatrix32_nonZeroRows(self)

    def zeroRows(self):
        """zeroRows(self) -> PyObject *"""
        return _math._SparseMatrix32_zeroRows(self)

    def nonZeroCols(self):
        """nonZeroCols(self) -> PyObject *"""
        return _math._SparseMatrix32_nonZeroCols(self)

    def zeroCols(self):
        """zeroCols(self) -> PyObject *"""
        return _math._SparseMatrix32_zeroCols(self)

    def zeroRowAndCol(self):
        """zeroRowAndCol(self) -> PyObject *"""
        return _math._SparseMatrix32_zeroRowAndCol(self)

    def setElements(self, *args, **kwargs):
        """setElements(self, py_i, py_j, py_v)"""
        return _math._SparseMatrix32_setElements(self, *args, **kwargs)

    def getElements(self, *args, **kwargs):
        """getElements(self, py_i, py_j) -> PyObject *"""
        return _math._SparseMatrix32_getElements(self, *args, **kwargs)

    def setOuter(self, *args, **kwargs):
        """setOuter(self, py_i, py_j, py_v)"""
        return _math._SparseMatrix32_setOuter(self, *args, **kwargs)

    def getOuter(self, *args, **kwargs):
        """getOuter(self, py_i, py_j) -> _SparseMatrix32"""
        return _math._SparseMatrix32_getOuter(self, *args, **kwargs)

    def getAllNonZeros(self, three_lists=False):
        """getAllNonZeros(self, three_lists=False) -> PyObject *"""
        return _math._SparseMatrix32_getAllNonZeros(self, three_lists)

    def setAllNonZeros(self, *args, **kwargs):
        """setAllNonZeros(self, nrows, ncols, py_i, py_j, py_v, sorted=True)"""
        return _math._SparseMatrix32_setAllNonZeros(self, *args, **kwargs)

    def getNonZerosInBox(self, *args, **kwargs):
        """getNonZerosInBox(self, row_begin, row_end, col_begin, col_end) -> PyObject *"""
        return _math._SparseMatrix32_getNonZerosInBox(self, *args, **kwargs)

    def tolist(self):
        """tolist(self) -> PyObject *"""
        return _math._SparseMatrix32_tolist(self)

    def setSlice(self, *args):
        """
        setSlice(self, i_begin, j_begin, other)
        setSlice(self, i_begin, j_begin, py_other)
        """
        return _math._SparseMatrix32_setSlice(self, *args)

    def getSlice(self, *args, **kwargs):
        """getSlice(self, i_begin, i_end, j_begin, j_end) -> _SparseMatrix32"""
        return _math._SparseMatrix32_getSlice(self, *args, **kwargs)

    def getSlice2(self, *args):
        """
        getSlice2(self, src_first_row, src_row_end, src_first_col, src_col_end, other)
        getSlice2(self, i_begin, i_end, j_begin, j_end) -> _SparseMatrix32
        """
        return _math._SparseMatrix32_getSlice2(self, *args)

    def setRowsToZero(self, *args, **kwargs):
        """setRowsToZero(self, py_rows)"""
        return _math._SparseMatrix32_setRowsToZero(self, *args, **kwargs)

    def setColsToZero(self, *args, **kwargs):
        """setColsToZero(self, py_cols)"""
        return _math._SparseMatrix32_setColsToZero(self, *args, **kwargs)

    def setDiagonal(self, *args, **kwargs):
        """setDiagonal(self, py_v)"""
        return _math._SparseMatrix32_setDiagonal(self, *args, **kwargs)

    def incrementOnOuterWNZ(self, *args, **kwargs):
        """incrementOnOuterWNZ(self, py_i, py_j, delta=1)"""
        return _math._SparseMatrix32_incrementOnOuterWNZ(self, *args, **kwargs)

    def incrementOnOuterWNZWThreshold(self, *args, **kwargs):
        """incrementOnOuterWNZWThreshold(self, py_i, py_j, threshold, delta=1)"""
        return _math._SparseMatrix32_incrementOnOuterWNZWThreshold(self, *args, **kwargs)

    def incrementNonZerosOnOuter(self, rows, cols, delta):
      self._incrementNonZerosOnOuter(numpy.asarray(rows, dtype="uint32"),
                                     numpy.asarray(cols, dtype="uint32"),
                                     delta)

    def _incrementNonZerosOnOuter(self, *args, **kwargs):
        """_incrementNonZerosOnOuter(self, py_rows, py_cols, delta)"""
        return _math._SparseMatrix32__incrementNonZerosOnOuter(self, *args, **kwargs)

    def incrementNonZerosOnRowsExcludingCols(self, rows, cols, delta):
      self._incrementNonZerosOnRowsExcludingCols(numpy.asarray(rows, dtype="uint32"),
                                                 numpy.asarray(cols, dtype="uint32"),
                                                 delta)

    def _incrementNonZerosOnRowsExcludingCols(self, *args, **kwargs):
        """_incrementNonZerosOnRowsExcludingCols(self, py_rows, py_cols, delta)"""
        return _math._SparseMatrix32__incrementNonZerosOnRowsExcludingCols(self, *args, **kwargs)

    def setZerosOnOuter(self, rows, cols, value):
      self._setZerosOnOuter(numpy.asarray(rows, dtype="uint32"),
                            numpy.asarray(cols, dtype="uint32"),
                            value)

    def _setZerosOnOuter(self, *args, **kwargs):
        """_setZerosOnOuter(self, py_rows, py_cols, value)"""
        return _math._SparseMatrix32__setZerosOnOuter(self, *args, **kwargs)

    def setRandomZerosOnOuter(self, rows, cols, numNewNonZeros, value, rng):
      if isinstance(numNewNonZeros, numbers.Number):
        self._setRandomZerosOnOuter_singleCount(
          numpy.asarray(rows, dtype="uint32"),
          numpy.asarray(cols, dtype="uint32"),
          numNewNonZeros,
          value,
          rng)
      else:
        self._setRandomZerosOnOuter_multipleCounts(
          numpy.asarray(rows, dtype="uint32"),
          numpy.asarray(cols, dtype="uint32"),
          numpy.asarray(numNewNonZeros, dtype="int32"),
          value,
          rng)

    def _setRandomZerosOnOuter_singleCount(self, *args, **kwargs):
        """_setRandomZerosOnOuter_singleCount(self, py_rows, py_cols, numNewNonZeros, value, rng)"""
        return _math._SparseMatrix32__setRandomZerosOnOuter_singleCount(self, *args, **kwargs)

    def _setRandomZerosOnOuter_multipleCounts(self, *args, **kwargs):
        """_setRandomZerosOnOuter_multipleCounts(self, py_rows, py_cols, py_newNonZeroCounts, value, rng)"""
        return _math._SparseMatrix32__setRandomZerosOnOuter_multipleCounts(self, *args, **kwargs)

    def increaseRowNonZeroCountsOnOuterTo(self, rows, cols, numDesiredNonZeros,
                                          initialValue, rng):
      self._increaseRowNonZeroCountsOnOuterTo(
        numpy.asarray(rows, dtype="uint32"),
        numpy.asarray(cols, dtype="uint32"),
        numDesiredNonZeros, initialValue, rng)

    def _increaseRowNonZeroCountsOnOuterTo(self, *args, **kwargs):
        """_increaseRowNonZeroCountsOnOuterTo(self, py_rows, py_cols, numDesiredNonZeros, initialValue, rng)"""
        return _math._SparseMatrix32__increaseRowNonZeroCountsOnOuterTo(self, *args, **kwargs)

    def clipRowsBelowAndAbove(self, rows, a, b):
      self._clipRowsBelowAndAbove(numpy.asarray(rows, dtype="uint32"),
                                  a,
                                  b)

    def _clipRowsBelowAndAbove(self, *args, **kwargs):
        """_clipRowsBelowAndAbove(self, py_rows, a, b)"""
        return _math._SparseMatrix32__clipRowsBelowAndAbove(self, *args, **kwargs)

    def nNonZerosPerRow(self, rows=None):
      if rows is None:
        return self._nNonZerosPerRow_allRows()
      else:
        return self._nNonZerosPerRow(numpy.asarray(rows, dtype="uint32"))

    def _nNonZerosPerRow_allRows(self):
        """_nNonZerosPerRow_allRows(self) -> PyObject *"""
        return _math._SparseMatrix32__nNonZerosPerRow_allRows(self)

    def _nNonZerosPerRow(self, *args, **kwargs):
        """_nNonZerosPerRow(self, py_rows) -> PyObject *"""
        return _math._SparseMatrix32__nNonZerosPerRow(self, *args, **kwargs)

    def nNonZerosPerRowOnCols(self, rows, cols):
      rows = numpy.asarray(rows, dtype="uint32")
      cols = numpy.asarray(cols, dtype="uint32")
      return self._nNonZerosPerRowOnCols(rows, cols)

    def _nNonZerosPerRowOnCols(self, *args, **kwargs):
        """_nNonZerosPerRowOnCols(self, py_rows, py_cols) -> PyObject *"""
        return _math._SparseMatrix32__nNonZerosPerRowOnCols(self, *args, **kwargs)

    def nNonZerosPerCol(self):
        """nNonZerosPerCol(self) -> PyObject *"""
        return _math._SparseMatrix32_nNonZerosPerCol(self)

    def rowBandwidths(self):
        """rowBandwidths(self) -> PyObject *"""
        return _math._SparseMatrix32_rowBandwidths(self)

    def colBandwidths(self):
        """colBandwidths(self) -> PyObject *"""
        return _math._SparseMatrix32_colBandwidths(self)

    def nNonZerosPerBox(self, *args, **kwargs):
        """nNonZerosPerBox(self, box_i, box_j) -> _SparseMatrix32"""
        return _math._SparseMatrix32_nNonZerosPerBox(self, *args, **kwargs)

    def max(self, *args):
        """
        max(self, max_row, max_col, max_val)
        max(self) -> PyObject *
        """
        return _math._SparseMatrix32_max(self, *args)

    def min(self, *args):
        """
        min(self, min_row, min_col, min_val)
        min(self) -> PyObject *
        """
        return _math._SparseMatrix32_min(self, *args)

    def rowMax(self, *args):
        """
        rowMax(self, row, row_max_j, row_max)
        rowMax(self, row_index) -> PyObject
        rowMax(self) -> PyObject *
        """
        return _math._SparseMatrix32_rowMax(self, *args)

    def rowMin(self, *args):
        """
        rowMin(self, row, row_min_j, row_min)
        rowMin(self, row_index) -> PyObject
        rowMin(self) -> PyObject *
        """
        return _math._SparseMatrix32_rowMin(self, *args)

    def colMax(self, *args):
        """
        colMax(self, col, col_max_i, col_max)
        colMax(self, row_index) -> PyObject
        colMax(self) -> PyObject *
        """
        return _math._SparseMatrix32_colMax(self, *args)

    def colMin(self, *args):
        """
        colMin(self, col, col_min_i, col_min)
        colMin(self, col_index) -> PyObject
        colMin(self) -> PyObject *
        """
        return _math._SparseMatrix32_colMin(self, *args)

    def boxMin(self, *args):
        """
        boxMin(self, begin_row, end_row, begin_col, end_col, min_row, min_col, min_val)
        boxMin(self, begin_row, end_row, begin_col, end_col) -> PyObject *
        """
        return _math._SparseMatrix32_boxMin(self, *args)

    def boxMax(self, *args):
        """
        boxMax(self, begin_row, end_row, begin_col, end_col, max_row, max_col, max_val)
        boxMax(self, begin_row, end_row, begin_col, end_col) -> PyObject *
        """
        return _math._SparseMatrix32_boxMax(self, *args)

    def whereEqual(self, *args, **kwargs):
        """whereEqual(self, begin_row, end_row, begin_col, end_col, value) -> PyObject *"""
        return _math._SparseMatrix32_whereEqual(self, *args, **kwargs)

    def whereGreater(self, *args, **kwargs):
        """whereGreater(self, begin_row, end_row, begin_col, end_col, value) -> PyObject *"""
        return _math._SparseMatrix32_whereGreater(self, *args, **kwargs)

    def whereGreaterEqual(self, *args, **kwargs):
        """whereGreaterEqual(self, begin_row, end_row, begin_col, end_col, value) -> PyObject *"""
        return _math._SparseMatrix32_whereGreaterEqual(self, *args, **kwargs)

    def countWhereGreaterOrEqual(self, *args, **kwargs):
        """countWhereGreaterOrEqual(self, begin_row, end_row, begin_col, end_col, value) -> nupic::UInt32"""
        return _math._SparseMatrix32_countWhereGreaterOrEqual(self, *args, **kwargs)

    def permuteRows(self, *args, **kwargs):
        """permuteRows(self, py_permutation)"""
        return _math._SparseMatrix32_permuteRows(self, *args, **kwargs)

    def permuteCols(self, *args, **kwargs):
        """permuteCols(self, py_permutation)"""
        return _math._SparseMatrix32_permuteCols(self, *args, **kwargs)

    def rowSums(self, *args):
        """
        rowSums(self, sums)
        rowSums(self) -> PyObject *
        """
        return _math._SparseMatrix32_rowSums(self, *args)

    def colSums(self):
        """colSums(self) -> PyObject *"""
        return _math._SparseMatrix32_colSums(self)

    def addRows(self, *args, **kwargs):
        """addRows(self, whichRows) -> PyObject *"""
        return _math._SparseMatrix32_addRows(self, *args, **kwargs)

    def addListOfRows(self, *args, **kwargs):
        """addListOfRows(self, py_whichRows) -> PyObject *"""
        return _math._SparseMatrix32_addListOfRows(self, *args, **kwargs)

    def rowProds(self):
        """rowProds(self) -> PyObject *"""
        return _math._SparseMatrix32_rowProds(self)

    def colProds(self):
        """colProds(self) -> PyObject *"""
        return _math._SparseMatrix32_colProds(self)

    def logRowSums(self):
        """logRowSums(self) -> PyObject *"""
        return _math._SparseMatrix32_logRowSums(self)

    def logColSums(self):
        """logColSums(self) -> PyObject *"""
        return _math._SparseMatrix32_logColSums(self)

    def scaleRows(self, *args, **kwargs):
        """scaleRows(self, py_s)"""
        return _math._SparseMatrix32_scaleRows(self, *args, **kwargs)

    def scaleCols(self, *args, **kwargs):
        """scaleCols(self, py_s)"""
        return _math._SparseMatrix32_scaleCols(self, *args, **kwargs)

    def normalizeBlockByRows(self, *args, **kwargs):
        """normalizeBlockByRows(self, py_inds, val=-1.0, eps_n=1e-6)"""
        return _math._SparseMatrix32_normalizeBlockByRows(self, *args, **kwargs)

    def normalizeBlockByRows_binary(self, *args, **kwargs):
        """normalizeBlockByRows_binary(self, py_inds, val=-1.0, eps_n=1e-6)"""
        return _math._SparseMatrix32_normalizeBlockByRows_binary(self, *args, **kwargs)

    def axby(self, *args):
        """
        axby(self, row, a, b, xIn)
        axby(self, a, b, xIn)
        """
        return _math._SparseMatrix32_axby(self, *args)

    def rightVecProd_fast(self, *args, **kwargs):
        """rightVecProd_fast(self, xIn, yOut)"""
        return _math._SparseMatrix32_rightVecProd_fast(self, *args, **kwargs)

    def rightVecProd(self, *args):
        """
        rightVecProd(self, row, x) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type
        rightVecProd(self, x, y)
        rightVecProd(self, row, xIn) -> nupic::Real32
        rightVecProd(self, xIn) -> PyObject
        rightVecProd(self, pyRows, xIn) -> PyObject *
        """
        return _math._SparseMatrix32_rightVecProd(self, *args)

    def blockRightVecProd(self, *args, **kwargs):
        """blockRightVecProd(self, block_size, xIn) -> _SparseMatrix32"""
        return _math._SparseMatrix32_blockRightVecProd(self, *args, **kwargs)

    def leftVecProd(self, *args):
        """
        leftVecProd(self, col, x) -> nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > >::value_type
        leftVecProd(self, x, y)
        leftVecProd(self, col, xIn) -> nupic::Real32
        leftVecProd(self, xIn) -> PyObject
        leftVecProd(self, pyCols, xIn) -> PyObject *
        """
        return _math._SparseMatrix32_leftVecProd(self, *args)

    def leftVecProd_binary(self, *args, **kwargs):
        """leftVecProd_binary(self, pyCols, xIn) -> PyObject *"""
        return _math._SparseMatrix32_leftVecProd_binary(self, *args, **kwargs)

    def rightDenseMatProd(self, *args, **kwargs):
        """rightDenseMatProd(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_rightDenseMatProd(self, *args, **kwargs)

    def rightDenseMatProdAtNZ(self, *args, **kwargs):
        """rightDenseMatProdAtNZ(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_rightDenseMatProdAtNZ(self, *args, **kwargs)

    def denseMatExtract(self, *args, **kwargs):
        """denseMatExtract(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_denseMatExtract(self, *args, **kwargs)

    def leftDenseMatProd(self, *args, **kwargs):
        """leftDenseMatProd(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_leftDenseMatProd(self, *args, **kwargs)

    def elementRowAdd(self, *args, **kwargs):
        """elementRowAdd(self, i, xIn)"""
        return _math._SparseMatrix32_elementRowAdd(self, *args, **kwargs)

    def elementRowSubtract(self, *args, **kwargs):
        """elementRowSubtract(self, i, xIn)"""
        return _math._SparseMatrix32_elementRowSubtract(self, *args, **kwargs)

    def elementRowMultiply(self, *args):
        """
        elementRowMultiply(self, row, val)
        elementRowMultiply(self, row, x, y)
        elementRowMultiply(self, i, xIn)
        """
        return _math._SparseMatrix32_elementRowMultiply(self, *args)

    def elementRowDivide(self, *args):
        """
        elementRowDivide(self, idx, val)
        elementRowDivide(self, i, xIn)
        """
        return _math._SparseMatrix32_elementRowDivide(self, *args)

    def elementColAdd(self, *args, **kwargs):
        """elementColAdd(self, i, xIn)"""
        return _math._SparseMatrix32_elementColAdd(self, *args, **kwargs)

    def elementColSubtract(self, *args, **kwargs):
        """elementColSubtract(self, i, xIn)"""
        return _math._SparseMatrix32_elementColSubtract(self, *args, **kwargs)

    def elementColMultiply(self, *args):
        """
        elementColMultiply(self, col, val)
        elementColMultiply(self, col, x, y)
        elementColMultiply(self, i, xIn)
        """
        return _math._SparseMatrix32_elementColMultiply(self, *args)

    def elementColDivide(self, *args):
        """
        elementColDivide(self, idx, val)
        elementColDivide(self, i, xIn)
        """
        return _math._SparseMatrix32_elementColDivide(self, *args)

    def elementMultiply(self, *args):
        """
        elementMultiply(self, b)
        elementMultiply(self, m, result)
        elementMultiply(self, dense)
        elementMultiply(self, dense, result)
        elementMultiply(self, mIn)
        """
        return _math._SparseMatrix32_elementMultiply(self, *args)

    def rightVecProdAtNZ(self, *args, **kwargs):
        """rightVecProdAtNZ(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_rightVecProdAtNZ(self, *args, **kwargs)

    def leftVecProdAtNZ(self, *args, **kwargs):
        """leftVecProdAtNZ(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_leftVecProdAtNZ(self, *args, **kwargs)

    def rightVecSumAtNZ(self, denseArray, out=None):
      denseArray = numpy.asarray(denseArray, dtype="float32")

      if out is None:
        out = numpy.empty(self.nRows(), dtype="float32")
      else:
        assert out.dtype == "float32"

      self._rightVecSumAtNZ(denseArray, out)

      return out


    def rightVecSumAtNZ_fast(self, denseArray, out):
      """
      Deprecated. Use rightVecSumAtNZ with an 'out' specified.
      """
      self.rightVecSumAtNZ(denseArray, out)

    def _rightVecSumAtNZ(self, *args, **kwargs):
        """_rightVecSumAtNZ(self, py_denseArray, py_out)"""
        return _math._SparseMatrix32__rightVecSumAtNZ(self, *args, **kwargs)

    def rightVecSumAtNZSparse(self, sparseBinaryArray, out=None):
      sparseBinaryArray = numpy.asarray(sparseBinaryArray, dtype="uint32")

      if out is None:
        out = numpy.empty(self.nRows(), dtype="int32")
      else:
        assert out.dtype == "int32"

      self._rightVecSumAtNZSparse(sparseBinaryArray, out)

      return out

    def _rightVecSumAtNZSparse(self, *args, **kwargs):
        """_rightVecSumAtNZSparse(self, py_sparseBinaryArray, py_out)"""
        return _math._SparseMatrix32__rightVecSumAtNZSparse(self, *args, **kwargs)

    def rightVecSumAtNZGtThreshold(self, denseArray, threshold, out=None):
      denseArray = numpy.asarray(denseArray, dtype="float32")

      if out is None:
        out = numpy.empty(self.nRows(), dtype="float32")
      else:
        assert out.dtype == "float32"

      self._rightVecSumAtNZGtThreshold(denseArray, threshold, out)

      return out


    def rightVecSumAtNZGtThreshold_fast(self, denseArray, threshold, out):
      """
      Deprecated. Use rightVecSumAtNZGtThreshold with an 'out' specified.
      """
      self.rightVecSumAtNZGtThreshold(denseArray, threshold, out)

    def _rightVecSumAtNZGtThreshold(self, *args, **kwargs):
        """_rightVecSumAtNZGtThreshold(self, py_denseArray, threshold, py_out)"""
        return _math._SparseMatrix32__rightVecSumAtNZGtThreshold(self, *args, **kwargs)

    def rightVecSumAtNZGtThresholdSparse(self, sparseBinaryArray, threshold, out=None):
      sparseBinaryArray = numpy.asarray(sparseBinaryArray, dtype="uint32")

      if out is None:
        out = numpy.empty(self.nRows(), dtype="int32")
      else:
        assert out.dtype == "int32"

      self._rightVecSumAtNZGtThresholdSparse(sparseBinaryArray, threshold, out)

      return out

    def _rightVecSumAtNZGtThresholdSparse(self, *args, **kwargs):
        """_rightVecSumAtNZGtThresholdSparse(self, py_sparseBinaryArray, threshold, py_out)"""
        return _math._SparseMatrix32__rightVecSumAtNZGtThresholdSparse(self, *args, **kwargs)

    def rightVecSumAtNZGteThreshold(self, denseArray, threshold, out=None):
      denseArray = numpy.asarray(denseArray, dtype="float32")

      if out is None:
        out = numpy.empty(self.nRows(), dtype="float32")
      else:
        assert out.dtype == "float32"

      self._rightVecSumAtNZGteThreshold(denseArray, threshold, out)

      return out

    def _rightVecSumAtNZGteThreshold(self, *args, **kwargs):
        """_rightVecSumAtNZGteThreshold(self, py_denseArray, threshold, py_out)"""
        return _math._SparseMatrix32__rightVecSumAtNZGteThreshold(self, *args, **kwargs)

    def rightVecSumAtNZGteThresholdSparse(self, sparseBinaryArray, threshold, out=None):
      sparseBinaryArray = numpy.asarray(sparseBinaryArray, dtype="uint32")

      if out is None:
        out = numpy.empty(self.nRows(), dtype="int32")
      else:
        assert out.dtype == "int32"

      self._rightVecSumAtNZGteThresholdSparse(sparseBinaryArray, threshold, out)

      return out

    def _rightVecSumAtNZGteThresholdSparse(self, *args, **kwargs):
        """_rightVecSumAtNZGteThresholdSparse(self, py_sparseBinaryArray, threshold, py_out)"""
        return _math._SparseMatrix32__rightVecSumAtNZGteThresholdSparse(self, *args, **kwargs)

    def leftVecSumAtNZ(self, *args, **kwargs):
        """leftVecSumAtNZ(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_leftVecSumAtNZ(self, *args, **kwargs)

    def leftVecSumAtNZ_fast(self, *args, **kwargs):
        """leftVecSumAtNZ_fast(self, xIn, yOut)"""
        return _math._SparseMatrix32_leftVecSumAtNZ_fast(self, *args, **kwargs)

    def leftDenseMatProdAtNZ(self, *args, **kwargs):
        """leftDenseMatProdAtNZ(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_leftDenseMatProdAtNZ(self, *args, **kwargs)

    def rightDenseMatSumAtNZ(self, *args, **kwargs):
        """rightDenseMatSumAtNZ(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_rightDenseMatSumAtNZ(self, *args, **kwargs)

    def leftDenseMatSumAtNZ(self, *args, **kwargs):
        """leftDenseMatSumAtNZ(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_leftDenseMatSumAtNZ(self, *args, **kwargs)

    def rightDenseMatMaxAtNZ(self, *args, **kwargs):
        """rightDenseMatMaxAtNZ(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_rightDenseMatMaxAtNZ(self, *args, **kwargs)

    def leftDenseMatMaxAtNZ(self, *args, **kwargs):
        """leftDenseMatMaxAtNZ(self, mIn) -> PyObject *"""
        return _math._SparseMatrix32_leftDenseMatMaxAtNZ(self, *args, **kwargs)

    def vecArgMaxAtNZ(self, *args, **kwargs):
        """vecArgMaxAtNZ(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_vecArgMaxAtNZ(self, *args, **kwargs)

    def vecMaxAtNZ(self, *args, **kwargs):
        """vecMaxAtNZ(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_vecMaxAtNZ(self, *args, **kwargs)

    def rowVecProd(self, *args, **kwargs):
        """rowVecProd(self, xIn, lb=Epsilon) -> PyObject *"""
        return _math._SparseMatrix32_rowVecProd(self, *args, **kwargs)

    def vecMaxProd(self, *args, **kwargs):
        """vecMaxProd(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_vecMaxProd(self, *args, **kwargs)

    def vecArgMaxProd(self, *args, **kwargs):
        """vecArgMaxProd(self, xIn) -> PyObject *"""
        return _math._SparseMatrix32_vecArgMaxProd(self, *args, **kwargs)

    def getNonZerosSorted(self, *args, **kwargs):
        """getNonZerosSorted(self, n=-1, ascending_values=True) -> PyObject *"""
        return _math._SparseMatrix32_getNonZerosSorted(self, *args, **kwargs)

    def threshold(self, *args):
        """
        threshold(self, threshold=Epsilon)
        threshold(self, threshold, getCuts=False) -> PyObject *
        """
        return _math._SparseMatrix32_threshold(self, *args)

    def toPyString(self):
        """toPyString(self) -> PyObject *"""
        return _math._SparseMatrix32_toPyString(self)

    def fromPyString(self, *args, **kwargs):
        """fromPyString(self, s) -> bool"""
        return _math._SparseMatrix32_fromPyString(self, *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, other) -> bool"""
        return _math._SparseMatrix32___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, other) -> bool"""
        return _math._SparseMatrix32___ne__(self, *args, **kwargs)

_SparseMatrix32_swigregister = _math._SparseMatrix32_swigregister
_SparseMatrix32_swigregister(_SparseMatrix32)

class _SM_01_32_32(object):
    """Proxy of C++ nupic::SparseBinaryMatrix<(nupic::UInt32,nupic::UInt32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> _SM_01_32_32
        __init__(self, inStream) -> _SM_01_32_32
        __init__(self, ncols) -> _SM_01_32_32
        __init__(self, nrows, ncols) -> _SM_01_32_32
        __init__(self, o) -> _SM_01_32_32
        """
        this = _math.new__SM_01_32_32(*args)
        try: self.this.append(this)
        except: self.this = this
    def copy(self, *args, **kwargs):
        """copy(self, o)"""
        return _math._SM_01_32_32_copy(self, *args, **kwargs)

    __swig_destroy__ = _math.delete__SM_01_32_32
    def randomInitialize(self, *args, **kwargs):
        """randomInitialize(self, nnz, seed=0)"""
        return _math._SM_01_32_32_randomInitialize(self, *args, **kwargs)

    def getVersion(self, binary=False):
        """getVersion(self, binary=False) -> std::string const"""
        return _math._SM_01_32_32_getVersion(self, binary)

    def nRows(self):
        """nRows(self) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_nRows(self)

    def nCols(self):
        """nCols(self) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::nz_index_type"""
        return _math._SM_01_32_32_nCols(self)

    def capacity(self):
        """capacity(self) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_capacity(self)

    def nBytes(self):
        """nBytes(self) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_nBytes(self)

    def compact(self):
        """compact(self)"""
        return _math._SM_01_32_32_compact(self)

    def clear(self):
        """clear(self)"""
        return _math._SM_01_32_32_clear(self)

    def resize(self, *args, **kwargs):
        """resize(self, new_nrows, new_ncols)"""
        return _math._SM_01_32_32_resize(self, *args, **kwargs)

    def nNonZerosOnRow(self, *args, **kwargs):
        """nNonZerosOnRow(self, row) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_nNonZerosOnRow(self, *args, **kwargs)

    def nNonZeros(self):
        """nNonZeros(self) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_nNonZeros(self)

    def nNonZerosInRowRange(self, *args, **kwargs):
        """nNonZerosInRowRange(self, row, col_begin, col_end) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_nNonZerosInRowRange(self, *args, **kwargs)

    def nNonZerosInBox(self, *args, **kwargs):
        """nNonZerosInBox(self, row_begin, row_end, col_begin, col_end) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_nNonZerosInBox(self, *args, **kwargs)

    def get(self, *args, **kwargs):
        """get(self, row, col) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_get(self, *args, **kwargs)

    def get_linear(self, *args, **kwargs):
        """get_linear(self, n) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_get_linear(self, *args, **kwargs)

    def ind_begin_(self, *args, **kwargs):
        """ind_begin_(self, row) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::Row::const_iterator"""
        return _math._SM_01_32_32_ind_begin_(self, *args, **kwargs)

    def ind_end_(self, *args, **kwargs):
        """ind_end_(self, row) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::Row::const_iterator"""
        return _math._SM_01_32_32_ind_end_(self, *args, **kwargs)

    def getSparseRow(self, *args, **kwargs):
        """getSparseRow(self, row) -> VectorOfUInt32"""
        return _math._SM_01_32_32_getSparseRow(self, *args, **kwargs)

    def appendEmptyCols(self, *args, **kwargs):
        """appendEmptyCols(self, n)"""
        return _math._SM_01_32_32_appendEmptyCols(self, *args, **kwargs)

    def setRangeToZero(self, *args, **kwargs):
        """setRangeToZero(self, row, begin, end)"""
        return _math._SM_01_32_32_setRangeToZero(self, *args, **kwargs)

    def setRangeToOne(self, *args, **kwargs):
        """setRangeToOne(self, row, begin, end)"""
        return _math._SM_01_32_32_setRangeToOne(self, *args, **kwargs)

    def transpose(self):
        """transpose(self)"""
        return _math._SM_01_32_32_transpose(self)

    def logicalNot(self):
        """logicalNot(self)"""
        return _math._SM_01_32_32_logicalNot(self)

    def logicalOr(self, *args, **kwargs):
        """logicalOr(self, o)"""
        return _math._SM_01_32_32_logicalOr(self, *args, **kwargs)

    def logicalAnd(self, *args, **kwargs):
        """logicalAnd(self, o)"""
        return _math._SM_01_32_32_logicalAnd(self, *args, **kwargs)

    def inside(self):
        """inside(self)"""
        return _math._SM_01_32_32_inside(self)

    def edges(self, insideBorder=1):
        """edges(self, insideBorder=1)"""
        return _math._SM_01_32_32_edges(self, insideBorder)

    def CSRSize(self):
        """CSRSize(self) -> nupic::SparseBinaryMatrix< unsigned int,unsigned int >::size_type"""
        return _math._SM_01_32_32_CSRSize(self)

    def fromBinary(self, *args, **kwargs):
        """fromBinary(self, inStream)"""
        return _math._SM_01_32_32_fromBinary(self, *args, **kwargs)

    def toBinary(self, *args, **kwargs):
        """toBinary(self, outStream)"""
        return _math._SM_01_32_32_toBinary(self, *args, **kwargs)

    def equals(self, *args, **kwargs):
        """equals(self, o) -> bool"""
        return _math._SM_01_32_32_equals(self, *args, **kwargs)

    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], basestring):
                self.this = _MATH.new__SM_01_32_32(1)
                self.fromCSR(args[0])
            elif isinstance(args[0], numpy.ndarray) or hasattr(args[0], '__iter__'):
                self.this = _MATH.new__SM_01_32_32(1)
                self.fromDense(numpy.asarray(args[0]))
            elif isinstance(args[0], int):
                self.this = _MATH.new__SM_01_32_32(args[0])
            elif isinstance(args[0], _SM_01_32_32):
                self.this = _MATH.new__SM_01_32_32(1)
                self.copy(args[0])
            elif isinstance(args[0], _SparseMatrix32):
                self.this = _MATH.new__SM_01_32_32(1)
                nz_i,nz_j,nz_v = args[0].getAllNonZeros(True)
                self.setAllNonZeros(args[0].nRows(), args[0].nCols(), nz_i, nz_j)
        elif len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                self.this = _MATH.new__SM_01_32_32(args[0], args[1])

    def __str__(self):
        return self.toDense().__str__()

    def __setstate__(self, inString):
        self.this = _MATH.new__SM_01_32_32(1)
        self.thisown = 1
        self.fromCSR(inString)


    def __getstate__(self):
        """__getstate__(self) -> PyObject *"""
        return _math._SM_01_32_32___getstate__(self)

    def readState(self, *args, **kwargs):
        """readState(self, str)"""
        return _math._SM_01_32_32_readState(self, *args, **kwargs)

    def set(self, *args):
        """
        set(self, i, j, v)
        set(self, row, py_indices, v)
        """
        return _math._SM_01_32_32_set(self, *args)

    def setForAllRows(self, *args, **kwargs):
        """setForAllRows(self, py_indices, v)"""
        return _math._SM_01_32_32_setForAllRows(self, *args, **kwargs)

    def getAllNonZeros(self, two_lists=False):
        """getAllNonZeros(self, two_lists=False) -> PyObject *"""
        return _math._SM_01_32_32_getAllNonZeros(self, two_lists)

    def setAllNonZeros(self, *args, **kwargs):
        """setAllNonZeros(self, nrows, ncols, py_i, py_j, sorted=True)"""
        return _math._SM_01_32_32_setAllNonZeros(self, *args, **kwargs)

    def setSlice(self, *args):
        """
        setSlice(self, i_begin, j_begin, other)
        setSlice(self, i_begin, j_begin, py_other)
        """
        return _math._SM_01_32_32_setSlice(self, *args)

    def getCol(self, *args, **kwargs):
        """getCol(self, col) -> PyObject *"""
        return _math._SM_01_32_32_getCol(self, *args, **kwargs)

    def zeroRowsIndicator(self):
        """zeroRowsIndicator(self) -> PyObject *"""
        return _math._SM_01_32_32_zeroRowsIndicator(self)

    def nonZeroRowsIndicator(self):
        """nonZeroRowsIndicator(self) -> PyObject *"""
        return _math._SM_01_32_32_nonZeroRowsIndicator(self)

    def nNonZerosPerRow(self):
        """nNonZerosPerRow(self) -> PyObject *"""
        return _math._SM_01_32_32_nNonZerosPerRow(self)

    def nNonZerosPerCol(self):
        """nNonZerosPerCol(self) -> PyObject *"""
        return _math._SM_01_32_32_nNonZerosPerCol(self)

    def nNonZerosPerBox(self, *args, **kwargs):
        """nNonZerosPerBox(self, box_i, box_j) -> _SparseMatrix32"""
        return _math._SM_01_32_32_nNonZerosPerBox(self, *args, **kwargs)

    def rowSums(self):
        """rowSums(self) -> PyObject *"""
        return _math._SM_01_32_32_rowSums(self)

    def colSums(self):
        """colSums(self) -> PyObject *"""
        return _math._SM_01_32_32_colSums(self)

    def overlap(self, *args, **kwargs):
        """overlap(self, py_x) -> PyObject *"""
        return _math._SM_01_32_32_overlap(self, *args, **kwargs)

    def maxAllowedOverlap(self, *args, **kwargs):
        """maxAllowedOverlap(self, maxDistance, py_x) -> bool"""
        return _math._SM_01_32_32_maxAllowedOverlap(self, *args, **kwargs)

    def appendSparseRow(self, *args, **kwargs):
        """appendSparseRow(self, py_x)"""
        return _math._SM_01_32_32_appendSparseRow(self, *args, **kwargs)

    def appendDenseRow(self, *args, **kwargs):
        """appendDenseRow(self, py_x)"""
        return _math._SM_01_32_32_appendDenseRow(self, *args, **kwargs)

    def replaceSparseRow(self, *args, **kwargs):
        """replaceSparseRow(self, row, py_x)"""
        return _math._SM_01_32_32_replaceSparseRow(self, *args, **kwargs)

    def appendSparseCol(self, *args, **kwargs):
        """appendSparseCol(self, py_x)"""
        return _math._SM_01_32_32_appendSparseCol(self, *args, **kwargs)

    def getRowSparse(self, *args, **kwargs):
        """getRowSparse(self, row) -> PyObject *"""
        return _math._SM_01_32_32_getRowSparse(self, *args, **kwargs)

    def findRowSparse(self, *args, **kwargs):
        """findRowSparse(self, py_x) -> nupic::UInt32"""
        return _math._SM_01_32_32_findRowSparse(self, *args, **kwargs)

    def findRowDense(self, *args, **kwargs):
        """findRowDense(self, py_x) -> nupic::UInt32"""
        return _math._SM_01_32_32_findRowDense(self, *args, **kwargs)

    def fromDense(self, *args, **kwargs):
        """fromDense(self, py_m)"""
        return _math._SM_01_32_32_fromDense(self, *args, **kwargs)

    def toDense(self):
        """toDense(self) -> PyObject *"""
        return _math._SM_01_32_32_toDense(self)

    def toCSR(self, *args):
        """
        toCSR(self, outStream)
        toCSR(self) -> PyObject *
        """
        return _math._SM_01_32_32_toCSR(self, *args)

    def fromCSR(self, *args):
        """
        fromCSR(self, inStream)
        fromCSR(self, str)
        """
        return _math._SM_01_32_32_fromCSR(self, *args)

    def toPyString(self):
        """toPyString(self) -> PyObject *"""
        return _math._SM_01_32_32_toPyString(self)

    def fromPyString(self, *args, **kwargs):
        """fromPyString(self, s) -> bool"""
        return _math._SM_01_32_32_fromPyString(self, *args, **kwargs)

    def CSRSaveToFile(self, *args, **kwargs):
        """CSRSaveToFile(self, filename)"""
        return _math._SM_01_32_32_CSRSaveToFile(self, *args, **kwargs)

    def CSRLoadFromFile(self, *args, **kwargs):
        """CSRLoadFromFile(self, filename)"""
        return _math._SM_01_32_32_CSRLoadFromFile(self, *args, **kwargs)

    def binarySaveToFile(self, *args, **kwargs):
        """binarySaveToFile(self, filename)"""
        return _math._SM_01_32_32_binarySaveToFile(self, *args, **kwargs)

    def binaryLoadFromFile(self, *args, **kwargs):
        """binaryLoadFromFile(self, filename)"""
        return _math._SM_01_32_32_binaryLoadFromFile(self, *args, **kwargs)

    def fromSparseVector(self, *args, **kwargs):
        """fromSparseVector(self, nrows, ncols, py_x, offset=0)"""
        return _math._SM_01_32_32_fromSparseVector(self, *args, **kwargs)

    def toSparseVector(self, offset=0):
        """toSparseVector(self, offset=0) -> PyObject *"""
        return _math._SM_01_32_32_toSparseVector(self, offset)

    def getRow(self, *args, **kwargs):
        """getRow(self, row) -> PyObject *"""
        return _math._SM_01_32_32_getRow(self, *args, **kwargs)

    def rowFromDense(self, *args, **kwargs):
        """rowFromDense(self, row, py_x)"""
        return _math._SM_01_32_32_rowFromDense(self, *args, **kwargs)

    def rowToDense(self, *args, **kwargs):
        """rowToDense(self, row) -> PyObject *"""
        return _math._SM_01_32_32_rowToDense(self, *args, **kwargs)

    def rightVecSumAtNZ(self, *args, **kwargs):
        """rightVecSumAtNZ(self, py_x) -> PyObject *"""
        return _math._SM_01_32_32_rightVecSumAtNZ(self, *args, **kwargs)

    def rightVecSumAtNZ_fast(self, *args, **kwargs):
        """rightVecSumAtNZ_fast(self, py_x, py_y)"""
        return _math._SM_01_32_32_rightVecSumAtNZ_fast(self, *args, **kwargs)

    def leftVecSumAtNZ(self, *args, **kwargs):
        """leftVecSumAtNZ(self, py_x) -> PyObject *"""
        return _math._SM_01_32_32_leftVecSumAtNZ(self, *args, **kwargs)

    def leftVecSumAtNZ_fast(self, *args, **kwargs):
        """leftVecSumAtNZ_fast(self, py_x, py_y)"""
        return _math._SM_01_32_32_leftVecSumAtNZ_fast(self, *args, **kwargs)

    def rightDenseMatMaxAtNZ(self, *args, **kwargs):
        """rightDenseMatMaxAtNZ(self, mIn) -> PyObject *"""
        return _math._SM_01_32_32_rightDenseMatMaxAtNZ(self, *args, **kwargs)

    def leftDenseMatSumAtNZ(self, *args, **kwargs):
        """leftDenseMatSumAtNZ(self, mIn) -> PyObject *"""
        return _math._SM_01_32_32_leftDenseMatSumAtNZ(self, *args, **kwargs)

    def leftDenseMatMaxAtNZ(self, *args, **kwargs):
        """leftDenseMatMaxAtNZ(self, mIn) -> PyObject *"""
        return _math._SM_01_32_32_leftDenseMatMaxAtNZ(self, *args, **kwargs)

    def minHammingDistance(self, *args, **kwargs):
        """minHammingDistance(self, py_x) -> PyObject *"""
        return _math._SM_01_32_32_minHammingDistance(self, *args, **kwargs)

    def firstRowCloserThan(self, *args, **kwargs):
        """firstRowCloserThan(self, py_x, distance) -> PyObject *"""
        return _math._SM_01_32_32_firstRowCloserThan(self, *args, **kwargs)

    def firstRowCloserThan_dense(self, *args, **kwargs):
        """firstRowCloserThan_dense(self, py_x, distance) -> PyObject *"""
        return _math._SM_01_32_32_firstRowCloserThan_dense(self, *args, **kwargs)

    def vecMaxProd(self, *args, **kwargs):
        """vecMaxProd(self, py_x) -> PyObject *"""
        return _math._SM_01_32_32_vecMaxProd(self, *args, **kwargs)

    def rightVecArgMaxAtNZ(self, *args, **kwargs):
        """rightVecArgMaxAtNZ(self, py_x) -> PyObject *"""
        return _math._SM_01_32_32_rightVecArgMaxAtNZ(self, *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, other) -> bool"""
        return _math._SM_01_32_32___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, other) -> bool"""
        return _math._SM_01_32_32___ne__(self, *args, **kwargs)

_SM_01_32_32_swigregister = _math._SM_01_32_32_swigregister
_SM_01_32_32_swigregister(_SM_01_32_32)


def kthroot_product(*args, **kwargs):
  """kthroot_product(sm, segment_size, xIn, threshold) -> PyObject *"""
  return _math.kthroot_product(*args, **kwargs)

def sparseRightVecProd(*args, **kwargs):
  """sparseRightVecProd(a, m, n, x) -> PyObject *"""
  return _math.sparseRightVecProd(*args, **kwargs)

def isZero_01(*args, **kwargs):
  """isZero_01(py_x) -> bool"""
  return _math.isZero_01(*args, **kwargs)

def dense_vector_sum(*args, **kwargs):
  """dense_vector_sum(py_x) -> nupic::Real32"""
  return _math.dense_vector_sum(*args, **kwargs)

def binarize_with_threshold(*args, **kwargs):
  """binarize_with_threshold(threshold, py_x) -> PyObject *"""
  return _math.binarize_with_threshold(*args, **kwargs)

def nonZeroRowsIndicator_01(*args, **kwargs):
  """nonZeroRowsIndicator_01(nrows, ncols, py_x) -> PyObject *"""
  return _math.nonZeroRowsIndicator_01(*args, **kwargs)

def nonZeroColsIndicator_01(*args, **kwargs):
  """nonZeroColsIndicator_01(nrows, ncols, py_x) -> PyObject *"""
  return _math.nonZeroColsIndicator_01(*args, **kwargs)

def nNonZeroRows_01(*args, **kwargs):
  """nNonZeroRows_01(nrows, ncols, py_x) -> nupic::UInt32"""
  return _math.nNonZeroRows_01(*args, **kwargs)

def nNonZeroCols_01(*args, **kwargs):
  """nNonZeroCols_01(nrows, ncols, py_x) -> nupic::UInt32"""
  return _math.nNonZeroCols_01(*args, **kwargs)

def matrix_entropy(*args, **kwargs):
  """matrix_entropy(sm, s=1.0) -> PyObject *"""
  return _math.matrix_entropy(*args, **kwargs)

def smoothVecMaxProd(*args, **kwargs):
  """smoothVecMaxProd(sm, k, xIn) -> PyObject *"""
  return _math.smoothVecMaxProd(*args, **kwargs)

def smoothVecArgMaxProd(*args, **kwargs):
  """smoothVecArgMaxProd(sm, k, xIn) -> PyObject *"""
  return _math.smoothVecArgMaxProd(*args, **kwargs)

def LBP_piPrime(*args, **kwargs):
  """LBP_piPrime(mat, min_floor=0)"""
  return _math.LBP_piPrime(*args, **kwargs)

def SM_subtractNoAlloc(*args, **kwargs):
  """SM_subtractNoAlloc(A, B, min_floor=0)"""
  return _math.SM_subtractNoAlloc(*args, **kwargs)

def SM_assignNoAlloc(*args, **kwargs):
  """SM_assignNoAlloc(A, B)"""
  return _math.SM_assignNoAlloc(*args, **kwargs)

def SM_assignNoAllocFromBinary(*args, **kwargs):
  """SM_assignNoAllocFromBinary(A, B)"""
  return _math.SM_assignNoAllocFromBinary(*args, **kwargs)

def SM_addConstantOnNonZeros(*args, **kwargs):
  """SM_addConstantOnNonZeros(A, B, cval)"""
  return _math.SM_addConstantOnNonZeros(*args, **kwargs)

def SM_logSumNoAlloc(*args, **kwargs):
  """SM_logSumNoAlloc(A, B, min_floor=0)"""
  return _math.SM_logSumNoAlloc(*args, **kwargs)

def SM_logAddValNoAlloc(*args, **kwargs):
  """SM_logAddValNoAlloc(A, val, min_floor=0)"""
  return _math.SM_logAddValNoAlloc(*args, **kwargs)

def SM_logDiffNoAlloc(*args, **kwargs):
  """SM_logDiffNoAlloc(A, B, min_floor=0)"""
  return _math.SM_logDiffNoAlloc(*args, **kwargs)

def SM_addToNZOnly(*args, **kwargs):
  """SM_addToNZOnly(A, v, min_floor=0)"""
  return _math.SM_addToNZOnly(*args, **kwargs)

def SM_addToNZDownCols(*args, **kwargs):
  """SM_addToNZDownCols(A, py_x, min_floor=0)"""
  return _math.SM_addToNZDownCols(*args, **kwargs)

def SM_addToNZAcrossRows(*args, **kwargs):
  """SM_addToNZAcrossRows(A, py_x, min_floor=0)"""
  return _math.SM_addToNZAcrossRows(*args, **kwargs)

def count_gt(*args, **kwargs):
  """count_gt(py_x, threshold) -> nupic::UInt32"""
  return _math.count_gt(*args, **kwargs)

def count_gte(*args, **kwargs):
  """count_gte(py_x, threshold) -> nupic::UInt32"""
  return _math.count_gte(*args, **kwargs)

def count_lt(*args, **kwargs):
  """count_lt(py_x, threshold) -> nupic::UInt32"""
  return _math.count_lt(*args, **kwargs)

def partialArgsort(*args, **kwargs):
  """partialArgsort(k, py_x, py_r, direction=-1)"""
  return _math.partialArgsort(*args, **kwargs)

def positiveLearningPartialArgsort(*args, **kwargs):
  """positiveLearningPartialArgsort(k, py_x, py_r, rng, real_random=False)"""
  return _math.positiveLearningPartialArgsort(*args, **kwargs)

def logicalAnd(*args, **kwargs):
  """logicalAnd(py_x, py_y) -> PyObject *"""
  return _math.logicalAnd(*args, **kwargs)

def logicalAnd2(*args, **kwargs):
  """logicalAnd2(py_x, py_y)"""
  return _math.logicalAnd2(*args, **kwargs)
def asType(input, smType=_SparseMatrix32):
  if isinstance(input, smType): return input # No-op.
  output = smType()
  converter = "_copyFrom_" + input.__class__.__name__
  funcs = globals()
  if converter in funcs:
    funcs[converter](input, output)
  else:
    output.copy(input)
  return output

def outer(a, b, smType=_SparseMatrix32):
  sm = smType()
  sm.setFromOuter(a, b)
  return sm

# For backward compatibility in pickling
_SparseMatrix = _SparseMatrix32

SM32 = _SparseMatrix32
#SM64 = _SparseMatrix64
#SM128 = _SparseMatrix128

def SparseMatrix(*args, **keywords):
  """
  See help(nupic.bindings.math.SM32).
  """
  if 'dtype' not in keywords:
    return _SparseMatrix32(*args)
  dtype = keywords.pop('dtype')
  assert not keywords
  if dtype == 'Float32':
    return _SparseMatrix32(*args)
  #elif dtype == 'Float64':
  #  return _SparseMatrix64(*args)
  #elif dtype == 'Float128':
  #  return _SparseMatrix128(*args)
  else:
    raise Exception('Unsupported type' + dtype)

class _NearestNeighbor32(_SparseMatrix32):
    """Proxy of C++ nupic::NearestNeighbor<(nupic::SparseMatrix<(nupic::UInt32,nupic::Real32,nupic::Int32,nupic::Real64,nupic::DistanceToZero<(nupic::Real32)>)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> _NearestNeighbor32
        __init__(self, nrows, ncols) -> _NearestNeighbor32
        __init__(self, inStream) -> _NearestNeighbor32
        __init__(self, other) -> _NearestNeighbor32
        """
        this = _math.new__NearestNeighbor32(*args)
        try: self.this.append(this)
        except: self.this = this
    stddev_ = _swig_property(_math._NearestNeighbor32_stddev__get, _math._NearestNeighbor32_stddev__set)
    def __init__(self, *args):
      """
      Constructs a new NearestNeighbor from the following available arguments:
                    NearestNeighbor(): An empty sparse matrix with 0 rows and columns.
        NearestNeighbor(nrows, ncols): A zero sparse matrix with the
                                       specified rows and columns.
        NearestNeighbor(NearestNeighbor): Copies an existing sparse matrix.
              NearestNeighbor(string): Loads a NearestNeighbor from its serialized form.
         NearestNeighbor(numpy.array): Loads a NearestNeighbor from a numpy array.
         NearestNeighbor([[...],[...]]): Creates an array from a list of lists.
      """
      serialized = None
      dense = None
      toCopy = None
      if (len(args) == 1):
        if isinstance(args[0], basestring):
          serialized = args[0]
          args = tuple()
        elif isinstance(args[0], numpy.ndarray):
          dense = args[0]
          args = tuple()
        elif isinstance(args[0], _SparseMatrix32):
          toCopy = args[0]
          args = tuple()
        elif hasattr(args[0], '__iter__'):
          dense = args[0]
          args = tuple()
      this = _MATH.new__NearestNeighbor32(*args)
      try:
        self.this.append(this)
      except:
        self.this = this
      if toCopy is not None: self.copy(toCopy)
      elif serialized is not None:
        s = serialized.split(None, 1)
        if s[0] != 'csr' and s[0] != 'sm_csr_1.5':
          raise "Wrong CSR format, should start with 'csr' or 'sm_csr_1.5'"
        self.fromPyString(serialized)
      elif dense is not None:
        self.fromDense(numpy.asarray(dense,dtype=GetNumpyDataType('NTA_Real' +"32")))

    def __getstate__(self):
      """
      Used by the pickling mechanism to get state that will be saved.
      """
      return (self.toPyString(),)

    def __setstate__(self,tup):
      """
      Used by the pickling mechanism to restore state that was saved.
      """
      self.this = _MATH.new__NearestNeighbor32(1, 1)
      self.thisown = 1
      self.fromPyString(tup[0])

    def __str__(self):
      return self.toDense().__str__()

    def rowDist(self, *args, **kwargs):
        """rowDist(self, row, xIn) -> nupic::Real"""
        return _math._NearestNeighbor32_rowDist(self, *args, **kwargs)

    def vecLpDist(self, *args, **kwargs):
        """vecLpDist(self, p, xIn, take_root=True) -> PyObject *"""
        return _math._NearestNeighbor32_vecLpDist(self, *args, **kwargs)

    def LpNearest(self, *args, **kwargs):
        """LpNearest(self, p, row, k=1, take_root=True) -> PyObject *"""
        return _math._NearestNeighbor32_LpNearest(self, *args, **kwargs)

    def closestLp_w(self, *args, **kwargs):
        """closestLp_w(self, p, row) -> PyObject *"""
        return _math._NearestNeighbor32_closestLp_w(self, *args, **kwargs)

    def closestDot(self, *args, **kwargs):
        """closestDot(self, row) -> PyObject *"""
        return _math._NearestNeighbor32_closestDot(self, *args, **kwargs)

    def projLpNearest(self, *args, **kwargs):
        """projLpNearest(self, p, py_x, k=1, take_root=False) -> PyObject *"""
        return _math._NearestNeighbor32_projLpNearest(self, *args, **kwargs)

    def projRbf(self, *args, **kwargs):
        """projRbf(self, p, k, py_x) -> PyObject *"""
        return _math._NearestNeighbor32_projRbf(self, *args, **kwargs)

    __swig_destroy__ = _math.delete__NearestNeighbor32
_NearestNeighbor32_swigregister = _math._NearestNeighbor32_swigregister
_NearestNeighbor32_swigregister(_NearestNeighbor32)

NN32 = _NearestNeighbor32
#NN64 = _NearestNeighbor64

def NearestNeighbor(*args, **keywords):
  if 'dtype' not in keywords:
    return _NearestNeighbor32(*args)
  dtype = keywords.pop('dtype')
  if dtype == 'Float32':
    return _NearestNeighbor32(*args)
  #elif dtype == 'Float64':
  #  return _NearestNeighbor64(*args)
  else:
    raise Exception('Unknown type' + dtype)



def min_score_per_category(*args, **kwargs):
  """min_score_per_category(maxCategoryIdx, c_py, d_py) -> PyObject *"""
  return _math.min_score_per_category(*args, **kwargs)
#SM_01_32_16 = _SM_01_32_16
SM_01_32_32 = _SM_01_32_32
SparseBinaryMatrix = _SM_01_32_32

def SparseBinaryMatrix(*args, **keywords):
  return _SM_01_32_32(*args)


def l2_norm(*args, **kwargs):
  """l2_norm(py_x) -> nupic::Real32"""
  return _math.l2_norm(*args, **kwargs)
class _Gaussian2D_32(object):
    """Proxy of C++ nupic::Gaussian2D<(nupic::Real32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    c_x = _swig_property(_math._Gaussian2D_32_c_x_get, _math._Gaussian2D_32_c_x_set)
    c_y = _swig_property(_math._Gaussian2D_32_c_y_get, _math._Gaussian2D_32_c_y_set)
    s00 = _swig_property(_math._Gaussian2D_32_s00_get, _math._Gaussian2D_32_s00_set)
    s01 = _swig_property(_math._Gaussian2D_32_s01_get, _math._Gaussian2D_32_s01_set)
    s10 = _swig_property(_math._Gaussian2D_32_s10_get, _math._Gaussian2D_32_s10_set)
    s11 = _swig_property(_math._Gaussian2D_32_s11_get, _math._Gaussian2D_32_s11_set)
    s2 = _swig_property(_math._Gaussian2D_32_s2_get, _math._Gaussian2D_32_s2_set)
    k1 = _swig_property(_math._Gaussian2D_32_k1_get, _math._Gaussian2D_32_k1_set)
    def __init__(self, *args): 
        """
        __init__(self, c_x_, c_y_, s00_, s01_, s10_, s11_) -> _Gaussian2D_32
        __init__(self, o) -> _Gaussian2D_32
        """
        this = _math.new__Gaussian2D_32(*args)
        try: self.this.append(this)
        except: self.this = this
    def __call__(self, *args, **kwargs):
        """__call__(self, x, y) -> float"""
        return _math._Gaussian2D_32___call__(self, *args, **kwargs)

    def __init__(self, *args):
      this = _MATH.new__Gaussian2D_32(*args)
      try:
        self.this.append(this)
      except:
        self.this = this

    def __call__(self, x, y):
      return self.eval(x, y)

    def eval(self, *args, **kwargs):
        """eval(self, x, y) -> nupic::Real32"""
        return _math._Gaussian2D_32_eval(self, *args, **kwargs)

    __swig_destroy__ = _math.delete__Gaussian2D_32
_Gaussian2D_32_swigregister = _math._Gaussian2D_32_swigregister
_Gaussian2D_32_swigregister(_Gaussian2D_32)

Gaussian_2D = _Gaussian2D_32

def Gaussian2D(*args, **keywords):
  return _Gaussian2D_32(*args)

class _Set(object):
    """Proxy of C++ nupic::Set<(nupic::UInt32)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> _Set
        __init__(self, _m, _n, ss) -> _Set
        __init__(self, o) -> _Set
        """
        this = _math.new__Set(*args)
        try: self.this.append(this)
        except: self.this = this
    def n_elements(self):
        """n_elements(self) -> unsigned int"""
        return _math._Set_n_elements(self)

    def max_index(self):
        """max_index(self) -> unsigned int"""
        return _math._Set_max_index(self)

    def n_bytes(self):
        """n_bytes(self) -> unsigned int"""
        return _math._Set_n_bytes(self)

    def __init__(self, *args):
      this = _MATH.new__Set()
      try:
        self.this.append(this)
      except:
        self.this = this
      self.construct(args[0], args[1])

    def construct(self, *args):
        """
        construct(self, _m, _n, ss)
        construct(self, m, py_a)
        """
        return _math._Set_construct(self, *args)

    def intersection(self, *args):
        """
        intersection(self, n2, s2, r) -> unsigned int
        intersection(self, py_s2, py_r) -> nupic::UInt32
        """
        return _math._Set_intersection(self, *args)

    __swig_destroy__ = _math.delete__Set
_Set_swigregister = _math._Set_swigregister
_Set_swigregister(_Set)

Set = _Set

def Set(*args, **keywords):
  return _Set(*args)

class SegmentSparseMatrix32(object):
    """Proxy of C++ nupic::SegmentMatrixAdapter<(nupic::SparseMatrix<(nupic::UInt32,nupic::Real32,nupic::Int32,nupic::Real64,nupic::DistanceToZero<(nupic::Real32)>)>)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, nCells, nCols) -> SegmentSparseMatrix32"""
        this = _math.new_SegmentSparseMatrix32(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def nCells(self):
        """nCells(self) -> nupic::SegmentMatrixAdapter< nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > > >::size_type"""
        return _math.SegmentSparseMatrix32_nCells(self)

    def nSegments(self):
        """nSegments(self) -> nupic::SegmentMatrixAdapter< nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > > >::size_type"""
        return _math.SegmentSparseMatrix32_nSegments(self)

    def createSegment(self, *args, **kwargs):
        """createSegment(self, cell) -> nupic::SegmentMatrixAdapter< nupic::SparseMatrix< unsigned int,float,int,double,nupic::DistanceToZero< float > > >::size_type"""
        return _math.SegmentSparseMatrix32_createSegment(self, *args, **kwargs)

    def destroySegment(self, *args, **kwargs):
        """destroySegment(self, segment)"""
        return _math.SegmentSparseMatrix32_destroySegment(self, *args, **kwargs)

    def getSegmentsForCell(self, *args, **kwargs):
        """getSegmentsForCell(self, cell) -> VectorOfUInt32"""
        return _math.SegmentSparseMatrix32_getSegmentsForCell(self, *args, **kwargs)

    matrix = _swig_property(_math.SegmentSparseMatrix32_matrix_get, _math.SegmentSparseMatrix32_matrix_set)
    def createSegments(self, cells):
      return self._createSegments(numpy.asarray(cells, dtype="uint32"))

    def _createSegments(self, *args, **kwargs):
        """_createSegments(self, py_cells) -> PyObject *"""
        return _math.SegmentSparseMatrix32__createSegments(self, *args, **kwargs)

    def destroySegments(self, segments):
      self._destroySegments(numpy.asarray(segments, dtype="uint32"))

    def _destroySegments(self, *args, **kwargs):
        """_destroySegments(self, py_segments)"""
        return _math.SegmentSparseMatrix32__destroySegments(self, *args, **kwargs)

    def getSegmentCounts(self, cells):
      return self._getSegmentCounts(numpy.asarray(cells, dtype="uint32"))

    def _getSegmentCounts(self, *args, **kwargs):
        """_getSegmentCounts(self, py_cells) -> PyObject *"""
        return _math.SegmentSparseMatrix32__getSegmentCounts(self, *args, **kwargs)

    def getSegmentsForCell(self, cell):
      return self._getSegmentsForCell(cell)

    def _getSegmentsForCell(self, *args, **kwargs):
        """_getSegmentsForCell(self, cell) -> PyObject *"""
        return _math.SegmentSparseMatrix32__getSegmentsForCell(self, *args, **kwargs)

    def sortSegmentsByCell(self, segments):
      # Can't convert it, since we're sorting it in place.
      assert segments.dtype == "uint32"
      self._sortSegmentsByCell(segments)

    def _sortSegmentsByCell(self, *args, **kwargs):
        """_sortSegmentsByCell(self, py_segments)"""
        return _math.SegmentSparseMatrix32__sortSegmentsByCell(self, *args, **kwargs)

    def filterSegmentsByCell(self, segments, cells, assumeSorted=False):
      segments = numpy.asarray(segments, dtype="uint32")
      cells = numpy.asarray(cells, dtype="uint32")

      if not assumeSorted:
        segments = numpy.copy(segments)
        self.sortSegmentsByCell(segments)
        cells = numpy.sort(cells)

      return self._filterSegmentsByCell(segments, cells)

    def _filterSegmentsByCell(self, *args, **kwargs):
        """_filterSegmentsByCell(self, py_segments, py_cells) -> PyObject *"""
        return _math.SegmentSparseMatrix32__filterSegmentsByCell(self, *args, **kwargs)

    def mapSegmentsToCells(self, segments):
      segments = numpy.asarray(segments, dtype="uint32")
      return self._mapSegmentsToCells(segments)

    def _mapSegmentsToCells(self, *args, **kwargs):
        """_mapSegmentsToCells(self, py_segments) -> PyObject *"""
        return _math.SegmentSparseMatrix32__mapSegmentsToCells(self, *args, **kwargs)

    __swig_destroy__ = _math.delete_SegmentSparseMatrix32
SegmentSparseMatrix32_swigregister = _math.SegmentSparseMatrix32_swigregister
SegmentSparseMatrix32_swigregister(SegmentSparseMatrix32)

def SegmentSparseMatrix(*args, **kwargs):
  if "dtype" in kwargs:
    dtype = keywords.pop("dtype")
    assert dtype == "Float32"

  return SegmentSparseMatrix32(*args, **kwargs)

class SparseMatrixConnections(SegmentSparseMatrix32):
    """Proxy of C++ nupic::SparseMatrixConnections class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, numCells, numInputs) -> SparseMatrixConnections"""
        this = _math.new_SparseMatrixConnections(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def computeActivity(self, *args):
        """
        computeActivity(self, activeInputs_begin, activeInputs_end, overlaps_begin)
        computeActivity(self, activeInputs_begin, activeInputs_end, permanenceThreshold, overlaps_begin)
        """
        return _math.SparseMatrixConnections_computeActivity(self, *args)

    def adjustSynapses(self, *args, **kwargs):
        """
        adjustSynapses(self, segments_begin, segments_end, activeInputs_begin, activeInputs_end, activePermanenceDelta, 
            inactivePermanenceDelta)
        """
        return _math.SparseMatrixConnections_adjustSynapses(self, *args, **kwargs)

    def adjustActiveSynapses(self, *args, **kwargs):
        """adjustActiveSynapses(self, segments_begin, segments_end, activeInputs_begin, activeInputs_end, permanenceDelta)"""
        return _math.SparseMatrixConnections_adjustActiveSynapses(self, *args, **kwargs)

    def adjustInactiveSynapses(self, *args, **kwargs):
        """adjustInactiveSynapses(self, segments_begin, segments_end, activeInputs_begin, activeInputs_end, permanenceDelta)"""
        return _math.SparseMatrixConnections_adjustInactiveSynapses(self, *args, **kwargs)

    def growSynapses(self, *args, **kwargs):
        """growSynapses(self, segments_begin, segments_end, inputs_begin, inputs_end, initialPermanence)"""
        return _math.SparseMatrixConnections_growSynapses(self, *args, **kwargs)

    def growSynapsesToSample(self, *args):
        """
        growSynapsesToSample(self, segments_begin, segments_end, inputs_begin, inputs_end, sampleSize, initialPermanence, 
            rng)
        growSynapsesToSample(self, segments_begin, segments_end, inputs_begin, inputs_end, sampleSizes_begin, sampleSizes_end, 
            initialPermanence, rng)
        """
        return _math.SparseMatrixConnections_growSynapsesToSample(self, *args)

    def clipPermanences(self, *args, **kwargs):
        """clipPermanences(self, segments_begin, segments_end)"""
        return _math.SparseMatrixConnections_clipPermanences(self, *args, **kwargs)

    def mapSegmentsToSynapseCounts(self, *args, **kwargs):
        """mapSegmentsToSynapseCounts(self, segments_begin, segments_end, out_begin)"""
        return _math.SparseMatrixConnections_mapSegmentsToSynapseCounts(self, *args, **kwargs)

    def computeActivity(self, activeInputs, permanenceThreshold=None, out=None):
      activeInputs = numpy.asarray(activeInputs, dtype="uint32")

      if out is None:
        out = numpy.empty(self.matrix.nRows(), dtype="int32")
      else:
        assert out.dtype == "int32"

      if permanenceThreshold is None:
        self._computeActivity(activeInputs, out)
      else:
        self._permanenceThresholdedComputeActivity(activeInputs,
                                                   permanenceThreshold, out)

      return out

    def _computeActivity(self, *args, **kwargs):
        """_computeActivity(self, py_activeInputs, py_overlaps)"""
        return _math.SparseMatrixConnections__computeActivity(self, *args, **kwargs)

    def _permanenceThresholdedComputeActivity(self, *args, **kwargs):
        """_permanenceThresholdedComputeActivity(self, py_activeInputs, permanenceThreshold, py_overlaps)"""
        return _math.SparseMatrixConnections__permanenceThresholdedComputeActivity(self, *args, **kwargs)

    def adjustSynapses(self, segments, activeInputs, activePermanenceDelta,
                       inactivePermanenceDelta):
      self._adjustSynapses(numpy.asarray(segments, dtype="uint32"),
                           numpy.asarray(activeInputs, dtype="uint32"),
                           activePermanenceDelta, inactivePermanenceDelta)

    def _adjustSynapses(self, *args, **kwargs):
        """_adjustSynapses(self, py_segments, py_activeInputs, activePermanenceDelta, inactivePermanenceDelta)"""
        return _math.SparseMatrixConnections__adjustSynapses(self, *args, **kwargs)

    def adjustActiveSynapses(self, segments, activeInputs, permanenceDelta):
      self._adjustActiveSynapses(numpy.asarray(segments, dtype="uint32"),
                                 numpy.asarray(activeInputs, dtype="uint32"),
                                 permanenceDelta)

    def _adjustActiveSynapses(self, *args, **kwargs):
        """_adjustActiveSynapses(self, py_segments, py_activeInputs, permanenceDelta)"""
        return _math.SparseMatrixConnections__adjustActiveSynapses(self, *args, **kwargs)

    def adjustInactiveSynapses(self, segments, activeInputs, permanenceDelta):
      self._adjustInactiveSynapses(numpy.asarray(segments, dtype="uint32"),
                                   numpy.asarray(activeInputs, dtype="uint32"),
                                   permanenceDelta)

    def _adjustInactiveSynapses(self, *args, **kwargs):
        """_adjustInactiveSynapses(self, py_segments, py_activeInputs, permanenceDelta)"""
        return _math.SparseMatrixConnections__adjustInactiveSynapses(self, *args, **kwargs)

    def growSynapses(self, segments, activeInputs, initialPermanence,
                     assumeInputsSorted=False):
      if not assumeInputsSorted:
        activeInputs = numpy.sort(activeInputs)

      self._growSynapses(
          numpy.asarray(segments, dtype="uint32"),
          numpy.asarray(activeInputs, dtype="uint32"),
          initialPermanence)

    def _growSynapses(self, *args, **kwargs):
        """_growSynapses(self, py_segments, py_activeInputs, initialPermanence)"""
        return _math.SparseMatrixConnections__growSynapses(self, *args, **kwargs)

    def growSynapsesToSample(self, segments, activeInputs, sampleSize,
                             initialPermanence, rng, assumeInputsSorted=False):
      if not assumeInputsSorted:
        activeInputs = numpy.sort(activeInputs)

      if isinstance(sampleSize, numbers.Number):
        self._growSynapsesToSample_singleCount(
          numpy.asarray(segments, dtype="uint32"),
          numpy.asarray(activeInputs, dtype="uint32"),
          sampleSize,
          initialPermanence,
          rng)
      else:
        self._growSynapsesToSample_multipleCounts(
          numpy.asarray(segments, dtype="uint32"),
          numpy.asarray(activeInputs, dtype="uint32"),
          numpy.asarray(sampleSize, dtype="int32"),
          initialPermanence,
          rng)

    def _growSynapsesToSample_singleCount(self, *args, **kwargs):
        """_growSynapsesToSample_singleCount(self, py_segments, py_activeInputs, sampleSize, initialPermanence, rng)"""
        return _math.SparseMatrixConnections__growSynapsesToSample_singleCount(self, *args, **kwargs)

    def _growSynapsesToSample_multipleCounts(self, *args, **kwargs):
        """_growSynapsesToSample_multipleCounts(self, py_segments, py_activeInputs, py_sampleSizes, initialPermanence, rng)"""
        return _math.SparseMatrixConnections__growSynapsesToSample_multipleCounts(self, *args, **kwargs)

    def clipPermanences(self, segments):
      self._clipPermanences(numpy.asarray(segments, dtype="uint32"))

    def _clipPermanences(self, *args, **kwargs):
        """_clipPermanences(self, py_segments)"""
        return _math.SparseMatrixConnections__clipPermanences(self, *args, **kwargs)

    def mapSegmentsToSynapseCounts(self, segments):
      return self._mapSegmentsToSynapseCounts(
        numpy.asarray(segments, dtype="uint32"))

    def _mapSegmentsToSynapseCounts(self, *args, **kwargs):
        """_mapSegmentsToSynapseCounts(self, py_segments) -> PyObject *"""
        return _math.SparseMatrixConnections__mapSegmentsToSynapseCounts(self, *args, **kwargs)

    __swig_destroy__ = _math.delete_SparseMatrixConnections
SparseMatrixConnections_swigregister = _math.SparseMatrixConnections_swigregister
SparseMatrixConnections_swigregister(SparseMatrixConnections)

PYSPARSETENSOR_MAX_RANK = _math.PYSPARSETENSOR_MAX_RANK
class PyTensorIndex(object):
    """Proxy of C++ PyTensorIndex class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self) -> PyTensorIndex
        __init__(self, x) -> PyTensorIndex
        __init__(self, i) -> PyTensorIndex
        __init__(self, i, j) -> PyTensorIndex
        __init__(self, i, j, k) -> PyTensorIndex
        __init__(self, i, j, k, l) -> PyTensorIndex
        __init__(self, i, j, k, l, m) -> PyTensorIndex
        __init__(self, i, j, k, l, m, n) -> PyTensorIndex
        __init__(self, i) -> PyTensorIndex
        __init__(self, i1, i2) -> PyTensorIndex
        """
        this = _math.new_PyTensorIndex(*args)
        try: self.this.append(this)
        except: self.this = this
    def size(self):
        """size(self) -> nupic::UInt32"""
        return _math.PyTensorIndex_size(self)

    def __getitem__(self, *args, **kwargs):
        """__getitem__(self, i) -> nupic::UInt32"""
        return _math.PyTensorIndex___getitem__(self, *args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        """__setitem__(self, i, d)"""
        return _math.PyTensorIndex___setitem__(self, *args, **kwargs)

    def __len__(self):
        """__len__(self) -> nupic::UInt32"""
        return _math.PyTensorIndex___len__(self)

    def begin(self, *args):
        """
        begin(self) -> nupic::UInt32 const
        begin(self) -> nupic::UInt32 *
        """
        return _math.PyTensorIndex_begin(self, *args)

    def end(self, *args):
        """
        end(self) -> nupic::UInt32 const
        end(self) -> nupic::UInt32 *
        """
        return _math.PyTensorIndex_end(self, *args)

    def __lt__(self, *args, **kwargs):
        """__lt__(self, j) -> bool"""
        return _math.PyTensorIndex___lt__(self, *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        """__gt__(self, j) -> bool"""
        return _math.PyTensorIndex___gt__(self, *args, **kwargs)

    def __eq__(self, *args):
        """
        __eq__(self, j) -> bool
        __eq__(self, j) -> bool
        """
        return _math.PyTensorIndex___eq__(self, *args)

    def __ne__(self, *args):
        """
        __ne__(self, j) -> bool
        __ne__(self, j) -> bool
        """
        return _math.PyTensorIndex___ne__(self, *args)

    def __str__(self):
        """__str__(self) -> std::string"""
        return _math.PyTensorIndex___str__(self)

    def __getslice__(self, *args, **kwargs):
        """__getslice__(self, i, j) -> VectorOfUInt32"""
        return _math.PyTensorIndex___getslice__(self, *args, **kwargs)

    def __setslice__(self, *args, **kwargs):
        """__setslice__(self, i, j, x)"""
        return _math.PyTensorIndex___setslice__(self, *args, **kwargs)

    def asTuple(self):
        """asTuple(self) -> VectorOfUInt32"""
        return _math.PyTensorIndex_asTuple(self)

    def __getstate__(self):
        """__getstate__(self) -> VectorOfUInt32"""
        return _math.PyTensorIndex___getstate__(self)

    def __setstate__(self, tup):
      self.this = _MATH.new_PyTensorIndex(tup)
      self.thisown = 1

    __swig_destroy__ = _math.delete_PyTensorIndex
PyTensorIndex_swigregister = _math.PyTensorIndex_swigregister
PyTensorIndex_swigregister(PyTensorIndex)


def concatenate(*args, **kwargs):
  """concatenate(i1, i2) -> PyTensorIndex"""
  return _math.concatenate(*args, **kwargs)
class PyDomain(_Domain32):
    """Proxy of C++ PyDomain class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, lowerHalfSpace) -> PyDomain
        __init__(self, lower, upper) -> PyDomain
        """
        this = _math.new_PyDomain(*args)
        try: self.this.append(this)
        except: self.this = this
    def getLowerBound(self):
        """getLowerBound(self) -> PyTensorIndex"""
        return _math.PyDomain_getLowerBound(self)

    def getUpperBound(self):
        """getUpperBound(self) -> PyTensorIndex"""
        return _math.PyDomain_getUpperBound(self)

    def __getitem__(self, *args, **kwargs):
        """__getitem__(self, i) -> VectorOfUInt32"""
        return _math.PyDomain___getitem__(self, *args, **kwargs)

    def getDimensions(self):
        """getDimensions(self) -> PyTensorIndex"""
        return _math.PyDomain_getDimensions(self)

    def getNumOpenDims(self):
        """getNumOpenDims(self) -> nupic::UInt32"""
        return _math.PyDomain_getNumOpenDims(self)

    def getOpenDimensions(self):
        """getOpenDimensions(self) -> PyTensorIndex"""
        return _math.PyDomain_getOpenDimensions(self)

    def getSliceBounds(self):
        """getSliceBounds(self) -> PyTensorIndex"""
        return _math.PyDomain_getSliceBounds(self)

    def doesInclude(self, *args, **kwargs):
        """doesInclude(self, x) -> bool"""
        return _math.PyDomain_doesInclude(self, *args, **kwargs)

    def __str__(self):
        """__str__(self) -> std::string"""
        return _math.PyDomain___str__(self)

    __swig_destroy__ = _math.delete_PyDomain
PyDomain_swigregister = _math.PyDomain_swigregister
PyDomain_swigregister(PyDomain)

class PySparseTensor(object):
    """Proxy of C++ PySparseTensor class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, state) -> PySparseTensor
        __init__(self, bounds) -> PySparseTensor
        __init__(self, bounds) -> PySparseTensor
        __init__(self, dense) -> PySparseTensor
        """
        this = _math.new_PySparseTensor(*args)
        try: self.this.append(this)
        except: self.this = this
    def getRank(self):
        """getRank(self) -> nupic::UInt32"""
        return _math.PySparseTensor_getRank(self)

    def getBounds(self):
        """getBounds(self) -> PyTensorIndex"""
        return _math.PySparseTensor_getBounds(self)

    def getBound(self, *args, **kwargs):
        """getBound(self, dim) -> nupic::UInt32"""
        return _math.PySparseTensor_getBound(self, *args, **kwargs)

    def get(self, *args):
        """
        get(self, i) -> nupic::Real
        get(self, i) -> nupic::Real
        """
        return _math.PySparseTensor_get(self, *args)

    def set(self, *args):
        """
        set(self, i, x)
        set(self, i, x)
        set(self, i, x)
        set(self, i, x)
        """
        return _math.PySparseTensor_set(self, *args)

    def getNNonZeros(self):
        """getNNonZeros(self) -> nupic::UInt32"""
        return _math.PySparseTensor_getNNonZeros(self)

    def nNonZeros(self):
        """nNonZeros(self) -> nupic::UInt32"""
        return _math.PySparseTensor_nNonZeros(self)

    def reshape(self, *args, **kwargs):
        """reshape(self, dims) -> PySparseTensor"""
        return _math.PySparseTensor_reshape(self, *args, **kwargs)

    def resize(self, *args):
        """
        resize(self, dims)
        resize(self, dims)
        """
        return _math.PySparseTensor_resize(self, *args)

    def extract(self, *args, **kwargs):
        """extract(self, dim, ind) -> PySparseTensor"""
        return _math.PySparseTensor_extract(self, *args, **kwargs)

    def reduce(self, *args, **kwargs):
        """reduce(self, dim, ind)"""
        return _math.PySparseTensor_reduce(self, *args, **kwargs)

    def getSlice(self, *args, **kwargs):
        """getSlice(self, range) -> PySparseTensor"""
        return _math.PySparseTensor_getSlice(self, *args, **kwargs)

    def setSlice(self, *args, **kwargs):
        """setSlice(self, range, slice)"""
        return _math.PySparseTensor_setSlice(self, *args, **kwargs)

    def setZero(self, *args, **kwargs):
        """setZero(self, range)"""
        return _math.PySparseTensor_setZero(self, *args, **kwargs)

    def addSlice(self, *args, **kwargs):
        """addSlice(self, which, src, dst)"""
        return _math.PySparseTensor_addSlice(self, *args, **kwargs)

    def factorMultiply(self, *args):
        """
        factorMultiply(self, dims, B) -> PySparseTensor
        factorMultiply(self, dims, B) -> PySparseTensor
        """
        return _math.PySparseTensor_factorMultiply(self, *args)

    def outerProduct(self, *args, **kwargs):
        """outerProduct(self, B) -> PySparseTensor"""
        return _math.PySparseTensor_outerProduct(self, *args, **kwargs)

    def innerProduct(self, *args, **kwargs):
        """innerProduct(self, dim1, dim2, B) -> PySparseTensor"""
        return _math.PySparseTensor_innerProduct(self, *args, **kwargs)

    def __add__(self, *args, **kwargs):
        """__add__(self, B) -> PySparseTensor"""
        return _math.PySparseTensor___add__(self, *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        """__sub__(self, B) -> PySparseTensor"""
        return _math.PySparseTensor___sub__(self, *args, **kwargs)

    def factorAdd(self, *args):
        """
        factorAdd(self, dims, B) -> PySparseTensor
        factorAdd(self, dims, B) -> PySparseTensor
        """
        return _math.PySparseTensor_factorAdd(self, *args)

    def getComplementBounds(self, *args, **kwargs):
        """getComplementBounds(self, dims) -> PySparseTensor"""
        return _math.PySparseTensor_getComplementBounds(self, *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        """__mul__(self, x) -> PySparseTensor"""
        return _math.PySparseTensor___mul__(self, *args, **kwargs)

    def __neg__(self):
        """__neg__(self) -> PySparseTensor"""
        return _math.PySparseTensor___neg__(self)

    def marginalize(self, *args):
        """
        marginalize(self) -> double
        marginalize(self, dims) -> PySparseTensor
        marginalize(self, dims) -> PySparseTensor
        """
        return _math.PySparseTensor_marginalize(self, *args)

    def argmax(self):
        """argmax(self) -> PyTensorIndex"""
        return _math.PySparseTensor_argmax(self)

    def max(self, *args):
        """
        max(self) -> nupic::Real
        max(self, dims) -> PySparseTensor
        max(self, dims) -> PySparseTensor
        """
        return _math.PySparseTensor_max(self, *args)

    def tolist(self):
        """tolist(self) -> PyObject *"""
        return _math.PySparseTensor_tolist(self)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, B) -> bool"""
        return _math.PySparseTensor___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, B) -> bool"""
        return _math.PySparseTensor___ne__(self, *args, **kwargs)

    def toDense(self):
        """toDense(self) -> PyObject *"""
        return _math.PySparseTensor_toDense(self)

    def __str__(self):
        """__str__(self) -> PyObject *"""
        return _math.PySparseTensor___str__(self)

    def __getstate__(self):
        """__getstate__(self) -> std::string"""
        return _math.PySparseTensor___getstate__(self)

    def copy(self):
        """copy(self) -> PySparseTensor"""
        return _math.PySparseTensor_copy(self)

    def _fixSlice(self, dim, ub):
        """Used internally to fill out blank fields in slicing records."""
        assert (dim.step == 1) or (dim.step is None)
        start = dim.start
        if start is None: start = 0
        elif start < 0: start += ub
        stop = dim.stop
        if stop is None: stop = ub
        elif stop < 0: stop += ub
        return slice(start, stop, 1)

    def _getDomain(self, key, bounds):
        """Used internally to convert a list of slices to a valid Domain."""
        slices = [None] * len(bounds)
        cur = 0
        hasEllipsis = False
        for dim in key:
            if dim is Ellipsis:
                assert not hasEllipsis
                hasEllipsis = True
                toFill = len(bounds) - len(key) + 1
                if toFill > 0:
                    for j in xrange(toFill-1):
                        slices[cur] = slice(0, bounds[cur], 1)
                        cur += 1
                    slices[cur] = slice(0, bounds[cur], 1)
            elif isinstance(dim, slice): 
                slices[cur] = self._fixSlice(dim, bounds[cur])
            else: slices[cur] = slice(dim, dim, 0)
            cur += 1
        return Domain([x.start for x in slices], [x.stop for x in slices])

    def getSliceWrap(self, key):
        return self.getSlice(self._getDomain(key, self.getBounds()))
          
    def setSliceWrap(self, key, value):
        self.setSlice(self._getDomain(key, self.getBounds()), value)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            hasSlices = False
            for dim in key:
                if (dim is Ellipsis) or isinstance(dim, slice):
                    hasSlices = True
                    break
            if hasSlices: return self.getSliceWrap(key)
            else: return _MATH.PySparseTensor_get(self, key)
        elif (key is Ellipsis) or isinstance(key, slice):
            return self.getSliceWrap((key,))
        else:
            return _MATH.PySparseTensor_get(self, (key,))
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            hasSlices = False
            for dim in key:
                if isinstance(dim, slice): hasSlices = True
            if hasSlices: return self.setSliceWrap(key, value)
            else: return _MATH.PySparseTensor_set(self, key, value)
        elif (key is Ellipsis) or isinstance(key, slice):
            return self.setSliceWrap((key,), value)
        else:
            return _MATH.PySparseTensor_set(self, (key,), value)
    def __setstate__(self, s):
        self.this = _MATH.new_PySparseTensor(s)
        self.thisown = 1

    __swig_destroy__ = _math.delete_PySparseTensor
PySparseTensor_swigregister = _math.PySparseTensor_swigregister
PySparseTensor_swigregister(PySparseTensor)

SparseTensor = PySparseTensor
TensorIndex = PyTensorIndex
Domain = PyDomain


def lgamma(*args, **kwargs):
  """lgamma(x) -> nupic::Real64"""
  return _math.lgamma(*args, **kwargs)

def digamma(*args, **kwargs):
  """digamma(x) -> nupic::Real64"""
  return _math.digamma(*args, **kwargs)

def beta(*args, **kwargs):
  """beta(x, y) -> nupic::Real64"""
  return _math.beta(*args, **kwargs)

def erf(*args, **kwargs):
  """erf(x) -> nupic::Real64"""
  return _math.erf(*args, **kwargs)

def nearlyZeroRange(*args, **kwargs):
  """nearlyZeroRange(py_x, eps=Epsilon) -> bool"""
  return _math.nearlyZeroRange(*args, **kwargs)

def nearlyEqualRange(*args, **kwargs):
  """nearlyEqualRange(py_x, py_y, eps=Epsilon) -> bool"""
  return _math.nearlyEqualRange(*args, **kwargs)

def positive_less_than(*args, **kwargs):
  """positive_less_than(py_x, eps=Epsilon) -> bool"""
  return _math.positive_less_than(*args, **kwargs)

def winnerTakesAll_3(*args, **kwargs):
  """winnerTakesAll_3(k, seg_size, py_x) -> PyObject *"""
  return _math.winnerTakesAll_3(*args, **kwargs)

def fact(*args, **kwargs):
  """fact(n) -> double"""
  return _math.fact(*args, **kwargs)

def lfact(*args, **kwargs):
  """lfact(n) -> double"""
  return _math.lfact(*args, **kwargs)

def binomial(*args, **kwargs):
  """binomial(n, k) -> double"""
  return _math.binomial(*args, **kwargs)
class LoggingException(object):
    """Proxy of C++ nupic::LoggingException class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _math.delete_LoggingException
    def getMessage(self):
        """getMessage(self) -> char const *"""
        return _math.LoggingException_getMessage(self)

    def __lshift__(self, *args, **kwargs):
        """__lshift__(self, v) -> LoggingException"""
        return _math.LoggingException___lshift__(self, *args, **kwargs)

    def __init__(self, *args): 
        """
        __init__(self, filename, lineno) -> LoggingException
        __init__(self, l) -> LoggingException
        """
        this = _math.new_LoggingException(*args)
        try: self.this.append(this)
        except: self.this = this
LoggingException_swigregister = _math.LoggingException_swigregister
LoggingException_swigregister(LoggingException)
pi = cvar.pi

class Random(object):
    """Proxy of C++ nupic::Random class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def getSeeder():
        """getSeeder() -> RandomSeedFuncPtr"""
        return _math.Random_getSeeder()

    getSeeder = staticmethod(getSeeder)
    def __init__(self, *args): 
        """
        __init__(self, seed=0) -> Random
        __init__(self, arg2) -> Random
        """
        this = _math.new_Random(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _math.delete_Random
    def getUInt32(self, *args, **kwargs):
        """getUInt32(self, max=MAX32) -> nupic::UInt32"""
        return _math.Random_getUInt32(self, *args, **kwargs)

    def getUInt64(self, *args, **kwargs):
        """getUInt64(self, max=MAX64) -> nupic::UInt64"""
        return _math.Random_getUInt64(self, *args, **kwargs)

    def getReal64(self):
        """getReal64(self) -> nupic::Real64"""
        return _math.Random_getReal64(self)

    def __call__(self, *args, **kwargs):
        """__call__(self, n=MAX32) -> nupic::UInt32"""
        return _math.Random___call__(self, *args, **kwargs)

    def getSeed(self):
        """getSeed(self) -> nupic::UInt64"""
        return _math.Random_getSeed(self)

    def max(self):
        """max(self) -> nupic::Random::result_type"""
        return _math.Random_max(self)

    def min(self):
        """min(self) -> nupic::Random::result_type"""
        return _math.Random_min(self)

    def __eq__(self, *args, **kwargs):
        """__eq__(self, other) -> bool"""
        return _math.Random___eq__(self, *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        """__ne__(self, other) -> bool"""
        return _math.Random___ne__(self, *args, **kwargs)

    def initSeeder(*args, **kwargs):
        """initSeeder(r)"""
        return _math.Random_initSeeder(*args, **kwargs)

    initSeeder = staticmethod(initSeeder)
    def shutdown():
        """shutdown()"""
        return _math.Random_shutdown()

    shutdown = staticmethod(shutdown)
    def __setstate__(self, state):
      self.this = _MATH.new_Random(1)
      self.thisown = 1
      self.setState(state)


    def __getstate__(self):
        """__getstate__(self) -> std::string"""
        return _math.Random___getstate__(self)

    def getState(self):
        """getState(self) -> std::string"""
        return _math.Random_getState(self)

    def setState(self, *args, **kwargs):
        """setState(self, s)"""
        return _math.Random_setState(self, *args, **kwargs)

    def setSeed(self, *args, **kwargs):
        """setSeed(self, x)"""
        return _math.Random_setSeed(self, *args, **kwargs)

    def jumpAhead(self, *args, **kwargs):
        """jumpAhead(self, n)"""
        return _math.Random_jumpAhead(self, *args, **kwargs)

    def initializeUInt32Array(self, *args, **kwargs):
        """initializeUInt32Array(self, py_array, max_value)"""
        return _math.Random_initializeUInt32Array(self, *args, **kwargs)

    def initializeReal32Array(self, *args, **kwargs):
        """initializeReal32Array(self, py_array)"""
        return _math.Random_initializeReal32Array(self, *args, **kwargs)

    def initializeReal32Array_01(self, *args, **kwargs):
        """initializeReal32Array_01(self, py_array, proba)"""
        return _math.Random_initializeReal32Array_01(self, *args, **kwargs)

    def sample(self, *args, **kwargs):
        """sample(self, population, choices) -> PyObject *"""
        return _math.Random_sample(self, *args, **kwargs)

    def shuffle(self, *args, **kwargs):
        """shuffle(self, obj) -> PyObject *"""
        return _math.Random_shuffle(self, *args, **kwargs)

Random_swigregister = _math.Random_swigregister
Random_swigregister(Random)

def Random_getSeeder():
  """Random_getSeeder() -> RandomSeedFuncPtr"""
  return _math.Random_getSeeder()
Random.MAX32 = _math.cvar.Random_MAX32
Random.MAX64 = _math.cvar.Random_MAX64

def Random_initSeeder(*args, **kwargs):
  """Random_initSeeder(r)"""
  return _math.Random_initSeeder(*args, **kwargs)

def Random_shutdown():
  """Random_shutdown()"""
  return _math.Random_shutdown()


def __lshift__(*args, **kwargs):
  """__lshift__(arg1, arg2) -> std::ostream &"""
  return _math.__lshift__(*args, **kwargs)

def __rshift__(*args, **kwargs):
  """__rshift__(arg1, arg2) -> std::istream &"""
  return _math.__rshift__(*args, **kwargs)

def GetRandomSeed():
  """GetRandomSeed() -> NTA_UInt64"""
  return _math.GetRandomSeed()


