class TaskManager:

    def __init__(self, packages):
        self.packages = packages


    def assign_tasks(self, robots, planner):

        for robot in robots:

            # if robot is free, give it a package
            if robot.status == "Idle" and robot.battery > 30:

                for package in self.packages:

                    if package.status == package.WAITING:

                        robot.current_package = package
                        robot.delivery_goal = package.destination
                        robot.status = "Going to pickup"

                        start = (
                            int(robot.y // 50),
                            int(robot.x // 50)
                        )

                        robot.path = planner.find_path(
                            start,
                            package.position
                        )

                        package.status = package.ASSIGNED

                        print(
                            "Assigned package to robot",
                            robot.color
                        )

                        break