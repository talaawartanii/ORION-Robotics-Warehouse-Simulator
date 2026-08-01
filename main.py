import pygame
import sys
from environment import Environment
from robot import Robot
from grid_map import GridMap
from astar import AStar
from package import Package 
from task_manager import TaskManager
from ui.splash_screen import show_splash
from ui.button import Button
# ----------------------------
# ORION ROBOTICS
# Warehouse Intelligence Simulator
# Milestone 1
# ----------------------------

pygame.init()

# Window size
WIDTH = 1000
HEIGHT = 700
CELL_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
show_splash(screen)
pause_button = Button(
    30,
    620,
    120,
    40,
    "PAUSE"
)
reset_button = Button(
    170,
    620,
    120,
    40,
    "RESET"
)
warehouse = Environment()
robots = [
    Robot(100, 100, 1),
    Robot(200, 100, 2),
    Robot(300, 100, 3)
]
robots[0].color = (0, 200, 255)
robots[1].color = (255, 100, 100)
robots[2].color = (100, 255, 100)
packages = [
    Package((6, 8), (1, 18)),
    Package((10, 12), (2, 17)),
    Package((12, 5), (1, 17))
]
task_manager = TaskManager(packages)

grid_map = GridMap(WIDTH, HEIGHT, CELL_SIZE)
for shelf in warehouse.shelves:
    grid_map.add_obstacle(shelf)
planner = AStar(grid_map)
for i in range(3):
    robot_row = int(robots[i].y // CELL_SIZE)
    robot_col = int(robots[i].x // CELL_SIZE)
    start = (robot_row, robot_col)
    path = planner.find_path(start, packages[i].position)
    robots[i].path = path
    print("Robot", i+1,path)
pygame.display.set_caption(
    "ORION ROBOTICS | Warehouse Intelligence Simulator"
)

# Colors
BACKGROUND = (25, 28, 35)
GRID_COLOR = (55, 60, 70)
TEXT_COLOR = (220, 230, 240)
PANEL_COLOR = (40, 45, 55)
def draw_dashboard(screen, robots, packages, completed_orders):
        

     font = pygame.font.Font(None, 24)

     panel = pygame.Rect(
         650,
         500,
         330,
         250
     )

     pygame.draw.rect(screen, PANEL_COLOR, panel)

     idle = 0
     delivering = 0
     pickup = 0

     total_battery = 0

     for robot in robots:

        total_battery += robot.battery

        if robot.status == "Idle":
            idle += 1

        elif robot.status == "Delivering":
            delivering += 1

        elif robot.status == "Going to pickup":
            pickup += 1

     waiting = 0
     delivered = 0

     for package in packages:

            if package.status == package.WAITING:
                waiting += 1

            elif package.status == package.DELIVERED:
                delivered += 1

     average_battery = total_battery / len(robots)

     lines = [

        "ORION ROBOTICS CENTER",
        " ",
        f"Robots: {len(robots)}",
        f'Completed Orders: {completed_orders}',
        
        f"Idle: {idle}",
        
        f"Pickup: {pickup}",
        
        f"Delivering: {delivering}",
        
        F"Waiting: {waiting}",
        
        f"Delivered: {delivered}",
        
        f"Battery Avg: {average_battery:.1f}%"

    ]
     for robot in robots:
        lines.append(f"Robot {robot.robot_id}: {robot.status} {int(robot.battery)}%")
     lines += [
        " ",
        f"Waiting: {waiting}",
        f"Delivered: {delivered}",
        f"Battery Avg: {average_battery:.1f}%"
    ]

     y = 505

     for line in lines:

        text = font.render(line, True, TEXT_COLOR)

        screen.blit(text, (680, y))

        y += 15
def draw_controls(screen):
    font = pygame.font.Font(None, 25)
    text = font.render(
       "P: Pause       R: Reset",
       True,
       (220,220,220) 
    )
    screen.blit(
        text,
        (30,650)
    )

# Grid settings
CELL_SIZE = 50
def reset_simulation():
    global robots, packages, task_manager, grid_map, planner
    robots = [
        Robot(100, 100, 1),
        Robot(200, 100, 2),
        Robot(300, 100, 3)
    ]
    robots[0].color = (0, 200, 255)
    robots[1].color = (255, 100, 100)
    robots[2].color = (100, 255, 100)
    packages = [
        Package((6, 8), (1, 18)),
        Package((10, 12), (2, 17)),
        Package((12, 5), (1, 17))
    ]
    task_manager = TaskManager(packages)

   


# Main loop

running = True
paused = False
completed_orders = 0
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                paused = not paused

                if paused:
                    pause_button.set_text("RESUME")
                else:
                    pause_button.set_text("PAUSE")

            if event.key == pygame.K_r:
                reset_simulation()


        if event.type == pygame.MOUSEBUTTONDOWN:

            if pause_button.rect.collidepoint(event.pos):

                paused = not paused

                if paused:
                    pause_button.set_text("RESUME")
                else:
                    pause_button.set_text("PAUSE")


            if reset_button.rect.collidepoint(event.pos):

                reset_simulation()             
    keys = pygame.key.get_pressed()
    if not paused:
      task_manager.assign_tasks(robots, planner)
      completed_orders = 0
      for package in packages:
         if package.status == "Delivered":
            completed_orders += 1

      for robot in robots:
     
          robot.follow_path(planner, warehouse, robots)

    # Background
    screen.fill(BACKGROUND)

    # Draw warehouse grid
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, y),
            (WIDTH, y)
        )
    
    warehouse.draw(screen)
    grid_map.draw(screen)
    for robot in robots:
        grid_map.draw_path(screen, robot.path)
    for i in range(3):
        if robots[i].status == "Delivering":
            packages[i].position = (
                int(robots[i].y // CELL_SIZE),
                int(robots[i].x // CELL_SIZE)
            )
        elif packages[i].status == "Delivered":
            packages[i].position = packages[i].destination  
        packages[i].draw(screen, CELL_SIZE)      
    for robot in robots:
        robot.draw(screen)
    draw_dashboard(screen, robots, packages, completed_orders)
    pause_button.draw(screen)
    reset_button.draw(screen)

       
    

    # Title
    font = pygame.font.Font(None, 40)

    title = font.render(
        "ORION ROBOTICS",
        True,
        TEXT_COLOR
    )

    screen.blit(title, (30, 20))
    if paused:
        pause_font = pygame.font.Font(None, 60)
        pause_text = pause_font.render(
            "PAUSED",
            True,
            (255, 80, 80)
        )
        screen.blit(
            pause_text,
            (430, 300)
        )
    
    

    
    pygame.display.update()


pygame.quit()
sys.exit()