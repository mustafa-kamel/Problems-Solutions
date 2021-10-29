def funWithAnagrams(text):
    ls, ret = [], []
    dic = {}
    for word in text:
        dic = dict((letter,word.count(letter)) for letter in set(word))
        if hash(frozenset(dic.items())) not in ls:
            ls.append(hash(frozenset(dic.items())))
            ret.append(word)
    return sorted(ret)

inputList = ['code', 'doce', 'aaanagrams', 'anagrams', 'ocde', 'aaangrms']
print(funWithAnagrams(inputList))