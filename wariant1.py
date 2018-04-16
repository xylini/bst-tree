from random import randint
from statistics import median


class TNode:
    # The node in tree contains: value, left child, right child and it's level (height)
    def __init__(self, value=None, level=None):
        self.value = value
        self.left = None
        self.right = None
        self.level = level

    def insert_node(self, value, level=1):
        if self.value is None:
            self.value = value
            self.level = 0
        elif value <= self.value:
            if self.left is None:
                self.left = TNode(value, level)
            else:
                self.left.insert_node(value, level+1)
        else:
            if self.right is None:
                self.right = TNode(value, level)
            else:
                self.right.insert_node(value, level+1)

    # Traversing using recursion
    def traverse(self):
        if self.left is not None:
            self.left.traverse()
        print(self.level * "--" + str(self.value))
        if self.right is not None:
            self.right.traverse()

    # Counts nodes in tree
    def count_nodes(self):
        el_s = 0
        stack = [self]
        while len(stack):
            el = stack.pop()
            el_s += 1
            if el.right is not None:
                stack.append(el.right)
            if el.left is not None:
                stack.append(el.left)
        return el_s

    # Returns median of the elements in tree
    def median(self):
        count = self.count_nodes()                  # count nodes
        is_even = (count % 2 == 0)                  # check type of median
        if is_even:
            steps = count/2 + 1
        else:
            steps = (count + 1)/2

        current = self                              # node which is currently proceed
        prev_val = self.value                       # prev_val and curr_val -> to calculate median
        curr_val = self.value
        stack = []                                  # stack

        while steps:                                # traverse until find median
            while current is not None:
                stack.append(current)
                current = current.left

            if current is None:
                if len(stack) != 0:
                    top = stack.pop()
                    current = top.right
                    prev_val, curr_val = curr_val, top.value
                    steps -= 1
                else:
                    break
        if is_even:
            return (prev_val + curr_val)/2
        else:
            return curr_val

    # Calculate a sum of elements from current node to its leaves
    def subtree_sum(self):
        res = 0
        if self.left is not None:
            res += self.left.subtree_sum()

        res += self.value
        if self.right is not None:
            res += self.right.subtree_sum()

        return res

    # Calculates the average of
    def average(self):
        summ = 0
        el_s = 0
        stack = [self]
        while len(stack):
            el = stack.pop()
            summ += el.value
            el_s += 1
            if el.right is not None:
                stack.append(el.right)
            if el.left is not None:
                stack.append(el.left)

        return summ / el_s


def main():

    trees = []
    values = []
    for i in range(10):
        trees.append(TNode())
        tmp = []
        for j in range(10):
            tmp.append(randint(0, 100))
            trees[-1].insert_node(tmp[-1])
        values.append(tmp)

    # tests for 10 random lists
    for i in range(10):
        print("Tree nr " + str(i) + ": sum - " + str(trees[i].subtree_sum()) + ", avg - " + str(trees[i].average()) +
              ", median - " + str(trees[i].median()))
        print("List nr " + str(i) + ": sum - " + str(sum(values[i])) + ", avg - " + str(sum(values[i])/len(values[i])) +
              ", median - " + str(median(values[i])))
        print()

if __name__ == "__main__":
    main()
