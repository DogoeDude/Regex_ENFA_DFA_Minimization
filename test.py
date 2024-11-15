class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}  # Dictionary where keys are symbols and values are lists of states
        self.is_final = False 

    def __str__(self):
        return f"{self.name}"

class NFA:
    def __init__(self):
        self.states = []        # List of states in the NFA
        self.final_states = []   # List of final states
        self.alphabet = set()    # Set to store the alphabet
        self.state_counter = 0   # Counter to create unique state names
        self.start_state = None

    def add_state(self, is_final=False):
        """Create and add a new state, marking as final if specified."""
        state = State(f"q{self.state_counter}")
        self.state_counter += 1
        state.is_final = is_final
        self.states.append(state)
        if is_final:
            self.final_states.append(state)
        return state

    def add_transition(self, from_state, to_state, symbol):
        """Add a transition from one state to another with a given symbol."""
        self.alphabet.add(symbol)
        if symbol not in from_state.transitions:
            from_state.transitions[symbol] = []
        from_state.transitions[symbol].append(to_state)
        if symbol!="":
            self.alphabet.add(symbol)

def create_nfa(symbol):
    nfa = NFA()
    start = nfa.add_state()
    end = nfa.add_state(is_final=True)

    nfa.start_state = start
    nfa.final_states = [end]
    nfa.add_transition(start, end, symbol)
    return nfa

def union(nfa1, nfa2):
    nfa = NFA()
    start = nfa.add_state()
    nfa.start_state = start