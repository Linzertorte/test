#./generate grammar1 3
import sys
import random

def remove_comment(line):
    last = line.find('#')
    if last == -1:
        return line
    else:
        return line[0:last]

def insert_rule(grammar, lhs, rhs):
    if lhs not in grammar:
        rules = []
        rules.append(rhs)
        grammar[lhs]=rules
    else:
        grammar[lhs].append(rhs)


def get_grammar(grammar_file):
    f = open(grammar_file,'r')
    grammar = {}
    for line in f:
        line = line.rstrip()
        line = remove_comment(line)
        if len(line)==0:
            continue
        symbols = line.split()
        lhs = symbols[1]
        rhs = symbols[2:]
        insert_rule(grammar,lhs,rhs)
    return grammar

def expand(grammar,symbol):
        if symbol not in grammar:
            return symbol
        rules = grammar[symbol] #get rules                
        rule = rules[random.randint(0,len(rules)-1)]
        sentence = ""
        for w in rule:
            sentence += expand(grammar,w) + " "
        return sentence[0:-1]



if __name__=='__main__':
    grammar_file = sys.argv[1]
    grammar = get_grammar(grammar_file)
    for i in xrange(int(sys.argv[2])):
        print expand(grammar,'ROOT')
