class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertLevelOrder(arr, root, i, n):
    if i < n: 
        temp = Node(arr[i])  
        root = temp 
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n) 
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

def largestValues(root):
        if not root:
            return None
        levels = [root]
        res = [root.val]
        while levels:
            val_arr = []
            node_arr = []
            for node in levels:
                if node.left:
                    if node.left.val!="null":
                        val_arr.append(node.left.val)
                        node_arr.append(node.left)
                        print(node.left.val)
                if node.right:
                    if node.right.val!="null":
                        val_arr.append(node.right.val)
                        node_arr.append(node.right)
                        print(node.right.val)
            if not val_arr:
                break
            res.append(max(val_arr))
            levels = node_arr
        return " ".join(res)
 
tree = input().split()
root1=None
root=insertLevelOrder(tree,root1,0,len(tree))
print(largestValues(root))
