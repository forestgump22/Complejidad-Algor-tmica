
class Heap:
    def __init__(self,comp):
        self.comp=comp;
        self.hp=[];
        self.size=0;
    
    def add(self,element):
        self.hp.append(element);
        self.size+=1;
        if self.size<=1:
            return;
        
        i=self.size-1;
        parent=(i-1)//2;
        while (parent>=0 and self.comp(self.hp[i],self.hp[parent])):
            self.hp[i],self.hp[parent]=self.hp[parent],self.hp[i];
            i=parent;
            parent=(i-1)//2;
            
    def pop(self):
        if self.size==0:
            return None;
        removeelement=self.hp[0];
        self.hp[0]=self.hp[self.size-1];
        self.hp.pop();
        self.size-=1;
        i=0;
        while (i<(self.size-1)//2):
            left=i*2+1;
            right=i*2+2;
            
            if (self.comp(self.hp[left],self.hp[i])\
                or self.comp(self.hp[right],self.hp[i])):
                if self.comp(self.hp[left],self.hp[right]):
                    self.hp[left],self.hp[i]=self.hp[i],self.hp[left];
                    i=left;
                else:
                    self.hp[right],self.hp[i]=self.hp[i],self.hp[right];
                    i=right;
            else:
                return;
        return removeelement;
    def Size(self):
        return self.size;
    def top(self):
        return self.hp[0];
    
    def __str__(self):
        return str(self.hp);

def practiceHeap():
    #maxheap:
    compmax=lambda a,b: a>b;
    
    #minheap:
    compmin=lambda a,b: a<b;
    
    hp=Heap(compmin);
    hp.add(45);
    hp.add(65);
    hp.add(45);
    hp.add(85);
    hp.add(25);
    print(hp);
def topologicalsort(graph):
    n=len(graph);
    ts=[];
    visited=[False]*n;
    prev=[None]*n;
    def dfs(at):
        if visited[at]: return;
        visited[at]=True;
        for neighbour in graph[at]:
            if not visited[neighbour]:
                prev[neighbour]=at;
                dfs(neighbour);
        ts.append(at);
    for i in range(n):
        if not visited[i]:
            dfs(i);
    return list(reversed(ts));

def practicetopological():
    n=9;
    graph=[[]for _ in range(9)];
    graph[0].append(1);
    graph[1].append(2);
    graph[1].append(5);
    graph[2].append(3);
    graph[3].append(4);
    graph[5].append(6);
    graph[6].append(7);
    graph[7].append(8);
    
    print(topologicalsort(graph,0));

def dijkstra(graph,start):
    #O(Edges * log(Vertex))
    n=len(graph);
    visited=[False]*n;
    dist=[float('inf')]*n;
    dist[start]=0;
    prev=[None]*n;
    pq=Heap(lambda a,b: a[0]<b[0]);
    pq.add((0,start))
    while pq.size:
        cost,node=pq.pop();
        if not visited[node]:
            visited[node]=True;
            for neighbour,weight in graph[node]:
                if visited[neighbour]:continue;
                newCost=dist[node]+weight;
                if newCost<dist[neighbour]:
                    dist[neighbour]=newCost;
                    prev[neighbour]=node;
                    pq.add((newCost,neighbour));
    return dist,prev;
        
def dagshortestpath(graph,start):
    n=len(graph);
    visited=[False]*n;
    prev=[None]*n;
    ts=topologicalSort(graph);
    dist=[float('inf')]*n;
    dist[start]=0;
    for i in range(len(ts)):
        node=ts[i];
        for neighbour,weight in graph[node]:
            if not visited[neighbour]:
                visited[neighbour]=True;
                newcost=dist[node]+weight;
                if newcost<dist[neighbour]:
                    dist[neighbour]=newcost;
                    prev[neighbour]=node;
    return dist,prev;
def practicedijkstra():
    n=5;
    graph=[[]for _ in range(n)];
    graph[0].append((2,75));
    graph[0].append((1,9));
    graph[1].append((2,95));
    graph[1].append((4,42));
    graph[2].append((3,51));
    graph[3].append((1,19));
    graph[4].append((3,31));
    
    dist,prev=dijkstra(graph,0);
    print("dist: ",dist);
    print("prev: ",prev);

from collections import defaultdict;
class IndexedPriorityQueuePreAlpha:
    def __init__(self,comp) -> None:
        self.comp=comp;
        self.values=defaultdict(int);
        
def main():
    practicedijkstra();
if __name__=="__main__":
    main(); 
         
