from collections import defaultdict
from logging import root
from platform import node

from sesion2_pruebas import heapdefinitivofrom collections import defaultdict
class IndexedPriorityQueueibrahim:
    def __init__(self,comp):
        self.comp=comp;
        self.size=0;
        self.values=defaultdict();
        self.pm=defaultdict(int);
        self.im=defaultdict();
        
    def insert(self,ki,value):
        self.values[ki]=value;
        self.pm[ki]=self.size;
        self.im[self.size]=ki;
        
        self.size+=1;
        if self.size<=1:
            return;
        i=self.size-1;
        parent=(i-1)//2;
        self.swim(i,parent);
    
    def __compa(self,i,j):
        return (self.comp(self.values[self.im[i]],
            self.values[self.im[j]]));
    def contains(self,ki):
        return self.pm.get(ki,-1)!=-1;
    def peekMinKeyIndex(self):
        return self.im[0];
    def pollMinKeyIndex(self):
        minki=self.peekMinKeyIndex();
        return  self.remove(minki);
    def swim(self,i,parent):
        while parent>=0 and self.__compa(i,parent):
            self.__swap(i,parent);
            if parent==0:
                return;
            i=parent;
            parent=(i-1)//2;
    def __swap(self,i,j):
        self.pm[self.im[i]]=j;
        self.pm[self.im[j]]=i;
        self.im[i],self.im[j]=self.im[j],self.im[i];
    
    def __sink(self,i):
        while (i<(self.size-1)//2):
            left=i*2+1;
            right=i*2+2;
            if self.__compa(left,i) or self.__compa(right,i):
                if self.__compa(right,left):
                    self.__swap(right,i);
                    i=right;
                else:
                    self.__swap(left,i);
                    i=left;
            else: break;
        
    def remove(self,ki):
        if self.size==0:
            return None;
        i=self.pm[ki];
        removeElement=self.values[ki];
        self.__swap(i,self.size-1);
        self.size-=1;
        self.__sink(i);
        parent=(i-1)//2;
        self.swim(i,parent);
        self.values[ki]=-1;
        self.pm[ki]=-1;
        self.im[self.size]=-1;
        return removeElement;
    
    def update(self,ki,value):
        i=self.pm[ki];
        self.values[ki]=value;
        self.__sink(i);
        parent=(i-1)//2;
        self.swim(i,parent);
    
    #
    def decreaseKey(self,key,value):
        if self.comp(value,self.values[key]):
            self.values[key]=value;
            parent=(self.pm[key]-1)//2;
            self.swim(self.pm[key],parent);
class HeapDefinitivo:
    def __init__(self,comp):
        self.hp=[];
        self.comp=comp;
        self.size=0;
        
    def add(self,element):
        self.hp.append(element);
        self.size+=1;
        if self.size<=1:
            return;
        i=self.size-1;
        parent=(i-1)//2;
        while self.comp(self.hp[i],self.hp[parent]):
            self.hp[parent],self.hp[i]=self.hp[i],self.hp[parent];
            if parent==0:
                break;
            i=parent;
            parent=(i-1)//2;
    def pop(self):
        if self.size==0:
            return None;
        removeElement=self.hp[0];
        self.hp[0]=self.hp[-1];
        self.hp.pop();
        self.size-=1;
        i=0;
        while (i<(self.size-1)//2):
            left=i*2+1;
            right=i*2+2;
            if (self.comp(self.hp[left],self.hp[i])\
                or self.comp(self.hp[right],self.hp[i])):
                if self.comp(self.hp[right],self.hp[left]):
                    self.hp[right],self.hp[i]=self.hp[i],self.hp[right];
                    i=right;
                else:
                    self.hp[left],self.hp[i]=self.hp[i],self.hp[left];
                    i=left;
            else: break;
        return removeElement;
    def Size(self):
        return self.size;
    
    def __str__(self):
        return str(self.hp);
    
    def top(self):
        return self.hp[0];
def prim(graph):
    n=len(graph);
    inMST=[False]*n;
    prev=[None]*n;
    MST=[];
    dist=[float('inf')]*n;
    dist[0]=0;
    #priority queue;
    pq=HeapDefinitivo(lambda a,b: a[0] <b[0]);
    pq.add((0,0));
    
    while pq.size:
        cost,node =pq.pop();
        if not inMST[node]:
            inMST[node]=True;
            if prev[node]!=None:
                MST.append((cost,prev[node],node));
            for neighbour, w in graph[node]:
                if not inMST[neighbour]:
                    if w <dist[neighbour]:
                        dist[neighbour]=w;
                        prev[neighbour]=node;
                        pq.add((dist[neighbour],neighbour));
    return MST;

class djset:
    def __init__(self,n):
        self.root=[i for i in range(n)];
        self.rank=[1]*n;
    
    def find(self,x):
        if x==self.root[x]:
            return x;
        self.root[x]=self.find(self.root[x]);
        return self.root[x];
    
    def unionset(self,x,y):
        rootX=self.find(x);
        rootY=self.find(y);
        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.root[rootY]=rootX;
            elif self.rank[rootX]<self.rank[rootY]:
                self.root[rootX]=rootY;
            else: 
                self.root[rootX]=rootY;
                self.rank[rootY]+=1;
    
    def connected(self,x,y):
        return self.find(x)==self.find(y);
    
def kruskal(graph):
    n=len(graph);
    dist=[float('inf')]*n;
    prev=[None]*n;
    MST=[];
    ds=djset(n);
    pq=HeapDefinitivo(lambda a,b: a[0]<b[0]);
    for i in range(n):
        for neighbour,weight in graph[i]:
            pq.add((weight,i,neighbour));
    
    while pq.size:
        cost,at,vecino=pq.pop();
        
        if not ds.connected(at,vecino):
            ds.unionset(at,vecino);
            prev[vecino]=at;
            MST.append((cost,at,vecino));
    return MST;
def practicemst():
    n=5;
    graph=[[] for _ in range(n)];
    graph[0].append((1,9));
    graph[1].append((0,9));
    graph[0].append((2,75));
    graph[2].append((0,75));
    graph[1].append((2,95));
    graph[2].append((1,95));
    graph[1].append((3,19));
    graph[3].append((1,19));
    graph[3].append((2,51));
    graph[2].append((3,51));
    graph[1].append((4,42));
    graph[4].append((1,42));
    graph[4].append((3,31));
    graph[3].append((4,31));
    
    mst=kruskal(graph);
    primMST=prim(graph);
    print(mst);
    print(primMST);

def main():
    practicemst();

if __name__=="__main__":
    main();
        
            
