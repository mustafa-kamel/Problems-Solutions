# This python code snippet finds if there's a parenthesis match/mismatch

def check(str):
    ls=[]
    for ch in str:
        if ch not in "()":
            continue
        if ')' == ch and len(ls) and '('== ls[-1]:
            del ls[-1]
        else:
            ls.append(ch)
    return int(not len(ls))


# Testing the code
strs = ["((Hello) world))", "(This (will)) (pass)", "((And)((This won't') (pass))", ")(Also(this)on(e))", "()))()()"]

for str in strs:
    print(check(str))