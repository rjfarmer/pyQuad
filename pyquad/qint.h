// SPDX-License-Identifier: GPL-2.0+
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "structmember.h"
#include <quadmath.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#pragma once

#ifndef Py_QIFLOAT_H
#define Py_QIFLOAT_H
#ifdef __cplusplus
extern "C" {
#endif

/* C API functions */
#define PyQInt_q2py_NUM 0
#define PyQInt_py2q_NUM 1
#define PyQInt_alloc_NUM 2
#define PyQInt_int128_NUM 3
#define PyQInt_check_NUM 4

/* Total number of C API pointers */
#define PyQInt_API_pointers 5


#define OP_add 1
#define OP_sub 2
#define OP_mult 3
#define OP_remainder 4
#define OP_divmod 5
#define OP_pow 6
#define OP_negative 7
#define OP_positive 8
#define OP_absolute 9
#define OP_bool 10
#define OP_invert 11
#define OP_lshift 12
#define OP_rshift 13
#define OP_and 14
#define OP_xor 15
#define OP_or 16
#define OP_int 17
//  void *nb_reserved; 18
#define OP_float 19

#define OP_inplace_add 20
#define OP_inplace_subtract 21
#define OP_inplace_multiply 22
#define OP_inplace_remainder 23
#define OP_inplace_power 24
#define OP_inplace_lshift 25
#define OP_inplace_rshift 26
#define OP_inplace_and 27
#define OP_inplace_xor 28
#define OP_inplace_or 29

#define OP_floor_divide 30
#define OP_true_divide 31
#define OP_inplace_floor_divide 32
#define OP_inplace_true_divide 33
#define OP_index 34
#define OP_matrix_multiply 35
#define OP_inplace_matrix_multiply 36

#define QUAD_BUF 128
#define QUAD_INT_STR_BUF QUAD_BUF+2 // +1 for sign bit and +1 for \0

#define PICKLE_VERSION_KEY  "_pickle_version"
#define PICKLE_VERSION 1

typedef struct {
    PyObject_HEAD
    union{
    __int128 value;
    char bytes[sizeof(__int128)];
    };
} QuadIObject;

bool str_to_int128(const char *str, Py_ssize_t length, __int128 *result);
bool int128_to_str(__int128 num, char* str, int len, int base);

#ifdef QINT_MODULE

// exported

static PyObject* QuadIObject_to_PyObject(QuadIObject out);
static bool PyObject_to_QuadIObject(PyObject * in, QuadIObject * out, const bool alloc);
static void alloc_QuadIType(QuadIObject * result);
static __int128 QuadIObject_int128(QuadIObject * out);
static bool QuadIObject_Check(PyObject * obj);

#else

static void **PyQInt_API;

#define QuadIObject_to_PyObject \
 (*(PyObject * (*)(QuadIObject)) PyQInt_API[PyQInt_q2py_NUM])

#define PyObject_to_QuadIObject \
 (*(bool (*)(PyObject *, QuadIObject *, const bool)) PyQInt_API[PyQInt_py2q_NUM])

#define alloc_QuadIType \
(*(void (*)(QuadIObject *)) PyQInt_API[PyQInt_alloc_NUM])

#define QuadIObject_int128 \
(*(__int128 (*)(QuadIObject *)) PyQInt_API[PyQInt_int128_NUM])

#define QuadIObject_Check \
(*(bool (*)(PyObject *)) PyQInt_API[PyQInt_check_NUM])


/* Return -1 on error, 0 on success.
 * PyCapsule_Import will set an exception if there's an error.
 */
static int
import_qint(void)
{
    PyQInt_API = (void **)PyCapsule_Import("qint._C_API", 0);
    return (PyQInt_API != NULL) ? 0 : -1;
}



#endif



// end exported


#ifdef __cplusplus
}
#endif

#endif
