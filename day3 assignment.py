def ispangram(str):
    alp = "abcdefghijklmnopqrstuvwxyz"
    for c in alp:
        if c not in str.lower():
            return False
    return True 
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print('yes')
else:
    print("no")                          