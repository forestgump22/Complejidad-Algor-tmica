from collections import deque
from inspect import stack
import queue


class BFS_DFS:
        
    def bfs(self,graph,startnode,end):
        n=len(graph);
        visited=[False]*n;
        prev=[None]*n;
        
        q=deque();
        q.append(startnode);
        visited[startnode]=True;
        path=[];
        def reconstruction():
            node=end;
            while node!=None:
                path.append(node);
                node=prev[node];
            path.reverse();
            if path[0]==startnode:
                return path;
            return [];
        while q:
            node=q.popleft();
            if node==end:
                return True;
            
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True;
                    prev[neighbour]=node;
                    q.append(neighbour);
        return reconstruction();
    
    
    def DFS(self, graph,start,end):
        n=len(graph);
        visited=[False]*n;
        prev=[None]*n;
        
        visited[start]=True;
        stacki=[start];
        while stacki:
            node=stacki.pop();
            if end==node:
                return True;
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True;
                    prev[neighbour]=node; 
                    stacki.append(neighbour); 
                    
        return False;

    def dfs(self, graph,startnode):
        n=len(graph);
        visited=[False]*n;
        prev=[None]*n;
        visited[startnode]=True;
        def _dfs(at):
            for neighbour in graph[at]:
                if not visited[neighbour]:
                    visited[neighbour]=True;
                    prev[neighbour]=at;
                    _dfs(neighbour);
                    
        _dfs(startnode);
        return prev;
    
def allpathsfromsource(graph):
    paths=[];
    n=len(graph);
    
    path=[0];
    q=queue.Queue();
    q.put(path);
    while q:
        current_p=q.get();
        node=current_p[-1];
        
        for neighbour in graph[node]:
            temp_p=current_p.copy();
            temp_p.append(neighbour);
            
            if neighbour==len(graph)-1:
                paths.append(temp_p);
            else: q.put(temp_p);
    return paths;

class tarjan:
    def solvefindSccs(self, graph):
        unvisited=id=-1;
        n=len(graph);
        sccCount=0;
        ids=[unvisited]*n;
        lows=[0]*n;
        onStack=[False]*n;
        stacki=stack();
        
        
        def dfs(at):
            stacki.append(at);
            onStack[at]=True;
            nonlocal id;
            id+=1;
            ids[at]=lows[at]=id;
            
            for to in graph[at]:
                if ids[to]==unvisited:
                    dfs(to);
                if onStack[to]:
                    lows[at]=min(lows[at],lows[to]);
            
            nonlocal sccCount;
            if ids[at]==lows[at]:
                node=stacki.pop();
                while True:
                    onStack[node]=False;
                    lows[node]=ids[at];
                    if node==at:   
                        break;
                    node=stacki.pop();
                sccCount+=1;
        for i in range(n):
            if ids[i]==unvisited:
                dfs(i);
        return lows, sccCount;

        