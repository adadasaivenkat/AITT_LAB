def Dfs(visited,graph,StartNode):
    if StartNode not in visited:
        print(StartNode,end=" ")
        visited.add(StartNode)
        for i in graph[StartNode]:
            Dfs(visited,graph,i)


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
visited=set()
print("DFS traversal is : ",end="")
Dfs(visited,graph,StartNode)