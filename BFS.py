def Bfs(graph, StartNode):
    visited=set()
    q=[StartNode]
    visited.add(StartNode)
    print("BFS traversal is : ",end="")
    while len(q)>0:
        vertex=q.pop(0)
        print(vertex,end=" ")
        for i in graph[vertex]:
            if i not in visited:
                visited.add(i)
                q.append(i)
            

V=int(input("Enter the number of nodes/vertices : "))
E=int(input("Enter the number of edges : "))
graph={}
for i in range(1,E+1):
    src,des=input(f"Enter edge {i} (source, destination) : ").split()
    if src not in graph:
        graph[src]={}
    if des not in graph:
        graph[des]={}
    graph[src][des]=1
    #graph[des][src]=1    # For undirected graph
StartNode=input("Enter the starting node : ")
Bfs(graph,StartNode)