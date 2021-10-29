def counting(s):
    counter, index, ls = 0, 0, []
    while(len(s) > 0):
        ocu = ''
        s = s[index:]
        index +=1
        for bit in s:
            ocu += bit
            if len(ocu) and ocu.count('1') == ocu.count('0'):
                counter += 1
                ls.append(ocu)
                ocu = ''
                break
    return counter, ls

print(counting("00110"))