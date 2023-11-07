
import networkx as nx
import matplotlib.pyplot as plt


def create_graph(list_of_points):
    # функция создания графа на основе листа точек
    n = len(list_of_points)
    graph = nx.DiGraph()
    list_of_edges = [(i, j) for i in range(n) for j in list_of_points[i]]
    graph.add_nodes_from(range(n))
    graph.add_edges_from(list_of_edges)
    return graph


def show_graph(graph):
    # функция рисования графа
    nx.draw(graph, with_labels=True)
    plt.show()


def search_in_width(graph, s, out=0):
    # реализация алгоритма поиска в ширину
    global w
    parents = {v: None for v in graph}
    level = {v: None for v in graph}
    level[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if level[w] is None:
                queue.append(w)
                parents[w] = v
                level[w] = level[v] + 1
        if out:
            print(level[w], level, queue)
    return level, parents


def bypass_route(end, parents):
    # функция поиска кратчайшего пути
    path = [end]
    parent = parents[end]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]


def shortest_route_and_visualization(graph):
    # самая главная функция, которая на основе обхода в ширину и кратчайшего пути --->
    # ---> рисует итерационно граф (отображает каждую итерацию)
    level, parents = search_in_width(graph, 0, out=0)
    print(level)
    print(parents)
    PATH = bypass_route(5, parents)
    print(PATH)
    red_node = set(PATH)
    red_edges = [(PATH[i], PATH[i + 1]) for i in range(len(PATH) - 1)]
    node_colours = ["g" if node not in red_node else "red" for node in graph.nodes()]
    black_edges = [edge for edge in graph.edges() if edge not in red_edges]
    p = nx.spring_layout(graph)

    for i in range(len(PATH)):
        plt.clf()  # Очистить предыдущий граф
        plt.title("Итерация {}".format(i + 1))
        current_path = PATH[:i + 1]
        current_red_edges = [(current_path[j], current_path[j + 1]) for j in range(len(current_path) - 1)]
        current_node_colours = ["g" if node not in current_path else "red" for node in graph.nodes()]
        current_black_edges = [edge for edge in graph.edges() if edge not in current_red_edges]

        nx.draw_networkx_nodes(graph, p, cmap=plt.get_cmap("jet"),
                               node_color=current_node_colours, node_size=500)
        nx.draw_networkx_labels(graph, p)
        nx.draw_networkx_edges(graph, p, edgelist=current_black_edges, width=2.0, edge_color="k", arrows=True)
        nx.draw_networkx_edges(graph, p, edgelist=current_red_edges, width=3.0, edge_color="r", arrows=True)

        plt.pause(2)  # Пауза (в секундах) для показа измененного графа

    plt.show()  # Показать окончательный граф


def task():
    list_of_points = {0: {1}, 1: {2, 3}, 2: {5}, 3: {4}, 4: {5}, 5: {}}
    graph = create_graph(list_of_points)
    show_graph(graph)
    print(search_in_width(graph, 0, 1))
    shortest_route_and_visualization(graph)


task()
