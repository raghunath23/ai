from collections import defaultdict

class FamilyTree:
    def __init__(self, head_name):
        self.family = defaultdict(list)
        self.head = head_name
        self.dead = set()

    def birth(self, p_name, c_name):
        self.family[p_name].append(c_name)

    def death(self, name):
        self.dead.add(name)

    def inheritance(self):
        self.ans = []
        self.search(self.head)
        return self.ans

    def search(self, current):
        if current not in self.dead:
            self.ans.append(current)
        for child in self.family[current]:
            self.search(child)

# Create an instance of FamilyTree with the head's name
head_name = input("Enter the Head: ")
ob = FamilyTree(head_name)

# Input the number of children
n = int(input("Enter no. of children: "))

# Input parent-child relationships
for _ in range(n):
    parent, child = input("Enter parent-child: ").split()
    ob.birth(parent, child)

# Print inheritance before and after head's death
print("Inheritance before head's death:", ob.inheritance())
ob.death(head_name)
print("Inheritance after head's death:", ob.inheritance())
