def dfs(graph, start, visited=None):
    if visited is None:
        visited= set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
         dfs(graph, next, visited)
    return visited
graph={'Rektor':{'warek 1', 'warek 2'},
       'warek 1':{'Rektor'},
       'warek 2':{'kaprodi 1','kaprodi 2','kaprodi 3','Rektor'},
       'kaprodi 1':{'dosen A','dosen B', 'dosen C','warek 2'},
       'kaprodi 2':{'dosen D', 'dosen E','warek 2'},
       'kaprodi 3':{'dosen F', 'dosen G','warek 2'},
       'dosen A':{'kaprodi 1'},
       'dosen B':{'dosen A','kaprodi 1'},
       'dosen C':{'dosen B'},
       'dosen D':{'kaprodi 2'},
       'dosen E':{'dosen D'},
       'dosen F':{'kaprodi 3'},
       'dosen G':{'dosen F'}}
print(dfs(graph,'Rektor'))
