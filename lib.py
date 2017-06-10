####################################################
#################  Constants  ######################
####################################################

####################################################
#################  Misc  ###########################
####################################################

# Next lexicographical permutation
#
# Computes the next lexicographical permutation of the specified list in place,
# returning whether a next permutation existed. (Returns False when the argument
# is already the last possible permutation.)
#
# Example:
#   arr = [0, 1, 0]
#   next_permutation(arr)  (returns True)
#   arr has been modified to be [1, 0, 0]
#
# Credit: Project Nayuki
# (https://www.nayuki.io/page/next-lexicographical-permutation-algorithm)
def next_permutation(arr): # O(n)
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True

# quickselect
#
# Find kth smallest element in a.
#
# Credit: KoderDojo
# http://www.koderdojo.com/blog/quickselect-algorithm-in-python
from random import randint
def quickselect(a, k): # O(n)ish
    def select(a, lo, hi, k):
        if hi == lo:
            return a[lo]

        pidx = randint(lo, hi)

        a[lo], a[pidx] = a[pidx], a[lo]

        i = lo
        for j in range(lo+1, hi+1):
            if a[j] < a[lo]:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i], a[lo] = a[lo], a[i]

        if k == i:
            return a[i]
        elif k < i:
            return select(a, lo, i-1, k)
        else:
            return select(a, i+1, hi, k)

    if a is None or len(a) < 1:
        return None

    if k < 0 or k > len(a) - 1:
        raise IndexError()

    return select(a, 0, len(a) - 1, k)

############################################################

# Counting inversions
#
# Credit: Shawn O'Hare
# (http://www.shawnohare.com/2013/08/counting-inversions-in-python.html)
def sort_count(L):
    if len(L) > 1:
        n = len(L)//2
        A, a = sort_count(L[:n])
        B, b = sort_count(L[n:])

        m = 0
        i = j = 0
        M = []

        list_append = M.append
        length_A, length_B = len(A), len(B)
        while i < length_A and j < length_B:
            if A[i] <= B[j]: 
                list_append(A[i])
                i += 1
            else: 
                m += length_A - i
                list_append(B[j])
                j += 1

        M.extend(A[i:])
        M.extend(B[j:])

        return M, a + b + m
    else:
        return L, 0

############################################################

# Convert an integer number n into a string of english words
#
# Credit: vegaseat
# (https://www.daniweb.com/programming/software-development/code/216839/number-to-word-converter-python)
def int2word(n):
    ones = ['', 'one ','two ','three ','four ', 'five ', 'six ','seven ','eight ','nine ']
    tens = ['ten ','eleven ','twelve ','thirteen ', 'fourteen ', 'fifteen ','sixteen ','seventeen ','eighteen ','nineteen ']
    twenties = ['','','twenty ','thirty ','forty ', 'fifty ','sixty ','seventy ','eighty ','ninety ']
    thousands = ['','thousand ','million ', 'billion ', 'trillion ', 'quadrillion ', 'quintillion ', 'sextillion ', 'septillion ','octillion ', 'nonillion ', 'decillion ', 'undecillion ', 'duodecillion ', 'tredecillion ', 'quattuordecillion ', 'quindecillion', 'sexdecillion ', 'septendecillion ', 'octodecillion ', 'novemdecillion ', 'vigintillion ']

    n3 = []
    r1 = ''
    ns = str(n)
    for k in range(3, 33, 3):
        r = ns[-k:]
        q = len(ns) - k
        if q < -2:
            break
        else:
            if  q >= 0:
                n3.append(int(r[:3]))
            elif q >= -1:
                n3.append(int(r[:2]))
            elif q >= -2:
                n3.append(int(r[:1]))
        r1 = r
    
    nw = ''
    for i, x in enumerate(n3):
        b1 = x % 10
        b2 = (x % 100)//10
        b3 = (x % 1000)//100
        if x == 0:
            continue 
        else:
            t = thousands[i]
        if b2 == 0:
            nw = ones[b1] + t + nw
        elif b2 == 1:
            nw = tens[b1] + t + nw
        elif b2 > 1:
            nw = twenties[b2] + ones[b1] + t + nw
        if b3 > 0:
            nw = ones[b3] + 'hundred ' + nw
    return nw


# TODO: Kadane's algorithm

# TODO: Segment tree

# Fenwick tree
#
# Python implementation of Binary Indexed Tree
# Credit: Raju Varshney
# 
# Returns sum of arr[0..index]. This function assumes
# that the array is preprocessed and partial sums of
# array elements are stored in BITree[].
def getsum(BITTree,i):
    s = 0  #initialize result
 
    # index in BITree[] is 1 more than the index in arr[]
    i = i+1
 
    # Traverse ancestors of BITree[index]
    while i > 0:
 
        # Add current element of BITree to sum
        s += BITTree+=1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                k+=1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                while j<len(right):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                [i]
 
        # Move index to parent node in getSum View
        i -= i & (-i)
    return s
 
# Updates a node in Binary Index Tree (BITree) at given index
# in BITree.  The given value 'val' is added to BITree[i] and
# all of its ancestors in tree.
def updatebit(BITTree , n , i ,v):
    # index in BITree[] is 1 more than the index in arr[]
    i += 1
 
    # Traverse all ancestors and add 'val'
    while i <= n:
 
        # Add 'val' to current node of BI Tree
        BITTree[i] += v
 
        # Update index to that of parent in update View
        i += i & (-i)
 
 
# Constructs and returns a Binary Indexed Tree for given
# array of size n.
def construct(arr, n):
    # Create and initialize BITree[] as 0
    BITTree = [0]*(n+1)
 
    # Store the actual values in BITree[] using update()
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
 
    # Uncomment below lines to see contents of BITree[]
    #for i in range(1,n+1):
    #      print BITTree[i],
    return BITTree
 
###################################################

# Credit Dave Abrahams
# (https://stackoverflow.com/questions/212358/binary-search-bisection-in-python)
def binary_search(a, x, lo=0, hi=None): # O(logn)
    from bisect import bisect_left
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi) 
    return (pos if pos != hi and a[pos] == x else -1)

####################################################
#################  Geometry  #######################
####################################################

# TODO: Andrew's algorithm (convex hull) - O(nlogn)

# Euclid's formula (generating Pythagorean triples)

#################################################
#################  Graph  #######################
#################################################

# TODO: Bellman-Ford

# TODO: Floyd-Warshall

# TODO: Hopkroft-Karp (bipartite matching)

# TODO: Ford-Fulkerson

# TODO: Kosaraju (strongly connected components)

# TODO: Kruskal's (MST)

# TODO: Prim's (MST)

# Union-find data structure. Based on Josiah Carlson's code,
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
# with significant additional changes by D. Eppstein.
class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

# TODO: BFS

# TODO: DFS

# g - graph as adjacency list
# w - nested dict of edge weights
# s - source node label
def dijkstra(g, w, s): # TODO: Runtime
    visited = set()

    dist = dict.fromkeys(g.keys(), float('inf'))
    dist[s] = 0
 
    while visited != g.keys():
        v = min((set(dist.keys()) - visited), key=dist.get)
        for u in g[v] - visited:
            new_path = dist[v] + w[v][u]
            if new_path < dist[u]:
                dist[u] = new_path
 
        visited.add(v)
          	
    return dist

# NOTE: Must be imported with topsort.
# g - graph as adjacency list
# w - nested dict of edge weights
# s - source node label
def dag_dijkstra(g, w, s): # O(n)
    dist = dict.fromkeys(g.keys(), float('inf'))
    dist[s] = 0

    top_order = topsort(g)
    for u in top_order:
        for v in g[u]:
            dist[v] = min(dist[v], dist[u] + w[u][v])

    return dist, top_order

# From StackOverflow
# Returns a topological ordering of an input DAG.
def topsort(g): # O(n)
    from collections import defaultdict
    from itertools import takewhile, count, chain
    levels_by_name = dict()
    names_by_level = defaultdict(set)

    def walk_depth_first(name):
        if name in levels_by_name:
            return levels_by_name[name]
        children = g.get(name, None)
        level = 0 if not children else (1 + max(walk_depth_first(lname) for lname in children))
        levels_by_name[name] = level
        names_by_level[level].add(name)
        return level

    for name in g:
        walk_depth_first(name)

    return reversed(list(chain.from_iterable(takewhile(lambda x: x is not None, (names_by_level.get(i, None) for i in count())))))
