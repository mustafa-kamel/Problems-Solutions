# [Returns the intersection of the two strings in the array as a comma separated string]
# @param [mixed] $strArr [Input Array]
# @return  [string] [string of comma seprated intersections charactes or false]
def FindIntersection(strArr):
  str1 = strArr[0].split(', ')
  str2 = strArr[1].split(', ')
  intersect = ''
  for ch in str1:
    if ch in str2:
      intersect += ch + ','
  return intersect[0:-1] if intersect else 'false'

# keep this function call here 
# print(FindIntersection(input()))
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
