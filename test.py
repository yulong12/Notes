
class TreeNode:  
    def __init__(self, value=0, left=None, right=None):  
        self.value = value  
        self.left = left  
        self.right = right  

def find_parent(root, target):  
    def dfs(node, parent):  
        if not node:  
            return None  
        if node.value == target.value:  
            return parent  
        left_parent = dfs(node.left, node)  
        if left_parent:  
            return left_parent  
        return dfs(node.right, node)   
    if root.value == target.value:  
        return None  
    return dfs(root, None)  
  
if __name__ == "__main__":  


    root = TreeNode(1)  
    root.left = TreeNode(2)  
    root.right = TreeNode(3)  
    root.left.left = TreeNode(4)  
    root.left.right = TreeNode(5)   
    target_node = root.left.right  
    parent_node = find_parent(root, target_node)  
      
    if parent_node:  
        print(f"节点 {target_node.value} 的父节点是 {parent_node.value}")  
    else:  
        print(f"节点 {target_node.value} 是根节点，没有父节点")

