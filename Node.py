class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def max_depth(self):
        if self is None:
            return 0

        else:
            left_depth = self.left.max_depth() if self.left else 0
            right_depth = self.right.max_depth() if self.right else 0
            return max(left_depth, right_depth) + 1

    def max_value(self):
        left_max = self.left.max_value() if self.left else int('-inf')
        right_max = self.right.max_value() if self.right else int('-inf')
        return max(self.data, left_max, right_max)
