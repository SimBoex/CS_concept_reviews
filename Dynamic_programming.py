# return the number of paths to reach x from 0. at each step i can make a move of 1 or 2 from the current value
def recursive_function(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    
    ## recursive step
    num_paths_for_x = recursive_function(x-2) + recursive_function(x-1)
    return num_paths_for_x


''' Recursion is the process in which a function calls itself until the base cases are reached. 
And during the process, complex situations will be traced recursively and become simpler and simpler. 
The whole structure of the process is tree-like. Recursion does not store any value until reaches the final stage(base case).
'''

'''Time Complexity for recursive functions:
- Draw the recursive tree for the given recurrence relation;
- Compute the cost at each level (except the last one) 
- Count total number of levels:
    - taking the longest path from the root to the leaf node to get the max number of depth (we need an expression in function of the depth of the tree)
    - we get the function is called on a given input that has its size that can be expressed as a function of k (k is the depth)
    - use the expression and put equal to the case base size to find the depth 
    - then since we started with k = 0, then we need to add 1 to the obtained value of k
- Count # of nodes in the last level:
    - here assuming is a binary tree (worst case), then at level k we have 2 ^ k nodes = n
- Compute cost at last level
    - and since the cost at the last level is constant we need to compute separately (n  x O(1))
- Sum up all the costs across the tree (each is the time to compute the function without the recursive part)
    - summing the constant parts at each level + the cost at last level
'''

'''And Dynamic Programming is mainly an optimization compared to simple recursion. The main idea is to decompose the original question into repeatable patterns and then store the results as many sub-answers. 
Therefore, we do not have to re-compute the pre-step answers when needed later. 
In terms of big O, this optimization method generally reduces time complexities from exponential to polynomial. '''

def dyn_prog_function(x):
    # store the number of paths to reach value j at index j
    paths = []
    ## initialization
    paths.append(0)
    paths.append(1)
    paths.append(2)
    
    # iterative step:
    for j in range(3,x + 1):
        # number of paths to reach value j
        paths.append(paths[j - 2] + paths[j - 1])
    return paths[x]
    