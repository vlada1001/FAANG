import math

from test_framework import generic_test


def is_arbitrage_exist(problems.graph):
    def bellman_ford(problems.graph, source):
        dis_to_source = ([float('inf')] * (source - 1) + [0] + [float('inf')] *
                         (len(problems.graph) - source))

        for _ in range(1, len(problems.graph)):
            have_update = False
            for i, row in enumerate(problems.graph):
                for j, g in enumerate(row):
                    if (dis_to_source[i] != float('inf')
                            and dis_to_source[j] > dis_to_source[i] + g):
                        have_update = True
                        dis_to_source[j] = dis_to_source[i] + g

            # No update in this iteration means no negative cycle.
            if not have_update:
                return False

        # Detects cycle if there is any further update.
        return any(dis_to_source[i] != float('inf')
                   and dis_to_source[j] > dis_to_source[i] + g
                   for i, row in enumerate(problems.graph) for j, g in enumerate(row))

    # Uses Bellman-ford to find negative weight cycle.
    return bellman_ford([[-math.log10(edge) for edge in edge_list]
                         for edge_list in problems.graph], 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("arbitrage.py", "arbitrage.tsv",
                                       is_arbitrage_exist))
