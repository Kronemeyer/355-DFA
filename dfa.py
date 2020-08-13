"""
DFA class creates a DFA from an input file and parses through a secondary input file
to deteremine whether or not the input to the DFA is accepted or rejected.
"""

class DFA:
    """
    Main class to create a DFA and hold the transition table, T, the Final accepting states, F,
    and the valid alphabet, Σ, accepted by the DFA
    """

    def __init__(self, path):
        """
        read input from file path of a DFA text file.
        First Line: q_num, Total number of states
        Second Line: final_states, Final states
        Third Line: alphabet, one string with no breaks describing acceptable alphabet
        Next 'S' lines will have |alphabet| columns showing if in in Si reading Σi go to Sx
        Create a transition table, T, from the possible transitions
        """
        file = open(path)
        line = file.readline().replace('Number of states: ', '')
        q_num = int(line)

        line = file.readline().replace('Accepting states: ', '')
        line = line.split(" ")
        self.final_states = [state.replace("\n", '') for state in line]

        line = file.readline().replace('Alphabet: ', '')
        self.alphabet = [char for char in line if char != '\n']

        table = {}
        for state in range(q_num):
            trans = {}
            line = file.readline()
            line = line.split()
            counter = 0
            for transition in self.alphabet:
                trans[transition] = line[counter]
                counter += 1
            table[str(state)] = trans
        self.transition_table = table
        self.partition = None

    def check_string(self, string):
        """
        read input strings that will be processed by DFA.
        each line is one input, followed by a new line character (not to be included with string).
        start in state 0, process input string one char at a time via transition table T,
        print to standard output either 'Accept' or 'Reject' based on F
        """
        state = '0'
        for char in string:
            if char not in self.alphabet:
                state = -1
                invalid = char
                break
            state = self.transition_table[state][char]

        if state == -1:
            print(f'Reject:\t{string}\nInvalid Symbol: {invalid}')
        elif state in self.final_states:
            print(f'Accept:\t{string}')
        else:
            print(f'Reject:\t{string}')

    def partition_dfa(self):
        """
        divide all states into a set of either final or non-final states to
        start the minimization algorithm
        """
        non_final = self.transition_table.keys()
        non_final = non_final - self.final_states
        non_final = sorted(non_final, key=None, reverse=False)
        self.partition = [self.final_states, non_final]

    def minimize_dfa(self):
        """
        First make a copy of the partition made, will be used as a queue.
        Then check one section of the copy at a time using each legal character in
        the language for each state and record which transitions lead to a state in
        the section. Those transitions are recorded in states and are used
        to find distinguishable states. Then use those valid
        transition states and find the intersection and difference in both. If those
        values are non-empty, remove original set of states from original partition
        and replace it with the difference and intersection sets.
        """
        part_k = self.partition.copy()
        while part_k:
            section = part_k.pop(0)
            for char in self.alphabet:
                states = []
                for state in self.transition_table:
                    if self.transition_table[state][char] in section:
                        states.append(state)
                for state_set in self.partition:
                    diff = [state for state in state_set if state not in states]
                    inter = [state for state in states if state in state_set]
                    if diff and inter:
                        self.partition.remove(state_set)
                        self.partition.insert(0, diff)
                        self.partition.insert(0, inter)
                        if state_set in part_k:
                            part_k.remove(state_set)
                            part_k.insert(0, diff)
                            part_k.insert(0, inter)

    def new_table(self):
        """
        creates a new transition table based on final partition and any
        transitions into a new state that includes a final state
        """
        new_table = {}
        for state in self.partition:
            new_transition = {}
            for char in self.alphabet:
                trans = self.transition_table[state[0]][char]
                if trans in state:
                    trans_state = state
                else:
                    for check in self.partition:
                        if trans in check:
                            trans_state = check
                new_transition[char] = trans_state
            new_table[repr(state)] = new_transition
        self.partition = new_table
        new_finals = []
        for final in self.final_states:
            for state in self.partition:
                if final in state:
                    new_finals.append(state)
        self.final_states = new_finals

    def format_print(self):
        """
        Format the output for reading
        """
        q_num = len(self.partition.keys())
        print(f'Number of states: {q_num}')
        print('Accepting states:', end=" ")
        for final in self.final_states:
            print(final, end=" ")
        print()
        print('Alphabet: ', end=" ")
        for char in self.alphabet:
            print(char, end="")
        print()
        print('New states: ')
        for state in self.partition:
            print(state, end=" ")
        print('\nTransitions from new states in order: ')
        for state in self.partition:
            for key in self.partition[state]:
                print(self.partition[state][key], end=" ")
            print()
