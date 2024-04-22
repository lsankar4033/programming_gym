import random
from itertools import combinations

# min-cut. karger's algo? pick random edge, contract graph, repeat until 2 nodes
# 2 nodes remaining, the edges to be cut between them should be 3 (check)
# if so, the 'combined nodes' of each node are the subgraph sizes

# representation?
# set of edges + set of nodes
# every 'cut', combine nodes.
# how to remove self-cycles?
# - node -> supernode?
# - node -> edges?

# NOTE: these objects are global

# {'ltm': {'mxc', 'fun'}}
node_to_edges = {}

# tracks 'combined' nodes, {'ltm': {'ltm', 'mxc', 'fun'}}
node_to_supernode = {}

# run this while node_to_supernode has more than 2 keys


def contract_random_edge(node_to_edges, node_to_supernode):
    # pick edge at random (random node + random edge in its list)
    node1 = random.choice(list(node_to_edges.keys()))
    node2 = random.choice(list(node_to_edges[node1]))

    # we know for every node in n2e that it's a supernode. we remove nodes in n2e for anythign combined
    # so really waht we want to do here is pick the *biggest* remaining supernode and collapse all the others into it

    # G[v1].extend(G[v2])
    # for x in G[v2]:
    #     G[x].remove(v2)
    #     G[x].append(v1)
    # while v1 in G[v1]:
    #     G[v1].remove(v1)
    # del G[v2]

    # we may want to do this for *all* items in the new supernode
    # for each end of ndoe, pick node to keep based on which has bigger supernode
    (to_keep, to_remove) = (node1, node2) if len(
        node_to_supernode[node1]) > len(node_to_supernode[node2]) else (node2, node1)

    # combine supernodes: remove new self-loops
    s1 = node_to_supernode[to_keep]
    s2 = node_to_supernode[to_remove]
    possible_self_loops = (s1 - s2) | (s2 - s1)
    for (n1, n2) in combinations(possible_self_loops, 2):
        # attempt remove
        # oh crap, we need to remove entire edges here...
        pass

    # remove original edge
    node_to_edges[to_keep].remove(to_remove)
    del node_to_edges[to_remove]

    return node_to_edges, node_to_supernode
