from node import Node


class AStar:

    def __init__(self, grid):

        self.grid = grid


    def heuristic(self, a, b):

        # Manhattan distance

        return abs(a[0] - b[0]) + abs(a[1] - b[1])


    def get_neighbors(self, node):

        neighbors = []

        row, col = node.position


        directions = [

            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)

        ]


        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc


            if (
                0 <= new_row < self.grid.rows
                and
                0 <= new_col < self.grid.cols
            ):

                if self.grid.grid[new_row][new_col] == 0:

                    neighbors.append(
                        Node((new_row, new_col))
                    )


        return neighbors



    def find_path(self, start, goal):

        start_node = Node(start)
        goal_node = Node(goal)


        open_list = []

        closed_list = []


        open_list.append(start_node)


        while open_list:


            current = open_list[0]


            for node in open_list:

                if node.f_cost < current.f_cost:

                    current = node


            open_list.remove(current)

            closed_list.append(current)



            if current.position == goal_node.position:

                path = []

                while current:

                    path.append(
                        current.position
                    )

                    current = current.parent


                return path[::-1]



            for neighbor in self.get_neighbors(current):


                if neighbor.position in [
                    node.position for node in closed_list
                ]:

                    continue



                neighbor.g_cost = current.g_cost + 1

                neighbor.h_cost = self.heuristic(
                    neighbor.position,
                    goal_node.position
                )

                neighbor.calculate_f_cost()

                neighbor.parent = current


                if neighbor.position not in [
                    node.position for node in open_list
                ]:

                    open_list.append(neighbor)



        return []