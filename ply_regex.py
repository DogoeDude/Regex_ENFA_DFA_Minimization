import ply.lex as lex
from pyformlang.regular_expression import Regex

# Define a regex that should have two final states
regex = Regex("(a)(c)|(b)(d)")  # This regex should allow for two different final states
nfa = regex.to_epsilon_nfa()  # Convert to epsilon NFA
# Collect symbols, including epsilon if it exists
nfa_symbols_list = [symbol for symbol in nfa.symbols]
def displayAuto(automaton):
    print(f"States: {automaton.states}")
    print(f"Initial State: {automaton.start_states}")
    print(f"Final State/s: {automaton.final_states}")
    print(f"Symbol/s: {nfa_symbols_list}")
    print("\nTransition Table")
    print(f"{'State':<10} | {'Symbol':<10} | {'Transition':<10}")
    print("-" * 35)

    # Get the transitions as a dictionary
    transition_dict = automaton.to_dict()

    # Sort the states using their string representation or some comparable attribute
    sorted_states = sorted(transition_dict.keys(), key=lambda state: str(state))

    for state in sorted_states:
        for symbol, next_states in transition_dict[state].items():
            for next_state in next_states:
                print(f"{str(state):<10} | {str(symbol):<10} | {str(next_state):<10}")


# Display the NFA in table format
displayAuto(nfa)
