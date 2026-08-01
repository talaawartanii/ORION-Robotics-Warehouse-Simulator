class Node:

    def __init__(self, position):

        self.position = position

        # Cost from start node
        self.g_cost = 0

        # Estimated cost to goal
        self.h_cost = 0

        # Total cost
        self.f_cost = 0

        # Previous node in the path
        self.parent = None


    def calculate_f_cost(self):

        self.f_cost = self.g_cost + self.h_cost