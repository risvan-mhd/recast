r"""Wrapper for vterm.h

Generated with:
ctypesgen /usr/include/vterm.h --all-headers --cpp clang -E -I/usr/include -I/usr/include/x86_64-linux-gnu -L/usr/lib/x86_64-linux-gnu -lvterm -o libvterm.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['/usr/lib/x86_64-linux-gnu']

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs(['/usr/lib/x86_64-linux-gnu'])

# Begin libraries
_libs["vterm"] = load_library("vterm")

# 1 libraries
# End libraries

# No modules

__u_char = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 31

__u_short = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 32

__u_int = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 33

__u_long = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 34

__int8_t = c_char# /usr/include/x86_64-linux-gnu/bits/types.h: 37

__uint8_t = c_ubyte# /usr/include/x86_64-linux-gnu/bits/types.h: 38

__int16_t = c_short# /usr/include/x86_64-linux-gnu/bits/types.h: 39

__uint16_t = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 40

__int32_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 41

__uint32_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 42

__int64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 44

__uint64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 45

__int_least8_t = c_int8# /usr/include/x86_64-linux-gnu/bits/types.h: 52

__uint_least8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/types.h: 53

__int_least16_t = c_int16# /usr/include/x86_64-linux-gnu/bits/types.h: 54

__uint_least16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/types.h: 55

__int_least32_t = c_int32# /usr/include/x86_64-linux-gnu/bits/types.h: 56

__uint_least32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/types.h: 57

__int_least64_t = c_int64# /usr/include/x86_64-linux-gnu/bits/types.h: 58

__uint_least64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 59

__quad_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 63

__u_quad_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 64

__intmax_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 72

__uintmax_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 73

__dev_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 145

__uid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 146

__gid_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 147

__ino_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 148

__ino64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 149

__mode_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 150

__nlink_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 151

__off_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 152

__off64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 153

__pid_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 154

# /usr/include/x86_64-linux-gnu/bits/types.h: 155
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__val',
]
struct_anon_1._fields_ = [
    ('__val', c_int * int(2)),
]

__fsid_t = struct_anon_1# /usr/include/x86_64-linux-gnu/bits/types.h: 155

__clock_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 156

__rlim_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 157

__rlim64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 158

__id_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 159

__time_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 160

__useconds_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 161

__suseconds_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 162

__suseconds64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 163

__daddr_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 165

__key_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 166

__clockid_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 169

__timer_t = POINTER(None)# /usr/include/x86_64-linux-gnu/bits/types.h: 172

__blksize_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 175

__blkcnt_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 180

__blkcnt64_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 181

__fsblkcnt_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 184

__fsblkcnt64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 185

__fsfilcnt_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 188

__fsfilcnt64_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 189

__fsword_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 192

__ssize_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 194

__syscall_slong_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 197

__syscall_ulong_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 199

__loff_t = __off64_t# /usr/include/x86_64-linux-gnu/bits/types.h: 203

__caddr_t = String# /usr/include/x86_64-linux-gnu/bits/types.h: 204

__intptr_t = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 207

__socklen_t = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 210

__sig_atomic_t = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 215

int8_t = c_int8# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 24

int16_t = c_int16# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 25

int32_t = c_int32# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 26

int64_t = c_int64# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 27

uint8_t = __uint8_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 27

int_least8_t = __int_least8_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 25

int_least16_t = __int_least16_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 26

int_least32_t = __int_least32_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 27

int_least64_t = __int_least64_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 28

uint_least8_t = __uint_least8_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 31

uint_least16_t = __uint_least16_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 32

uint_least32_t = __uint_least32_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 33

uint_least64_t = __uint_least64_t# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 34

int_fast8_t = c_char# /usr/include/stdint.h: 47

int_fast16_t = c_long# /usr/include/stdint.h: 49

int_fast32_t = c_long# /usr/include/stdint.h: 50

int_fast64_t = c_long# /usr/include/stdint.h: 51

uint_fast8_t = c_ubyte# /usr/include/stdint.h: 60

uint_fast16_t = c_ulong# /usr/include/stdint.h: 62

uint_fast32_t = c_ulong# /usr/include/stdint.h: 63

uint_fast64_t = c_ulong# /usr/include/stdint.h: 64

intptr_t = c_long# /usr/include/stdint.h: 76

uintptr_t = c_ulong# /usr/include/stdint.h: 79

intmax_t = __intmax_t# /usr/include/stdint.h: 90

uintmax_t = __uintmax_t# /usr/include/stdint.h: 91

size_t = c_ulong# /usr/lib/llvm-18/lib/clang/18/include/__stddef_size_t.h: 18

wchar_t = c_int# /usr/lib/llvm-18/lib/clang/18/include/__stddef_wchar_t.h: 24

_Float32 = c_float# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 214

_Float64 = c_double# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 251

_Float32x = c_double# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 268

_Float64x = c_longdouble# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 285

# /usr/include/stdlib.h: 63
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'quot',
    'rem',
]
struct_anon_2._fields_ = [
    ('quot', c_int),
    ('rem', c_int),
]

div_t = struct_anon_2# /usr/include/stdlib.h: 63

# /usr/include/stdlib.h: 71
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'quot',
    'rem',
]
struct_anon_3._fields_ = [
    ('quot', c_long),
    ('rem', c_long),
]

ldiv_t = struct_anon_3# /usr/include/stdlib.h: 71

# /usr/include/stdlib.h: 81
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'quot',
    'rem',
]
struct_anon_4._fields_ = [
    ('quot', c_longlong),
    ('rem', c_longlong),
]

lldiv_t = struct_anon_4# /usr/include/stdlib.h: 81

# /usr/include/stdlib.h: 98
if _libs["vterm"].has("__ctype_get_mb_cur_max", "cdecl"):
    __ctype_get_mb_cur_max = _libs["vterm"].get("__ctype_get_mb_cur_max", "cdecl")
    __ctype_get_mb_cur_max.argtypes = []
    __ctype_get_mb_cur_max.restype = c_size_t

# /usr/include/stdlib.h: 102
if _libs["vterm"].has("atof", "cdecl"):
    atof = _libs["vterm"].get("atof", "cdecl")
    atof.argtypes = [String]
    atof.restype = c_double

# /usr/include/stdlib.h: 105
if _libs["vterm"].has("atoi", "cdecl"):
    atoi = _libs["vterm"].get("atoi", "cdecl")
    atoi.argtypes = [String]
    atoi.restype = c_int

# /usr/include/stdlib.h: 108
if _libs["vterm"].has("atol", "cdecl"):
    atol = _libs["vterm"].get("atol", "cdecl")
    atol.argtypes = [String]
    atol.restype = c_long

# /usr/include/stdlib.h: 113
if _libs["vterm"].has("atoll", "cdecl"):
    atoll = _libs["vterm"].get("atoll", "cdecl")
    atoll.argtypes = [String]
    atoll.restype = c_longlong

# /usr/include/stdlib.h: 118
if _libs["vterm"].has("strtod", "cdecl"):
    strtod = _libs["vterm"].get("strtod", "cdecl")
    strtod.argtypes = [String, POINTER(POINTER(c_char))]
    strtod.restype = c_double

# /usr/include/stdlib.h: 124
if _libs["vterm"].has("strtof", "cdecl"):
    strtof = _libs["vterm"].get("strtof", "cdecl")
    strtof.argtypes = [String, POINTER(POINTER(c_char))]
    strtof.restype = c_float

# /usr/include/stdlib.h: 127
if _libs["vterm"].has("strtold", "cdecl"):
    strtold = _libs["vterm"].get("strtold", "cdecl")
    strtold.argtypes = [String, POINTER(POINTER(c_char))]
    strtold.restype = c_longdouble

# /usr/include/stdlib.h: 177
if _libs["vterm"].has("strtol", "cdecl"):
    strtol = _libs["vterm"].get("strtol", "cdecl")
    strtol.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtol.restype = c_long

# /usr/include/stdlib.h: 181
if _libs["vterm"].has("strtoul", "cdecl"):
    strtoul = _libs["vterm"].get("strtoul", "cdecl")
    strtoul.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoul.restype = c_ulong

# /usr/include/stdlib.h: 188
if _libs["vterm"].has("strtoq", "cdecl"):
    strtoq = _libs["vterm"].get("strtoq", "cdecl")
    strtoq.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoq.restype = c_longlong

# /usr/include/stdlib.h: 193
if _libs["vterm"].has("strtouq", "cdecl"):
    strtouq = _libs["vterm"].get("strtouq", "cdecl")
    strtouq.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtouq.restype = c_ulonglong

# /usr/include/stdlib.h: 201
if _libs["vterm"].has("strtoll", "cdecl"):
    strtoll = _libs["vterm"].get("strtoll", "cdecl")
    strtoll.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoll.restype = c_longlong

# /usr/include/stdlib.h: 206
if _libs["vterm"].has("strtoull", "cdecl"):
    strtoull = _libs["vterm"].get("strtoull", "cdecl")
    strtoull.argtypes = [String, POINTER(POINTER(c_char)), c_int]
    strtoull.restype = c_ulonglong

# /usr/include/stdlib.h: 505
if _libs["vterm"].has("l64a", "cdecl"):
    l64a = _libs["vterm"].get("l64a", "cdecl")
    l64a.argtypes = [c_long]
    if sizeof(c_int) == sizeof(c_void_p):
        l64a.restype = ReturnString
    else:
        l64a.restype = String
        l64a.errcheck = ReturnString

# /usr/include/stdlib.h: 508
if _libs["vterm"].has("a64l", "cdecl"):
    a64l = _libs["vterm"].get("a64l", "cdecl")
    a64l.argtypes = [String]
    a64l.restype = c_long

u_char = __u_char# /usr/include/x86_64-linux-gnu/sys/types.h: 33

u_short = __u_short# /usr/include/x86_64-linux-gnu/sys/types.h: 34

u_int = __u_int# /usr/include/x86_64-linux-gnu/sys/types.h: 35

u_long = __u_long# /usr/include/x86_64-linux-gnu/sys/types.h: 36

quad_t = __quad_t# /usr/include/x86_64-linux-gnu/sys/types.h: 37

u_quad_t = __u_quad_t# /usr/include/x86_64-linux-gnu/sys/types.h: 38

fsid_t = __fsid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 39

loff_t = __loff_t# /usr/include/x86_64-linux-gnu/sys/types.h: 42

ino_t = __ino_t# /usr/include/x86_64-linux-gnu/sys/types.h: 47

dev_t = __dev_t# /usr/include/x86_64-linux-gnu/sys/types.h: 59

gid_t = __gid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 64

mode_t = __mode_t# /usr/include/x86_64-linux-gnu/sys/types.h: 69

nlink_t = __nlink_t# /usr/include/x86_64-linux-gnu/sys/types.h: 74

uid_t = __uid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 79

off_t = __off_t# /usr/include/x86_64-linux-gnu/sys/types.h: 85

pid_t = __pid_t# /usr/include/x86_64-linux-gnu/sys/types.h: 97

id_t = __id_t# /usr/include/x86_64-linux-gnu/sys/types.h: 103

ssize_t = __ssize_t# /usr/include/x86_64-linux-gnu/sys/types.h: 108

daddr_t = __daddr_t# /usr/include/x86_64-linux-gnu/sys/types.h: 114

caddr_t = __caddr_t# /usr/include/x86_64-linux-gnu/sys/types.h: 115

key_t = __key_t# /usr/include/x86_64-linux-gnu/sys/types.h: 121

clock_t = __clock_t# /usr/include/x86_64-linux-gnu/bits/types/clock_t.h: 7

clockid_t = __clockid_t# /usr/include/x86_64-linux-gnu/bits/types/clockid_t.h: 7

time_t = __time_t# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 10

timer_t = __timer_t# /usr/include/x86_64-linux-gnu/bits/types/timer_t.h: 7

ulong = c_ulong# /usr/include/x86_64-linux-gnu/sys/types.h: 148

ushort = c_ushort# /usr/include/x86_64-linux-gnu/sys/types.h: 149

uint = c_uint# /usr/include/x86_64-linux-gnu/sys/types.h: 150

u_int8_t = __uint8_t# /usr/include/x86_64-linux-gnu/sys/types.h: 158

u_int16_t = __uint16_t# /usr/include/x86_64-linux-gnu/sys/types.h: 159

u_int32_t = __uint32_t# /usr/include/x86_64-linux-gnu/sys/types.h: 160

u_int64_t = __uint64_t# /usr/include/x86_64-linux-gnu/sys/types.h: 161

register_t = c_int# /usr/include/x86_64-linux-gnu/sys/types.h: 166

# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 8
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    '__val',
]
struct_anon_5._fields_ = [
    ('__val', c_ulong * int((1024 / (8 * sizeof(c_ulong))))),
]

__sigset_t = struct_anon_5# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 8

sigset_t = __sigset_t# /usr/include/x86_64-linux-gnu/bits/types/sigset_t.h: 7

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8
class struct_timeval(Structure):
    pass

struct_timeval.__slots__ = [
    'tv_sec',
    'tv_usec',
]
struct_timeval._fields_ = [
    ('tv_sec', __time_t),
    ('tv_usec', __suseconds_t),
]

# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 11
class struct_timespec(Structure):
    pass

struct_timespec.__slots__ = [
    'tv_sec',
    'tv_nsec',
]
struct_timespec._fields_ = [
    ('tv_sec', __time_t),
    ('tv_nsec', __syscall_slong_t),
]

suseconds_t = __suseconds_t# /usr/include/x86_64-linux-gnu/sys/select.h: 43

__fd_mask = c_long# /usr/include/x86_64-linux-gnu/sys/select.h: 49

# /usr/include/x86_64-linux-gnu/sys/select.h: 70
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    '__fds_bits',
]
struct_anon_6._fields_ = [
    ('__fds_bits', __fd_mask * int((1024 / (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)))),
]

fd_set = struct_anon_6# /usr/include/x86_64-linux-gnu/sys/select.h: 70

fd_mask = __fd_mask# /usr/include/x86_64-linux-gnu/sys/select.h: 77

# /usr/include/x86_64-linux-gnu/sys/select.h: 102
if _libs["vterm"].has("select", "cdecl"):
    select = _libs["vterm"].get("select", "cdecl")
    select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timeval)]
    select.restype = c_int

# /usr/include/x86_64-linux-gnu/sys/select.h: 127
if _libs["vterm"].has("pselect", "cdecl"):
    pselect = _libs["vterm"].get("pselect", "cdecl")
    pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(struct_timespec), POINTER(__sigset_t)]
    pselect.restype = c_int

blksize_t = __blksize_t# /usr/include/x86_64-linux-gnu/sys/types.h: 185

blkcnt_t = __blkcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 192

fsblkcnt_t = __fsblkcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 196

fsfilcnt_t = __fsfilcnt_t# /usr/include/x86_64-linux-gnu/sys/types.h: 200

# /usr/include/x86_64-linux-gnu/bits/atomic_wide_counter.h: 28
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    '__low',
    '__high',
]
struct_anon_7._fields_ = [
    ('__low', c_uint),
    ('__high', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/atomic_wide_counter.h: 33
class union_anon_8(Union):
    pass

union_anon_8.__slots__ = [
    '__value64',
    '__value32',
]
union_anon_8._fields_ = [
    ('__value64', c_ulonglong),
    ('__value32', struct_anon_7),
]

__atomic_wide_counter = union_anon_8# /usr/include/x86_64-linux-gnu/bits/atomic_wide_counter.h: 33

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 51
class struct___pthread_internal_list(Structure):
    pass

struct___pthread_internal_list.__slots__ = [
    '__prev',
    '__next',
]
struct___pthread_internal_list._fields_ = [
    ('__prev', POINTER(struct___pthread_internal_list)),
    ('__next', POINTER(struct___pthread_internal_list)),
]

__pthread_list_t = struct___pthread_internal_list# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 55

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 57
class struct___pthread_internal_slist(Structure):
    pass

struct___pthread_internal_slist.__slots__ = [
    '__next',
]
struct___pthread_internal_slist._fields_ = [
    ('__next', POINTER(struct___pthread_internal_slist)),
]

__pthread_slist_t = struct___pthread_internal_slist# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 60

# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 22
class struct___pthread_mutex_s(Structure):
    pass

struct___pthread_mutex_s.__slots__ = [
    '__lock',
    '__count',
    '__owner',
    '__nusers',
    '__kind',
    '__spins',
    '__elision',
    '__list',
]
struct___pthread_mutex_s._fields_ = [
    ('__lock', c_int),
    ('__count', c_uint),
    ('__owner', c_int),
    ('__nusers', c_uint),
    ('__kind', c_int),
    ('__spins', c_short),
    ('__elision', c_short),
    ('__list', __pthread_list_t),
]

# /usr/include/x86_64-linux-gnu/bits/struct_rwlock.h: 23
class struct___pthread_rwlock_arch_t(Structure):
    pass

struct___pthread_rwlock_arch_t.__slots__ = [
    '__readers',
    '__writers',
    '__wrphase_futex',
    '__writers_futex',
    '__pad3',
    '__pad4',
    '__cur_writer',
    '__shared',
    '__rwelision',
    '__pad1',
    '__pad2',
    '__flags',
]
struct___pthread_rwlock_arch_t._fields_ = [
    ('__readers', c_uint),
    ('__writers', c_uint),
    ('__wrphase_futex', c_uint),
    ('__writers_futex', c_uint),
    ('__pad3', c_uint),
    ('__pad4', c_uint),
    ('__cur_writer', c_int),
    ('__shared', c_int),
    ('__rwelision', c_char),
    ('__pad1', c_ubyte * int(7)),
    ('__pad2', c_ulong),
    ('__flags', c_uint),
]

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 94
class struct___pthread_cond_s(Structure):
    pass

struct___pthread_cond_s.__slots__ = [
    '__wseq',
    '__g1_start',
    '__g_refs',
    '__g_size',
    '__g1_orig_size',
    '__wrefs',
    '__g_signals',
]
struct___pthread_cond_s._fields_ = [
    ('__wseq', __atomic_wide_counter),
    ('__g1_start', __atomic_wide_counter),
    ('__g_refs', c_uint * int(2)),
    ('__g_size', c_uint * int(2)),
    ('__g1_orig_size', c_uint),
    ('__wrefs', c_uint),
    ('__g_signals', c_uint * int(2)),
]

__tss_t = c_uint# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 105

__thrd_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 106

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 111
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    '__data',
]
struct_anon_9._fields_ = [
    ('__data', c_int),
]

__once_flag = struct_anon_9# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 111

pthread_t = c_ulong# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 27

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 36
class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    '__size',
    '__align',
]
union_anon_10._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_mutexattr_t = union_anon_10# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 36

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 45
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    '__size',
    '__align',
]
union_anon_11._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_condattr_t = union_anon_11# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 45

pthread_key_t = c_uint# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 49

pthread_once_t = c_int# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 53

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 56
class union_pthread_attr_t(Union):
    pass

union_pthread_attr_t.__slots__ = [
    '__size',
    '__align',
]
union_pthread_attr_t._fields_ = [
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_attr_t = union_pthread_attr_t# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 62

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 72
class union_anon_12(Union):
    pass

union_anon_12.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_12._fields_ = [
    ('__data', struct___pthread_mutex_s),
    ('__size', c_char * int(40)),
    ('__align', c_long),
]

pthread_mutex_t = union_anon_12# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 72

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 80
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_13._fields_ = [
    ('__data', struct___pthread_cond_s),
    ('__size', c_char * int(48)),
    ('__align', c_longlong),
]

pthread_cond_t = union_anon_13# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 80

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 91
class union_anon_14(Union):
    pass

union_anon_14.__slots__ = [
    '__data',
    '__size',
    '__align',
]
union_anon_14._fields_ = [
    ('__data', struct___pthread_rwlock_arch_t),
    ('__size', c_char * int(56)),
    ('__align', c_long),
]

pthread_rwlock_t = union_anon_14# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 91

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 97
class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    '__size',
    '__align',
]
union_anon_15._fields_ = [
    ('__size', c_char * int(8)),
    ('__align', c_long),
]

pthread_rwlockattr_t = union_anon_15# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 97

pthread_spinlock_t = c_int# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 103

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 112
class union_anon_16(Union):
    pass

union_anon_16.__slots__ = [
    '__size',
    '__align',
]
union_anon_16._fields_ = [
    ('__size', c_char * int(32)),
    ('__align', c_long),
]

pthread_barrier_t = union_anon_16# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 112

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 118
class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    '__size',
    '__align',
]
union_anon_17._fields_ = [
    ('__size', c_char * int(4)),
    ('__align', c_int),
]

pthread_barrierattr_t = union_anon_17# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 118

# /usr/include/stdlib.h: 521
if _libs["vterm"].has("random", "cdecl"):
    random = _libs["vterm"].get("random", "cdecl")
    random.argtypes = []
    random.restype = c_long

# /usr/include/stdlib.h: 524
if _libs["vterm"].has("srandom", "cdecl"):
    srandom = _libs["vterm"].get("srandom", "cdecl")
    srandom.argtypes = [c_uint]
    srandom.restype = None

# /usr/include/stdlib.h: 530
if _libs["vterm"].has("initstate", "cdecl"):
    initstate = _libs["vterm"].get("initstate", "cdecl")
    initstate.argtypes = [c_uint, String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        initstate.restype = ReturnString
    else:
        initstate.restype = String
        initstate.errcheck = ReturnString

# /usr/include/stdlib.h: 535
if _libs["vterm"].has("setstate", "cdecl"):
    setstate = _libs["vterm"].get("setstate", "cdecl")
    setstate.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        setstate.restype = ReturnString
    else:
        setstate.restype = String
        setstate.errcheck = ReturnString

# /usr/include/stdlib.h: 543
class struct_random_data(Structure):
    pass

struct_random_data.__slots__ = [
    'fptr',
    'rptr',
    'state',
    'rand_type',
    'rand_deg',
    'rand_sep',
    'end_ptr',
]
struct_random_data._fields_ = [
    ('fptr', POINTER(c_int32)),
    ('rptr', POINTER(c_int32)),
    ('state', POINTER(c_int32)),
    ('rand_type', c_int),
    ('rand_deg', c_int),
    ('rand_sep', c_int),
    ('end_ptr', POINTER(c_int32)),
]

# /usr/include/stdlib.h: 554
if _libs["vterm"].has("random_r", "cdecl"):
    random_r = _libs["vterm"].get("random_r", "cdecl")
    random_r.argtypes = [POINTER(struct_random_data), POINTER(c_int32)]
    random_r.restype = c_int

# /usr/include/stdlib.h: 557
if _libs["vterm"].has("srandom_r", "cdecl"):
    srandom_r = _libs["vterm"].get("srandom_r", "cdecl")
    srandom_r.argtypes = [c_uint, POINTER(struct_random_data)]
    srandom_r.restype = c_int

# /usr/include/stdlib.h: 560
if _libs["vterm"].has("initstate_r", "cdecl"):
    initstate_r = _libs["vterm"].get("initstate_r", "cdecl")
    initstate_r.argtypes = [c_uint, String, c_size_t, POINTER(struct_random_data)]
    initstate_r.restype = c_int

# /usr/include/stdlib.h: 565
if _libs["vterm"].has("setstate_r", "cdecl"):
    setstate_r = _libs["vterm"].get("setstate_r", "cdecl")
    setstate_r.argtypes = [String, POINTER(struct_random_data)]
    setstate_r.restype = c_int

# /usr/include/stdlib.h: 573
if _libs["vterm"].has("rand", "cdecl"):
    rand = _libs["vterm"].get("rand", "cdecl")
    rand.argtypes = []
    rand.restype = c_int

# /usr/include/stdlib.h: 575
if _libs["vterm"].has("srand", "cdecl"):
    srand = _libs["vterm"].get("srand", "cdecl")
    srand.argtypes = [c_uint]
    srand.restype = None

# /usr/include/stdlib.h: 579
if _libs["vterm"].has("rand_r", "cdecl"):
    rand_r = _libs["vterm"].get("rand_r", "cdecl")
    rand_r.argtypes = [POINTER(c_uint)]
    rand_r.restype = c_int

# /usr/include/stdlib.h: 587
if _libs["vterm"].has("drand48", "cdecl"):
    drand48 = _libs["vterm"].get("drand48", "cdecl")
    drand48.argtypes = []
    drand48.restype = c_double

# /usr/include/stdlib.h: 588
if _libs["vterm"].has("erand48", "cdecl"):
    erand48 = _libs["vterm"].get("erand48", "cdecl")
    erand48.argtypes = [c_ushort * int(3)]
    erand48.restype = c_double

# /usr/include/stdlib.h: 591
if _libs["vterm"].has("lrand48", "cdecl"):
    lrand48 = _libs["vterm"].get("lrand48", "cdecl")
    lrand48.argtypes = []
    lrand48.restype = c_long

# /usr/include/stdlib.h: 592
if _libs["vterm"].has("nrand48", "cdecl"):
    nrand48 = _libs["vterm"].get("nrand48", "cdecl")
    nrand48.argtypes = [c_ushort * int(3)]
    nrand48.restype = c_long

# /usr/include/stdlib.h: 596
if _libs["vterm"].has("mrand48", "cdecl"):
    mrand48 = _libs["vterm"].get("mrand48", "cdecl")
    mrand48.argtypes = []
    mrand48.restype = c_long

# /usr/include/stdlib.h: 597
if _libs["vterm"].has("jrand48", "cdecl"):
    jrand48 = _libs["vterm"].get("jrand48", "cdecl")
    jrand48.argtypes = [c_ushort * int(3)]
    jrand48.restype = c_long

# /usr/include/stdlib.h: 601
if _libs["vterm"].has("srand48", "cdecl"):
    srand48 = _libs["vterm"].get("srand48", "cdecl")
    srand48.argtypes = [c_long]
    srand48.restype = None

# /usr/include/stdlib.h: 602
if _libs["vterm"].has("seed48", "cdecl"):
    seed48 = _libs["vterm"].get("seed48", "cdecl")
    seed48.argtypes = [c_ushort * int(3)]
    seed48.restype = POINTER(c_ushort)

# /usr/include/stdlib.h: 604
if _libs["vterm"].has("lcong48", "cdecl"):
    lcong48 = _libs["vterm"].get("lcong48", "cdecl")
    lcong48.argtypes = [c_ushort * int(7)]
    lcong48.restype = None

# /usr/include/stdlib.h: 610
class struct_drand48_data(Structure):
    pass

struct_drand48_data.__slots__ = [
    '__x',
    '__old_x',
    '__c',
    '__init',
    '__a',
]
struct_drand48_data._fields_ = [
    ('__x', c_ushort * int(3)),
    ('__old_x', c_ushort * int(3)),
    ('__c', c_ushort),
    ('__init', c_ushort),
    ('__a', c_ulonglong),
]

# /usr/include/stdlib.h: 621
if _libs["vterm"].has("drand48_r", "cdecl"):
    drand48_r = _libs["vterm"].get("drand48_r", "cdecl")
    drand48_r.argtypes = [POINTER(struct_drand48_data), POINTER(c_double)]
    drand48_r.restype = c_int

# /usr/include/stdlib.h: 623
if _libs["vterm"].has("erand48_r", "cdecl"):
    erand48_r = _libs["vterm"].get("erand48_r", "cdecl")
    erand48_r.argtypes = [c_ushort * int(3), POINTER(struct_drand48_data), POINTER(c_double)]
    erand48_r.restype = c_int

# /usr/include/stdlib.h: 628
if _libs["vterm"].has("lrand48_r", "cdecl"):
    lrand48_r = _libs["vterm"].get("lrand48_r", "cdecl")
    lrand48_r.argtypes = [POINTER(struct_drand48_data), POINTER(c_long)]
    lrand48_r.restype = c_int

# /usr/include/stdlib.h: 631
if _libs["vterm"].has("nrand48_r", "cdecl"):
    nrand48_r = _libs["vterm"].get("nrand48_r", "cdecl")
    nrand48_r.argtypes = [c_ushort * int(3), POINTER(struct_drand48_data), POINTER(c_long)]
    nrand48_r.restype = c_int

# /usr/include/stdlib.h: 637
if _libs["vterm"].has("mrand48_r", "cdecl"):
    mrand48_r = _libs["vterm"].get("mrand48_r", "cdecl")
    mrand48_r.argtypes = [POINTER(struct_drand48_data), POINTER(c_long)]
    mrand48_r.restype = c_int

# /usr/include/stdlib.h: 640
if _libs["vterm"].has("jrand48_r", "cdecl"):
    jrand48_r = _libs["vterm"].get("jrand48_r", "cdecl")
    jrand48_r.argtypes = [c_ushort * int(3), POINTER(struct_drand48_data), POINTER(c_long)]
    jrand48_r.restype = c_int

# /usr/include/stdlib.h: 646
if _libs["vterm"].has("srand48_r", "cdecl"):
    srand48_r = _libs["vterm"].get("srand48_r", "cdecl")
    srand48_r.argtypes = [c_long, POINTER(struct_drand48_data)]
    srand48_r.restype = c_int

# /usr/include/stdlib.h: 649
if _libs["vterm"].has("seed48_r", "cdecl"):
    seed48_r = _libs["vterm"].get("seed48_r", "cdecl")
    seed48_r.argtypes = [c_ushort * int(3), POINTER(struct_drand48_data)]
    seed48_r.restype = c_int

# /usr/include/stdlib.h: 652
if _libs["vterm"].has("lcong48_r", "cdecl"):
    lcong48_r = _libs["vterm"].get("lcong48_r", "cdecl")
    lcong48_r.argtypes = [c_ushort * int(7), POINTER(struct_drand48_data)]
    lcong48_r.restype = c_int

# /usr/include/stdlib.h: 657
if _libs["vterm"].has("arc4random", "cdecl"):
    arc4random = _libs["vterm"].get("arc4random", "cdecl")
    arc4random.argtypes = []
    arc4random.restype = __uint32_t

# /usr/include/stdlib.h: 661
if _libs["vterm"].has("arc4random_buf", "cdecl"):
    arc4random_buf = _libs["vterm"].get("arc4random_buf", "cdecl")
    arc4random_buf.argtypes = [POINTER(None), c_size_t]
    arc4random_buf.restype = None

# /usr/include/stdlib.h: 666
if _libs["vterm"].has("arc4random_uniform", "cdecl"):
    arc4random_uniform = _libs["vterm"].get("arc4random_uniform", "cdecl")
    arc4random_uniform.argtypes = [__uint32_t]
    arc4random_uniform.restype = __uint32_t

# /usr/include/stdlib.h: 672
if _libs["vterm"].has("malloc", "cdecl"):
    malloc = _libs["vterm"].get("malloc", "cdecl")
    malloc.argtypes = [c_size_t]
    malloc.restype = POINTER(c_ubyte)
    malloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 675
if _libs["vterm"].has("calloc", "cdecl"):
    calloc = _libs["vterm"].get("calloc", "cdecl")
    calloc.argtypes = [c_size_t, c_size_t]
    calloc.restype = POINTER(c_ubyte)
    calloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 683
if _libs["vterm"].has("realloc", "cdecl"):
    realloc = _libs["vterm"].get("realloc", "cdecl")
    realloc.argtypes = [POINTER(None), c_size_t]
    realloc.restype = POINTER(c_ubyte)
    realloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 687
if _libs["vterm"].has("free", "cdecl"):
    free = _libs["vterm"].get("free", "cdecl")
    free.argtypes = [POINTER(None)]
    free.restype = None

# /usr/include/stdlib.h: 695
if _libs["vterm"].has("reallocarray", "cdecl"):
    reallocarray = _libs["vterm"].get("reallocarray", "cdecl")
    reallocarray.argtypes = [POINTER(None), c_size_t, c_size_t]
    reallocarray.restype = POINTER(c_ubyte)
    reallocarray.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 701
if _libs["vterm"].has("reallocarray", "cdecl"):
    reallocarray = _libs["vterm"].get("reallocarray", "cdecl")
    reallocarray.argtypes = [POINTER(None), c_size_t, c_size_t]
    reallocarray.restype = POINTER(c_ubyte)
    reallocarray.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 712
if _libs["vterm"].has("valloc", "cdecl"):
    valloc = _libs["vterm"].get("valloc", "cdecl")
    valloc.argtypes = [c_size_t]
    valloc.restype = POINTER(c_ubyte)
    valloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 718
if _libs["vterm"].has("posix_memalign", "cdecl"):
    posix_memalign = _libs["vterm"].get("posix_memalign", "cdecl")
    posix_memalign.argtypes = [POINTER(POINTER(None)), c_size_t, c_size_t]
    posix_memalign.restype = c_int

# /usr/include/stdlib.h: 724
if _libs["vterm"].has("aligned_alloc", "cdecl"):
    aligned_alloc = _libs["vterm"].get("aligned_alloc", "cdecl")
    aligned_alloc.argtypes = [c_size_t, c_size_t]
    aligned_alloc.restype = POINTER(c_ubyte)
    aligned_alloc.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 730
if _libs["vterm"].has("abort", "cdecl"):
    abort = _libs["vterm"].get("abort", "cdecl")
    abort.argtypes = []
    abort.restype = None

# /usr/include/stdlib.h: 734
for _lib in _libs.values():
    if not _lib.has("atexit", "cdecl"):
        continue
    atexit = _lib.get("atexit", "cdecl")
    atexit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    atexit.restype = c_int
    break

# /usr/include/stdlib.h: 742
for _lib in _libs.values():
    if not _lib.has("at_quick_exit", "cdecl"):
        continue
    at_quick_exit = _lib.get("at_quick_exit", "cdecl")
    at_quick_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), )]
    at_quick_exit.restype = c_int
    break

# /usr/include/stdlib.h: 749
if _libs["vterm"].has("on_exit", "cdecl"):
    on_exit = _libs["vterm"].get("on_exit", "cdecl")
    on_exit.argtypes = [CFUNCTYPE(UNCHECKED(None), c_int, POINTER(None)), POINTER(None)]
    on_exit.restype = c_int

# /usr/include/stdlib.h: 756
if _libs["vterm"].has("exit", "cdecl"):
    exit = _libs["vterm"].get("exit", "cdecl")
    exit.argtypes = [c_int]
    exit.restype = None

# /usr/include/stdlib.h: 762
if _libs["vterm"].has("quick_exit", "cdecl"):
    quick_exit = _libs["vterm"].get("quick_exit", "cdecl")
    quick_exit.argtypes = [c_int]
    quick_exit.restype = None

# /usr/include/stdlib.h: 768
if _libs["vterm"].has("_Exit", "cdecl"):
    _Exit = _libs["vterm"].get("_Exit", "cdecl")
    _Exit.argtypes = [c_int]
    _Exit.restype = None

# /usr/include/stdlib.h: 773
if _libs["vterm"].has("getenv", "cdecl"):
    getenv = _libs["vterm"].get("getenv", "cdecl")
    getenv.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        getenv.restype = ReturnString
    else:
        getenv.restype = String
        getenv.errcheck = ReturnString

# /usr/include/stdlib.h: 786
if _libs["vterm"].has("putenv", "cdecl"):
    putenv = _libs["vterm"].get("putenv", "cdecl")
    putenv.argtypes = [String]
    putenv.restype = c_int

# /usr/include/stdlib.h: 792
if _libs["vterm"].has("setenv", "cdecl"):
    setenv = _libs["vterm"].get("setenv", "cdecl")
    setenv.argtypes = [String, String, c_int]
    setenv.restype = c_int

# /usr/include/stdlib.h: 796
if _libs["vterm"].has("unsetenv", "cdecl"):
    unsetenv = _libs["vterm"].get("unsetenv", "cdecl")
    unsetenv.argtypes = [String]
    unsetenv.restype = c_int

# /usr/include/stdlib.h: 803
if _libs["vterm"].has("clearenv", "cdecl"):
    clearenv = _libs["vterm"].get("clearenv", "cdecl")
    clearenv.argtypes = []
    clearenv.restype = c_int

# /usr/include/stdlib.h: 814
if _libs["vterm"].has("mktemp", "cdecl"):
    mktemp = _libs["vterm"].get("mktemp", "cdecl")
    mktemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mktemp.restype = ReturnString
    else:
        mktemp.restype = String
        mktemp.errcheck = ReturnString

# /usr/include/stdlib.h: 827
if _libs["vterm"].has("mkstemp", "cdecl"):
    mkstemp = _libs["vterm"].get("mkstemp", "cdecl")
    mkstemp.argtypes = [String]
    mkstemp.restype = c_int

# /usr/include/stdlib.h: 849
if _libs["vterm"].has("mkstemps", "cdecl"):
    mkstemps = _libs["vterm"].get("mkstemps", "cdecl")
    mkstemps.argtypes = [String, c_int]
    mkstemps.restype = c_int

# /usr/include/stdlib.h: 870
if _libs["vterm"].has("mkdtemp", "cdecl"):
    mkdtemp = _libs["vterm"].get("mkdtemp", "cdecl")
    mkdtemp.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        mkdtemp.restype = ReturnString
    else:
        mkdtemp.restype = String
        mkdtemp.errcheck = ReturnString

# /usr/include/stdlib.h: 923
if _libs["vterm"].has("system", "cdecl"):
    system = _libs["vterm"].get("system", "cdecl")
    system.argtypes = [String]
    system.restype = c_int

# /usr/include/stdlib.h: 940
if _libs["vterm"].has("realpath", "cdecl"):
    realpath = _libs["vterm"].get("realpath", "cdecl")
    realpath.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        realpath.restype = ReturnString
    else:
        realpath.restype = String
        realpath.errcheck = ReturnString

__compar_fn_t = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))# /usr/include/stdlib.h: 948

# /usr/include/stdlib.h: 960
if _libs["vterm"].has("bsearch", "cdecl"):
    bsearch = _libs["vterm"].get("bsearch", "cdecl")
    bsearch.argtypes = [POINTER(None), POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    bsearch.restype = POINTER(c_ubyte)
    bsearch.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/stdlib.h: 970
if _libs["vterm"].has("qsort", "cdecl"):
    qsort = _libs["vterm"].get("qsort", "cdecl")
    qsort.argtypes = [POINTER(None), c_size_t, c_size_t, __compar_fn_t]
    qsort.restype = None

# /usr/include/stdlib.h: 980
if _libs["vterm"].has("abs", "cdecl"):
    abs = _libs["vterm"].get("abs", "cdecl")
    abs.argtypes = [c_int]
    abs.restype = c_int

# /usr/include/stdlib.h: 981
if _libs["vterm"].has("labs", "cdecl"):
    labs = _libs["vterm"].get("labs", "cdecl")
    labs.argtypes = [c_long]
    labs.restype = c_long

# /usr/include/stdlib.h: 984
if _libs["vterm"].has("llabs", "cdecl"):
    llabs = _libs["vterm"].get("llabs", "cdecl")
    llabs.argtypes = [c_longlong]
    llabs.restype = c_longlong

# /usr/include/stdlib.h: 992
if _libs["vterm"].has("div", "cdecl"):
    div = _libs["vterm"].get("div", "cdecl")
    div.argtypes = [c_int, c_int]
    div.restype = div_t

# /usr/include/stdlib.h: 994
if _libs["vterm"].has("ldiv", "cdecl"):
    ldiv = _libs["vterm"].get("ldiv", "cdecl")
    ldiv.argtypes = [c_long, c_long]
    ldiv.restype = ldiv_t

# /usr/include/stdlib.h: 998
if _libs["vterm"].has("lldiv", "cdecl"):
    lldiv = _libs["vterm"].get("lldiv", "cdecl")
    lldiv.argtypes = [c_longlong, c_longlong]
    lldiv.restype = lldiv_t

# /usr/include/stdlib.h: 1012
if _libs["vterm"].has("ecvt", "cdecl"):
    ecvt = _libs["vterm"].get("ecvt", "cdecl")
    ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        ecvt.restype = ReturnString
    else:
        ecvt.restype = String
        ecvt.errcheck = ReturnString

# /usr/include/stdlib.h: 1018
if _libs["vterm"].has("fcvt", "cdecl"):
    fcvt = _libs["vterm"].get("fcvt", "cdecl")
    fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        fcvt.restype = ReturnString
    else:
        fcvt.restype = String
        fcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 1024
if _libs["vterm"].has("gcvt", "cdecl"):
    gcvt = _libs["vterm"].get("gcvt", "cdecl")
    gcvt.argtypes = [c_double, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        gcvt.restype = ReturnString
    else:
        gcvt.restype = String
        gcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 1030
if _libs["vterm"].has("qecvt", "cdecl"):
    qecvt = _libs["vterm"].get("qecvt", "cdecl")
    qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        qecvt.restype = ReturnString
    else:
        qecvt.restype = String
        qecvt.errcheck = ReturnString

# /usr/include/stdlib.h: 1033
if _libs["vterm"].has("qfcvt", "cdecl"):
    qfcvt = _libs["vterm"].get("qfcvt", "cdecl")
    qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
    if sizeof(c_int) == sizeof(c_void_p):
        qfcvt.restype = ReturnString
    else:
        qfcvt.restype = String
        qfcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 1036
if _libs["vterm"].has("qgcvt", "cdecl"):
    qgcvt = _libs["vterm"].get("qgcvt", "cdecl")
    qgcvt.argtypes = [c_longdouble, c_int, String]
    if sizeof(c_int) == sizeof(c_void_p):
        qgcvt.restype = ReturnString
    else:
        qgcvt.restype = String
        qgcvt.errcheck = ReturnString

# /usr/include/stdlib.h: 1042
if _libs["vterm"].has("ecvt_r", "cdecl"):
    ecvt_r = _libs["vterm"].get("ecvt_r", "cdecl")
    ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    ecvt_r.restype = c_int

# /usr/include/stdlib.h: 1045
if _libs["vterm"].has("fcvt_r", "cdecl"):
    fcvt_r = _libs["vterm"].get("fcvt_r", "cdecl")
    fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    fcvt_r.restype = c_int

# /usr/include/stdlib.h: 1049
if _libs["vterm"].has("qecvt_r", "cdecl"):
    qecvt_r = _libs["vterm"].get("qecvt_r", "cdecl")
    qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    qecvt_r.restype = c_int

# /usr/include/stdlib.h: 1053
if _libs["vterm"].has("qfcvt_r", "cdecl"):
    qfcvt_r = _libs["vterm"].get("qfcvt_r", "cdecl")
    qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), String, c_size_t]
    qfcvt_r.restype = c_int

# /usr/include/stdlib.h: 1062
if _libs["vterm"].has("mblen", "cdecl"):
    mblen = _libs["vterm"].get("mblen", "cdecl")
    mblen.argtypes = [String, c_size_t]
    mblen.restype = c_int

# /usr/include/stdlib.h: 1065
if _libs["vterm"].has("mbtowc", "cdecl"):
    mbtowc = _libs["vterm"].get("mbtowc", "cdecl")
    mbtowc.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbtowc.restype = c_int

# /usr/include/stdlib.h: 1069
if _libs["vterm"].has("wctomb", "cdecl"):
    wctomb = _libs["vterm"].get("wctomb", "cdecl")
    wctomb.argtypes = [String, c_wchar]
    wctomb.restype = c_int

# /usr/include/stdlib.h: 1073
if _libs["vterm"].has("mbstowcs", "cdecl"):
    mbstowcs = _libs["vterm"].get("mbstowcs", "cdecl")
    mbstowcs.argtypes = [POINTER(c_wchar), String, c_size_t]
    mbstowcs.restype = c_size_t

# /usr/include/stdlib.h: 1077
if _libs["vterm"].has("wcstombs", "cdecl"):
    wcstombs = _libs["vterm"].get("wcstombs", "cdecl")
    wcstombs.argtypes = [String, POINTER(c_wchar), c_size_t]
    wcstombs.restype = c_size_t

# /usr/include/stdlib.h: 1088
if _libs["vterm"].has("rpmatch", "cdecl"):
    rpmatch = _libs["vterm"].get("rpmatch", "cdecl")
    rpmatch.argtypes = [String]
    rpmatch.restype = c_int

# /usr/include/stdlib.h: 1099
if _libs["vterm"].has("getsubopt", "cdecl"):
    getsubopt = _libs["vterm"].get("getsubopt", "cdecl")
    getsubopt.argtypes = [POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), POINTER(POINTER(c_char))]
    getsubopt.restype = c_int

# /usr/include/stdlib.h: 1145
if _libs["vterm"].has("getloadavg", "cdecl"):
    getloadavg = _libs["vterm"].get("getloadavg", "cdecl")
    getloadavg.argtypes = [POINTER(c_double), c_int]
    getloadavg.restype = c_int

enum_anon_18 = c_int# /usr/include/vterm_keycodes.h: 11

VTERM_MOD_NONE = 0x00# /usr/include/vterm_keycodes.h: 11

VTERM_MOD_SHIFT = 0x01# /usr/include/vterm_keycodes.h: 11

VTERM_MOD_ALT = 0x02# /usr/include/vterm_keycodes.h: 11

VTERM_MOD_CTRL = 0x04# /usr/include/vterm_keycodes.h: 11

VTERM_ALL_MODS_MASK = 0x07# /usr/include/vterm_keycodes.h: 11

VTermModifier = enum_anon_18# /usr/include/vterm_keycodes.h: 11

enum_anon_19 = c_int# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_NONE = 0# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_ENTER = (VTERM_KEY_NONE + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_TAB = (VTERM_KEY_ENTER + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_BACKSPACE = (VTERM_KEY_TAB + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_ESCAPE = (VTERM_KEY_BACKSPACE + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_UP = (VTERM_KEY_ESCAPE + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_DOWN = (VTERM_KEY_UP + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_LEFT = (VTERM_KEY_DOWN + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_RIGHT = (VTERM_KEY_LEFT + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_INS = (VTERM_KEY_RIGHT + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_DEL = (VTERM_KEY_INS + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_HOME = (VTERM_KEY_DEL + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_END = (VTERM_KEY_HOME + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_PAGEUP = (VTERM_KEY_END + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_PAGEDOWN = (VTERM_KEY_PAGEUP + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_FUNCTION_0 = 256# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_FUNCTION_MAX = (VTERM_KEY_FUNCTION_0 + 255)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_0 = (VTERM_KEY_FUNCTION_MAX + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_1 = (VTERM_KEY_KP_0 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_2 = (VTERM_KEY_KP_1 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_3 = (VTERM_KEY_KP_2 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_4 = (VTERM_KEY_KP_3 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_5 = (VTERM_KEY_KP_4 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_6 = (VTERM_KEY_KP_5 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_7 = (VTERM_KEY_KP_6 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_8 = (VTERM_KEY_KP_7 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_9 = (VTERM_KEY_KP_8 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_MULT = (VTERM_KEY_KP_9 + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_PLUS = (VTERM_KEY_KP_MULT + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_COMMA = (VTERM_KEY_KP_PLUS + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_MINUS = (VTERM_KEY_KP_COMMA + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_PERIOD = (VTERM_KEY_KP_MINUS + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_DIVIDE = (VTERM_KEY_KP_PERIOD + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_ENTER = (VTERM_KEY_KP_DIVIDE + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_KP_EQUAL = (VTERM_KEY_KP_ENTER + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_KEY_MAX = (VTERM_KEY_KP_EQUAL + 1)# /usr/include/vterm_keycodes.h: 57

VTERM_N_KEYS = VTERM_KEY_MAX# /usr/include/vterm_keycodes.h: 57

VTermKey = enum_anon_19# /usr/include/vterm_keycodes.h: 57

# /usr/include/vterm.h: 26
class struct_VTerm(Structure):
    pass

VTerm = struct_VTerm# /usr/include/vterm.h: 26

# /usr/include/vterm.h: 27
class struct_VTermState(Structure):
    pass

VTermState = struct_VTermState# /usr/include/vterm.h: 27

# /usr/include/vterm.h: 28
class struct_VTermScreen(Structure):
    pass

VTermScreen = struct_VTermScreen# /usr/include/vterm.h: 28

# /usr/include/vterm.h: 33
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'row',
    'col',
]
struct_anon_20._fields_ = [
    ('row', c_int),
    ('col', c_int),
]

VTermPos = struct_anon_20# /usr/include/vterm.h: 33

# /usr/include/vterm.h: 48
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'start_row',
    'end_row',
    'start_col',
    'end_col',
]
struct_anon_21._fields_ = [
    ('start_row', c_int),
    ('end_row', c_int),
    ('start_col', c_int),
    ('end_col', c_int),
]

VTermRect = struct_anon_21# /usr/include/vterm.h: 48

enum_anon_22 = c_int# /usr/include/vterm.h: 103

VTERM_COLOR_RGB = 0x00# /usr/include/vterm.h: 103

VTERM_COLOR_INDEXED = 0x01# /usr/include/vterm.h: 103

VTERM_COLOR_TYPE_MASK = 0x01# /usr/include/vterm.h: 103

VTERM_COLOR_DEFAULT_FG = 0x02# /usr/include/vterm.h: 103

VTERM_COLOR_DEFAULT_BG = 0x04# /usr/include/vterm.h: 103

VTERM_COLOR_DEFAULT_MASK = 0x06# /usr/include/vterm.h: 103

VTermColorType = enum_anon_22# /usr/include/vterm.h: 103

# /usr/include/vterm.h: 154
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'type',
    'red',
    'green',
    'blue',
]
struct_anon_23._fields_ = [
    ('type', uint8_t),
    ('red', uint8_t),
    ('green', uint8_t),
    ('blue', uint8_t),
]

# /usr/include/vterm.h: 170
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'type',
    'idx',
]
struct_anon_24._fields_ = [
    ('type', uint8_t),
    ('idx', uint8_t),
]

# /usr/include/vterm.h: 181
class union_anon_25(Union):
    pass

union_anon_25.__slots__ = [
    'type',
    'rgb',
    'indexed',
]
union_anon_25._fields_ = [
    ('type', uint8_t),
    ('rgb', struct_anon_23),
    ('indexed', struct_anon_24),
]

VTermColor = union_anon_25# /usr/include/vterm.h: 181

# /usr/include/vterm.h: 208
if _libs["vterm"].has("vterm_color_is_equal", "cdecl"):
    vterm_color_is_equal = _libs["vterm"].get("vterm_color_is_equal", "cdecl")
    vterm_color_is_equal.argtypes = [POINTER(VTermColor), POINTER(VTermColor)]
    vterm_color_is_equal.restype = c_int

enum_anon_26 = c_int# /usr/include/vterm.h: 218

VTERM_VALUETYPE_BOOL = 1# /usr/include/vterm.h: 218

VTERM_VALUETYPE_INT = (VTERM_VALUETYPE_BOOL + 1)# /usr/include/vterm.h: 218

VTERM_VALUETYPE_STRING = (VTERM_VALUETYPE_INT + 1)# /usr/include/vterm.h: 218

VTERM_VALUETYPE_COLOR = (VTERM_VALUETYPE_STRING + 1)# /usr/include/vterm.h: 218

VTERM_N_VALUETYPES = (VTERM_VALUETYPE_COLOR + 1)# /usr/include/vterm.h: 218

VTermValueType = enum_anon_26# /usr/include/vterm.h: 218

# /usr/include/vterm.h: 225
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'str',
    'len',
    'initial',
    'final',
]
struct_anon_27._fields_ = [
    ('str', String),
    ('len', c_size_t, 30),
    ('initial', c_bool, 1),
    ('final', c_bool, 1),
]

VTermStringFragment = struct_anon_27# /usr/include/vterm.h: 225

# /usr/include/vterm.h: 232
class union_anon_28(Union):
    pass

union_anon_28.__slots__ = [
    'boolean',
    'number',
    'string',
    'color',
]
union_anon_28._fields_ = [
    ('boolean', c_int),
    ('number', c_int),
    ('string', VTermStringFragment),
    ('color', VTermColor),
]

VTermValue = union_anon_28# /usr/include/vterm.h: 232

enum_anon_29 = c_int# /usr/include/vterm.h: 250

VTERM_ATTR_BOLD = 1# /usr/include/vterm.h: 250

VTERM_ATTR_UNDERLINE = (VTERM_ATTR_BOLD + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_ITALIC = (VTERM_ATTR_UNDERLINE + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_BLINK = (VTERM_ATTR_ITALIC + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_REVERSE = (VTERM_ATTR_BLINK + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_CONCEAL = (VTERM_ATTR_REVERSE + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_STRIKE = (VTERM_ATTR_CONCEAL + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_FONT = (VTERM_ATTR_STRIKE + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_FOREGROUND = (VTERM_ATTR_FONT + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_BACKGROUND = (VTERM_ATTR_FOREGROUND + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_SMALL = (VTERM_ATTR_BACKGROUND + 1)# /usr/include/vterm.h: 250

VTERM_ATTR_BASELINE = (VTERM_ATTR_SMALL + 1)# /usr/include/vterm.h: 250

VTERM_N_ATTRS = (VTERM_ATTR_BASELINE + 1)# /usr/include/vterm.h: 250

VTermAttr = enum_anon_29# /usr/include/vterm.h: 250

enum_anon_30 = c_int# /usr/include/vterm.h: 265

VTERM_PROP_CURSORVISIBLE = 1# /usr/include/vterm.h: 265

VTERM_PROP_CURSORBLINK = (VTERM_PROP_CURSORVISIBLE + 1)# /usr/include/vterm.h: 265

VTERM_PROP_ALTSCREEN = (VTERM_PROP_CURSORBLINK + 1)# /usr/include/vterm.h: 265

VTERM_PROP_TITLE = (VTERM_PROP_ALTSCREEN + 1)# /usr/include/vterm.h: 265

VTERM_PROP_ICONNAME = (VTERM_PROP_TITLE + 1)# /usr/include/vterm.h: 265

VTERM_PROP_REVERSE = (VTERM_PROP_ICONNAME + 1)# /usr/include/vterm.h: 265

VTERM_PROP_CURSORSHAPE = (VTERM_PROP_REVERSE + 1)# /usr/include/vterm.h: 265

VTERM_PROP_MOUSE = (VTERM_PROP_CURSORSHAPE + 1)# /usr/include/vterm.h: 265

VTERM_PROP_FOCUSREPORT = (VTERM_PROP_MOUSE + 1)# /usr/include/vterm.h: 265

VTERM_N_PROPS = (VTERM_PROP_FOCUSREPORT + 1)# /usr/include/vterm.h: 265

VTermProp = enum_anon_30# /usr/include/vterm.h: 265

enum_anon_31 = c_int# /usr/include/vterm.h: 267

VTERM_PROP_CURSORSHAPE_BLOCK = 1# /usr/include/vterm.h: 267

VTERM_PROP_CURSORSHAPE_UNDERLINE = (VTERM_PROP_CURSORSHAPE_BLOCK + 1)# /usr/include/vterm.h: 267

VTERM_PROP_CURSORSHAPE_BAR_LEFT = (VTERM_PROP_CURSORSHAPE_UNDERLINE + 1)# /usr/include/vterm.h: 267

VTERM_N_PROP_CURSORSHAPES = (VTERM_PROP_CURSORSHAPE_BAR_LEFT + 1)# /usr/include/vterm.h: 267

enum_anon_32 = c_int# /usr/include/vterm.h: 275

VTERM_PROP_MOUSE_NONE = 0# /usr/include/vterm.h: 275

VTERM_PROP_MOUSE_CLICK = (VTERM_PROP_MOUSE_NONE + 1)# /usr/include/vterm.h: 275

VTERM_PROP_MOUSE_DRAG = (VTERM_PROP_MOUSE_CLICK + 1)# /usr/include/vterm.h: 275

VTERM_PROP_MOUSE_MOVE = (VTERM_PROP_MOUSE_DRAG + 1)# /usr/include/vterm.h: 275

VTERM_N_PROP_MOUSES = (VTERM_PROP_MOUSE_MOVE + 1)# /usr/include/vterm.h: 275

enum_anon_33 = c_int# /usr/include/vterm.h: 290

VTERM_SELECTION_CLIPBOARD = (1 << 0)# /usr/include/vterm.h: 290

VTERM_SELECTION_PRIMARY = (1 << 1)# /usr/include/vterm.h: 290

VTERM_SELECTION_SECONDARY = (1 << 2)# /usr/include/vterm.h: 290

VTERM_SELECTION_SELECT = (1 << 3)# /usr/include/vterm.h: 290

VTERM_SELECTION_CUT0 = (1 << 4)# /usr/include/vterm.h: 290

VTermSelectionMask = enum_anon_33# /usr/include/vterm.h: 290

# /usr/include/vterm.h: 298
class struct_anon_34(Structure):
    pass

struct_anon_34.__slots__ = [
    'chars',
    'width',
    'protected_cell',
    'dwl',
    'dhl',
]
struct_anon_34._fields_ = [
    ('chars', POINTER(uint32_t)),
    ('width', c_int),
    ('protected_cell', c_uint, 1),
    ('dwl', c_uint, 1),
    ('dhl', c_uint, 2),
]

VTermGlyphInfo = struct_anon_34# /usr/include/vterm.h: 298

# /usr/include/vterm.h: 304
class struct_anon_35(Structure):
    pass

struct_anon_35.__slots__ = [
    'doublewidth',
    'doubleheight',
    'continuation',
]
struct_anon_35._fields_ = [
    ('doublewidth', c_uint, 1),
    ('doubleheight', c_uint, 2),
    ('continuation', c_uint, 1),
]

VTermLineInfo = struct_anon_35# /usr/include/vterm.h: 304

# /usr/include/vterm.h: 314
class struct_anon_36(Structure):
    pass

struct_anon_36.__slots__ = [
    'pos',
    'lineinfos',
]
struct_anon_36._fields_ = [
    ('pos', VTermPos),
    ('lineinfos', POINTER(VTermLineInfo) * int(2)),
]

VTermStateFields = struct_anon_36# /usr/include/vterm.h: 314

# /usr/include/vterm.h: 321
class struct_anon_37(Structure):
    pass

struct_anon_37.__slots__ = [
    'malloc',
    'free',
]
struct_anon_37._fields_ = [
    ('malloc', CFUNCTYPE(UNCHECKED(POINTER(c_ubyte)), c_size_t, POINTER(None))),
    ('free', CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(None))),
]

VTermAllocatorFunctions = struct_anon_37# /usr/include/vterm.h: 321

# /usr/include/vterm.h: 323
if _libs["vterm"].has("vterm_check_version", "cdecl"):
    vterm_check_version = _libs["vterm"].get("vterm_check_version", "cdecl")
    vterm_check_version.argtypes = [c_int, c_int]
    vterm_check_version.restype = None

# /usr/include/vterm.h: 325
class struct_VTermBuilder(Structure):
    pass

struct_VTermBuilder.__slots__ = [
    'ver',
    'rows',
    'cols',
    'allocator',
    'allocdata',
    'outbuffer_len',
    'tmpbuffer_len',
]
struct_VTermBuilder._fields_ = [
    ('ver', c_int),
    ('rows', c_int),
    ('cols', c_int),
    ('allocator', POINTER(VTermAllocatorFunctions)),
    ('allocdata', POINTER(None)),
    ('outbuffer_len', c_size_t),
    ('tmpbuffer_len', c_size_t),
]

# /usr/include/vterm.h: 338
if _libs["vterm"].has("vterm_build", "cdecl"):
    vterm_build = _libs["vterm"].get("vterm_build", "cdecl")
    vterm_build.argtypes = [POINTER(struct_VTermBuilder)]
    vterm_build.restype = POINTER(VTerm)

# /usr/include/vterm.h: 341
if _libs["vterm"].has("vterm_new", "cdecl"):
    vterm_new = _libs["vterm"].get("vterm_new", "cdecl")
    vterm_new.argtypes = [c_int, c_int]
    vterm_new.restype = POINTER(VTerm)

# /usr/include/vterm.h: 343
if _libs["vterm"].has("vterm_new_with_allocator", "cdecl"):
    vterm_new_with_allocator = _libs["vterm"].get("vterm_new_with_allocator", "cdecl")
    vterm_new_with_allocator.argtypes = [c_int, c_int, POINTER(VTermAllocatorFunctions), POINTER(None)]
    vterm_new_with_allocator.restype = POINTER(VTerm)

# /usr/include/vterm.h: 345
if _libs["vterm"].has("vterm_free", "cdecl"):
    vterm_free = _libs["vterm"].get("vterm_free", "cdecl")
    vterm_free.argtypes = [POINTER(VTerm)]
    vterm_free.restype = None

# /usr/include/vterm.h: 347
if _libs["vterm"].has("vterm_get_size", "cdecl"):
    vterm_get_size = _libs["vterm"].get("vterm_get_size", "cdecl")
    vterm_get_size.argtypes = [POINTER(VTerm), POINTER(c_int), POINTER(c_int)]
    vterm_get_size.restype = None

# /usr/include/vterm.h: 348
if _libs["vterm"].has("vterm_set_size", "cdecl"):
    vterm_set_size = _libs["vterm"].get("vterm_set_size", "cdecl")
    vterm_set_size.argtypes = [POINTER(VTerm), c_int, c_int]
    vterm_set_size.restype = None

# /usr/include/vterm.h: 350
if _libs["vterm"].has("vterm_get_utf8", "cdecl"):
    vterm_get_utf8 = _libs["vterm"].get("vterm_get_utf8", "cdecl")
    vterm_get_utf8.argtypes = [POINTER(VTerm)]
    vterm_get_utf8.restype = c_int

# /usr/include/vterm.h: 351
if _libs["vterm"].has("vterm_set_utf8", "cdecl"):
    vterm_set_utf8 = _libs["vterm"].get("vterm_set_utf8", "cdecl")
    vterm_set_utf8.argtypes = [POINTER(VTerm), c_int]
    vterm_set_utf8.restype = None

# /usr/include/vterm.h: 353
if _libs["vterm"].has("vterm_input_write", "cdecl"):
    vterm_input_write = _libs["vterm"].get("vterm_input_write", "cdecl")
    vterm_input_write.argtypes = [POINTER(VTerm), String, c_size_t]
    vterm_input_write.restype = c_size_t

VTermOutputCallback = CFUNCTYPE(UNCHECKED(None), String, c_size_t, POINTER(None))# /usr/include/vterm.h: 356

# /usr/include/vterm.h: 357
if _libs["vterm"].has("vterm_output_set_callback", "cdecl"):
    vterm_output_set_callback = _libs["vterm"].get("vterm_output_set_callback", "cdecl")
    vterm_output_set_callback.argtypes = [POINTER(VTerm), POINTER(VTermOutputCallback), POINTER(None)]
    vterm_output_set_callback.restype = None

# /usr/include/vterm.h: 361
if _libs["vterm"].has("vterm_output_get_buffer_size", "cdecl"):
    vterm_output_get_buffer_size = _libs["vterm"].get("vterm_output_get_buffer_size", "cdecl")
    vterm_output_get_buffer_size.argtypes = [POINTER(VTerm)]
    vterm_output_get_buffer_size.restype = c_size_t

# /usr/include/vterm.h: 362
if _libs["vterm"].has("vterm_output_get_buffer_current", "cdecl"):
    vterm_output_get_buffer_current = _libs["vterm"].get("vterm_output_get_buffer_current", "cdecl")
    vterm_output_get_buffer_current.argtypes = [POINTER(VTerm)]
    vterm_output_get_buffer_current.restype = c_size_t

# /usr/include/vterm.h: 363
if _libs["vterm"].has("vterm_output_get_buffer_remaining", "cdecl"):
    vterm_output_get_buffer_remaining = _libs["vterm"].get("vterm_output_get_buffer_remaining", "cdecl")
    vterm_output_get_buffer_remaining.argtypes = [POINTER(VTerm)]
    vterm_output_get_buffer_remaining.restype = c_size_t

# /usr/include/vterm.h: 366
if _libs["vterm"].has("vterm_output_read", "cdecl"):
    vterm_output_read = _libs["vterm"].get("vterm_output_read", "cdecl")
    vterm_output_read.argtypes = [POINTER(VTerm), String, c_size_t]
    vterm_output_read.restype = c_size_t

# /usr/include/vterm.h: 368
if _libs["vterm"].has("vterm_keyboard_unichar", "cdecl"):
    vterm_keyboard_unichar = _libs["vterm"].get("vterm_keyboard_unichar", "cdecl")
    vterm_keyboard_unichar.argtypes = [POINTER(VTerm), uint32_t, VTermModifier]
    vterm_keyboard_unichar.restype = None

# /usr/include/vterm.h: 369
if _libs["vterm"].has("vterm_keyboard_key", "cdecl"):
    vterm_keyboard_key = _libs["vterm"].get("vterm_keyboard_key", "cdecl")
    vterm_keyboard_key.argtypes = [POINTER(VTerm), VTermKey, VTermModifier]
    vterm_keyboard_key.restype = None

# /usr/include/vterm.h: 371
if _libs["vterm"].has("vterm_keyboard_start_paste", "cdecl"):
    vterm_keyboard_start_paste = _libs["vterm"].get("vterm_keyboard_start_paste", "cdecl")
    vterm_keyboard_start_paste.argtypes = [POINTER(VTerm)]
    vterm_keyboard_start_paste.restype = None

# /usr/include/vterm.h: 372
if _libs["vterm"].has("vterm_keyboard_end_paste", "cdecl"):
    vterm_keyboard_end_paste = _libs["vterm"].get("vterm_keyboard_end_paste", "cdecl")
    vterm_keyboard_end_paste.argtypes = [POINTER(VTerm)]
    vterm_keyboard_end_paste.restype = None

# /usr/include/vterm.h: 374
if _libs["vterm"].has("vterm_mouse_move", "cdecl"):
    vterm_mouse_move = _libs["vterm"].get("vterm_mouse_move", "cdecl")
    vterm_mouse_move.argtypes = [POINTER(VTerm), c_int, c_int, VTermModifier]
    vterm_mouse_move.restype = None

# /usr/include/vterm.h: 375
if _libs["vterm"].has("vterm_mouse_button", "cdecl"):
    vterm_mouse_button = _libs["vterm"].get("vterm_mouse_button", "cdecl")
    vterm_mouse_button.argtypes = [POINTER(VTerm), c_int, c_bool, VTermModifier]
    vterm_mouse_button.restype = None

# /usr/include/vterm.h: 413
class struct_anon_38(Structure):
    pass

struct_anon_38.__slots__ = [
    'text',
    'control',
    'escape',
    'csi',
    'osc',
    'dcs',
    'apc',
    'pm',
    'sos',
    'resize',
]
struct_anon_38._fields_ = [
    ('text', CFUNCTYPE(UNCHECKED(c_int), String, c_size_t, POINTER(None))),
    ('control', CFUNCTYPE(UNCHECKED(c_int), c_ubyte, POINTER(None))),
    ('escape', CFUNCTYPE(UNCHECKED(c_int), String, c_size_t, POINTER(None))),
    ('csi', CFUNCTYPE(UNCHECKED(c_int), String, POINTER(c_long), c_int, String, c_char, POINTER(None))),
    ('osc', CFUNCTYPE(UNCHECKED(c_int), c_int, VTermStringFragment, POINTER(None))),
    ('dcs', CFUNCTYPE(UNCHECKED(c_int), String, c_size_t, VTermStringFragment, POINTER(None))),
    ('apc', CFUNCTYPE(UNCHECKED(c_int), VTermStringFragment, POINTER(None))),
    ('pm', CFUNCTYPE(UNCHECKED(c_int), VTermStringFragment, POINTER(None))),
    ('sos', CFUNCTYPE(UNCHECKED(c_int), VTermStringFragment, POINTER(None))),
    ('resize', CFUNCTYPE(UNCHECKED(c_int), c_int, c_int, POINTER(None))),
]

VTermParserCallbacks = struct_anon_38# /usr/include/vterm.h: 413

# /usr/include/vterm.h: 415
if _libs["vterm"].has("vterm_parser_set_callbacks", "cdecl"):
    vterm_parser_set_callbacks = _libs["vterm"].get("vterm_parser_set_callbacks", "cdecl")
    vterm_parser_set_callbacks.argtypes = [POINTER(VTerm), POINTER(VTermParserCallbacks), POINTER(None)]
    vterm_parser_set_callbacks.restype = None

# /usr/include/vterm.h: 416
if _libs["vterm"].has("vterm_parser_get_cbdata", "cdecl"):
    vterm_parser_get_cbdata = _libs["vterm"].get("vterm_parser_get_cbdata", "cdecl")
    vterm_parser_get_cbdata.argtypes = [POINTER(VTerm)]
    vterm_parser_get_cbdata.restype = POINTER(c_ubyte)
    vterm_parser_get_cbdata.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/vterm.h: 421
if _libs["vterm"].has("vterm_parser_set_emit_nul", "cdecl"):
    vterm_parser_set_emit_nul = _libs["vterm"].get("vterm_parser_set_emit_nul", "cdecl")
    vterm_parser_set_emit_nul.argtypes = [POINTER(VTerm), c_bool]
    vterm_parser_set_emit_nul.restype = None

# /usr/include/vterm.h: 440
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'putglyph',
    'movecursor',
    'scrollrect',
    'moverect',
    'erase',
    'initpen',
    'setpenattr',
    'settermprop',
    'bell',
    'resize',
    'setlineinfo',
    'sb_clear',
]
struct_anon_39._fields_ = [
    ('putglyph', CFUNCTYPE(UNCHECKED(c_int), POINTER(VTermGlyphInfo), VTermPos, POINTER(None))),
    ('movecursor', CFUNCTYPE(UNCHECKED(c_int), VTermPos, VTermPos, c_int, POINTER(None))),
    ('scrollrect', CFUNCTYPE(UNCHECKED(c_int), VTermRect, c_int, c_int, POINTER(None))),
    ('moverect', CFUNCTYPE(UNCHECKED(c_int), VTermRect, VTermRect, POINTER(None))),
    ('erase', CFUNCTYPE(UNCHECKED(c_int), VTermRect, c_int, POINTER(None))),
    ('initpen', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('setpenattr', CFUNCTYPE(UNCHECKED(c_int), VTermAttr, POINTER(VTermValue), POINTER(None))),
    ('settermprop', CFUNCTYPE(UNCHECKED(c_int), VTermProp, POINTER(VTermValue), POINTER(None))),
    ('bell', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('resize', CFUNCTYPE(UNCHECKED(c_int), c_int, c_int, POINTER(VTermStateFields), POINTER(None))),
    ('setlineinfo', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(VTermLineInfo), POINTER(VTermLineInfo), POINTER(None))),
    ('sb_clear', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
]

VTermStateCallbacks = struct_anon_39# /usr/include/vterm.h: 440

# /usr/include/vterm.h: 450
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'control',
    'csi',
    'osc',
    'dcs',
    'apc',
    'pm',
    'sos',
]
struct_anon_40._fields_ = [
    ('control', CFUNCTYPE(UNCHECKED(c_int), c_ubyte, POINTER(None))),
    ('csi', CFUNCTYPE(UNCHECKED(c_int), String, POINTER(c_long), c_int, String, c_char, POINTER(None))),
    ('osc', CFUNCTYPE(UNCHECKED(c_int), c_int, VTermStringFragment, POINTER(None))),
    ('dcs', CFUNCTYPE(UNCHECKED(c_int), String, c_size_t, VTermStringFragment, POINTER(None))),
    ('apc', CFUNCTYPE(UNCHECKED(c_int), VTermStringFragment, POINTER(None))),
    ('pm', CFUNCTYPE(UNCHECKED(c_int), VTermStringFragment, POINTER(None))),
    ('sos', CFUNCTYPE(UNCHECKED(c_int), VTermStringFragment, POINTER(None))),
]

VTermStateFallbacks = struct_anon_40# /usr/include/vterm.h: 450

# /usr/include/vterm.h: 455
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'set',
    'query',
]
struct_anon_41._fields_ = [
    ('set', CFUNCTYPE(UNCHECKED(c_int), VTermSelectionMask, VTermStringFragment, POINTER(None))),
    ('query', CFUNCTYPE(UNCHECKED(c_int), VTermSelectionMask, POINTER(None))),
]

VTermSelectionCallbacks = struct_anon_41# /usr/include/vterm.h: 455

# /usr/include/vterm.h: 457
if _libs["vterm"].has("vterm_obtain_state", "cdecl"):
    vterm_obtain_state = _libs["vterm"].get("vterm_obtain_state", "cdecl")
    vterm_obtain_state.argtypes = [POINTER(VTerm)]
    vterm_obtain_state.restype = POINTER(VTermState)

# /usr/include/vterm.h: 459
if _libs["vterm"].has("vterm_state_set_callbacks", "cdecl"):
    vterm_state_set_callbacks = _libs["vterm"].get("vterm_state_set_callbacks", "cdecl")
    vterm_state_set_callbacks.argtypes = [POINTER(VTermState), POINTER(VTermStateCallbacks), POINTER(None)]
    vterm_state_set_callbacks.restype = None

# /usr/include/vterm.h: 460
if _libs["vterm"].has("vterm_state_get_cbdata", "cdecl"):
    vterm_state_get_cbdata = _libs["vterm"].get("vterm_state_get_cbdata", "cdecl")
    vterm_state_get_cbdata.argtypes = [POINTER(VTermState)]
    vterm_state_get_cbdata.restype = POINTER(c_ubyte)
    vterm_state_get_cbdata.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/vterm.h: 462
if _libs["vterm"].has("vterm_state_set_unrecognised_fallbacks", "cdecl"):
    vterm_state_set_unrecognised_fallbacks = _libs["vterm"].get("vterm_state_set_unrecognised_fallbacks", "cdecl")
    vterm_state_set_unrecognised_fallbacks.argtypes = [POINTER(VTermState), POINTER(VTermStateFallbacks), POINTER(None)]
    vterm_state_set_unrecognised_fallbacks.restype = None

# /usr/include/vterm.h: 463
if _libs["vterm"].has("vterm_state_get_unrecognised_fbdata", "cdecl"):
    vterm_state_get_unrecognised_fbdata = _libs["vterm"].get("vterm_state_get_unrecognised_fbdata", "cdecl")
    vterm_state_get_unrecognised_fbdata.argtypes = [POINTER(VTermState)]
    vterm_state_get_unrecognised_fbdata.restype = POINTER(c_ubyte)
    vterm_state_get_unrecognised_fbdata.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/vterm.h: 465
if _libs["vterm"].has("vterm_state_reset", "cdecl"):
    vterm_state_reset = _libs["vterm"].get("vterm_state_reset", "cdecl")
    vterm_state_reset.argtypes = [POINTER(VTermState), c_int]
    vterm_state_reset.restype = None

# /usr/include/vterm.h: 466
if _libs["vterm"].has("vterm_state_get_cursorpos", "cdecl"):
    vterm_state_get_cursorpos = _libs["vterm"].get("vterm_state_get_cursorpos", "cdecl")
    vterm_state_get_cursorpos.argtypes = [POINTER(VTermState), POINTER(VTermPos)]
    vterm_state_get_cursorpos.restype = None

# /usr/include/vterm.h: 467
if _libs["vterm"].has("vterm_state_get_default_colors", "cdecl"):
    vterm_state_get_default_colors = _libs["vterm"].get("vterm_state_get_default_colors", "cdecl")
    vterm_state_get_default_colors.argtypes = [POINTER(VTermState), POINTER(VTermColor), POINTER(VTermColor)]
    vterm_state_get_default_colors.restype = None

# /usr/include/vterm.h: 468
if _libs["vterm"].has("vterm_state_get_palette_color", "cdecl"):
    vterm_state_get_palette_color = _libs["vterm"].get("vterm_state_get_palette_color", "cdecl")
    vterm_state_get_palette_color.argtypes = [POINTER(VTermState), c_int, POINTER(VTermColor)]
    vterm_state_get_palette_color.restype = None

# /usr/include/vterm.h: 469
if _libs["vterm"].has("vterm_state_set_default_colors", "cdecl"):
    vterm_state_set_default_colors = _libs["vterm"].get("vterm_state_set_default_colors", "cdecl")
    vterm_state_set_default_colors.argtypes = [POINTER(VTermState), POINTER(VTermColor), POINTER(VTermColor)]
    vterm_state_set_default_colors.restype = None

# /usr/include/vterm.h: 470
if _libs["vterm"].has("vterm_state_set_palette_color", "cdecl"):
    vterm_state_set_palette_color = _libs["vterm"].get("vterm_state_set_palette_color", "cdecl")
    vterm_state_set_palette_color.argtypes = [POINTER(VTermState), c_int, POINTER(VTermColor)]
    vterm_state_set_palette_color.restype = None

# /usr/include/vterm.h: 471
if _libs["vterm"].has("vterm_state_set_bold_highbright", "cdecl"):
    vterm_state_set_bold_highbright = _libs["vterm"].get("vterm_state_set_bold_highbright", "cdecl")
    vterm_state_set_bold_highbright.argtypes = [POINTER(VTermState), c_int]
    vterm_state_set_bold_highbright.restype = None

# /usr/include/vterm.h: 472
if _libs["vterm"].has("vterm_state_get_penattr", "cdecl"):
    vterm_state_get_penattr = _libs["vterm"].get("vterm_state_get_penattr", "cdecl")
    vterm_state_get_penattr.argtypes = [POINTER(VTermState), VTermAttr, POINTER(VTermValue)]
    vterm_state_get_penattr.restype = c_int

# /usr/include/vterm.h: 473
if _libs["vterm"].has("vterm_state_set_termprop", "cdecl"):
    vterm_state_set_termprop = _libs["vterm"].get("vterm_state_set_termprop", "cdecl")
    vterm_state_set_termprop.argtypes = [POINTER(VTermState), VTermProp, POINTER(VTermValue)]
    vterm_state_set_termprop.restype = c_int

# /usr/include/vterm.h: 474
if _libs["vterm"].has("vterm_state_focus_in", "cdecl"):
    vterm_state_focus_in = _libs["vterm"].get("vterm_state_focus_in", "cdecl")
    vterm_state_focus_in.argtypes = [POINTER(VTermState)]
    vterm_state_focus_in.restype = None

# /usr/include/vterm.h: 475
if _libs["vterm"].has("vterm_state_focus_out", "cdecl"):
    vterm_state_focus_out = _libs["vterm"].get("vterm_state_focus_out", "cdecl")
    vterm_state_focus_out.argtypes = [POINTER(VTermState)]
    vterm_state_focus_out.restype = None

# /usr/include/vterm.h: 476
if _libs["vterm"].has("vterm_state_get_lineinfo", "cdecl"):
    vterm_state_get_lineinfo = _libs["vterm"].get("vterm_state_get_lineinfo", "cdecl")
    vterm_state_get_lineinfo.argtypes = [POINTER(VTermState), c_int]
    vterm_state_get_lineinfo.restype = POINTER(VTermLineInfo)

# /usr/include/vterm.h: 488
if _libs["vterm"].has("vterm_state_convert_color_to_rgb", "cdecl"):
    vterm_state_convert_color_to_rgb = _libs["vterm"].get("vterm_state_convert_color_to_rgb", "cdecl")
    vterm_state_convert_color_to_rgb.argtypes = [POINTER(VTermState), POINTER(VTermColor)]
    vterm_state_convert_color_to_rgb.restype = None

# /usr/include/vterm.h: 490
if _libs["vterm"].has("vterm_state_set_selection_callbacks", "cdecl"):
    vterm_state_set_selection_callbacks = _libs["vterm"].get("vterm_state_set_selection_callbacks", "cdecl")
    vterm_state_set_selection_callbacks.argtypes = [POINTER(VTermState), POINTER(VTermSelectionCallbacks), POINTER(None), String, c_size_t]
    vterm_state_set_selection_callbacks.restype = None

# /usr/include/vterm.h: 493
if _libs["vterm"].has("vterm_state_send_selection", "cdecl"):
    vterm_state_send_selection = _libs["vterm"].get("vterm_state_send_selection", "cdecl")
    vterm_state_send_selection.argtypes = [POINTER(VTermState), VTermSelectionMask, VTermStringFragment]
    vterm_state_send_selection.restype = None

# /usr/include/vterm.h: 512
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'bold',
    'underline',
    'italic',
    'blink',
    'reverse',
    'conceal',
    'strike',
    'font',
    'dwl',
    'dhl',
    'small',
    'baseline',
]
struct_anon_42._fields_ = [
    ('bold', c_uint, 1),
    ('underline', c_uint, 2),
    ('italic', c_uint, 1),
    ('blink', c_uint, 1),
    ('reverse', c_uint, 1),
    ('conceal', c_uint, 1),
    ('strike', c_uint, 1),
    ('font', c_uint, 4),
    ('dwl', c_uint, 1),
    ('dhl', c_uint, 2),
    ('small', c_uint, 1),
    ('baseline', c_uint, 2),
]

VTermScreenCellAttrs = struct_anon_42# /usr/include/vterm.h: 512

enum_anon_43 = c_int# /usr/include/vterm.h: 514

VTERM_UNDERLINE_OFF = 0# /usr/include/vterm.h: 514

VTERM_UNDERLINE_SINGLE = (VTERM_UNDERLINE_OFF + 1)# /usr/include/vterm.h: 514

VTERM_UNDERLINE_DOUBLE = (VTERM_UNDERLINE_SINGLE + 1)# /usr/include/vterm.h: 514

VTERM_UNDERLINE_CURLY = (VTERM_UNDERLINE_DOUBLE + 1)# /usr/include/vterm.h: 514

enum_anon_44 = c_int# /usr/include/vterm.h: 521

VTERM_BASELINE_NORMAL = 0# /usr/include/vterm.h: 521

VTERM_BASELINE_RAISE = (VTERM_BASELINE_NORMAL + 1)# /usr/include/vterm.h: 521

VTERM_BASELINE_LOWER = (VTERM_BASELINE_RAISE + 1)# /usr/include/vterm.h: 521

# /usr/include/vterm.h: 532
class struct_anon_45(Structure):
    pass

struct_anon_45.__slots__ = [
    'chars',
    'width',
    'attrs',
    'fg',
    'bg',
]
struct_anon_45._fields_ = [
    ('chars', uint32_t * int(6)),
    ('width', c_char),
    ('attrs', VTermScreenCellAttrs),
    ('fg', VTermColor),
    ('bg', VTermColor),
]

VTermScreenCell = struct_anon_45# /usr/include/vterm.h: 532

# /usr/include/vterm.h: 544
class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    'damage',
    'moverect',
    'movecursor',
    'settermprop',
    'bell',
    'resize',
    'sb_pushline',
    'sb_popline',
    'sb_clear',
]
struct_anon_46._fields_ = [
    ('damage', CFUNCTYPE(UNCHECKED(c_int), VTermRect, POINTER(None))),
    ('moverect', CFUNCTYPE(UNCHECKED(c_int), VTermRect, VTermRect, POINTER(None))),
    ('movecursor', CFUNCTYPE(UNCHECKED(c_int), VTermPos, VTermPos, c_int, POINTER(None))),
    ('settermprop', CFUNCTYPE(UNCHECKED(c_int), VTermProp, POINTER(VTermValue), POINTER(None))),
    ('bell', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
    ('resize', CFUNCTYPE(UNCHECKED(c_int), c_int, c_int, POINTER(None))),
    ('sb_pushline', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(VTermScreenCell), POINTER(None))),
    ('sb_popline', CFUNCTYPE(UNCHECKED(c_int), c_int, POINTER(VTermScreenCell), POINTER(None))),
    ('sb_clear', CFUNCTYPE(UNCHECKED(c_int), POINTER(None))),
]

VTermScreenCallbacks = struct_anon_46# /usr/include/vterm.h: 544

# /usr/include/vterm.h: 546
if _libs["vterm"].has("vterm_obtain_screen", "cdecl"):
    vterm_obtain_screen = _libs["vterm"].get("vterm_obtain_screen", "cdecl")
    vterm_obtain_screen.argtypes = [POINTER(VTerm)]
    vterm_obtain_screen.restype = POINTER(VTermScreen)

# /usr/include/vterm.h: 548
if _libs["vterm"].has("vterm_screen_set_callbacks", "cdecl"):
    vterm_screen_set_callbacks = _libs["vterm"].get("vterm_screen_set_callbacks", "cdecl")
    vterm_screen_set_callbacks.argtypes = [POINTER(VTermScreen), POINTER(VTermScreenCallbacks), POINTER(None)]
    vterm_screen_set_callbacks.restype = None

# /usr/include/vterm.h: 549
if _libs["vterm"].has("vterm_screen_get_cbdata", "cdecl"):
    vterm_screen_get_cbdata = _libs["vterm"].get("vterm_screen_get_cbdata", "cdecl")
    vterm_screen_get_cbdata.argtypes = [POINTER(VTermScreen)]
    vterm_screen_get_cbdata.restype = POINTER(c_ubyte)
    vterm_screen_get_cbdata.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/vterm.h: 551
if _libs["vterm"].has("vterm_screen_set_unrecognised_fallbacks", "cdecl"):
    vterm_screen_set_unrecognised_fallbacks = _libs["vterm"].get("vterm_screen_set_unrecognised_fallbacks", "cdecl")
    vterm_screen_set_unrecognised_fallbacks.argtypes = [POINTER(VTermScreen), POINTER(VTermStateFallbacks), POINTER(None)]
    vterm_screen_set_unrecognised_fallbacks.restype = None

# /usr/include/vterm.h: 552
if _libs["vterm"].has("vterm_screen_get_unrecognised_fbdata", "cdecl"):
    vterm_screen_get_unrecognised_fbdata = _libs["vterm"].get("vterm_screen_get_unrecognised_fbdata", "cdecl")
    vterm_screen_get_unrecognised_fbdata.argtypes = [POINTER(VTermScreen)]
    vterm_screen_get_unrecognised_fbdata.restype = POINTER(c_ubyte)
    vterm_screen_get_unrecognised_fbdata.errcheck = lambda v,*a : cast(v, c_void_p)

# /usr/include/vterm.h: 554
if _libs["vterm"].has("vterm_screen_enable_reflow", "cdecl"):
    vterm_screen_enable_reflow = _libs["vterm"].get("vterm_screen_enable_reflow", "cdecl")
    vterm_screen_enable_reflow.argtypes = [POINTER(VTermScreen), c_bool]
    vterm_screen_enable_reflow.restype = None

# /usr/include/vterm.h: 559
if _libs["vterm"].has("vterm_screen_enable_altscreen", "cdecl"):
    vterm_screen_enable_altscreen = _libs["vterm"].get("vterm_screen_enable_altscreen", "cdecl")
    vterm_screen_enable_altscreen.argtypes = [POINTER(VTermScreen), c_int]
    vterm_screen_enable_altscreen.restype = None

enum_anon_47 = c_int# /usr/include/vterm.h: 568

VTERM_DAMAGE_CELL = 0# /usr/include/vterm.h: 568

VTERM_DAMAGE_ROW = (VTERM_DAMAGE_CELL + 1)# /usr/include/vterm.h: 568

VTERM_DAMAGE_SCREEN = (VTERM_DAMAGE_ROW + 1)# /usr/include/vterm.h: 568

VTERM_DAMAGE_SCROLL = (VTERM_DAMAGE_SCREEN + 1)# /usr/include/vterm.h: 568

VTERM_N_DAMAGES = (VTERM_DAMAGE_SCROLL + 1)# /usr/include/vterm.h: 568

VTermDamageSize = enum_anon_47# /usr/include/vterm.h: 568

# /usr/include/vterm.h: 570
if _libs["vterm"].has("vterm_screen_flush_damage", "cdecl"):
    vterm_screen_flush_damage = _libs["vterm"].get("vterm_screen_flush_damage", "cdecl")
    vterm_screen_flush_damage.argtypes = [POINTER(VTermScreen)]
    vterm_screen_flush_damage.restype = None

# /usr/include/vterm.h: 571
if _libs["vterm"].has("vterm_screen_set_damage_merge", "cdecl"):
    vterm_screen_set_damage_merge = _libs["vterm"].get("vterm_screen_set_damage_merge", "cdecl")
    vterm_screen_set_damage_merge.argtypes = [POINTER(VTermScreen), VTermDamageSize]
    vterm_screen_set_damage_merge.restype = None

# /usr/include/vterm.h: 573
if _libs["vterm"].has("vterm_screen_reset", "cdecl"):
    vterm_screen_reset = _libs["vterm"].get("vterm_screen_reset", "cdecl")
    vterm_screen_reset.argtypes = [POINTER(VTermScreen), c_int]
    vterm_screen_reset.restype = None

# /usr/include/vterm.h: 576
if _libs["vterm"].has("vterm_screen_get_chars", "cdecl"):
    vterm_screen_get_chars = _libs["vterm"].get("vterm_screen_get_chars", "cdecl")
    vterm_screen_get_chars.argtypes = [POINTER(VTermScreen), POINTER(uint32_t), c_size_t, VTermRect]
    vterm_screen_get_chars.restype = c_size_t

# /usr/include/vterm.h: 577
if _libs["vterm"].has("vterm_screen_get_text", "cdecl"):
    vterm_screen_get_text = _libs["vterm"].get("vterm_screen_get_text", "cdecl")
    vterm_screen_get_text.argtypes = [POINTER(VTermScreen), String, c_size_t, VTermRect]
    vterm_screen_get_text.restype = c_size_t

enum_anon_48 = c_int# /usr/include/vterm.h: 594

VTERM_ATTR_BOLD_MASK = (1 << 0)# /usr/include/vterm.h: 594

VTERM_ATTR_UNDERLINE_MASK = (1 << 1)# /usr/include/vterm.h: 594

VTERM_ATTR_ITALIC_MASK = (1 << 2)# /usr/include/vterm.h: 594

VTERM_ATTR_BLINK_MASK = (1 << 3)# /usr/include/vterm.h: 594

VTERM_ATTR_REVERSE_MASK = (1 << 4)# /usr/include/vterm.h: 594

VTERM_ATTR_STRIKE_MASK = (1 << 5)# /usr/include/vterm.h: 594

VTERM_ATTR_FONT_MASK = (1 << 6)# /usr/include/vterm.h: 594

VTERM_ATTR_FOREGROUND_MASK = (1 << 7)# /usr/include/vterm.h: 594

VTERM_ATTR_BACKGROUND_MASK = (1 << 8)# /usr/include/vterm.h: 594

VTERM_ATTR_CONCEAL_MASK = (1 << 9)# /usr/include/vterm.h: 594

VTERM_ATTR_SMALL_MASK = (1 << 10)# /usr/include/vterm.h: 594

VTERM_ATTR_BASELINE_MASK = (1 << 11)# /usr/include/vterm.h: 594

VTERM_ALL_ATTRS_MASK = ((1 << 12) - 1)# /usr/include/vterm.h: 594

VTermAttrMask = enum_anon_48# /usr/include/vterm.h: 594

# /usr/include/vterm.h: 596
if _libs["vterm"].has("vterm_screen_get_attrs_extent", "cdecl"):
    vterm_screen_get_attrs_extent = _libs["vterm"].get("vterm_screen_get_attrs_extent", "cdecl")
    vterm_screen_get_attrs_extent.argtypes = [POINTER(VTermScreen), POINTER(VTermRect), VTermPos, VTermAttrMask]
    vterm_screen_get_attrs_extent.restype = c_int

# /usr/include/vterm.h: 598
if _libs["vterm"].has("vterm_screen_get_cell", "cdecl"):
    vterm_screen_get_cell = _libs["vterm"].get("vterm_screen_get_cell", "cdecl")
    vterm_screen_get_cell.argtypes = [POINTER(VTermScreen), VTermPos, POINTER(VTermScreenCell)]
    vterm_screen_get_cell.restype = c_int

# /usr/include/vterm.h: 600
if _libs["vterm"].has("vterm_screen_is_eol", "cdecl"):
    vterm_screen_is_eol = _libs["vterm"].get("vterm_screen_is_eol", "cdecl")
    vterm_screen_is_eol.argtypes = [POINTER(VTermScreen), VTermPos]
    vterm_screen_is_eol.restype = c_int

# /usr/include/vterm.h: 606
if _libs["vterm"].has("vterm_screen_convert_color_to_rgb", "cdecl"):
    vterm_screen_convert_color_to_rgb = _libs["vterm"].get("vterm_screen_convert_color_to_rgb", "cdecl")
    vterm_screen_convert_color_to_rgb.argtypes = [POINTER(VTermScreen), POINTER(VTermColor)]
    vterm_screen_convert_color_to_rgb.restype = None

# /usr/include/vterm.h: 612
if _libs["vterm"].has("vterm_screen_set_default_colors", "cdecl"):
    vterm_screen_set_default_colors = _libs["vterm"].get("vterm_screen_set_default_colors", "cdecl")
    vterm_screen_set_default_colors.argtypes = [POINTER(VTermScreen), POINTER(VTermColor), POINTER(VTermColor)]
    vterm_screen_set_default_colors.restype = None

# /usr/include/vterm.h: 618
if _libs["vterm"].has("vterm_get_attr_type", "cdecl"):
    vterm_get_attr_type = _libs["vterm"].get("vterm_get_attr_type", "cdecl")
    vterm_get_attr_type.argtypes = [VTermAttr]
    vterm_get_attr_type.restype = VTermValueType

# /usr/include/vterm.h: 619
if _libs["vterm"].has("vterm_get_prop_type", "cdecl"):
    vterm_get_prop_type = _libs["vterm"].get("vterm_get_prop_type", "cdecl")
    vterm_get_prop_type.argtypes = [VTermProp]
    vterm_get_prop_type.restype = VTermValueType

# /usr/include/vterm.h: 621
if _libs["vterm"].has("vterm_scroll_rect", "cdecl"):
    vterm_scroll_rect = _libs["vterm"].get("vterm_scroll_rect", "cdecl")
    vterm_scroll_rect.argtypes = [VTermRect, c_int, c_int, CFUNCTYPE(UNCHECKED(c_int), VTermRect, VTermRect, POINTER(None)), CFUNCTYPE(UNCHECKED(c_int), VTermRect, c_int, POINTER(None)), POINTER(None)]
    vterm_scroll_rect.restype = None

# /usr/include/vterm.h: 628
if _libs["vterm"].has("vterm_copy_cells", "cdecl"):
    vterm_copy_cells = _libs["vterm"].get("vterm_copy_cells", "cdecl")
    vterm_copy_cells.argtypes = [VTermRect, VTermRect, CFUNCTYPE(UNCHECKED(None), VTermPos, VTermPos, POINTER(None)), POINTER(None)]
    vterm_copy_cells.restype = None

# <built-in>
try:
    __clang_major__ = 18
except:
    pass

# <built-in>
try:
    __clang_minor__ = 1
except:
    pass

# <built-in>
try:
    __WCHAR_MAX__ = 2147483647
except:
    pass

# <built-in>
try:
    __LDBL_MANT_DIG__ = 64
except:
    pass

# /usr/include/stdint.h: 23
try:
    _STDINT_H = 1
except:
    pass

# /usr/include/features.h: 19
try:
    _FEATURES_H = 1
except:
    pass

# /usr/include/features.h: 173
def __GNUC_PREREQ(maj, min):
    return 0

# /usr/include/features.h: 181
def __glibc_clang_prereq(maj, min):
    return (((__clang_major__ << 16) + __clang_minor__) >= ((maj << 16) + min))

# /usr/include/features.h: 238
try:
    _DEFAULT_SOURCE = 1
except:
    pass

# /usr/include/features.h: 246
try:
    __GLIBC_USE_ISOC2X = 0
except:
    pass

# /usr/include/features.h: 252
try:
    __USE_ISOC11 = 1
except:
    pass

# /usr/include/features.h: 259
try:
    __USE_ISOC99 = 1
except:
    pass

# /usr/include/features.h: 266
try:
    __USE_ISOC95 = 1
except:
    pass

# /usr/include/features.h: 287
try:
    __USE_POSIX_IMPLICITLY = 1
except:
    pass

# /usr/include/features.h: 290
try:
    _POSIX_SOURCE = 1
except:
    pass

# /usr/include/features.h: 292
try:
    _POSIX_C_SOURCE = 200809
except:
    pass

# /usr/include/features.h: 327
try:
    __USE_POSIX = 1
except:
    pass

# /usr/include/features.h: 331
try:
    __USE_POSIX2 = 1
except:
    pass

# /usr/include/features.h: 335
try:
    __USE_POSIX199309 = 1
except:
    pass

# /usr/include/features.h: 339
try:
    __USE_POSIX199506 = 1
except:
    pass

# /usr/include/features.h: 343
try:
    __USE_XOPEN2K = 1
except:
    pass

# /usr/include/features.h: 344
# #undef __USE_ISOC95
try:
    del __USE_ISOC95
except NameError:
    pass

# /usr/include/features.h: 345
try:
    __USE_ISOC95 = 1
except:
    pass

# /usr/include/features.h: 346
# #undef __USE_ISOC99
try:
    del __USE_ISOC99
except NameError:
    pass

# /usr/include/features.h: 347
try:
    __USE_ISOC99 = 1
except:
    pass

# /usr/include/features.h: 351
try:
    __USE_XOPEN2K8 = 1
except:
    pass

# /usr/include/features.h: 353
try:
    _ATFILE_SOURCE = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timesize.h: 26
try:
    __TIMESIZE = __WORDSIZE
except:
    pass

# /usr/include/features.h: 397
try:
    __USE_MISC = 1
except:
    pass

# /usr/include/features.h: 401
try:
    __USE_ATFILE = 1
except:
    pass

# /usr/include/features.h: 433
try:
    __USE_FORTIFY_LEVEL = 0
except:
    pass

# /usr/include/features.h: 441
try:
    __GLIBC_USE_DEPRECATED_GETS = 0
except:
    pass

# /usr/include/features.h: 464
try:
    __GLIBC_USE_DEPRECATED_SCANF = 0
except:
    pass

# /usr/include/features.h: 475
try:
    __GLIBC_USE_C2X_STRTOL = 0
except:
    pass

# /usr/include/stdc-predef.h: 19
try:
    _STDC_PREDEF_H = 1
except:
    pass

# /usr/include/stdc-predef.h: 42
try:
    __STDC_IEC_559__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 43
try:
    __STDC_IEC_60559_BFP__ = 201404
except:
    pass

# /usr/include/stdc-predef.h: 52
try:
    __STDC_IEC_559_COMPLEX__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 53
try:
    __STDC_IEC_60559_COMPLEX__ = 201404
except:
    pass

# /usr/include/stdc-predef.h: 62
try:
    __STDC_ISO_10646__ = 201706
except:
    pass

# /usr/include/features.h: 489
try:
    __GNU_LIBRARY__ = 6
except:
    pass

# /usr/include/features.h: 493
try:
    __GLIBC__ = 2
except:
    pass

# /usr/include/features.h: 494
try:
    __GLIBC_MINOR__ = 39
except:
    pass

# /usr/include/features.h: 496
def __GLIBC_PREREQ(maj, min):
    return (((__GLIBC__ << 16) + __GLIBC_MINOR__) >= ((maj << 16) + min))

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 20
try:
    _SYS_CDEFS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 125
def __P(args):
    return args

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 126
def __PMT(args):
    return args

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 132
def __STRING(x):
    return x

__ptr_t = POINTER(None)# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 135

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 226
try:
    __glibc_c99_flexarr_available = 1
except:
    pass

__restrict_arr = c_int# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 512

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/long-double.h: 21
try:
    __LDOUBLE_REDIRECTS_TO_FLOAT128_ABI = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 634
def __LDBL_REDIR1(name, proto, alias):
    return (name + proto)

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 635
def __LDBL_REDIR(name, proto):
    return (name + proto)

# /usr/include/x86_64-linux-gnu/sys/cdefs.h: 672
try:
    __HAVE_GENERIC_SELECTION = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 42
try:
    __GLIBC_USE_LIB_EXT2 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 71
try:
    __GLIBC_USE_IEC_60559_BFP_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 77
try:
    __GLIBC_USE_IEC_60559_BFP_EXT_C2X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 83
try:
    __GLIBC_USE_IEC_60559_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 94
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 100
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 109
try:
    __GLIBC_USE_IEC_60559_TYPES_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types.h: 24
try:
    _BITS_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/timesize.h: 26
try:
    __TIMESIZE = __WORDSIZE
except:
    pass

__S16_TYPE = c_short# /usr/include/x86_64-linux-gnu/bits/types.h: 109

__U16_TYPE = c_ushort# /usr/include/x86_64-linux-gnu/bits/types.h: 110

__S32_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 111

__U32_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 112

__SLONGWORD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 113

__ULONGWORD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 114

__SQUAD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 128

__UQUAD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 129

__SWORD_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 130

__UWORD_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 131

__SLONG32_TYPE = c_int# /usr/include/x86_64-linux-gnu/bits/types.h: 132

__ULONG32_TYPE = c_uint# /usr/include/x86_64-linux-gnu/bits/types.h: 133

__S64_TYPE = c_long# /usr/include/x86_64-linux-gnu/bits/types.h: 134

__U64_TYPE = c_ulong# /usr/include/x86_64-linux-gnu/bits/types.h: 135

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 24
try:
    _BITS_TYPESIZES_H = 1
except:
    pass

__TIMER_T_TYPE = POINTER(None)# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 71

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 73
class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    '__val',
]
struct_anon_49._fields_ = [
    ('__val', c_int * int(2)),
]

__FSID_T_TYPE = struct_anon_49# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 73

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 81
try:
    __OFF_T_MATCHES_OFF64_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 84
try:
    __INO_T_MATCHES_INO64_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 87
try:
    __RLIM_T_MATCHES_RLIM64_T = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 90
try:
    __STATFS_MATCHES_STATFS64 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 93
try:
    __KERNEL_OLD_TIMEVAL_MATCHES_TIMEVAL64 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/typesizes.h: 103
try:
    __FD_SETSIZE = 1024
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/time64.h: 24
try:
    _BITS_TIME64_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wchar.h: 20
try:
    _BITS_WCHAR_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wchar.h: 34
try:
    __WCHAR_MAX = __WCHAR_MAX__
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wchar.h: 46
try:
    __WCHAR_MIN = ((-__WCHAR_MAX) - 1)
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stdint-intn.h: 20
try:
    _BITS_STDINT_INTN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stdint-uintn.h: 20
try:
    _BITS_STDINT_UINTN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/stdint-least.h: 20
try:
    _BITS_STDINT_LEAST_H = 1
except:
    pass

# /usr/include/stdint.h: 105
try:
    INT8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 106
try:
    INT16_MIN = ((-32767) - 1)
except:
    pass

# /usr/include/stdint.h: 107
try:
    INT32_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 110
try:
    INT8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 111
try:
    INT16_MAX = 32767
except:
    pass

# /usr/include/stdint.h: 112
try:
    INT32_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 116
try:
    UINT8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 117
try:
    UINT16_MAX = 65535
except:
    pass

# /usr/include/stdint.h: 118
try:
    UINT32_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 123
try:
    INT_LEAST8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 124
try:
    INT_LEAST16_MIN = ((-32767) - 1)
except:
    pass

# /usr/include/stdint.h: 125
try:
    INT_LEAST32_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 128
try:
    INT_LEAST8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 129
try:
    INT_LEAST16_MAX = 32767
except:
    pass

# /usr/include/stdint.h: 130
try:
    INT_LEAST32_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 134
try:
    UINT_LEAST8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 135
try:
    UINT_LEAST16_MAX = 65535
except:
    pass

# /usr/include/stdint.h: 136
try:
    UINT_LEAST32_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 141
try:
    INT_FAST8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 143
try:
    INT_FAST16_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 144
try:
    INT_FAST32_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 151
try:
    INT_FAST8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 153
try:
    INT_FAST16_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 154
try:
    INT_FAST32_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 162
try:
    UINT_FAST8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 164
try:
    UINT_FAST16_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 165
try:
    UINT_FAST32_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 175
try:
    INTPTR_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 176
try:
    INTPTR_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 177
try:
    UINTPTR_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 198
try:
    PTRDIFF_MIN = ((-9223372036854775807) - 1)
except:
    pass

# /usr/include/stdint.h: 199
try:
    PTRDIFF_MAX = 9223372036854775807
except:
    pass

# /usr/include/stdint.h: 211
try:
    SIG_ATOMIC_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 212
try:
    SIG_ATOMIC_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 216
try:
    SIZE_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 228
try:
    WCHAR_MIN = __WCHAR_MIN
except:
    pass

# /usr/include/stdint.h: 229
try:
    WCHAR_MAX = __WCHAR_MAX
except:
    pass

# /usr/include/stdint.h: 233
try:
    WINT_MIN = 0
except:
    pass

# /usr/include/stdint.h: 234
try:
    WINT_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 237
def INT8_C(c):
    return c

# /usr/include/stdint.h: 238
def INT16_C(c):
    return c

# /usr/include/stdint.h: 239
def INT32_C(c):
    return c

# /usr/include/stdint.h: 247
def UINT8_C(c):
    return c

# /usr/include/stdint.h: 248
def UINT16_C(c):
    return c

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 37
# #undef __GLIBC_USE_LIB_EXT2
try:
    del __GLIBC_USE_LIB_EXT2
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 42
try:
    __GLIBC_USE_LIB_EXT2 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 67
# #undef __GLIBC_USE_IEC_60559_BFP_EXT
try:
    del __GLIBC_USE_IEC_60559_BFP_EXT
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 71
try:
    __GLIBC_USE_IEC_60559_BFP_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 73
# #undef __GLIBC_USE_IEC_60559_BFP_EXT_C2X
try:
    del __GLIBC_USE_IEC_60559_BFP_EXT_C2X
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 77
try:
    __GLIBC_USE_IEC_60559_BFP_EXT_C2X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 79
# #undef __GLIBC_USE_IEC_60559_EXT
try:
    del __GLIBC_USE_IEC_60559_EXT
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 83
try:
    __GLIBC_USE_IEC_60559_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 90
# #undef __GLIBC_USE_IEC_60559_FUNCS_EXT
try:
    del __GLIBC_USE_IEC_60559_FUNCS_EXT
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 94
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 96
# #undef __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X
try:
    del __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 100
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 105
# #undef __GLIBC_USE_IEC_60559_TYPES_EXT
try:
    del __GLIBC_USE_IEC_60559_TYPES_EXT
except NameError:
    pass

# /usr/include/x86_64-linux-gnu/bits/libc-header-start.h: 109
try:
    __GLIBC_USE_IEC_60559_TYPES_EXT = 0
except:
    pass

# /usr/include/stdlib.h: 36
try:
    _STDLIB_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 25
try:
    WNOHANG = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 26
try:
    WUNTRACED = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 30
try:
    WSTOPPED = 2
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 31
try:
    WEXITED = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 32
try:
    WCONTINUED = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 33
try:
    WNOWAIT = 0x01000000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 36
try:
    __WNOTHREAD = 0x20000000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 38
try:
    __WALL = 0x40000000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitflags.h: 39
try:
    __WCLONE = 0x80000000
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 28
def __WEXITSTATUS(status):
    return ((status & 0xff00) >> 8)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 31
def __WTERMSIG(status):
    return (status & 0x7f)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 34
def __WSTOPSIG(status):
    return (__WEXITSTATUS (status))

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 37
def __WIFEXITED(status):
    return ((__WTERMSIG (status)) == 0)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 40
def __WIFSIGNALED(status):
    return (((c_char ((((status & 0x7f) + 1)))).value >> 1) > 0)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 44
def __WIFSTOPPED(status):
    return ((status & 0xff) == 0x7f)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 49
def __WIFCONTINUED(status):
    return (status == __W_CONTINUED)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 53
def __WCOREDUMP(status):
    return (status & __WCOREFLAG)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 56
def __W_EXITCODE(ret, sig):
    return ((ret << 8) | sig)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 57
def __W_STOPCODE(sig):
    return ((sig << 8) | 0x7f)

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 58
try:
    __W_CONTINUED = 0xffff
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/waitstatus.h: 59
try:
    __WCOREFLAG = 0x80
except:
    pass

# /usr/include/stdlib.h: 44
def WEXITSTATUS(status):
    return (__WEXITSTATUS (status))

# /usr/include/stdlib.h: 45
def WTERMSIG(status):
    return (__WTERMSIG (status))

# /usr/include/stdlib.h: 46
def WSTOPSIG(status):
    return (__WSTOPSIG (status))

# /usr/include/stdlib.h: 47
def WIFEXITED(status):
    return (__WIFEXITED (status))

# /usr/include/stdlib.h: 48
def WIFSIGNALED(status):
    return (__WIFSIGNALED (status))

# /usr/include/stdlib.h: 49
def WIFSTOPPED(status):
    return (__WIFSTOPPED (status))

# /usr/include/stdlib.h: 51
def WIFCONTINUED(status):
    return (__WIFCONTINUED (status))

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 34
try:
    __HAVE_FLOAT128 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 42
try:
    __HAVE_DISTINCT_FLOAT128 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 48
try:
    __HAVE_FLOAT64X = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn.h: 54
try:
    __HAVE_FLOAT64X_LONG_DOUBLE = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/long-double.h: 21
try:
    __LDOUBLE_REDIRECTS_TO_FLOAT128_ABI = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 34
try:
    __HAVE_FLOAT16 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 35
try:
    __HAVE_FLOAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 36
try:
    __HAVE_FLOAT64 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 37
try:
    __HAVE_FLOAT32X = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 38
try:
    __HAVE_FLOAT128X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 52
try:
    __HAVE_DISTINCT_FLOAT16 = __HAVE_FLOAT16
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 53
try:
    __HAVE_DISTINCT_FLOAT32 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 54
try:
    __HAVE_DISTINCT_FLOAT64 = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 55
try:
    __HAVE_DISTINCT_FLOAT32X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 56
try:
    __HAVE_DISTINCT_FLOAT64X = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 57
try:
    __HAVE_DISTINCT_FLOAT128X = __HAVE_FLOAT128X
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 63
try:
    __HAVE_FLOAT128_UNLIKE_LDBL = (__HAVE_DISTINCT_FLOAT128 and (__LDBL_MANT_DIG__ != 113))
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 72
try:
    __HAVE_FLOATN_NOT_TYPEDEF = 0
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 102
def __f64(x):
    return x

# /usr/include/x86_64-linux-gnu/bits/floatn-common.h: 111
def __f32x(x):
    return x

# /usr/include/stdlib.h: 72
try:
    __ldiv_t_defined = 1
except:
    pass

# /usr/include/stdlib.h: 82
try:
    __lldiv_t_defined = 1
except:
    pass

# /usr/include/stdlib.h: 87
try:
    RAND_MAX = 2147483647
except:
    pass

# /usr/include/stdlib.h: 92
try:
    EXIT_FAILURE = 1
except:
    pass

# /usr/include/stdlib.h: 93
try:
    EXIT_SUCCESS = 0
except:
    pass

# /usr/include/stdlib.h: 97
try:
    MB_CUR_MAX = (__ctype_get_mb_cur_max ())
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/types.h: 23
try:
    _SYS_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/clock_t.h: 2
try:
    __clock_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/clockid_t.h: 2
try:
    __clockid_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/time_t.h: 2
try:
    __time_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/timer_t.h: 2
try:
    __timer_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/types.h: 171
try:
    __BIT_TYPES_DEFINED__ = 1
except:
    pass

# /usr/include/endian.h: 19
try:
    _ENDIAN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 20
try:
    _BITS_ENDIAN_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 30
try:
    __LITTLE_ENDIAN = 1234
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 31
try:
    __BIG_ENDIAN = 4321
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 32
try:
    __PDP_ENDIAN = 3412
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endianness.h: 2
try:
    _BITS_ENDIANNESS_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endianness.h: 9
try:
    __BYTE_ORDER = __LITTLE_ENDIAN
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/endian.h: 40
try:
    __FLOAT_WORD_ORDER = __BYTE_ORDER
except:
    pass

# /usr/include/endian.h: 27
try:
    LITTLE_ENDIAN = __LITTLE_ENDIAN
except:
    pass

# /usr/include/endian.h: 28
try:
    BIG_ENDIAN = __BIG_ENDIAN
except:
    pass

# /usr/include/endian.h: 29
try:
    PDP_ENDIAN = __PDP_ENDIAN
except:
    pass

# /usr/include/endian.h: 30
try:
    BYTE_ORDER = __BYTE_ORDER
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 24
try:
    _BITS_BYTESWAP_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 30
def __bswap_constant_16(x):
    return (__uint16_t (ord_if_char((((x >> 8) & 0xff) | ((x & 0xff) << 8))))).value

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 44
def __bswap_constant_32(x):
    return (((((x & 0xff000000) >> 24) | ((x & 0x00ff0000) >> 8)) | ((x & 0x0000ff00) << 8)) | ((x & 0x000000ff) << 24))

# /usr/include/x86_64-linux-gnu/bits/byteswap.h: 59
def __bswap_constant_64(x):
    return (((((((((x & 0xff00000000000000) >> 56) | ((x & 0x00ff000000000000) >> 40)) | ((x & 0x0000ff0000000000) >> 24)) | ((x & 0x000000ff00000000) >> 8)) | ((x & 0x00000000ff000000) << 8)) | ((x & 0x0000000000ff0000) << 24)) | ((x & 0x000000000000ff00) << 40)) | ((x & 0x00000000000000ff) << 56))

# /usr/include/x86_64-linux-gnu/bits/uintn-identity.h: 24
try:
    _BITS_UINTN_IDENTITY_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 22
try:
    _SYS_SELECT_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/select.h: 32
def __FD_SET(d, s):
    return None

# /usr/include/x86_64-linux-gnu/bits/select.h: 34
def __FD_CLR(d, s):
    return None

# /usr/include/x86_64-linux-gnu/bits/select.h: 36
def __FD_ISSET(d, s):
    return ((((__FDS_BITS (s)) [(__FD_ELT (d))]) & (__FD_MASK (d))) != 0)

# /usr/include/x86_64-linux-gnu/bits/types/sigset_t.h: 2
try:
    __sigset_t_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/__sigset_t.h: 4
try:
    _SIGSET_NWORDS = (1024 / (8 * sizeof(c_ulong)))
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 2
try:
    __timeval_defined = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 3
try:
    _STRUCT_TIMESPEC = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 54
try:
    __NFDBITS = (8 * (c_int (ord_if_char(sizeof(__fd_mask)))).value)
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 55
def __FD_ELT(d):
    return (d / __NFDBITS)

# /usr/include/x86_64-linux-gnu/sys/select.h: 56
def __FD_MASK(d):
    return (__fd_mask (ord_if_char((1 << (d % __NFDBITS))))).value

# /usr/include/x86_64-linux-gnu/sys/select.h: 68
def __FDS_BITS(set):
    return (set.contents.__fds_bits)

# /usr/include/x86_64-linux-gnu/sys/select.h: 73
try:
    FD_SETSIZE = __FD_SETSIZE
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 80
try:
    NFDBITS = __NFDBITS
except:
    pass

# /usr/include/x86_64-linux-gnu/sys/select.h: 85
def FD_SET(fd, fdsetp):
    return (__FD_SET (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/sys/select.h: 86
def FD_CLR(fd, fdsetp):
    return (__FD_CLR (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/sys/select.h: 87
def FD_ISSET(fd, fdsetp):
    return (__FD_ISSET (fd, fdsetp))

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 20
try:
    _BITS_PTHREADTYPES_COMMON_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 20
try:
    _THREAD_SHARED_TYPES_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 19
try:
    _BITS_PTHREADTYPES_ARCH_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 25
try:
    __SIZEOF_PTHREAD_MUTEX_T = 40
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 26
try:
    __SIZEOF_PTHREAD_ATTR_T = 56
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 27
try:
    __SIZEOF_PTHREAD_RWLOCK_T = 56
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 28
try:
    __SIZEOF_PTHREAD_BARRIER_T = 32
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 41
try:
    __SIZEOF_PTHREAD_MUTEXATTR_T = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 42
try:
    __SIZEOF_PTHREAD_COND_T = 48
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 43
try:
    __SIZEOF_PTHREAD_CONDATTR_T = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 44
try:
    __SIZEOF_PTHREAD_RWLOCKATTR_T = 8
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes-arch.h: 45
try:
    __SIZEOF_PTHREAD_BARRIERATTR_T = 4
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 20
try:
    _THREAD_MUTEX_INTERNAL_H = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 37
try:
    __PTHREAD_MUTEX_HAVE_PREV = 1
except:
    pass

# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 63
try:
    __have_pthread_attr_t = 1
except:
    pass

# /usr/include/alloca.h: 19
try:
    _ALLOCA_H = 1
except:
    pass

# /usr/lib/llvm-18/lib/clang/18/include/stdbool.h: 13
try:
    __bool_true_false_are_defined = 1
except:
    pass

bool = c_bool# /usr/lib/llvm-18/lib/clang/18/include/stdbool.h: 20

# /usr/lib/llvm-18/lib/clang/18/include/stdbool.h: 21
try:
    true = 1
except:
    pass

# /usr/lib/llvm-18/lib/clang/18/include/stdbool.h: 22
try:
    false = 0
except:
    pass

# /usr/include/vterm_keycodes.h: 59
def VTERM_KEY_FUNCTION(n):
    return (VTERM_KEY_FUNCTION_0 + n)

# /usr/include/vterm.h: 14
try:
    VTERM_VERSION_MAJOR = 0
except:
    pass

# /usr/include/vterm.h: 15
try:
    VTERM_VERSION_MINOR = 3
except:
    pass

# /usr/include/vterm.h: 16
try:
    VTERM_VERSION_PATCH = 3
except:
    pass

# /usr/include/vterm.h: 18
try:
    VTERM_CHECK_VERSION = (vterm_check_version (VTERM_VERSION_MAJOR, VTERM_VERSION_MINOR))
except:
    pass

# /usr/include/vterm.h: 24
try:
    VTERM_MAX_CHARS_PER_CELL = 6
except:
    pass

# /usr/include/vterm.h: 109
def VTERM_COLOR_IS_INDEXED(col):
    return ((((col.contents.type).value) & VTERM_COLOR_TYPE_MASK) == VTERM_COLOR_INDEXED)

# /usr/include/vterm.h: 116
def VTERM_COLOR_IS_RGB(col):
    return ((((col.contents.type).value) & VTERM_COLOR_TYPE_MASK) == VTERM_COLOR_RGB)

# /usr/include/vterm.h: 124
def VTERM_COLOR_IS_DEFAULT_FG(col):
    return (not (not (((col.contents.type).value) & VTERM_COLOR_DEFAULT_FG)))

# /usr/include/vterm.h: 132
def VTERM_COLOR_IS_DEFAULT_BG(col):
    return (not (not (((col.contents.type).value) & VTERM_COLOR_DEFAULT_BG)))

# /usr/include/vterm.h: 389
try:
    CSI_ARG_FLAG_MORE = (1 << 31)
except:
    pass

# /usr/include/vterm.h: 390
try:
    CSI_ARG_MASK = (~(1 << 31))
except:
    pass

# /usr/include/vterm.h: 392
def CSI_ARG_HAS_MORE(a):
    return (a & CSI_ARG_FLAG_MORE)

# /usr/include/vterm.h: 393
def CSI_ARG(a):
    return (a & CSI_ARG_MASK)

# /usr/include/vterm.h: 396
try:
    CSI_ARG_MISSING = ((1 << 31) - 1)
except:
    pass

# /usr/include/vterm.h: 398
def CSI_ARG_IS_MISSING(a):
    return ((CSI_ARG (a)) == CSI_ARG_MISSING)

# /usr/include/vterm.h: 399
def CSI_ARG_OR(a, default):
    return ((CSI_ARG (a)) == CSI_ARG_MISSING) and default or (CSI_ARG (a))

# /usr/include/vterm.h: 400
def CSI_ARG_COUNT(a):
    return (((CSI_ARG (a)) == CSI_ARG_MISSING) or ((CSI_ARG (a)) == 0)) and 1 or (CSI_ARG (a))

# /usr/include/vterm.h: 557
try:
    vterm_screen_set_reflow = vterm_screen_enable_reflow
except:
    pass

timeval = struct_timeval# /usr/include/x86_64-linux-gnu/bits/types/struct_timeval.h: 8

timespec = struct_timespec# /usr/include/x86_64-linux-gnu/bits/types/struct_timespec.h: 11

__pthread_internal_list = struct___pthread_internal_list# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 51

__pthread_internal_slist = struct___pthread_internal_slist# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 57

__pthread_mutex_s = struct___pthread_mutex_s# /usr/include/x86_64-linux-gnu/bits/struct_mutex.h: 22

__pthread_rwlock_arch_t = struct___pthread_rwlock_arch_t# /usr/include/x86_64-linux-gnu/bits/struct_rwlock.h: 23

__pthread_cond_s = struct___pthread_cond_s# /usr/include/x86_64-linux-gnu/bits/thread-shared-types.h: 94

pthread_attr_t = union_pthread_attr_t# /usr/include/x86_64-linux-gnu/bits/pthreadtypes.h: 56

random_data = struct_random_data# /usr/include/stdlib.h: 543

drand48_data = struct_drand48_data# /usr/include/stdlib.h: 610

VTerm = struct_VTerm# /usr/include/vterm.h: 26

VTermState = struct_VTermState# /usr/include/vterm.h: 27

VTermScreen = struct_VTermScreen# /usr/include/vterm.h: 28

VTermBuilder = struct_VTermBuilder# /usr/include/vterm.h: 325

# No inserted files

# No prefix-stripping

