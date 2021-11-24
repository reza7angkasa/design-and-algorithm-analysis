def bfs(graph, start):
    visited= []
    queue = [start]
    
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours=graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited
graph={'Amin':{'Wasim', 'Nick','Mike'},
       'Wasim':{'Imran','Faras','Amin'},
       'Imran':{'Wasim'},
       'Faras':{'Wasim'},
       'Mike':{'Amin'},
       'Nick':{'Amin'}}
print(bfs(graph,'Amin'))
