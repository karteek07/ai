def BFS(tree,level=["A"]):
  bfs_list = []
  if len(level) > 0:
    bfs_list += level
    sub_level = []
    for vertex in level:
      sub_level += tree[vertex]
    bfs_list += BFS(tree,sub_level)
  return bfs_list


#            ___A___
#           /       \
#          C         D
#        / | \     / | \
#       P  R  L   F  Q  S
#         / \       / \
#        O   E     G   H
#                 / \
#                N   M
#
tree = {
        "A" : ["C", "D"], 
        "C" : ["P","R","L"],
        "R" : ["O","E"],
        "G" : ["N", "M"], 
        "Q" : ["G", "H"], 
        "D" : ["F", "Q", "S"],
        "P" : [], 
        "L" : [], 
        "N" : [], 
        "M" : [], 
        "H" : [], 
        "S" : [], 
        "F" : [], 
        "O" : [], 
        "E" : []}

print(BFS(tree))