# Does the Voronoi partition of CP^2 by the 9 Hesse SIC lines give a Borsuk cover?
# Class i = {u : |<u,c_i>| maximal}. Cover valid iff no class contains two orthogonal unit vectors.
# We minimize |<u,v>| over pairs u,v in the same class (numerical search).
import numpy as np, itertools
rng=np.random.default_rng(1)
w=np.exp(2j*np.pi/3)
base=np.array([0,1,-1],dtype=complex)/np.sqrt(2)
C=[]
for a in range(3):
    for b in range(3):
        v=np.array([base[(k-a)%3]*w**(b*k) for k in range(3)])  # Weyl-Heisenberg orbit
        C.append(v)
C=np.array(C)
G=np.abs(C.conj()@C.T)**2
print("SIC overlaps |<ci,cj>|^2 (offdiag set):", sorted(set(np.round(G[~np.eye(9,dtype=bool)],6))))
def cls(U): return np.argmax(np.abs(U.conj()@C.T),axis=1)
N=200000
U=rng.normal(size=(N,3))+1j*rng.normal(size=(N,3)); U/=np.linalg.norm(U,axis=1,keepdims=True)
L=cls(U)
best=[]
for i in range(9):
    S=U[L==i][:4000]
    M=np.abs(S.conj()@S.T)
    best.append(M.min())
print("min |<u,v>| within each class (sampled):", np.round(best,4))
# local optimization: for each class, gradient-free search for orthogonal pair inside the class
def penalty(x):
    u=x[:3]+1j*x[3:6]; v=x[6:9]+1j*x[9:12]
    u/=np.linalg.norm(u); v/=np.linalg.norm(v)
    return u,v
worst=1
for trial in range(3000):
    i=rng.integers(9)
    # start: pick an orthogonal pair near class i boundary: u in class i, v orthogonal to u, project v toward c_i
    u=U[L==i][rng.integers((L==i).sum())]
    # search v ⟂ u maximizing |<v,c_i>| - max_{j!=i}|<v,c_j>|
    Bperp=np.linalg.svd(u.conj()[None,:])[2][1:].conj()  # basis of u^perp (2 x 3)
    bestv=None;bestm=-9
    for th in np.linspace(0,np.pi,60):
        for ph in np.linspace(0,2*np.pi,60):
            v=np.cos(th)*Bperp[0]+np.sin(th)*np.exp(1j*ph)*Bperp[1]
            s=np.abs(C.conj()@v)
            m=s[i]-np.max(np.delete(s,i))
            if m>bestm: bestm,bestv=m,v
    if bestm>=0:
        print("FOUND orthogonal pair in class",i,"margin",bestm); break
    worst=min(worst,-bestm)
else:
    print("no orthogonal pair found inside any class; smallest deficit",worst)
