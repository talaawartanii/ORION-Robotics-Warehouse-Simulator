import pygame


class Robot:

    def __init__(self, x, y, robot_id):

        self.x = x
        self.y = y
        self.robot_id = robot_id

        self.width = 35
        self.height = 35

        self.speed = 3

        self.battery = 100
        self.low_battery_threshold = 20
        self.charging = False
        self.going_to_charge = False
        self.path = []
        
        self.status = "Idle"
        self.charging = False
        self.current_package = None
        self.delivery_goal = None
        self.color = (0, 200, 255)

    def move(self, keys, environment):
        old_x = self.x
        old_y = self.y

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        robot_rect = pygame.Rect(
            
            self.x,
            self.y,
            self.width,
            self.height
        )    
        if environment.check_collision(robot_rect):
            self.x = old_x
            self.y = old_y
    def follow_path(self, planner, environment, robots):
     old_x = self.x
     old_y = self.y
     for other_robot in robots:
        if other_robot != self:
            distance = ((self.x - other_robot.x) ** 2 + (self.y - other_robot.y) ** 2) ** 0.5
            if distance < 50:
               return 
     if self.battery <= self.low_battery_threshold and not self.going_to_charge:
        self.go_charge(planner, environment)
     if (
        self.battery <= 30
        and self.status == "Idle"
        and self.current_package is None
     ):
        self.status = "Charging"
        start = (
           int(self.y // 50),
           int(self.x // 50)
        )
        charging_goal = (11, 1)
        self.path = planner.find_path(start, charging_goal)
      
     if len(self.path) == 0:
        return
     self.battery -= 0.02
     if self.battery < 0:
        self.battery = 0
        return


     target_row, target_col = self.path[0]
     print(self.color,"moving to:", target_row, target_col, "current", int(self.y // 50), int(self.x // 50), "status:", self.status)


     target_x = target_col * 50
     target_y = target_row * 50


     if abs(self.x - target_x) < self.speed:
        self.x = target_x

     else:
        if self.x < target_x:
            self.x += self.speed

        elif self.x > target_x:
            self.x -= self.speed
     robot_rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
     if environment.check_collision(robot_rect):
        self.x = old_x
        self.y = old_y     
          



     if abs(self.y - target_y) < self.speed:
        self.y = target_y

     else:
        if self.y < target_y:
            self.y += self.speed

        elif self.y > target_y:
            self.y -= self.speed


     robot_rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
     if environment.check_collision(robot_rect):
        self.x = old_x
        self.y = old_y
        return
     if abs(self.x - target_x) <= self.speed and abs(self.y - target_y) <= self.speed:
        self.x = target_x
        self.y = target_y
        self.path.pop(0)
     
     if self.current_package:
        package_row, package_col = self.current_package.position
        robot_row = int(self.y // 50)
        robot_col = int(self.x // 50)
        print(
           "Robot:", robot_row, robot_col, "Package:", package_row, package_col
        )
        if abs(robot_row - package_row) <= 1 and abs(robot_col - package_col) <= 1 and self.status == "Going to pickup":
         print("PICKUP TRIGGERED")
         self.current_package.status = self.current_package.PICKED_UP
         self.status = "Delivering"
         print("Robot switched to delivery mode")
         goal = self.delivery_goal
         new_path = planner.find_path(
            self.current_package.position, 
            goal
         )
         self.path = new_path 
         
         

         print("Delivery:", self.path)
         return
     if self.status == "Delivering" and self.current_package and len(self.path) == 0:
                  
         print("DELIVERY COMPLETED")
                  
         self.current_package.status = self.current_package.DELIVERED
         self.current_package.delivered = True
         self.current_package = None 
         self.status = "Idle"
     if self.status == "Charging" and len(self.path) == 0:
        self.battery += 0.5
        if self.battery >= 100:
           self.battery = 100  
           self.status = "Idle"  
            
    def charge(self):
       if self.chargeing:
          self.battery += 0.5
          if self.battery >= 100:
             self.battery = 100
             self.charging = False
             self.status = "Idle"
    def go_charge(self, planner, environment):
       station_row = environment.charging.station.y // 50
       station_col = environment.charging.station.x // 50
       start = (
          int(self.y // 50),
          int(self.x // 50)
       )
       goal = (station_row, station_col)
       self.path = planner.find_path(start, goal)
       self.status = "Charging"
       self.going_to_charge = True
    def draw(self, screen):

        robot_rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )
        current_color = self.color
        if self.status == "Idle":
            self.color = (80, 220, 100)
        elif self.status == "Going to pickup":
            self.color = (255, 220, 50)
        elif self.status == "Delivering":
            self.color = (0, 200, 255)
        elif self.status == "Charging":
            self.color = (180, 0, 255)
        else:
            current_color = self.color

        pygame.draw.rect(
            screen,
            current_color,
            robot_rect
        )
        #Battery bar
        bar_width = 35
        bar_height = 5
        battery_ratio = self.battery / 100
        pygame.draw.rect(
            screen,
            (80, 80, 80),
            (
                self.x,
                self.y - 10,
                bar_width,
                bar_height
            )
        )
        pygame.draw.rect(
            screen,
            (50, 220, 50),
            (
                self.x,
                self.y - 10,
                bar_width * battery_ratio,
                bar_height
            )
        )
        font = pygame.font.Font(None, 18)
        info = font.render(
           f"R{self.robot_id} | {int(self.battery)}%",
           True,
           (255, 255, 255)
        )
        screen.blit(
           info,
            (
              self.x - 5,
              self.y - 20
            )
        )
