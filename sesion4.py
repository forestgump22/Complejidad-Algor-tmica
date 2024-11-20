from collections import defaultdict
class IndexedPriorityQueue:
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
    
    #just use it when it is a MinIndexed PriorityQueue
    def decreaseKey(self,key,value):
        if self.comp(value,self.values[key]):
            self.values[key]=value;
            parent=(self.pm[key]-1)//2;
            self.swim(self.pm[key],parent);
            
def dijkstraIndexed(graph,start):
    n=len(graph);
    prev=[None]*n;
    visited=[False]*n;
    dist=[float('inf')]*n;
    dist[start]=0;
    ipq= IndexedPriorityQueue(lambda a,b: a<b);
    ipq.insert(start,0);
    
    while ipq.size:
        nodeid=ipq.peekMinKeyIndex();
        visited[nodeid]=True;
        minValue=ipq.pollMinKeyIndex();
        
        for to,w in graph[nodeid]:
            if not visited[to]:
                newDist=dist[nodeid]+w;
                if newDist <dist[to]:
                    prev[to]=nodeid;
                    dist[to]=newDist;
                    
                    if not ipq.contains(to):
                        ipq.insert(to,newDist);
                    else:
                        ipq.decreaseKey(to,newDist);
        #if nodeid==end: return dist[end];
    return dist,prev;

def practicedijkstrawithIndexedPQ():
    
    n=8;
    graph=[[] for _ in range(n)];
    graph[0].append((1,3));
    graph[0].append((2,5));
    graph[0].append((3,4));
    graph[1].append((0,3));
    graph[1].append((2,6));
    graph[1].append((5,2));
    graph[1].append((6,1));
    graph[2].append((0,5));
    graph[2].append((1,6));
    graph[2].append((4,5));
    graph[2].append((6,9));
    graph[3].append((0,4));
    graph[3].append((7,8));
    graph[4].append((2,5));
    graph[4].append((6,4));
    graph[5].append((1,2));
    graph[6].append((1,1));
    graph[6].append((2,9));
    graph[6].append((4,4));
    graph[7].append((3,8));
    graph[7].append((6,8));
    cost,path = dijkstraIndexed(graph,0);
    print(path)
    print(cost)


def prim(graph):
    n=len(graph);
    inMST=[False]*n;
    prev=[None]*n;
    MST=[];
    dist=[float('inf')]*n;
    dist[0]=0;
    #indexed priority queue;
    ipq=IndexedPriorityQueue(lambda a,b: a<b);
    ipq.insert(0,0);
    
    while ipq.size:
        node=ipq.peekMinKeyIndex();
        cost =ipq.pollMinKeyIndex();
        if not inMST[node]:
            inMST[node]=True;
            if prev[node]!=None:
                MST.append((cost,prev[node],node));
            for neighbour, w in graph[node]:
                if not inMST[neighbour]:
                    if w <dist[neighbour]:
                        dist[neighbour]=w;
                        prev[neighbour]=node;
                        if not ipq.contains(neighbour):
                            ipq.insert(neighbour,dist[neighbour]);
                        else: ipq.decreaseKey(neighbour,dist[neighbour]);
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
    ipq=IndexedPriorityQueue(lambda a,b: a[0]<b[0]);
    for i in range(n):
        for neighbour,weight in graph[i]:
            if not ipq.contains(neighbour):
                ipq.insert(neighbour,(weight,i,neighbour));
            else: 
                ipq.decreaseKey(neighbour,(weight,i,neighbour));
    
    while ipq.size:
        vecino=ipq.peekMinKeyIndex();
        cost,at,vecino=ipq.pollMinKeyIndex();
        
        if not ds.connected(at,vecino):
            ds.unionset(at,vecino);
            prev[vecino]=at;
            MST.append((cost,at,vecino));
    return MST;
def practicemst():
    n=8;
    graph=[[] for _ in range(n)];
    graph[0].append((1,3));
    graph[0].append((2,5));
    graph[0].append((3,4));
    graph[1].append((0,3));
    graph[1].append((2,6));
    graph[1].append((5,2));
    graph[1].append((6,1));
    graph[2].append((0,5));
    graph[2].append((1,6));
    graph[2].append((4,5));
    graph[2].append((6,9));
    graph[3].append((0,4));
    graph[3].append((7,8));
    graph[4].append((2,5));
    graph[4].append((6,4));
    graph[5].append((1,2));
    graph[6].append((1,1));
    graph[6].append((2,9));
    graph[6].append((4,4));
    graph[7].append((3,8));
    graph[7].append((6,8));
    
    mst=kruskal(graph);
    primMST=prim(graph);
    print(mst);
    print(primMST);

def findBridges_tarjan(graph):
    n=len(graph);
    unvisited=-1;
    ids=[unvisited]*n;
    lows=[-1]*n;
    parent=[-1]*n;
    bridges=[()];
    id=-1;
    def dfs(at):
        nonlocal id;
        nonlocal unvisited;
        id+=1;
        ids[at]=lows[at]=id;
        for neighbour in graph[at]:
            if ids[neighbour]==unvisited: # if neighbour is not visited
                parent[neighbour]=at;
                dfs(at);
                lows[at]=min(lows[at],lows[neighbour]);
                if lows[neighbour]> ids[at]:
                    bridges.append((at,neighbour));
            elif parent[at]!=neighbour: #ignore child to parent edge
                lows[at]=min(lows[at],ids[neighbour]);
    
    for i in range(n):
        if ids[i]==unvisited:
            dfs(i);
    return bridges;

def findArticulationsPoints_Tarjan(graph):
    unvisited=id=-1;
    n=len(graph);
    ids=[unvisited]*n;
    lows=[-1]*n;
    parent=[-1]*n;
    artPointsTF=[False]*n;
    artPoints=[];
    def dfs(at):
        nonlocal id;
        nonlocal unvisited;
        id+=1;
        ids[at]=lows[at]=id;
        children=0;
        for neighbour in graph[at]:
            if ids[neighbour]==unvisited:
                children+=1;
                parent[neighbour]=at;
                dfs(neighbour);
                lows[at]=min(lows[at],lows[neighbour]);
                
                if parent[at]==-1 and children>1: #case1: at is root
                    artPointsTF[at]=True;
                    artPoints.append(at);
                if parent[at]!=-1 and lows[neighbour]>=ids[at]: #case2: at least 1 component wil get separated;
                    artPointsTF[at]=True;
                    artPoints.append(at);
            elif parent[at]!=neighbour: #ignore child to parent edge
                lows[at]=min(lows[at],ids[neighbour]);
    for i in range(n):
        if ids[i]==unvisited:
            dfs(i);
    return artPoints;

def main():
    practicedijkstrawithIndexedPQ();
    print("practice Minimum Spanning Tree");
    practicemst();
if __name__=="__main__":
    main();