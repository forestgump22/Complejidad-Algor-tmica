from collections import deque
class EulerianPathCircuits:
    def findEulerianPath(self,graph,n):
        indegree=[0]*n;
        outdegree=[0]*n;
        edgeCount=0;
        path=deque();
        def countInOutDegrees():
            for at in range(n):
                for to in graph[at]:
                    indegree[to]+=1;
                    outdegree[at]+=1;
                    nonlocal edgeCount;
                    edgeCount+=1;

        def graphHasEulerianPath():
            if edgeCount==0: return False;
            start_nodes,end_nodes=0,0;
            for i in range(n):
                if outdegree[i] -indegree[i]>1 or \
                    indegree[i]- outdegree[i]>1:
                        return False;
                elif outdegree[i]-indegree[i]==1:
                    start_nodes+=1;
                elif indegree[i]-outdegree[i]==1:
                    end_nodes+=1;
            return ((end_nodes==0 and start_nodes==0) or\
                    (end_nodes==1 and start_nodes==1));

        countInOutDegrees();
        if not graphHasEulerianPath():
            return None;
        
        def findStartNode():
            start=0;
            nonlocal n;
            for i in range(n):
                #Unique starting node
                if outdegree[i]-indegree[i]==1:
                    return i;
                
                if outdegree[i]>0:
                    start=i;
            return start;
        
        def dfs(at):
            while outdegree[at]!=0:
                
                outdegree[at]-=1;
                next_edge=graph[at][outdegree[at]];
                dfs(next_edge);
            
            path.appendleft(at);
        
        dfs(findStartNode());
        
        if len(path)!=edgeCount+1: return None;
        return path;
    def findEulerianCircuit(self,graph,n):
        indegree=[0]*n;
        outdegree=[0]*n;
        edgeCount=0;
        path=deque();
        def countInOutDegree():
            for at in range(n):
                for to in graph[at]:
                    indegree[to]+=1;
                    outdegree[at]+=1;
                    nonlocal edgeCount;
                    edgeCount+=1;
        def graphHasEulerianCircuit():
            if edgeCount==0:
                return False;
            for at in range(n):
                if indegree[at]!=outdegree[at]:
                    return False;
            return True;
        
        countInOutDegree();
        if not graphHasEulerianCircuit():
            return None;
        def dfs(at):
            while outdegree[at]!=0:
                outdegree[at]-=1;
                next_edge=graph[at][outdegree[at]];
                dfs(next_edge);
            path.appendleft(at);
        dfs(0);
        if len(path)!=edgeCount+1:
            return None;
        
        return path;

def addDirectedEdge(graph,at,to):
    graph[at].append(to);
def practiceEulerianPaths():
    n=7;
    graph=[[]for _ in range(n)];
    
    addDirectedEdge(graph, 1, 2);
    addDirectedEdge(graph, 1, 3);
    addDirectedEdge(graph, 2, 2);
    addDirectedEdge(graph, 2, 4);
    addDirectedEdge(graph, 2, 4);
    addDirectedEdge(graph, 3, 1);
    addDirectedEdge(graph, 3, 2);
    addDirectedEdge(graph, 3, 5);
    addDirectedEdge(graph, 4, 3);
    addDirectedEdge(graph, 4, 6);
    addDirectedEdge(graph, 5, 6);
    addDirectedEdge(graph, 6, 3);
    
    solver=EulerianPathCircuits();
    sol=solver.findEulerianPath(graph,n);
    print(sol);
def practiceEulerianCircuits():
    n=7;
    graph=[[]for _ in range(n)];
    
    addDirectedEdge(graph, 0, 1);
    addDirectedEdge(graph, 0, 3);
    addDirectedEdge(graph, 1, 0);
    addDirectedEdge(graph, 1, 3);
    addDirectedEdge(graph, 2, 0);
    addDirectedEdge(graph, 2, 2);
    addDirectedEdge(graph, 2, 1);
    addDirectedEdge(graph, 3, 2);
    addDirectedEdge(graph, 3, 2);
    
    solver=EulerianPathCircuits();
    solpath=solver.findEulerianPath(graph,n);
    solcircuit=solver.findEulerianCircuit(graph,n);
    print("Eulerian path: ",solpath);
    print("Eulerian Circuit",solcircuit);

if __name__=="__main__":
    print("practice eulerian paths");
    practiceEulerianPaths(); 
    
    print("practice eulerian circuits");
    practiceEulerianCircuits();    