
#direction you have - direction you want - nessisary turn
turn_mapping = {'north':{'north':'forward','east':'right','south':'backward','west':'left'},
                'east':{'north':'left','east':'forward','south':'right','west':'backward'},
                'south':{'north':'backward','east':'left','south':'forward','west':'right'},
                'west':{'north':'right','east':'backward','south':'left','west':'forward'}}

class junction:
    def __init__(self, valid_moves, name):
        self.valid_moves = valid_moves
        self.north = None
        self.south = None
        self.west = None
        self.east = None
        self.name = name

def init_map():
    #Valid moves = (Up, Down, Left, Right)
    #B0 = junction((False, False, False, False), 'B0)
    B1 = junction((True, False, False, True)  , 'B1')
    B2 = junction((True, False, True, True)   , 'B2')
    B3 = junction((True, False, True, False)  , 'B3')
    B4 = junction((True, True, False, True)   , 'B4')
    B5 = junction((True, True, True, True)    , 'B5')
    B6 = junction((True, True, True, True)    , 'B6')
    B7 = junction((True, False, True, False)  , 'B7')
    B8 = junction((False, True, True, False)  , 'B8')
    B9 = junction((True, False, False, True)  , 'B9')
    B10= junction((False, True, True, False)  , 'B10')
    B11= junction((True, False, True, True)   , 'B11')
    B12= junction((False, True, True, True)   , 'B12')
    B13= junction((False, True, True, True)   , 'B13')
    B14= junction((False, True, True, True)   , 'B14')

    B1.north = B4
    B1.east = B2

    B2.west = B1
    B2.east = B3
    B2.north = B6

    B3.west = B2
    B3.north = None

    B4.south = B1
    B4.east = B5
    #B4.north = B13

    B5.west = B4
    B5.east = B6
    B5.south = None
    B5.north = B13

    B6.north = B12
    B6.west = B5
    B6.east = B7
    B6.south = B2

    B7.west = B6
    B7.north = B8

    B8.south = B7
    B8.west = B9

    B9.north = B10
    B9.east = B8

    B10.west = B11
    B10.south = B9

    B11.west = B12
    B11.east = B10
    B11.north = B14

    B12.west = B13
    B12.east = B11
    B12.south = B6

    #B13.west = B4
    B13.south = B5
    B13.east = B12

    B14.west = None
    B14.east = None
    B14.south = B11


    #Change the return to the starting node
    return B1

def print_map(start):
    explored = []
    to_explore = []
    to_explore.append(start)
    #start with start
    while to_explore:
        current_node = to_explore.pop()
        move_set = current_node.valid_moves
        #list of nodes to explore
        new_nodes = []
            
        #up
        if move_set[0] == True and current_node.north != None:
            new_nodes.append(current_node.north)
            print(current_node.name, "--North-->", current_node.north.name)
            
        #down
        if move_set[1] == True and current_node.south != None:
            new_nodes.append(current_node.south)
            print(current_node.name, "--South-->", current_node.south.name)
            
        #left
        if move_set[2] == True and current_node.west != None:
            new_nodes.append(current_node.west)
            print(current_node.name, "--West-->", current_node.west.name)

        #right
        if move_set[3] == True and current_node.east != None:
            new_nodes.append(current_node.east)
            print(current_node.name, "--East-->", current_node.east.name)

        explored.append(current_node)
        
        for term in new_nodes:
            if term not in to_explore and term not in explored:
                to_explore.append(term)

junction_count = 14

def junction_generate_moves(junction):
    move_set = junction.valid_moves

    junctions = []
    #up
    if move_set[0] == True and junction.north != None:
        junctions.append(junction.north)
        
    #down
    if move_set[1] == True and junction.south != None:
        junctions.append(junction.south)

    #left
    if move_set[2] == True and junction.west != None:
        junctions.append(junction.west)

    #right
    if move_set[3] == True and junction.east != None:
        junctions.append(junction.east)

    return junctions

#Source
#http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
def bfs(start, goal):
    queue = []

    queue.append([start])

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node.name == goal:
            return path

        branching = junction_generate_moves(node)
        for branch in branching:
            new_path = list(path)
            new_path.append(branch)
            queue.append(new_path)

def cardinal_mapping(current_direction, turn_direction):
    new_direction = None;
    if turn_direction == "forward":
        return current_direction
    
    if current_direction == "north":
        if turn_direction == "left":
            new_direction = "west"
        elif turn_direction == "right":
            new_direction = "east"

    elif current_direction == "south":
        if turn_direction == "left":
            new_diection = "east"
        elif turn_direction == "right":
            new_diection = "west"
            
    elif current_direction == "west":
        if turn_direction == "left":
            new_diection = "south"
        elif turn_direction == "right":
            new_diection = "north"
            
    elif current_direction == "east":
        if turn_direction == "left":
            new_diection = "north"
        elif turn_direction == "right":
            new_diection = "south"
            
    return new_direction

def find_direction(current, goal):
    if current.north != None:
        if current.north.name == goal:
            return "north"

    if current.south != None:
        if current.south.name == goal:
            return "south"
            
    if current.east != None:
        if current.east.name == goal:
            return "east"

    if current.west != None:
        if current.west.name == goal:
            return "west"

def turn_direction(current_direction, goal_direction):

    return turn_mapping[current_direction][goal_direction]

def update_location(junction, direction):
    if direction == "north":
        return junction.north
        
    elif direction == "south":
        return junction.south

    elif direction == "west":
        return junction.west

    elif direction == "east":
        return junction.east

def print_path(path):
    path_list = []
    for node in path:
        path_list.append(node.name)

    #print("Path:", end="")
    path_str = ", ".join(path_list)
    print (path_str)

#iterative
def navigate(start, goal):
    reached_goal = False
    current = start
    
    while not reached_goal:
        if current.name == goal:        #At goal
            reached_goal = True
            break
        
        path = bfs(current, goal)       #Get the path
        print_path(path)
        go_to = path.pop(1)             #Get the next node
        
        #Get the movement path that it should move
        direction = find_direction(current, go_to.name) 
        #print(current.name, "-->", direction, "--> ", end= "") 
        
        #move the direction needed
        

        #update the current node to be the one travelled to
        current = update_location(current, direction)
        print(current.name, "\n\n")

    if reached_goal:
        print("\nReached the goal:", goal)


def navigate_single(start, goal):
    if start.name == goal:      #Already at goal
        return None, None, True

    path = bfs(start, goal)
    print_path(path)
    go_to = path.pop(1)

    direction = find_direction(start, go_to.name)

    #update the current node to be the one travelled to
    start = update_location(start, direction)

    return go_to, direction, False
    

#EXAMPLE USAGE   
start = init_map()          #init_map returns right now B1
print_map(start)            #print the connections
goal = 'B14'                #The goal node name

#print ("\n\nNAVIGATE:")
#Looped navigate
#navigate(start, goal)


print ("\n\nNAVIGATE SINGLE:")

nav_continue = False                    #Reached the goal?
while not nav_continue:                 #While haven't
    go_to, direction, nav_continue = navigate_single(start, goal)   #Get the direction of travel

    if nav_continue != True:                                        #Is it the goal?
        print (start.name, "-->", direction, "-->", go_to.name)     #no, do a printout
    #update location
    start = go_to
    









