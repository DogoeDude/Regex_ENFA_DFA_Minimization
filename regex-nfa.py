from pyformlang.regular_expression import Regex

# Define a regex and convert it to an epsilon NFA
regex = Regex("a(b|c)")
nfa = regex.to_epsilon_nfa()

# Collect symbols from the NFA
nfa_symbols_list = []
for symbol in nfa.symbols:
    nfa_symbols_list.append(symbol)

# Check for the empty string and append 'ε' if found
if '' in nfa_symbols_list:
    nfa_symbols_list.append('ε')

# Print the symbols list
print(nfa_symbols_list)
