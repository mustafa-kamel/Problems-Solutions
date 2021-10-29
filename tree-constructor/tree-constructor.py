def TreeConstructor(strArr):
  nodes = {}
  children = []
  for item in strArr:
    item = eval(item)
    if item[0] in children:
      return False
    children.append(item[0])
    if item[1] in nodes:
      nodes[item[1]].append(item[0])
    else:
      nodes[item[1]] = [item[0]]
  for node in nodes.values():
    if len(node) > 2:
      return False
  return True

# keep this function call here 
print(TreeConstructor(input()))