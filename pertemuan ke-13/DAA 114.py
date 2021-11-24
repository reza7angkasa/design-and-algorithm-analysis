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
graph={'Faras':{'Imran'},
       'Imran':{'Wasim','Nick','Mike','Faras'},
       'Amin':{'Wasim','Nick','Mike'},
       'Wasim':{'Amin','Imran'},
       'Nick':{'Amin','Imran'},
       'Mike':{'Amin','Imran'}}
print(bfs(graph,'Faras'))