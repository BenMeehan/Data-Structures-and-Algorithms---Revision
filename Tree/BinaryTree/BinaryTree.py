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

    def diameter(self,root):
        if root==None:
            return 0
        dia=self.height(root.left)+self.height(root.right)
        lh=self.diameter(root.left)
        rh=self.diameter(root.right)

        if lh>dia:
            return lh 
        elif rh>dia:
            return rh 
        else:
            return dia

    def levelInput(self,root):
        q=[]
        n=int(input("Enter value : "))
        root=Node(n)
        q.append(root)

        while len(q)>0:
            i=q.pop(0)
            n=int(input("Enter the value : "))
            if n!=-1:
                i.left=Node(n)
                q.append(i.left)  
            n=int(input("Enter the value : "))
            if n!=-1:
                i.right=Node(n)
                q.append(i.right)   
        return root  

    def postorder(self,root):
        if root==None:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)
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

        # print(lin,rin,lpre,rpre)

        left=self.construct(lin,lpre)
        right=self.construct(rin,rpre)

        # if left is not None:
        #     print(left.right)
        #     self.inorder(left)
        # if right is not None:
        #     self.inorder(right)

        root.left=left
        root.right=right

        return root

    def duplicate(self,root):
        if root==None:
            return 
        temp=root.left
        root.left=Node(root.data)
        root.left.left=temp

        self.duplicate(root.left.left)
        self.duplicate(root.right)
        return root

    def sumToLeaf(self,root,k,arr):
        # print(arr)
        if root==None:
            return 0
        
        n=sum(arr)+root.data

        if n==k:
            arr.append(root.data)
            print(arr)
            return 0
        elif n>k:
            return 0
        elif n<k:
            temp1=arr.copy()
            temp1.append(root.data)
            temp2=arr.copy()
            temp2.append(root.data)
            self.sumToLeaf(root.right,k,temp1)+self.sumToLeaf(root.left,k,temp2)
            return 0

    def getDepth(self,root,n,d):
        if root==None:
            return None 
        elif root.data==n:
            return d 
        v=self.getDepth(root.left,n,d+1)
        if v is not None:
            return v
        v=self.getDepth(root.right,n,d+1)
        if v is not None:
            return v
    
    def atDistance(self,root,dt,to):
        if to==None:
            return 0
        dt[to.data]=self.getDepth(root,to.data,0)
        self.atDistance(root,dt,to.left)
        self.atDistance(root,dt,to.right)
        
        return dt

    def fromDist(self,targ,root,k):
        dt=self.atDistance(root,{},root)
        req=dt[targ]

        for ke,v in dt.items():
            if ke==targ:
                continue
            if v-req==k or v+req==k:
                print(ke) 

        
root=0 
t=BT()
# root=t.levelInput(root)
# t.inorder(root)

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
# print(t.checkBalance(root))


# print(t.diameter(root))
root=t.construct([6,5,7,2,4,3,0,1,8],[3,5,6,2,7,4,1,0,8])
# t.postorder(root)
# root=t.duplicate(root)
# t.sumToLeaf(root,7,[])
# t.postorder(root)
t.fromDist(5,root,2)