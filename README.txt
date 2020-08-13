For the project I completed Simulating a DFA and Minizing a DFA. The code is written in python and is sectioned into 3 main files:
dfa.py, including the DFA class with all the functionalility needed to simulate and minimize a DFA.
simulator.py, a python script to simulate the DFA using a DFA descriptor file and an input file to test input strings
minimizer.py, a python script to minimize a DFA and return a print out of the minimized DFA.

These files will require at least python 3.7 to run. The command line to execute the scripts,
used in the same directory the files are contained in, are:

python simulator.py <dfa> <input>
python minimizer.py <dfa>

where <dfa> is the DFA descriptor text file and <input> is the list of string(s) to be tested in a text file.

DFA descriptor file requirements:
    1. The first three lines must be formatted as such:
        'Number of states: ' <number of states>
        'Accepting states: ' <state(s) separated by a ' ' if multiple>
        'Alphabet: ' <single string of accepted characters, no spaces>
    2. The lines following the first three are the transitions for a state based on input alphabet 
        each state must be in order from state 0 -> state n. For example, 2 states with alphabet 01:
            <state=row> <transition reading 0> <transition reading 1>
                                0                        1
                                1                        1 
        IMPORTANT: All symbols in the alphabet must have a transition listed, blank transition will not parse correctly. 
            Therefore if a state has no transition from reading a specific character the starting state must be
            listed as the resulting transition reading that symbol. ie. state 0 reading a results in state 0.

Input file requirements:
    1. A string of any length can be checked but each string must be seperated by a new line.
    2. No special character is required to signify the end of file. 

    NOTE: Entering a symbol that is not in the DFA's language will automatically cause the string to be rejected. 

Upon running simulator.py output will be written to standard output in the form of:
    Accept: <string>
    --or--
    Reject: <string>
    --or--
    Reject: <string>
    Invalid Symbol: <symbol>

Upon running minimizer.py output will be written to standard output in the form of:
    Number of states: <number>
    Accepting states: <numbers, each state in closed brackets []>
    Alphabet: <single string no spaces>
    New states:
    <state(s), each state in closed brackets []>
    Transitions from new states in order: <each state will be in its own row>
    <one state transition per alphabet symbol in order, each state in closed brackets []> 
