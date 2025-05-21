from typing import List, Optional
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Preorder goes: root, left, right
        Inorder goes left, root, right
        
        So the first node of my preorder traversal is my root. That's a start.
        
        If the first of my inorder is the root, I have a right tree. But assuming we don't then, preorder[1] (2nd val) is the left child of r.
        
        Wait, everything before the root in inorder is part of the left subtree, and everything after the root is part of the right subtree.
        
        It's recursive, too. So if I know the left subtree, I can repeat the process. The root of the left subtree is the second node in preorder. 
        
        How can I tell when I'm out of roots?
        
        Think about this. I know the root. And I can find it's left and right children. So get the root, split the tree, and do buildTree again. It's recursive.
        
        Take the testcase: 
        po = [3, 9, 20, 15, 7]
        io = [9, 3, 15, 20, 7]
        
        Iteration 1:
        po = [3, 9, 20, 15, 7]
        io = [9, 3, 15, 20, 7]
        root = 3
        left = 9
        right = [15, 20, 7]
        
        Iteration 2:
        po = [20, 15, 7]
        io = [15, 20, 7]
        root = 20
        left = 15
        right = 7
        
        So my tree is:
        3.left = 9
        3.right = 20
        20.left = 15
        20.right = 7
        
        Okay, that works. Now how can I code this?
        Here's how: Keep root (Which you know is po[0]) and build that. Use 2 function calls for left and right that call a recursive helper.
        
        The helper has a base case: if there is no node, return None
        Otherwise, assign the left and right nodes to the current accordingly based on the po and io
        
        Let's think more about treeHelper
        Given a node, what exactly should it do?
        It should assign that node's left and right nodes, and call treeHelper on the left and right.
        
        The preorder and inorder passed to it are unmodified, so it must modify them.
        
        First, find the nodes to the left and right using inorder. (9 vs 15, 20, 7)
        Then split preorder based on that.
        And split inorder based on that (remove the root from both)
        
        It also needs to find the left and right children, which it can do as follows:
        node.left = preorder[r-1]
        
        To find node.right, you iterate until you find the first node in preorder that isn't to the left.
        node.right = preorder[first that isn't left or root]
        
        So we can find the halves, and we can find the left/right.
        
        (could be worth using sets as I iterate through due to sizes, runtime is O(nlogn))
        
        Wait, I'm stupid. The left node is always the first node (preorder[1]) after root, not the one to the left in inorder... okay I'm dumb. That explains the error though.
        '''
        
        root = TreeNode(preorder[0])
        
        def treeHelper(node, preorder, inorder):
            if not preorder:
                return 
            if len(preorder) <= 1: # then len(inorder = 1 as well)
                return 
            
            rootIndex = inorder.index(node.val)
            leftInOrder = []
            leftSet = set() # provide O(1) lookups for efficiency, avoids O(n^2logn) complexity.
            rightInOrder = []
            rightSet = set()
            
            leftPreorder = []
            rightPreorder = []
            
            i = 0
            while i != rootIndex:
                leftInOrder.append(inorder[i])
                leftSet.add(inorder[i])
                i += 1
            
            i += 1 # skip root node
            
            while i < len(inorder):
                rightInOrder.append(inorder[i])
                rightSet.add(inorder[i])
                i += 1
            
            #print(node.val, leftInOrder, rightInOrder, leftSet, rootIndex)

            # Now find node.left and node.right
            if leftInOrder:
                leftNode = TreeNode(preorder[1])
            else:
                leftNode = None
            rightNode = None
            for val in preorder:
                if val != node.val and val not in leftSet:
                    rightNode = TreeNode(val)
                    break
            #print(leftNode.val, rightNode.val)
            for val in preorder: # make our new preorder lists for recursive call
                if val in leftSet:
                    leftPreorder.append(val)
                if val in rightSet:
                    rightPreorder.append(val)
            
            if not leftNode:
                node.left = None
            else:
                node.left = leftNode
            if node.left:
                print(node.left.val, leftPreorder, leftInOrder)
                treeHelper(node.left, leftPreorder, leftInOrder)
            node.right = rightNode
            if node.right:
                print(node.right.val, rightPreorder, rightInOrder)
                treeHelper(node.right, rightPreorder, rightInOrder)
                
            
        
        treeHelper(root, preorder, inorder)
        return root