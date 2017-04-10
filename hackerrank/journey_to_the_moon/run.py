# Challenge here: https://www.hackerrank.com/challenges/journey-to-the-moon
# Keep track of size of each 'country'. For those without a country, each person is his/her own country.
# Take the sum of product of each size-2 combination of countries
import sys
from math import factorial
from collections import defaultdict

def get_num_valid_pairs(country_counts, num_islands):
    total = 0

    # islands crossed with eachother
    if num_islands > 1:
        total += factorial(num_islands) / (2 * factorial(num_islands - 2))

    # islands crossed with countries
    total += sum(country_counts) * num_islands

    # countries crossed with other countries
    for i in range(len(country_counts)):
        for j in range(i + 1, len(country_counts)):
            total += country_counts[i] * country_counts[j]

    return int(total)

def build_country_counts(adjacency_list):
    country_counts = []
    while len(adjacency_list) > 0:
        # Search
        cur_node_count = 1
        (n, frontier) = adjacency_list.popitem()
        visited = {n}

        while len(frontier) > 0:
            cur = frontier.pop()

            if cur not in visited:
                visited.add(cur)
                cur_node_count += 1

                new_neighbors = adjacency_list[cur]
                del adjacency_list[cur]

                frontier.update(new_neighbors - visited)

        country_counts.append(cur_node_count)

    return country_counts

# NOTE - this method is just copied around in all hackerrank modules
def get_tuple_from_f(f):
    l = f.readline().strip()
    return [int(i) for i in l.split(" ")]

if __name__ == "__main__":
    # if arg specified, read from file instead
    f = sys.stdin
    if len(sys.argv) > 1:
        f = open(sys.argv[1])

    (n, p) = get_tuple_from_f(f)

    adjacency_list = defaultdict(set)
    seen_nodes = set() # subtract this size from n at the end to determine islands

    for _ in range(p):
        (p1, p2) = get_tuple_from_f(f)

        seen_nodes.add(p1)
        seen_nodes.add(p2)

        adjacency_list[p1].add(p2)
        adjacency_list[p2].add(p1)

    country_counts = build_country_counts(adjacency_list)

    num_islands= n - len(seen_nodes)
    print(get_num_valid_pairs(country_counts, num_islands))
