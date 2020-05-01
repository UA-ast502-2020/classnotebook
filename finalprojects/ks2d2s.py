import numpy as np
from scipy import stats

def ks2d2s(x1, y1, x2, y2):
    assert (len(x1) == len(y1)) & (len(x2) == len(y2))
    n1 = len(x1)
    n2 = len(x2)
    d1 = maxdist(x1, y1, x2, y2)
    d2 = maxdist(x2, y2, x1, y1)
    d = np.mean([d1, d2])
    sqen = np.sqrt(n1 * n2 / (n1+n2))
    r1 = stats.pearsonr(x1, y1)[0]
    r2 = stats.pearsonr(x2, y2)[0]
    rr =  np.sqrt(1 - 0.5 * (r1 * r1 + r2  *r2))
    p = stats.kstwobign.sf(d * sqen / (1 + rr * (0.25 - 0.75/sqen)))
    return p


def quadct(x, y, xx, yy):
    nn  = len(xx)
    yyg = (yy > y)
    xxg = (xx > x)
    na = np.sum(yyg & xxg)
    nb = np.sum(yyg & ~xxg)
    nc = np.sum(~yyg & ~xxg)
    nd = np.sum(~yyg & xxg)

    ff = 1 / nn
    fa = na * ff
    fb = nb * ff
    fc = nc * ff
    fd = nd * ff
    return fa, fb, fc, fd


def maxdist(x1, y1, x2, y2):
    n1 = len(x1)

    d1 = np.zeros((n1,4))
    n1_inv = 1 / n1
    for i in range(n1):
        fa, fb, fc, fd = quadct(x1[i], y1[i], x1, y1)
        ga, gb, gc, gd = quadct(x1[i], y1[i], x2, y2)
        if fa > ga:
            fa += n1_inv
        if fb > gb:
            fb += n1_inv
        if fc > gc:
            fc += n1_inv
        if fd > gd:
            fd += n1_inv
        d1[i] = [fa - ga, fb - gb, fc - gc, fd - gd]
    dmin, dmax = np.min(d1), np.max(d1)
    return np.max([dmin, dmax])


# def quadct(x, y, xx, yy):
#     assert len(xx) == len(yy)
#     nn = len(xx)
#     na = nb = nc = nd = 0
#
#     for i in range(nn):
#         if (yy[i] == y) & (xx[i] ==x):
#             continue
#         if yy[i] > y:
#             if xx[i] > x:
#                 na += 1
#             else:
#                 nb += 1
#         else:
#             if xx[k] > x:
#                 nd += 1
#             else:
#                 nc += 1
#
#     ff = 1 / nn
#     fa = ff * na
#     fb = ff * nb
#     fc = ff * nc
#     fd = ff * nd
#
#     return fa, fb, fc, fd
