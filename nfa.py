# Example Usage
nfa = NFA()
q0 = nfa.add_state()              # Start state
q1 = nfa.add_state()
q2 = nfa.add_state(is_final=True) # Final state for `ab`
q3 = nfa.add_state()
q4 = nfa.add_state()
q5 = nfa.add_state()
q6 = nfa.add_state(is_final=True) # Final state for `cd(a|b)*`

# Add transitions to match the pattern ab|cd(a|b)*

# Branch for `ab` and `cd(a|b)*`
nfa.add_transition(q0, q1, 'ε')   # ε-transition to `ab` path
nfa.add_transition(q0, q3, 'ε')   # ε-transition to `cd(a|b)*` path

# Path `ab`
nfa.add_transition(q1, q2, 'a')   # Transition on 'a' for `ab`
nfa.add_transition(q2, q6, 'b')   # Transition on 'b' in `ab`, move to final

# Path `cd(a|b)*`
nfa.add_transition(q3, q4, 'c')   # Transition on 'c' in `cd`
nfa.add_transition(q4, q5, 'd')   # Transition on 'd' in `cd`

# Epsilon transition to `(a|b)*` loop
nfa.add_transition(q5, q6, 'ε')   # Move to final or repeat `(a|b)*`

# `(a|b)*` loop at the end
nfa.add_transition(q6, q6, 'a')   # Loop on 'a'
nfa.add_transition(q6, q6, 'b')

# Display the NFA
nfa.display()


#FUNCTION
# def display(self):
#         print("NFA Representation:")
#         print("\nStates:", [state.name for state in self.states])
#         print("Start State:", self.states[0].name)
#         print("Final States:", [state.name for state in self.final_states])
#         print("\nTransitions:")

#         # Display in a table format
#         print(f"{'State':<8} {'Input':<8} {'Next State(s)':<15}")
#         print("-" * 32)
#         for state in self.states:
#             for symbol, next_states in state.transitions.items():
#                 for next_state in next_states:
#                     print(f"{state.name:<8} {symbol:<8} {next_state.name:<15}")