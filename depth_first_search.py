from queue import LifoQueue
from hanoi_tower.tree_hanoi import NodeHanoi
from hanoi_tower.hanoi_states import ProblemHanoi

def depth_first_search(problem: ProblemHanoi, verbose: bool = False):
    """
    This function implements the depth-first search algorithm to solve the Hanoi Tower problem.
    
    Parameters:
    - problem: The problem instance to solve.
    
    Returns:
    - The goal node if the goal state is reached, None otherwise.
    """
    # Create the root node with the initial state
    root_node = NodeHanoi(problem.initial)
    # Initialize the LIFO queue
    frontier = LifoQueue()
    # Add the root node to the LIFO queue
    frontier.put(root_node)
    # Initialize the set of explored states
    explored = set()
    # Perform the search
    while not frontier.empty():
        # Get the next node from the LIFO queue
        node = frontier.get()
        # Add the current state to the set of explored states
        explored.add(node.state)
        # Print the current node
        if verbose:
            print(f'Current node: {node}')
        # Check if the goal state is reached
        if problem.goal_test(node.state):
            return node
        # Expand the current node and add the child nodes to the LIFO queue
        for child in node.expand(problem):
            if child.state not in explored:
                frontier.put(child)
    # Return None if no solution is found
    return None

if __name__=="__main__":
    pass
