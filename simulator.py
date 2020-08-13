"""
Simple main to initialize a dfa and test input strings.
Read from input until empty string is read, then terminate
"""
import sys
from dfa import DFA

if __name__ == '__main__':
    A_DFA = DFA(sys.argv[1])
    IN_FILE = open(sys.argv[2])
    IN_STRING = IN_FILE.readline().replace('\n', '')
    while IN_STRING != '':
        A_DFA.check_string(IN_STRING)
        IN_STRING = IN_FILE.readline().replace('\n', '')
