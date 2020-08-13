"""
Simple main to minimize a dfa, create a new transition
table and print.
"""

import sys
from dfa import DFA

if __name__ == '__main__':
    A_DFA = DFA(sys.argv[1])
    A_DFA.partition_dfa()
    A_DFA.minimize_dfa()
    A_DFA.new_table()
    A_DFA.format_print()
