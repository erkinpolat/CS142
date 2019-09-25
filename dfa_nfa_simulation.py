from threading import Thread

#The NFA

def q_2(s):
    if s[0] == 'b':
        q_1(s[1:])

    
def q_1(s):
    for i in range(len(s)):
        
        if s[i] == 'a':
            t1 = Thread(target=q_2, args=[s[i+1:]])
            t1.start()
            
        if s[i] == 'b':
            q_2(s[i+1:])
            break
            
    tname = threading.currentThread().getName()
    if len(s) == 0:
        print(tname,': accepts' )
        
    print('Main program ends')
    
    
#The DFA

def p_1(s):
    if len(s) == 0:
        print('===> D1 reaches an accept state')
    if s[0] == 'a':
        p_1_2(s[1:])
    if s[0] == 'b':
        p_2(s[1:])
    
    
def p_2(s):
    if s[0] == 'a':
        p_empty(s[1:])
    if s[0] == 'b':
        p_1(s[1:])
    

def p_1_2(s):
    if s[0] == 'a':
        p_1(s[1:])
    if s[0] == 'b':
        p_1_2(s[1:])
    

def p_empty(s):
    return
