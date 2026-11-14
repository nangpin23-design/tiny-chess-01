import json as j,os,sys,urllib.request as u
U=os.environ.get("MAKEFUN_ENV_URL")or sys.exit()
def P(p,b):
 r=u.Request(U+p,data=j.dumps(b).encode())
 try:
  with u.urlopen(r)as s:return j.load(s)
 except:sys.exit()
V=(0,100,320,330,500,900,0)
KN=(-33,-31,-18,-14,14,18,31,33);KI=(-17,-16,-15,-1,1,15,16,17)
D=(KN,(-17,-15,15,17),(-16,-1,1,16),KI,KI)
S='abcdefgh';N=0;M=200000
PA=[0,0,4,8,14,24,40,0]
CT=[min(f,7-f)+min(r,7-r)for r in range(8)for f in range(8)]
K={0:13,7:14,4:12,112:7,119:11,116:3}
def un(m):
 f=m&127;t=m>>7&127
 return f'{S[f&7]}{(f>>4)+1}{S[t&7]}{(t>>4)+1}'+(' qrbn'[m>>14]if m>>14 else'')
def pa(f):
 p=f.split();b=[0]*130;q=112;s=0
 for r in p[0].split('/'):
  x=0
  for c in r:
   if c.isdigit():x+=int(c)
   else:v=('PNBRQK'.index(c.upper())+1)*(1 if c.isupper()else-1);b[q+x]=v;s+=ps(v,q+x);x+=1
  q-=16
 b[128]=('K'in p[2])+2*('Q'in p[2])+4*('k'in p[2])+8*('q'in p[2])
 b[129]=S.index(p[3][0])+(int(p[3][1])-1)*16 if p[3]!='-'else -1
 return b,p[1]=='w',s
def at(b,q,w):
 o=1 if w else-1
 for Y,Z in(((-15,-17)if w else(15,17),1),(KN,2),(KI,6)):
  for s in Y:
   t=q+s
   if not t&136 and b[t]==Z*o:return 1
 for Y,Z in(((-17,-15,15,17),(3,5)),((-16,-1,1,16),(4,5))):
  for d in Y:
   t=q+d
   while not t&136:
    c=b[t]
    if c:
     if abs(c)in Z and(c>0)==w:return 1
     break
    t+=d
 return 0
def ge(b,w):
 ms=[];qs=[];ep=b[129];cr=b[128]
 def ap(m,t,L):
  if(t>>4)==(7 if w else 0):
   for k in(1,2,3,4):ms.append(m|k<<14)
  else:L.append(m)
 for f in range(128):
  if f&136:continue
  c=b[f]
  if not c or(c>0)!=w:continue
  p=abs(c)
  if p==1:
   d=16 if w else-16
   for o,cp in((d,0),(d-1,1),(d+1,1)):
    t=f+o
    if t&136:continue
    v=b[t]
    if cp:
     if v and(v>0)!=w or t==ep:ap(f|t<<7,t,ms)
    elif not v:
     ap(f|t<<7,t,qs)
     if(f>>4)==(1 if w else 6)and not b[f+2*d]:qs.append(f|f+2*d<<7)
  else:
   for d in D[p-2]:
    t=f+d
    while not t&136:
     v=b[t]
     if v:
      if(v>0)!=w:ms.append(f|t<<7)
      break
     qs.append(f|t<<7)
     if p in(2,6):break
     t+=d
   if p==6 and f in(4,116):
    z=f-4;k=1 if f==4 else 4
    for B,E in((1,(5,6)),(2,(3,2,1))):
     if cr&B*k and all(not b[z+i]for i in E)and all(not at(b,z+i,not w)for i in(4,)+E):qs.append(f|z+E[1]<<7)
 return ms+qs
def ps(c,f):
 t=abs(c);u=c>0;r=f>>4 if u else 7-(f>>4);fl=f&7;ce=CT[r*8+fl]
 if t==1:v=100+PA[r]
 elif t==2:v=320+6*ce-20
 elif t==3:v=330+4*ce-8
 elif t==4:v=500
 elif t==5:v=900+2*ce-6
 else:v=10 if r==0 else max(-50,-15*r)
 return v if u else-v
def do(b,m,s):
 f=m&127;t=m>>7&127;c=b[f];b[f]=0;s-=ps(c,f)
 if abs(c)==1 and not b[t] and abs(t-f)in(15,17):
  e=t-16 if c>0 else t+16;s-=ps(b[e],e);b[e]=0
 v=b[t]
 if v:s-=ps(v,t)
 pc=m>>14
 n=(6-pc)*(1 if c>0 else-1)if pc else c
 b[t]=n;s+=ps(n,t)
 if abs(c)==6 and abs(t-f)==2:
  r=t+1 if t>f else t-2;rr=4 if c>0 else-4;z=t-1 if t>f else t+1;s+=ps(rr,z)-ps(rr,r);b[r]=0;b[z]=rr
 b[128]&=K.get(f,15)&K.get(t,15)
 b[129]=t if abs(c)==1 and abs(t-f)==32 else -1
 return s
def se(b,w,d,a,be,pl,s):
 global N;N+=1
 if N>M:raise ValueError
 q=d<=0;k=6 if w else-6
 if q:
  sp=s if w else-s
  if sp>=be:return be
  if sp>a:a=sp
  ck=at(b,b.index(k),not w)
  if pl>6 and not ck:return a
 else:ck=0
 n=0
 for m in ge(b,w):
  if q and not ck:
   v=b[m>>7&127]
   if not v and not m>>14:continue
   if v and sp+V[abs(v)]+200<a:continue
  b2=b[:];s2=do(b2,m,s)
  if at(b2,b2.index(k),not w):continue
  n+=1
  v=-se(b2,not w,d-1,-be,-a,pl+1,s2)
  if v>a:a=v
  if a>=be:return a
 if n==0:return -M+pl if at(b,b.index(k),not w)else a if q else 0
 return a
def rt(b,w,legal,s):
 ms=[m for m in ge(b,w)if un(m)in legal]
 if not ms:return None
 best=ms[0]
 global N;N=0
 for D in range(1,8):
  try:
   bv=-M
   for m in ms:
    b2=b[:];s2=do(b2,m,s);v=-se(b2,not w,D-1,-M,-bv,1,s2)
    if v>bv:bv=v;bb=m
   best=bb;ms.remove(bb);ms.insert(0,bb)
  except ValueError:break
 return best
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  b,w,s=pa(g['fen']);m=rt(b,w,set(g['legal_moves']),s)
  g=P('/move',{'game':g['game'],'move':un(m)if m else g['legal_moves'][0]})
