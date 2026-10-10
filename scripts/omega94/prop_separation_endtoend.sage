# Independent end-to-end check of the separation degeneration (Prop. 3 of the note)
# over F_{p^k}: build sum_r (substituted copy r) with eps-weights as a polynomial in eps,
# and verify (a) no negative eps-degree, (b) eps^0 coefficient == D (the target direct sum).
import itertools, random, sys
def run(p, M, dX=2, dY=1, dZ=1, seed=1):
    random.seed(seed)
    L = 5*M if (5*M) % p else 5*M+1
    k = 1
    while (p**k - 1) % L: k += 1
    F = GF(p**k, 'g'); g = F.multiplicative_generator(); zeta = g**((p**k-1)//L)
    R.<e> = LaurentPolynomialRing(F)
    hs = range(1, M+1)
    # random source tensor A = sum_h A_h, A_h in X (dX) x Y_h (dY) x Z_h (dZ)
    c = {(h,a,b,cc): F.random_element() for h in hs for a in range(dX) for b in range(dY) for cc in range(dZ)}
    # target coefficient T[(a,gg),(h,b,u),(h,cc,v)] = sum_r of substituted products with weights
    T = {}
    invL = F(L)**-1
    for (h,a,b,cc), coef in c.items():
        if coef == 0: continue
        for gg in hs:
            for u in hs:
                for v in hs:
                    s = sum(zeta**(r*(2*gg + (u-h) + (-v-h))) for r in range(L)) * invL
                    if s == 0: continue
                    w = gg**2 + (h*u - h**2) + (-h*v)
                    key = ((a,gg),(h,b,u),(h,cc,v))
                    T[key] = T.get(key, R(0)) + coef*s*e**w
    neg = sum(1 for val in T.values() if val != 0 and val.valuation() < 0)
    low = {key: val.constant_coefficient() for key, val in T.items() if val != 0 and val.valuation() == 0}
    low = {k_: v_ for k_, v_ in low.items() if v_ != 0}
    D = {}
    for (h,a,b,cc), coef in c.items():
        if coef == 0: continue
        for u in hs:
            D[((a,h),(h,b,u),(h,cc,u))] = coef
    return dict(p=p, M=M, L=L, field=p**k, neg_weight=neg, lowest_equals_D=(low == D), terms=len(D))
cases = [(2,2),(2,3),(3,2),(3,3),(5,1),(5,2),(5,3),(5,4),(7,2),(11,3),(2,4),(3,5)]
for (p,M) in cases:
    print(run(p,M)); sys.stdout.flush()
# negative control: force L = 5M when p | 5M is impossible (no primitive root); instead use a
# too-small period L = 3(M-1) to show the no-wrap condition is necessary.
def run_small_L(p, M):
    L = 3*(M-1)
    if L % p == 0: return None
    k = 1
    while (p**k - 1) % L: k += 1
    F = GF(p**k,'g'); zeta = F.multiplicative_generator()**((p**k-1)//L)
    hs = range(1, M+1); bad = 0
    for h in hs:
        for gg in hs:
            for u in hs:
                for v in hs:
                    ex = 2*gg+(u-h)+(-v-h)
                    s = sum(zeta**(r*ex) for r in range(L))*F(L)**-1
                    if (s != 0) != (ex == 0): bad += 1
    return dict(p=p, M=M, L=L, filter_errors=bad)
print("control (L too small):", run_small_L(7,4), run_small_L(5,3))
