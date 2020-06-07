from collections import defaultdict

def dfs(source,dest,visited,path):
    visited[source]= True
    path.append(source)

    if source == dest:
        total =0
        print(path)
        l = len(path)
        for i in range(l-1):
            total += graph[path[i]][path[i+1]]

        print(total)

    else:
        for i in graph[source]:
            if visited[i] == False:
                dfs(i,dest,visited,path)
    path.pop()
    visited[source]=False


graph = defaultdict(dict)
graph[0][1]=35
graph[0][2]=45
graph[1][3]=22
graph[1][4]=32
graph[2][4]=28
graph[2][5]=36
graph[2][6]=27
graph[4][7]=30
graph[3][4]=31
graph[3][7]=47
graph[4][7]=30
graph[5][7]=26

source = int(input("Source: "))
dest = int(input("Destination: "))

visited = [False]*8
path=[]
dfs(source,dest, visited, path)
