class State:
    def __init__(self, label=None):
        self.label = label
        self.transitions = {}
        self.final = False

class NFA:
    def __init__(self):
        self.start = None
        self.end = None

    @staticmethod
    def from_char(c):
        """Creates an NFA for a single character."""
        start = State()
        end = State()
        start.transitions[c] = [end]
        nfa = NFA()
        nfa.start = start
        nfa.end = end
        return nfa

    @staticmethod
    def concatenate(nfa1, nfa2):
        """Concatenates two NFAs."""
        nfa1.end.transitions[''] = [nfa2.start]  # epsilon transition
        nfa1.end.final = False
        new_nfa = NFA()
        new_nfa.start = nfa1.start
        new_nfa.end = nfa2.end
        return new_nfa

    @staticmethod
    def union(nfa1, nfa2):
        """Creates an NFA for the union (|) of two NFAs."""
        start = State()
        end = State()
        start.transitions[''] = [nfa1.start, nfa2.start]  # epsilon transitions to both
        nfa1.end.transitions[''] = [end]
        nfa2.end.transitions[''] = [end]
        nfa1.end.final = False
        nfa2.end.final = False
        new_nfa = NFA()
        new_nfa.start = start
        new_nfa.end = end
        return new_nfa

    @staticmethod
    def kleene_star(nfa):
        """Applies the Kleene star (*) to an NFA."""
        start = State()
        end = State()
        start.transitions[''] = [nfa.start, end]  # epsilon to start and end
        nfa.end.transitions[''] = [nfa.start, end]  # loop back to start
        nfa.end.final = False
        new_nfa = NFA()
        new_nfa.start = start
        new_nfa.end = end
        return new_nfa

def regex_to_nfa(regex):
    """Converts a regex into an NFA."""
    stack = []
    for char in regex:
        if char == '*':
            nfa = stack.pop()
            stack.append(NFA.kleene_star(nfa))
        elif char == '|':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            stack.append(NFA.union(nfa1, nfa2))
        elif char == '.':
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            stack.append(NFA.concatenate(nfa1, nfa2))
        else:
            stack.append(NFA.from_char(char))
    return stack.pop()

# Testing the regex to NFA conversion
regex = 'a.b*|c'
nfa = regex_to_nfa(regex)

# Display NFA structure
def print_nfa(nfa):
    visited = set()
    def dfs(state):
        if state in visited:
            return
        visited.add(state)
        for symbol, states in state.transitions.items():
            for s in states:
                print(f'{state.label} --{symbol}--> {s.label}')
                dfs(s)
    nfa.start.label = "start"
    dfs(nfa.start)

print_nfa(nfa)
