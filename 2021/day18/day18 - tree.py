import ast
lines = []
with open('test1.txt') as f:
    for line in f:
        line = ast.literal_eval(line.strip())
        lines.append(line)
f.close()

class Node:
    def __init__(self, val, depth=0):
        self.left = None
        self.right = None
        self.parent = None
        self.val = None
        self.depth = depth

        if type(val) == int:
            self.val = val
        else: # If value is list, split into left anf right and set parent
            self.left = Node(val[0], depth+1)
            self.right = Node(val[1], depth+1)
            self.left.parent = self
            self.right.parent = self

    def isleafNode(self): # A leaf node has its own value
        return self.val != None

    def root(self): # Root node has no parent
        x = self
        while x.parent is not None:
            x = x.parent
        return x

    def leaves(self): 
        if self.isleafNode(): # Return if it is a leaf node
            return [self]
        else: # Else find leaves in both left and right side
            x = []
            if self.left is not None:
                x += self.left.leaves()
            if self.right is not None:
                x += self.right.leaves()
            return x

    def ispair(self): # A pair is 2 values from the same parent
        left = self.left is not None and self.left.isleafNode()
        right = self.right is not None and self.right.isleafNode()
        return left and right

    def explode(self):
        leaves = self.root().leaves()
        # Find left value to update
        if self.left.isleafNode() and leaves.index(self.left) > 0:
            # A value on the left of the exploding list exist
            pos = leaves.index(self.left) - 1
            leaves[pos].val += self.left.val

        # Find right value to update
        if self.right.isleafNode() and leaves.index(self.right) < (len(leaves)-1):
            # A value on the right of the exploding list exist
            pos = leaves.index(self.right) + 1
            leaves[pos].val += self.right.val

        # Set exploding list to 0
        self.left = None
        self.right = None
        self.val = 0

    def split(self):
        self.left = Node(self.data//2, self.depth+1)
        self.right = Node(self.data//2 + 1, self.depth+1)
        self.left.parent = self
        self.right.parent = self
        self.data = None

    def simplify(self):
        def check_explode(x):
            nonlocal flag
            if not flag and x.left != None:
                check_explode(x.left)

            if not flag and x.right != None:
                check_explode(x.right)
                
            if not flag and x.ispair() and x.depth >= 4:
                x.explode()
                flag = True

        def check_split(x):
            nonlocal flag
            if not flag and x.left != None:
                check_split(x.left)

            if not flag and x.right != None:
                check_split(x.right)

            if not flag and x.isleafNode() and x.val >= 10:
                x.split()
                flag = True

        while True:
            flag = False
            if not flag:
                check_explode(self)
                
            if not flag:
                check_split(self)

            if not flag:
                break

    def magnitude(self):
        if self.isleaf():
            return self.data
        else:
            return 3*self.left.magnitude() + 2*self.right.magnitude()
                
final = Node(lines[0])
final.simplify()
for line in lines[1:]:
    # Add next line
    line = Node(line)
    line.simplify()
    final = Node([final, line])

print(final.magnitude())



            
