from simpleai.search import SearchProblem, breadth_first, uniform_cost, depth_first, greedy, astar, limited_depth_first, iterative_limited_depth_first

class NQueens(SearchProblem):
    def __init__(self, N, initial_state=None):
        super().__init__(initial_state)
        self.N = N

    def actions(self, state):
        # Define the list of possible actions
        # Each action is represented as ('Move Queen i to row j', i, j)
        possible_actions = []
        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                possible_actions.append(('Move Queen {} to row {}'.format(i, j), i, j))
        return possible_actions

    def result(self, state, action):
        # Compute and return the resulting new state when the given action is performed
        # Each action is represented as ('Move Queen i to row j', i, j)
        _, i, j = action
        new_state = state[:i - 1] + str(j) + state[i:]
        return new_state

    def is_goal(self, state):
        # Returns whether the state is a goal state (no attacking pairs)
        return self._count_attacking_pairs(state) == 0

    def heuristic(self, state):
        # Returns the estimated solution cost using the number of attacking pairs as a heuristic
        return self._count_attacking_pairs(state)

    def _count_attacking_pairs(self, state):
        # Helper function to count the number of attacking pairs in the given state
        # (Same as the one from your initial code)
        count = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or abs(int(state[i]) - int(state[j])) == abs(i - j):
                    count += 1
        return count


# Testing function
def test_algorithms(N, initial_states):
    for initial_state in initial_states:
        problem = NQueens(N, initial_state)
        algorithms = [
            breadth_first,
            uniform_cost,
            depth_first,
            limited_depth_first,
            iterative_limited_depth_first,
            greedy,
            astar,
        ]

        for algorithm in algorithms:
            print('*' * 50)
            print(f'{algorithm.__name__}')
            result = limited_depth_first(problem, depth_limit=5)
            print('Resulting path:')
            print(result.path())
            print('Resulting state:', result.state)
            print('Total costs:', result.cost)
            print('Viewer stats:')
            print(result.state)
            print('Correct solution?:', problem.is_goal(result.state))
            print('*' * 50)


test_algorithms(4, ['2323', '4311', '3442', '1234'])
#test_algorithms(7, ['2323232', '4311431', '3442342', '1234512'])
