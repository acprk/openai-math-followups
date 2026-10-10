# Voronoi covers of RP^3 (lines in R^4) by K centre lines. Cell i is valid iff it contains no
# orthogonal pair. For each cell compute worst = max over orthogonal (u,v) of min(margin_i(u),margin_i(v)),
# margin_i(x)=|<x,c_i>| - max_{j!=i}|<x,c_j>|. Cover valid iff worst<0 for every cell.
import numpy as np, sys
from scipy.optimize import minimize
rng=np.random.default_rng(int(sys.argv[2]) if len(sys.argv)>2 else 0)
def margins(X,C):
    s=np.abs(X@C.T); idx=np.argsort(-s,axis=1); return s,idx
def cell_worst(C,i,starts=400):
    best=-9
    def f(z):
        u=z[:4]; u=u/np.linalg.norm(u)
        w=z[4:]; v=w-(w@u)*u; v=v/np.linalg.norm(v)
        su=np.abs(C@u); sv=np.abs(C@v)
        mu=su[i]-np.max(np.delete(su,i)); mv=sv[i]-np.max(np.delete(sv,i))
        return -min(mu,mv)
    for _ in range(starts):
        u=C[i]+0.6*rng.normal(size=4); w=rng.normal(size=4)
        r=minimize(f,np.r_[u,w],method='Nelder-Mead',options={'maxiter':800,'xatol':1e-9,'fatol':1e-12})
        best=max(best,-r.fun)
    return best
def d4_lines():
    L=[]
    import itertools
    for i,j in itertools.combinations(range(4),2):
        for s in (1,-1):
            v=np.zeros(4); v[i]=1; v[j]=s; L.append(v/np.sqrt(2))
    return np.array(L)            # 12 lines (24-cell roots mod sign)
def optimized(K,iters=4000):
    # spread K lines: minimize max |<ci,cj>| (Grassmannian packing) by repulsion
    C=rng.normal(size=(K,4)); C/=np.linalg.norm(C,axis=1,keepdims=True)
    for t in range(iters):
        G=C@C.T; np.fill_diagonal(G,0)
        F=-(np.sign(G)*np.abs(G)**7)@C
        C=C+0.02*F; C/=np.linalg.norm(C,axis=1,keepdims=True)
    return C
mode=sys.argv[1]
if mode=="d4": C=d4_lines()
else: C=optimized(int(mode))
G=np.abs(C@C.T); np.fill_diagonal(G,0)
print("K=",len(C),"max coherence",G.max().round(4))
ws=[cell_worst(C,i,starts=150) for i in range(len(C))]
print("cell worst margins:",np.round(ws,4))
print("VALID COVER" if max(ws)<0 else "INVALID (some cell has orthogonal pair)", "max=",round(max(ws),4))
