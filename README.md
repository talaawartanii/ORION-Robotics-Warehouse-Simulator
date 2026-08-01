🤖 ORION Robotics

Autonomous Multi-Robot Warehouse Simulator

About The Project

ORION Robotics is a warehouse simulation project I built to explore how autonomous robots can work together in a smart warehouse environment.

The idea is inspired by real-world warehouse automation systems, where multiple robots need to move packages efficiently, avoid obstacles, manage their battery, and complete tasks without human control.

This project started as a learning experiment in robotics and AI, but it evolved into a complete simulation system with path planning, task assignment, robot coordination, and a monitoring dashboard.
## Demo

![ORION Robotics Warehouse Simulation](screenshot%201.png)

⸻

What The Simulator Does

The warehouse contains multiple autonomous robots that can:

* Receive package delivery tasks automatically
* Calculate efficient routes using A*
* Navigate around shelves and obstacles
* Avoid collisions with other robots
* Pick up and deliver packages
* Monitor battery levels
* Travel to charging stations when needed

The simulation runs on a grid-based warehouse map where each robot makes decisions based on its current state.

⸻

Main Systems Implemented

🧭 A* Path Planning

The robots use the A* algorithm to find efficient paths between locations.

The implementation includes:

* Grid-based navigation
* Manhattan distance heuristic
* Obstacle detection
* Path reconstruction

⸻

🤖 Multi-Robot System

The simulator supports multiple robots working at the same time.

Each robot has:

* Unique ID
* Individual path
* Battery level
* Current task
* Operational status

Robots also check nearby robots to reduce collisions during movement.

⸻

📦 Package Management

Packages have their own lifecycle:

Waiting → Assigned → Picked Up → Delivered

A task manager automatically assigns available packages to idle robots.

⸻

🔋 Battery & Charging System

Robots continuously monitor their battery level.

When energy becomes low:

* The robot changes its state
* Finds the charging station
* Recharge before continuing operations

⸻

📊 Warehouse Dashboard

The interface displays:

* Number of active robots
* Robot states
* Battery percentage
* Waiting packages
* Completed deliveries

⸻

Technologies

* Python
* Pygame
* Object-Oriented Programming
* A* Search Algorithm
* Simulation Design
* Grid-Based Robotics Navigation

⸻

Project Structure

src/
│
├── main.py
├── robot.py
├── astar.py
├── node.py
├── grid_map.py
├── environment.py
├── package.py
├── task_manager.py
│
└── ui/
    ├── splash_screen.py
    └── button.py

⸻

Controls

* P → Pause / Resume simulation
* R → Reset simulation

⸻

Current Version

This is the first milestone of ORION Robotics.

The current version focuses on:

* Autonomous navigation
* Multi-robot behavior
* Warehouse simulation logic

Future versions will explore more advanced robotics concepts such as better coordination strategies, optimization methods, and real-world robotics frameworks.

⸻

Tala
Robotics & Artificial Intelligence 
Engineering Student


