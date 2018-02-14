import sys
import random 

def rr(L3):
    return random.choice (list(L3))
    
def dict_keys(params):
    listD = []
    d_keys = params.keys()
    for elem in d_keys:
        key = elem.split("_")
        listD.append(int(key[1]))
    return listD

def occupied_to_free(L2):
    L1 = set(list(range(9)))
    L3 = L1 - set(L2)
    return L3

def do_move(params):
    # type: (dict) -> int
    L2 = dict_keys(params)
    print(L2, file=sys.stderr)
    L3 = occupied_to_free(L2)
    print(L3, file=sys.stderr)
    return rr(L3)







