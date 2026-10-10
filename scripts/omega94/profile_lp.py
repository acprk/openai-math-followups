# Axiomatic LP for the symmetrized profile P(a,b) of OAI 9/4 paper.
# Feasible(s) <=> exists P on box [1..B]^2 satisfying:
#  P sym, P(1,b)=b, monotone, concave in each arg, chain inequalities,
#  and P(a,b) <= (a+b-1)^s.  Infeasible at s  =>  true 1/t > s  => omega < 3/s.
import sys, itertools, numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
def build(B, s, chains=("tri_equal",), extra5=False):
    idx = {}
    for a in range(1,B+1):
        for b in range(a,B+1):
            idx[(a,b)] = len(idx)
    def v(a,b): return idx[(min(a,b),max(a,b))]
    rows=[]; rhs=[]   # A x <= rhs
    def add(coefs, r):
        rows.append(coefs); rhs.append(r)
    n=len(idx)
    lb=np.zeros(n); ub=np.full(n,np.inf)
    for (a,b),i in idx.items():
        ub[i]=(a+b-1)**s
        if a==1: lb[i]=b; ub[i]=b
        else: lb[i]=1
    for a in range(1,B+1):
        for b in range(1,B):
            add({v(a,b):1.0, v(a,b+1):-1.0}, 0.0)           # monotone
        for b in range(2,B):
            add({v(a,b+1):1.0, v(a,b-1):1.0, v(a,b):-2.0}, 0.0)  # concave
    for a in range(1,B+1):
        for h1 in range(1,B):
            for h2 in range(1,B):
                if "tri_equal" in chains and h1!=h2: pass
                hs_list=[]
                if "tri_all" in chains:
                    for h3 in range(1,B):
                        if h1+h2+h3+a-1<=B: hs_list.append((h1,h2,h3))
                else:
                    if h1==h2 and 3*h1+a-1<=B: hs_list.append((h1,h1,h1))
                for (x,y,z) in hs_list:
                    c={}
                    for h in (x,y,z): c[v(a,h)]=c.get(v(a,h),0)-1.0
                    c[v(a,x+y+z+a-1)]=c.get(v(a,x+y+z+a-1),0)+1.0
                    add({k:-w for k,w in c.items()},0.0)   # -(P(big)-sum) <=0
        if extra5:
            for m in range(2,6):
                for h in range(1,B):
                    L=(2*m+1)*h+m*(a-1)
                    if L<=B:
                        c={v(a,h):float(2*m+1), v(a,L):-1.0}
                        add(c,0.0)
    r=[];c=[];d=[]
    for k,co in enumerate(rows):
        for j,w in co.items(): r.append(k);c.append(j);d.append(w)
    A=coo_matrix((d,(r,c)),shape=(len(rows),n)).tocsr()
    return A,np.array(rhs),lb,ub,n
def feasible(B,s,**kw):
    A,b,lb,ub,n=build(B,s,**kw)
    res=linprog(np.zeros(n),A_ub=A,b_ub=b,bounds=list(zip(lb,ub)),method="highs")
    return res.status==0
def crit(B,**kw):
    lo,hi=1.0,2.0
    for _ in range(30):
        mid=(lo+hi)/2
        if feasible(B,mid,**kw): hi=mid
        else: lo=mid
    return hi
if __name__=="__main__":
    mode=sys.argv[1]; Bs=[int(x) for x in sys.argv[2:]]
    for B in Bs:
        if mode=="paper": s=crit(B,chains=("tri_equal",))
        elif mode=="tri_all": s=crit(B,chains=("tri_all",))
        elif mode=="tri_all5": s=crit(B,chains=("tri_all",),extra5=True)
        print(mode,B,"s_crit=%.6f"%s,"omega_bound=%.6f"%(3/s)); sys.stdout.flush()
