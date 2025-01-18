def Palidrome(i,str):
    if i>=(len(str)/2):
        return True
    if str[i]!=str[len(str)-i-1]:
        return False
    return Palidrome(i+1,str)

s="Nischal"
result =Palidrome(0,s)
print(result)
    