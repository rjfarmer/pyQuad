# SPDX-License-Identifier: GPL-2.0+

import os, sys
from pprint import pprint

import numpy as np
import pytest
import math

from hypothesis import given
from hypothesis.strategies import floats

import pyquad as pq
import pyquad.qmath as qm


class TestQMathFloat:
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_acosq(self, x):
        assert float(qm.acosq(x)) == pytest.approx(math.acos(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=1))
    def test_acoshq(self, x):
        assert float(qm.acoshq(x)) == pytest.approx(math.acosh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_asinq(self, x):
        assert float(qm.asinq(x)) == pytest.approx(math.asin(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_asinhq(self, x):
        assert float(qm.asinhq(x)) == pytest.approx(math.asinh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_atanq(self, x):
        assert float(qm.atanq(x)) == pytest.approx(math.atan(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_atanhq(self, x):
        assert float(qm.atanhq(x)) == pytest.approx(math.atanh(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_atan2q(self, x, y):
    #     assert float(qm.atan2q(x,y)) == pytest.approx(math.atan2(x,y))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_cbrtq(self, x):
        assert float(qm.cbrtq(x)) == pytest.approx(math.cbrt(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_ceilq(self, x):
        assert float(qm.ceilq(x)) == pytest.approx(math.ceil(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_copysignq(self, x, y):
    #     assert float(qm.copysignq(x,y)) == pytest.approx(math.copysign(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False,min_value=1))
    # def test_coshq(self, x):
    #     assert float(qm.coshq(x)) == pytest.approx(math.cosh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_cosq(self, x):
        assert float(qm.cosq(x)) == pytest.approx(math.cos(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_erfq(self, x):
        assert float(qm.erfq(x)) == pytest.approx(math.erf(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_erfcq(self, x):
        assert float(qm.erfcq(x)) == pytest.approx(math.erfc(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_exp2q(self, x):
    #     assert float(qm.exp2q(x)) == pytest.approx(math.exp2(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_expq(self, x):
    #     assert float(qm.expq(x)) == pytest.approx(math.exp(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_expm1q(self, x):
    #     assert float(qm.expm1q(x)) == pytest.approx(math.expm1(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_fabsq(self, x):
        assert float(qm.fabsq(x)) == pytest.approx(math.fabs(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_fdimq(self, x, y):
    #     assert float(qm.fdimq(x,y)) == pytest.approx(math.fdim(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_finiteq(self, x):
    #     assert float(qm.finiteq(x)) == pytest.approx(math.finite(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_floorq(self, x):
        assert float(qm.floorq(x)) == pytest.approx(math.floor(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_fmaq(self, x, y):
    #     assert float(qm.fmaq(x,y)) == pytest.approx(math.fma(x,y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_fmaxq(self, x, y):
    #     assert float(qm.fmaxq(x,y)) == pytest.approx(math.fmax(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_fminq(self, x, y):
    #     assert float(qm.fminq(x,y)) == pytest.approx(math.fmin(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_fmodq(self, x, y):
    #     assert float(qm.fmodq(x,y)) == pytest.approx(math.fmod(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_frexpq(self, x):
    #     assert float(qm.frexpq(x)) == pytest.approx(math.frexp(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_hypotq(self, x, y):
    #     assert float(qm.hypotq(x,y)) == pytest.approx(math.hypot(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_ilogbq(self, x):
    #     assert float(qm.ilogbq(x)) == pytest.approx(math.ilogb(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_isinfq(self, x):
        assert float(qm.isinfq(x)) == pytest.approx(math.isinf(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_isnanq(self, x):
        assert float(qm.isnanq(x)) == pytest.approx(math.isnan(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_issignalingq(self, x):
    #     assert float(qm.issignalingq(x)) == pytest.approx(math.issignaling(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_j0q(self, x):
    #     assert float(qm.j0q(x)) == pytest.approx(math.j0(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_j1q(self, x):
    #     assert float(qm.j1q(x)) == pytest.approx(math.j1(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_jnq(self, x):
    #     assert float(qm.jnq(x)) == pytest.approx(math.jn(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_ldexpq(self, x):
    #     assert float(qm.ldexpq(x)) == pytest.approx(math.ldexp(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_lgammaq(self, x):
    #     assert float(qm.lgammaq(x)) == pytest.approx(math.lgamma(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_llrintq(self, x):
    #     assert float(qm.llrintq(x)) == pytest.approx(math.llrint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_llroundq(self, x):
    #     assert float(qm.llroundq(x)) == pytest.approx(math.llround(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_logbq(self, x):
    #     assert float(qm.logbq(x)) == pytest.approx(math.logb(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_logq(self, x):
        assert float(qm.logq(x)) == pytest.approx(math.log(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log10q(self, x):
        assert float(qm.log10q(x)) == pytest.approx(math.log10(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log1pq(self, x):
        assert float(qm.log1pq(x)) == pytest.approx(math.log1p(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log2q(self, x):
        assert float(qm.log2q(x)) == pytest.approx(math.log2(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_lrintq(self, x):
    #     assert float(qm.lrintq(x)) == pytest.approx(math.lrint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_lroundq(self, x):
    #     assert float(qm.lroundq(x)) == pytest.approx(math.lround(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_modfq(self, x):
    #     assert float(qm.modfq(x)) == pytest.approx(math.modf(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_nanq(self, x):
    #     assert float(qm.nanq(x)) == pytest.approx(math.nan(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_nearbyintq(self, x):
    #     assert float(qm.nearbyintq(x)) == pytest.approx(math.nearbyint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_nextafterq(self, x, y):
    #     assert float(qm.nextafterq(x,y)) == pytest.approx(math.nextafter(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_powq(self, x, y):
    #     assert float(qm.powq(x,y)) == pytest.approx(math.pow(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_remainderq(self, x, y):
    #     assert float(qm.remainderq(x,y)) == pytest.approx(math.remainder(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_remquoq(self, x):
    #     assert float(qm.remquoq(x)) == pytest.approx(math.remquo(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_rintq(self, x):
    #     assert float(qm.rintq(x)) == pytest.approx(math.rint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_roundq(self, x):
    #     assert float(qm.roundq(x)) == pytest.approx(math.round(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_scalblnq(self, x):
    #     assert float(qm.scalblnq(x)) == pytest.approx(math.scalbln(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_scalbnq(self, x):
    #     assert float(qm.scalbnq(x)) == pytest.approx(math.scalbn(x))

    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_signbitq(self, x):
    #     assert float(qm.signbitq(x)) == pytest.approx(math.signbit(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_sincosq(self, x):
    #     assert float(qm.sincosq(x)) == pytest.approx(math.sincos(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_sinhq(self, x):
    #     assert float(qm.sinhq(x)) == pytest.approx(math.sinh(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_sinq(self, x):
    #     assert float(qm.sinq(x)) == pytest.approx(math.sin(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_sqrtq(self, x):
        assert float(qm.sqrtq(x)) == pytest.approx(math.sqrt(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_tanq(self, x):
        assert float(qm.tanq(x)) == pytest.approx(math.tan(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_tanhq(self, x):
        assert float(qm.tanhq(x)) == pytest.approx(math.tanh(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_tgammaq(self, x):
    #     assert float(qm.tgammaq(x)) == pytest.approx(math.tgamma(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_truncq(self, x):
        assert float(qm.truncq(x)) == pytest.approx(math.trunc(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_y0q(self, x):
    #     assert float(qm.y0q(x)) == pytest.approx(math.y0(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_y1q(self, x):
    #     assert float(qm.y1q(x)) == pytest.approx(math.y1(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_ynq(self, x):
    #     assert float(qm.ynq(x)) == pytest.approx(math.yn(x))
    



class TestQMathPy:
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_acos(self, x):
        assert float(qm.acos(x)) == pytest.approx(math.acos(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=1))
    def test_acosh(self, x):
        assert float(qm.acosh(x)) == pytest.approx(math.acosh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_asin(self, x):
        assert float(qm.asin(x)) == pytest.approx(math.asin(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_asinh(self, x):
        assert float(qm.asinh(x)) == pytest.approx(math.asinh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_atan(self, x):
        assert float(qm.atan(x)) == pytest.approx(math.atan(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=-1,max_value=1))
    def test_atanh(self, x):
        assert float(qm.atanh(x)) == pytest.approx(math.atanh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    def test_atan2(self, x, y):
        assert float(qm.atan2(x,y)) == pytest.approx(math.atan2(x,y))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_cbrt(self, x):
        assert float(qm.cbrt(x)) == pytest.approx(math.cbrt(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_ceil(self, x):
        assert float(qm.ceil(x)) == pytest.approx(math.ceil(x))
    
    @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    def test_copysign(self, x, y):
        assert float(qm.copysign(x,y)) == pytest.approx(math.copysign(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_cosh(self, x):
    #     assert float(qm.cosh(x)) == pytest.approx(math.cosh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_cos(self, x):
        assert float(qm.cos(x)) == pytest.approx(math.cos(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_erf(self, x):
        assert float(qm.erf(x)) == pytest.approx(math.erf(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_erfc(self, x):
        assert float(qm.erfc(x)) == pytest.approx(math.erfc(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_exp2(self, x):
    #     assert float(qm.exp2(x)) == pytest.approx(math.exp2(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_exp(self, x):
    #     assert float(qm.exp(x)) == pytest.approx(math.exp(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_expm1(self, x):
    #     assert float(qm.expm1(x)) == pytest.approx(math.expm1(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_fabs(self, x):
        assert float(qm.fabs(x)) == pytest.approx(math.fabs(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_fdim(self, x, y):
    #     assert float(qm.fdim(x,y)) == pytest.approx(math.fdim(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_finite(self, x):
    #     assert float(qm.finite(x)) == pytest.approx(math.finite(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_floor(self, x):
        assert float(qm.floor(x)) == pytest.approx(math.floor(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_fma(self, x, y):
    #     assert float(qm.fma(x,y)) == pytest.approx(math.fma(x,y))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_fmax(self, x, y):
    #     assert float(qm.fmax(x,y)) == pytest.approx(math.fmax(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_fmin(self, x, y):
    #     assert float(qm.fmin(x,y)) == pytest.approx(math.fmin(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_fmod(self, x, y):
    #     assert float(qm.fmod(x,y)) == pytest.approx(math.fmod(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_frexp(self, x):
    #     assert float(qm.frexp(x)) == pytest.approx(math.frexp(x))
    
    @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    def test_hypot(self, x, y):
        assert float(qm.hypot(x,y)) == pytest.approx(math.hypot(x,y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_ilogb(self, x):
    #     assert float(qm.ilogb(x)) == pytest.approx(math.ilogb(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_isinf(self, x):
        assert float(qm.isinf(x)) == pytest.approx(math.isinf(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_isnan(self, x):
        assert float(qm.isnan(x)) == pytest.approx(math.isnan(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_issignaling(self, x):
    #     assert float(qm.issignaling(x)) == pytest.approx(math.issignaling(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_j0(self, x):
    #     assert float(qm.j0(x)) == pytest.approx(math.j0(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_j1(self, x):
    #     assert float(qm.j1(x)) == pytest.approx(math.j1(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_jn(self, x):
    #     assert float(qm.jn(x)) == pytest.approx(math.jn(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_ldexp(self, x):
    #     assert float(qm.ldexp(x)) == pytest.approx(math.ldexp(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_lgamma(self, x):
    #     assert float(qm.lgamma(x)) == pytest.approx(math.lgamma(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_llrint(self, x):
    #     assert float(qm.llrint(x)) == pytest.approx(math.llrint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_llround(self, x):
    #     assert float(qm.llround(x)) == pytest.approx(math.llround(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_logb(self, x):
    #     assert float(qm.logb(x)) == pytest.approx(math.logb(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log(self, x):
        assert float(qm.log(x)) == pytest.approx(math.log(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log10(self, x):
        assert float(qm.log10(x)) == pytest.approx(math.log10(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log1p(self, x):
        assert float(qm.log1p(x)) == pytest.approx(math.log1p(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_log2(self, x):
        assert float(qm.log2(x)) == pytest.approx(math.log2(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_lrint(self, x):
    #     assert float(qm.lrint(x)) == pytest.approx(math.lrint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_lround(self, x):
    #     assert float(qm.lround(x)) == pytest.approx(math.lround(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_modf(self, x):
    #     assert float(qm.modf(x)) == pytest.approx(math.modf(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_nan(self, x):
    #     assert float(qm.nan(x)) == pytest.approx(math.nan(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_nearbyint(self, x):
    #     assert float(qm.nearbyint(x)) == pytest.approx(math.nearbyint(x))
    
    @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    def test_nextafter(self, x, y):
        assert float(qm.nextafter(x,y)) == pytest.approx(math.nextafter(x, y))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_pow(self, x, y):
    #     assert float(qm.pow(x,y)) == pytest.approx(math.pow(x,y))
    
    # @given(floats(allow_infinity=False,allow_nan=False),floats(allow_infinity=False,allow_nan=False))
    # def test_remainder(self, x, y):
    #     assert float(qm.remainder(x,y)) == pytest.approx(math.remainder(x,y))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_remquo(self, x):
    #     assert float(qm.remquo(x)) == pytest.approx(math.remquo(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_rint(self, x):
    #     assert float(qm.rint(x)) == pytest.approx(math.rint(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_round(self, x):
    #     assert float(qm.round(x)) == pytest.approx(math.round(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_scalbln(self, x):
    #     assert float(qm.scalbln(x)) == pytest.approx(math.scalbln(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_scalbn(self, x):
    #     assert float(qm.scalbn(x)) == pytest.approx(math.scalbn(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_signbit(self, x):
    #     assert float(qm.signbit(x)) == pytest.approx(math.signbit(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_sincos(self, x):
    #     assert float(qm.sincos(x)) == pytest.approx(math.sincos(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_sinh(self, x):
    #     assert float(qm.sinh(x)) == pytest.approx(math.sinh(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_sin(self, x):
        assert float(qm.sin(x)) == pytest.approx(math.sin(x))
    
    @given(floats(allow_infinity=False,allow_nan=False,min_value=0,exclude_min=True))
    def test_sqrt(self, x):
        assert float(qm.sqrt(x)) == pytest.approx(math.sqrt(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_tan(self, x):
        assert float(qm.tan(x)) == pytest.approx(math.tan(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_tanh(self, x):
        assert float(qm.tanh(x)) == pytest.approx(math.tanh(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_tgamma(self, x):
    #     assert float(qm.tgamma(x)) == pytest.approx(math.tgamma(x))
    
    @given(floats(allow_infinity=False,allow_nan=False))
    def test_trunc(self, x):
        assert float(qm.trunc(x)) == pytest.approx(math.trunc(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_y0(self, x):
    #     assert float(qm.y0(x)) == pytest.approx(math.y0(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_y1(self, x):
    #     assert float(qm.y1(x)) == pytest.approx(math.y1(x))
    
    # @given(floats(allow_infinity=False,allow_nan=False))
    # def test_yn(self, x):
    #     assert float(qm.yn(x)) == pytest.approx(math.yn(x))
    

