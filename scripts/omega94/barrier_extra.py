from fractions import Fraction as Fr
import itertools
B=160
phi=[None,Fr(1)]
for a in range(2,10*B): phi.append(phi[-1]*(1+Fr(1,3*(a-1))))
def P(a,b):
    lo,hi=min(a,b),max(a,b); return phi[lo]*(hi+Fr(lo-1,2))
viol={'chain3':0,'chain5':0,'kron':0}; ex=[]
for a in range(1,25):
    for h1 in range(1,40):
        for h2 in range(1,40):
            for h3 in range(1,40):
                L=h1+h2+h3+a-1
                if P(a,L) < P(a,h1)+P(a,h2)+P(a,h3): viol['chain3']+=1; ex.append(('c3',a,h1,h2,h3))
    for hs in itertools.product(range(1,12),repeat=5):
        L=sum(hs)+2*(a-1)
        if P(a,L) < sum(P(a,h) for h in hs): viol['chain5']+=1; ex.append(('c5',a,hs)); break
for a in range(1,12):
  for b in range(1,12):
    N=a+b-1
    for a2 in range(1,10):
      for b2 in range(1,10):
        A=a+(a2-1)*N; Bb=b+(b2-1)*N
        if P(a,b)*P(a2,b2) > P(A,Bb): viol['kron']+=1; ex.append(('kron',a,b,a2,b2,float(P(a,b)*P(a2,b2)),float(P(A,Bb))))
print(viol, ex[:6])
