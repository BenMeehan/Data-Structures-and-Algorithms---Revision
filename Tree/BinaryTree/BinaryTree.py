class Node:
    def __init__(self,d):
        self.data=d 
        self.left=None 
        self.right=None 

class BT:   
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def getInput(self,root):
        n=int(input("Enter value : "))
        if n==-1:
            return None 
        root=Node(n)
        root.left=self.getInput(root.left)
        root.right=self.getInput(root.right)
        return root
        
    def nnodes(self,root):
        if root==None:
            return 0
        return 1+self.nnodes(root.left)+self.nnodes(root.right)
    
    def sumofnodes(self,root):
        if root==None:
            return 0
        return root.data+self.sumofnodes(root.left)+self.sumofnodes(root.right)
   
    def largest(self,root):
        if root==None:
            return None
        if root.left==None and root.right==None:
            return root.data
        l=self.largest(root.left)
        r=self.largest(root.right)
        return max(root.data,l,r)

    def greaterThan(self,root,x):
        if root==None:
            return 0 
        if root.data>x:
            return 1+self.greaterThan(root.left,x)+self.greaterThan(root.right,x)
        return self.greaterThan(root.left,x)+self.greaterThan(root.right,x)
    
    def height(self,root):
        if root==None:
            return 0 
        return 1+max(self.height(root.left),self.height(root.right))

    def leaves(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leaves(root.left)+self.leaves(root.right)
    
    def printAtDepth(self,root):
        if root==None:
            return 

        q=[]
        q.append(root)
        print(q)
        while len(q)>0:
            e=q.pop(0)
            print(e.data)
            if e.left is not None:
                q.append(e.left)
            if e.right is not None:
                q.append(e.right)

    def replaceDepth(self,root,d):
        if root==None:
            return
        root.data=d 
        self.replaceDepth(root.left,d+1)
        self.replaceDepth(root.right,d+1)

    def isPresent(self,root,d):
        if root==None:
            return False
        if root.data==d:
            return True
        return self.isPresent(root.left,d) or self.isPresent(root.right,d)

    def noSibling(self,root):
        if root==None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is None and root.right is not None:
            return 1+self.noSibling(root.right)
        if root.right is None and root.left is not None:
            return 1+self.noSibling(root.left)
        return self.noSibling(root.left)+self.noSibling(root.right)
        
    def removeLeaf(self,root):
        if root==None:
            return 
        if root.left==None and root.right==None:
            return None 
        root.left=self.removeLeaf(root.left)
        root.right=self.removeLeaf(root.right)
        return root
    def mirror(self,root):
        if root==None:
            return

        t1=self.mirror(root.right)
        t2=self.mirror(root.left)
        root.left=t1
        root.right=t2
        return root

    def checkBalance(self,root):
        if root==None:
            return 0,True  
        lh,isLeft=self.checkBalance(root.left)
        rh,isRight=self.checkBalance(root.right)
        h=1+max(lh,rh)
        if abs(lh-rh)>=2:
            return h,False 
        else:
            return h,True and isLeft and isRight
root=0 
t=BT()
root=t.getInput(root)
t.inorder(root)

# print(t.nnodes(root))
# print(t.sumofnodes(root))
# print(t.largest(root))
# print(t.greaterThan(root,5))
# print("height ",t.height(root))
# print("leaves ",t.leaves(root))
# t.replaceDepth(root,0)
# t.printAtDepth(root)
# print(t.isPresent(root,5))
# print(t.noSibling(root))

# root=t.removeLeaf0(root)
# root=t.mirror(root)
# t.inorder(root)
print(t.checkBalance(root))