#!/bin/env python3
# -*- coding: utf-8 -*-

def build_graph(fname, cutoff, has_title=True):
    graph = {}
    with open(fname, "r") as fin:
        if has_title:
            fin.readline()
        for line in fin:
            lst = line.split()
            kinship = float(lst[4])
            if kinship >= cutoff:
                id1, id2 = lst[:2]
                if id1 not in graph.keys():
                    graph[id1] = [id2]
                else:
                    graph[id1].append(id2)
                if id2 not in graph.keys():
                    graph[id2] = [id1]
                else:
                    graph[id2].append(id1)
    return graph

def BFS(graph, vertex):
    queue = []
    queue.append(vertex)
    degree = len(graph[vertex])
    max_degree = degree
    md_vertex = vertex
    visited = {vertex : degree}
    while queue:
        vertex = queue.pop(0)
        for iv in graph[vertex]:
            if iv not in visited.keys():
                queue.append(iv)
                degree = len(graph[iv])
                visited[iv] = degree
                if degree > max_degree:
                    max_degree = degree 
                    md_vertex = iv
    return md_vertex, max_degree

def break_graph(graph):
    removed = []
    while len(graph) > 0:
        vtx = list(graph.keys())[0]
        vertex, max_degree = BFS(graph, vtx)
        removed.append(vertex)
        for v in graph[vertex]:
            graph[v].remove(vertex)
            if len(graph[v]) == 0:
                graph.pop(v)
        graph.pop(vertex)
        # print(vertex)
    return removed

def main(args):
    if args.cutoff > 3:
        args.cutoff = 3
    if args.cutoff >= 1:
        degree = int(args.cutoff)
        cutoff = 1 / (2**((2 * degree + 3) / 2))
    else:
        cutoff = args.cutoff
    graph = build_graph(args.input, cutoff, args.has_title)
    removed = break_graph(graph)
    with open(args.output, "w") as fout:
        for eid in removed:
            fout.write("{}\n".format(eid))

if __name__ == "__main__":
    import argparse                
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True, 
                        help="Filename of input (kinship file)")
    parser.add_argument("-o", "--output", type=str, default="removed.txt",
                        help="Filename of output (removed eid list)")
    parser.add_argument("-c", "--cutoff",type=float, default=0.0884,
                        help="Cutoff for kinship, support absolute kinship value or degree such as (1, 2, or 3), default=0.0884")
    parser.add_argument("-t", "--has-title", action="store_true",
                        help="The input has title or not, default=False")
    args = parser.parse_args()
    main(args)
    
