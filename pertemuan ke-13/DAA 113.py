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
graph={'Wasim':{'Imran', 'Amin'},
       'Imran':{'Faras','Wasim'},
       'Faras':{'Imran'},
       'Amin':{'Nick','Mike','Wasim'},
       'Nick':{'Amin'},
       'Mike':{'Amin'}}
print(bfs(graph,'Wasim'))

