class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def max_depth(self):
        if self is None:
            return 0;

        else:
            left_depth = self.left.max_depth() if self.left else 0;
            right_depth = self.right.max_depth() if self.right else 0;
            return max(left_depth, right_depth) + 1;
