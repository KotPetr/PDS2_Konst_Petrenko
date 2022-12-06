import networkx as nx
import matplotlib.pyplot as plt


def read_list_from_file(file_name: str):
    my_list = []
    with open(file_name, mode='r') as f:
       for line in f:
           ls = line.split(';')
           ls[2] = int(ls[2])
           my_list.append(ls)

    return my_list


def show_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos)
    plt.title('Graph')
    plt.show()


def get_shortest_route(G, start_point, end_point):
    route = nx.shortest_path(G, start_point, end_point, weight='weight')
    dist = nx.shortest_path_length(G, start_point, end_point, weight='weight')
    return route, dist


edge_city_list = read_list_from_file('cities.csv')
graph = nx.Graph()

for edge in edge_city_list:
    graph.add_edge(edge[0], edge[1], weight=edge[2])

show_graph(graph)

# Examples: 'Myrhorod', 'Hadiach', 'Romny', 'Rozdilna', 'Teplodar', 'Selydove'

s_route, dist = get_shortest_route(graph, 'Myrhorod', 'Selydove')

print(*s_route, sep=' - ')
print('Distance = ', dist)



