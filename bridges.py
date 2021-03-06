"""
Finding bridges in undirected graph
using functions from graph_analyses.py
"""

# importing
from sys import setrecursionlimit

# setting recursion limit to 10^9
setrecursionlimit(10**9)


def dfs(v, used, timer, tin, fup, g, ans, p=-1):
    """
    Just a recursive DFS algorithm
    """
    used[v] = True
    tin[v] = fup[v] = timer
    timer += 1
    for to in g[v]:
        if to == p:
            continue
        if used[to]:
            fup[v] = min(fup[v], tin[to])
        else:
            dfs(to, used, timer, tin, fup, g, ans, v)
            fup[v] = min(fup[v], fup[to])
            if fup[to] > tin[v]:
                ans.add((v, to))


def find_bridges_helper(n, used, timer, tin, fup, g, ans):
    """
    Function that starts algorithm
    """
    for i in range(n):
        used[i] = False
    for i in range(n):
        if not used[i]:
            dfs(i, used, timer, tin, fup, g, ans)


def find_bridges(data, n):
    """
    Initial function
    str -> set(tuple)
    """
    n=n[0]
    g = [[] for _ in range(0, n + 1)]
    # creating unordered list
    for i in data:
        u = i[0]
        v = i[1]
        g[u].append(v)
        g[v].append(u)
    used = [False for _ in range(n+1)]
    timer = 0
    tin = [-1 for _ in range(n+1)]
    fup = [-1 for _ in range(n+1)]
    ans = set()
    find_bridges_helper(n, used, timer, tin, fup, g, ans)
    if ans==set():
        return 'У цьому графі мостів немає.'
    return ans
    