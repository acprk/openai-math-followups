import sys, numpy as np
from scipy.optimize import linprog
from profile_lp import build
def minD(N, B, **kw):
    A,b,lb,ub,n=build(B, 50.0, **kw)   # upper bound effectively off
    idx={}; k=0
    for a in range(1,B+1):
        for bb in range(a,B+1):
            idx[(a,bb)]=k; k+=1
    c=np.zeros(n); c[idx[(N,N)]]=1.0
    res=linprog(c,A_ub=A,b_ub=b,bounds=list(zip(lb,ub)),method="highs")
    return res.fun
mode=sys.argv[1]
prev=None
for N in [int(x) for x in sys.argv[2:]]:
    B=4*N
    kw=dict(chains=("tri_equal",)) if mode=="paper" else dict(chains=("tri_all",), extra5=(mode=="all5"))
    D=minD(N,B,**kw)
    print(mode, N, "minD=%.4f"%D, "D/N^(4/3)=%.4f"%(D/N**(4/3)), "log_N D=%.4f"%(np.log(D)/np.log(N))); sys.stdout.flush()
