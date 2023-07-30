from .constant import *
import qmathc as _qmathc


def acosq(x):
    return _qmathc._acos(x)


def acoshq(x):
    return _qmathc._acosh(x)


def asinq(x):
    return _qmathc._asin(x)


def asinhq(x):
    return _qmathc._asinh(x)


def atanq(x):
    return _qmathc._atan(x)


def atanhq(x):
    return _qmathc._atanh(x)


def atan2q(x, y):
    return _qmathc._atan2(x, y)


def cbrtq(x):
    return _qmathc._cbrt(x)


def ceilq(x):
    return _qmathc._ceil(x)


def copysignq(x, y):
    return _qmathc._copysign(x, y)


def coshq(x):
    return _qmathc._cosh(x)


def cosq(x):
    return _qmathc._cos(x)


def erfq(x):
    return _qmathc._erf(x)


def erfcq(x):
    return _qmathc._erfc(x)


def exp2q(x):
    return _qmathc._exp2(x)


def expq(x):
    return _qmathc._exp(x)


def expm1q(x):
    return _qmathc._expm1(x)


def fdimq(x, y):
    return _qmathc._fdim(x, y)


def fabsq(x):
    return _qmathc._fabs(x)


def finiteq(x):
    return _qmathc._finite(x)


def floorq(x):
    return _qmathc._floor(x)


def fmaq(x, y, z):
    return _qmathc._fma(x, y, z)


def fmaxq(x, y):
    return _qmathc._fmax(x, y)


def fminq(x, y):
    return _qmathc._fmin(x, y)


def fmodq(x, y):
    return _qmathc._fmod(x, y)


def frexpq(x):
    return _qmathc._frexp(x)


def hypotq(x, y):
    return _qmathc._hypot(x, y)


def ilogbq(x):
    return _qmathc._ilogb(x)


def isinfq(x):
    return _qmathc._isinf(x)


def isnanq(x):
    return _qmathc._isnan(x)


def issignalingq(x):
    return _qmathc._issignaling(x)


def j0q(x):
    return _qmathc._j0(x)


def j1q(x):
    return _qmathc._j1(x)


def jnq(n, x):
    return _qmathc._jn(n, x)


def ldexpq(x, i):
    return _qmathc._ldexp(x, i)


def lgammaq(x):
    return _qmathc._lgamma(x)


def llrintq(x):
    return _qmathc._llrint(x)


def llroundq(x):
    return _qmathc._llround(x)


def logbq(x):
    return _qmathc._logb(x)


def logq(x):
    return _qmathc._log(x)


def log10q(x):
    return _qmathc._log10(x)


def log1p(x):
    return _qmathc._log1p(x)


def log1pq(x):
    return _qmathc._log1p(x)


def log2q(x):
    return _qmathc._log2(x)


def lrintq(x):
    return _qmathc._lrint(x)


def lroundq(x):
    return _qmathc._lround(x)


def modfq(x):
    return _qmathc._modf(x)


def nanq(x=None):
    return qfloat("nan")


def nearbyintq(x):
    return _qmathc._nearbyint(x)


def nextafterq(x, y):
    return _qmathc._nextafter(x, y)


def powq(x, y):
    return _qmathc._pow(x, y)


def remainderq(x, y):
    return _qmathc._remainder(x, y)


def remquoq(x, y):
    return _qmathc._remquo(x, y)


def rintq(x):
    return _qmathc._rint(x)


def roundq(x):
    return _qmathc._round(x)


def scalbnq(x, n):
    return _qmathc._scalbn(x, n)


def scalblnq(x, n):
    return _qmathc._scalbln(x, n)


def signbitq(x):
    return _qmathc._signbit(x)


def sincosq(x):
    return _qmathc._sincos(x)


def sinh(x):
    return _qmathc._sinh(x)


def sinhq(x):
    return _qmathc._sinh(x)


def sinq(x):
    return _qmathc._sin(x)


def sqrtq(x):
    return _qmathc._sqrt(x)


def tanq(x):
    return _qmathc._tan(x)


def tanh(x):
    return _qmathc._tanh(x)


def tanhq(x):
    return _qmathc._tanh(x)


def tgammaq(x):
    return _qmathc._tgamma(x)


def trunc(x):
    return _qmathc._trunc(x)


def truncq(x):
    return _qmathc._trunc(x)


def y0q(x):
    return _qmathc._y0(x)


def y1q(x):
    return _qmathc._y1(x)


def ynq(n, x):
    return _qmathc._yn(n, x)


#################################
# Python math library functions #
#################################


def acos(x):
    res = _qmathc._acos(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def acosh(x):
    res = _qmathc._acosh(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def asin(x):
    res = _qmathc._asin(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def asinh(x):
    res = _qmathc._asinh(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def atan(x):
    res = _qmathc._atan(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def atanh(x):
    res = _qmathc._atanh(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def atan2(x, y):
    res = _qmathc._atan2(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def cbrt(x):
    res = _qmathc._cbrt(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def ceil(x):
    res = _qmathc._ceil(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def copysign(x, y):
    res = _qmathc._copysign(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def cosh(x):
    res = _qmathc._cosh(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def cos(x):
    res = _qmathc._cos(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def erf(x):
    res = _qmathc._erf(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def erfc(x):
    res = _qmathc._erfc(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def exp2(x):
    res = _qmathc._exp2(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def exp(x):
    res = _qmathc._exp(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def expm1(x):
    res = _qmathc._expm1(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def fabs(x):
    res = _qmathc._fabs(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def fdim(x):
    res = _qmathc._fdim(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def finite(x):
    res = _qmathc._finite(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def floor(x):
    res = _qmathc._floor(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def fma(x):
    res = _qmathc._fma(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def fmax(x):
    res = _qmathc._fmax(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def fmin(x):
    res = _qmathc._fmin(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def fmod(x, y):
    res = _qmathc._fmod(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def frexp(x):
    res = _qmathc._frexp(x)
    if not _qmathc._finite(res[0]):
        raise ValueError("math domain error")
    return res


def hypot(*iterable):
    # Naive way of doing things
    sum = qfloat(0)
    for i in iterable:
        sum += qfloat(i) ** 2

    res = _qmathc._sqrt(sum)

    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def ilogb(x):
    res = _qmathc._ilogb(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def isinf(x):
    res = _qmathc._isinf(x)
    return res


def isnan(x):
    res = _qmathc._isnan(x)
    return res


def issignaling(x):
    res = _qmathc._issignaling(x)
    return res


def j0(x):
    res = _qmathc._j0(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def j1(x):
    res = _qmathc._j1(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def jn(x):
    res = _qmathc._jn(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def ldexp(x, y):
    res = _qmathc._ldexp(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def lgamma(x):
    res = _qmathc._lgamma(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def llrint(x):
    res = _qmathc._llrint(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def llround(x):
    res = _qmathc._llround(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def logb(x):
    res = _qmathc._logb(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def log(x, base=None):
    res = _qmathc._log(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")

    if base is not None:
        res = res / _qmathc._log(base)

    if not _qmathc._finite(res):
        raise ValueError("math domain error")

    return res


def log10(x):
    res = _qmathc._log10(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def log1p(x):
    res = _qmathc._log1p(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def log2(x):
    res = _qmathc._log2(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def lrint(x):
    res = _qmathc._lrint(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def lround(x):
    res = _qmathc._lround(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def modf(x):
    res = _qmathc._modf(x)
    if not _qmathc._finite(res[0]):
        raise ValueError("math domain error")
    return res


def nan(x):
    res = _qmathc._nan(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def nearbyint(x):
    res = _qmathc._nearbyint(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def nextafter(x, y):
    res = _qmathc._nextafter(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def pow(x, y):
    res = _qmathc._pow(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def remainder(x, y):
    res = _qmathc._remainder(x, y)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def remquo(x):
    res = _qmathc._remquo(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def rint(x):
    res = _qmathc._rint(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def round(x):
    res = _qmathc._round(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def scalbln(x):
    res = _qmathc._scalbln(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def scalbn(x):
    res = _qmathc._scalbn(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def signbit(x):
    res = _qmathc._signbit(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def sincos(x):
    res = _qmathc._sincos(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def sinh(x):
    res = _qmathc._sinh(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def sin(x):
    res = _qmathc._sin(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def sqrt(x):
    res = _qmathc._sqrt(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def tan(x):
    res = _qmathc._tan(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def tanh(x):
    res = _qmathc._tanh(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def tgamma(x):
    res = _qmathc._tgamma(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def trunc(x):
    res = _qmathc._trunc(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def y0(x):
    res = _qmathc._y0(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def y1(x):
    res = _qmathc._y1(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def yn(x):
    res = _qmathc._yn(x)
    if not _qmathc._finite(res):
        raise ValueError("math domain error")
    return res


def comb(n, k):
    raise NotImplementedError


def factorial(n):
    raise NotImplementedError


def fsum(iterable):
    raise NotImplementedError


def gcd(integers):
    raise NotImplementedError


def isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0):
    raise NotImplementedError


def isfinite(x):
    raise NotImplementedError


def isqrt(n):
    raise NotImplementedError


def lcm(integers):
    raise NotImplementedError


def perm(iterable, *, start=1):
    raise NotImplementedError


def prod(iterable, *, start=1):
    raise NotImplementedError


def ulp(x):
    raise NotImplementedError


def dist(p, q):
    raise NotImplementedError


def degrees(x):
    raise NotImplementedError


def radians(x):
    raise NotImplementedError
