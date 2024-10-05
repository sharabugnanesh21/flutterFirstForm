str1 = '4201398675'
str2 = '805'
c = 0
str1Pointer = 0
str2Pointer = 0
trackSet= set()
while (str2Pointer<len(str2)):
  if (str1[str1Pointer] == str2[str2Pointer]):
    trackSet.add(str1[str1Pointer])
    str1Pointer+=1
  else:
    if (str2[str2Pointer] in trackSet):
      trackSet.remove(str1[str1Pointer])
      str1Pointer-=1
    else:
      trackSet.add(str1[str1Pointer])
      str1Pointer+=1
    c+=1
    
print(c)
print('working')
