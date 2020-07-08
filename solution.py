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
                    val_arr.append(node.left.val)
                    node_arr.append(node.left)
                if node.right:
                    val_arr.append(node.right.val)
                    node_arr.append(node.right)
            if not val_arr:
                break
            res.append(max(val_arr))
            levels = node_arr
        return " ".join(res)
 
