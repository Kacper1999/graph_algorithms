# this program finds the smallest weight on a path from "s" to "t"
# where the smallest weight on that path is biggest in comparison to others
from dimacs import load_weighted_graph


def union(x, y, p):
    a = find(x, p)
    b = find(y, p)

    if a != b:
        p[a] = b


def find(x, p):
    if p[x] != x:
        v = p[x]
        p[x] = find(v, p)
        return p[x]
    return x


def sort_edges_descending(edges):
    edges.sort(key=lambda tup: tup[2], reverse=True)


def find_result(graph_name):  # this function has a crappy name because I couldn't think of anything else
    (V, L) = load_weighted_graph(graph_name)

    sort_edges_descending(L)

    s = 1  # start
    t = 2  # destination
    p = {i: i for i in range(1, V + 1)}

    result = -1
    for (x, y, c) in L:
        union(x, y, p)
        if find(s, p) == find(t, p):
            result = c
            break
    return result


def load_and_print_edges(graph_name):
    (V, L) = load_weighted_graph(graph_name)  # load graph
    print_edges(L)


def print_edges(edges):
    for (x, y, c) in edges:  # search through edges
        print("edge between", x, "and", y, "with weight", c)


def main():
    graph_name = "path1000"
    (V, L) = load_weighted_graph(graph_name)
    sort_edges_descending(L)
    print(find_result(graph_name))


if __name__ == "__main__":
    main()
