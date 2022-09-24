"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res_ls = list()
        dic = dict()
        def hasChildren(node):
            if not node:
                return
            else:
                res_ls.append(node.val)
                if node.children:
                    for child in node.children:
                        hasChildren(child)
        
        hasChildren(root)
        return res_ls
                