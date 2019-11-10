from collections import defaultdict 


class Graph:

    def __init__(self):
        self.__graph = defaultdict(set)
        self.__cyclic_path_temp = []
        self.__cyclic_path = []

    def add_edge(self, point1, point2):
        self.__graph[point1].add(point2)
        self.__graph[point2].add(point1)

    def find_circular_path(self):
        for start_point, adjacent_points in self.__graph.iteritems():
            for each_adjacent_point in adjacent_points:
                self.__traverse(start_point, each_adjacent_point, [])
        return self.__cyclic_path
    
    def __traverse(self, parent, current_point, stack):
        stack.append(current_point)
        for each_point in list(self.__graph[current_point]):
            if each_point != parent and each_point not in stack:
                self.__traverse(current_point, each_point, stack)
            if  each_point != parent and each_point == stack[0]:
                if set(stack) not in self.__cyclic_path_temp:
                    self.__cyclic_path_temp.append(set(stack))
                    self.__cyclic_path.append(list(stack))
        stack.pop()

list_coordinate = [
    ['(1,1)','(3,1)'], 
    ['(3,1)','(3,3)'], 
    ['(3,3)','(1,3)'], 
    ['(1,3)','(1,1)']
]

graph = Graph()
for each_coordinate in list_coordinate:
    graph.add_edge(each_coordinate[0], each_coordinate[1])

cyclic_path = graph.find_circular_path()
print(cyclic_path)