# Regex_ENFA_DFA_Minimization
This is our final project for our 3rd year 1st sem Computer Science: Automata Theory and Formal Languages

We will also be using testing cases for Python to ensure that this project runs well. Namely: 
    1.) UnitTest
    2.) PyTest
    3.) Nose and Nose2
With the use of [PLY](https://pypi.org/project/pyformlang/) and
Due to time contraints,we will only be utilizing the function where it converts any desired Regular Expression into an Epsilon NFA.

We will be converting the E-NFA into a normal NFA and then a DFA where we then proceed to convert it into its minimize state.

E-NFA --> Normal NFA
  1.) Elimite all Epsilon entries
  2.) Find all null closures for the states
  3.) Create new transitions based off from the previous result of eliminating the Epsilons
  4.) Create a table of accepted states for the Converted NFA
