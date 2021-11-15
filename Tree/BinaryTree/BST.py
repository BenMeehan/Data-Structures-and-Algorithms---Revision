import math 

class Node:
    def __init__(self,d):
        self.data=d 
        self.left=None 
        self.right=None 

class BST:
    def construct(self,inorder,preorder):
        if len(preorder)<=0 or len(inorder)<=0:
            return None 
        root=Node(preorder[0])
        c=0
        for i in inorder:
            if i==root.data:
                break
            c+=1


        lin=inorder[:c]
        rin=inorder[c+1:]

        lpre=preorder[1:1+len(lin)]
        rpre=preorder[1+len(lin):]

        left=self.construct(lin,lpre)
        right=self.construct(rin,rpre)

        root.left=left
        root.right=right

        return root
    
    def preorder(self,root):
        if root==None:
            return 
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def search(self,root,k):
        if root==None:
            return -1 
        elif root.data==k:
            return root 
        elif root.data>k:
            return self.search(root.right,k)
        elif root.data<k:
            return self.search(root.left,k)
    
    def inRange(self,root,k1,k2):
        if root==None:
            return -1 

        if root.data<k1:
            self.inRange(root.left,k1,k2)
        elif root.data>k2:
            self.inRange(root.right,k1,k2)
        elif root.data>=k1 and root.data<=k2:
            print(root.data)
            self.inRange(root.left,k1,k2)
            self.inRange(root.right,k1,k2)

    def sortedArrayToBST(self,arr):
        if len(arr)<=0:
            return None 
        
        m=len(arr)//2
        root=Node(arr[m])
        root.left=self.sortedArrayToBST(arr[:m])
        root.right=self.sortedArrayToBST(arr[m+1:])
        return root

    def isBstHelper(self,root,a,b):
        if root==None:
            return True 
        if root.data<=a or root.data>b:
            return False 
        return self.isBstHelper(root.left,a,root.data-1) and self.isBstHelper(root.right,root.data,b)
    def isBst(self,root):
        return self.isBstHelper(root,-math.inf,math.inf)
        
t=BST()
root=None 
# root=t.construct([2,3,4,5,6,7,8],[5,3,2,4,7,6,8])
# t.inorder(root)
# print(t.search(root,10))
# print(t.inRange(root,3,6))
root=t.sortedArrayToBST([1,2,3,4,5,6,7,8])
t.preorder(root)
print(t.isBst(root))