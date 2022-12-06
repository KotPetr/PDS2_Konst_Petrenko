import networkx


def read_list_from_file(file_name : str):
    graph = []
    with open(file_name, mode='r') as f:
       for line in f:
           ls = line.split(';')
           ls[2] = int(ls[2])
           graph.append(ls)

    return graph

edge_sity_list = read_list_from_file('cities.csv')

for i in range(10):
    print(edge_sity_list[i])

print(edge_sity_list[2][2] + edge_sity_list[4][2])