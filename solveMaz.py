from Stack import Stack

def solveMaze(maze,x,y):
    s = Stack()
    s.push((x,y))
    count = 1 
    
    while not s.isEmpty():
        (x,y) = s.peek()
        if maze[x][y] == 'G':
            return True   
        elif maze[x-1][y] == ' ':#North
            
            if maze[x][y] == ' ':
                maze[x][y] = count
            s.push((x-1,y))
            count += 1
        elif maze[x-1][y] == 'G':#if North is Goal
            if maze[x][y] == ' ':
                maze[x][y] = count
            return True

        elif maze[x][y+1] == ' ':#East
            if maze[x][y] == ' ':
                maze[x][y] = count
            s.push((x,y+1))
            count += 1
        elif maze[x][y+1] == 'G':#if East is goal
            if maze[x][y] == ' ':
                maze[x][y] = count
            return True

        elif maze[x+1][y] == ' ':#South
            if maze[x][y] == ' ':
                maze[x][y] = count
            s.push((x+1,y))
            count += 1
        elif maze[x+1][y] == 'G':#if South is goal
            if maze[x][y] == ' ':
                maze[x][y] = count
            return True

        elif maze[x][y-1] == ' ':#West
            if maze[x][y] == ' ':
                maze[x][y] = count
            s.push((x,y-1))
            count += 1
        elif maze[x][y-1] == 'G':#if West is goal
            if maze[x][y] == ' ':
                maze[x][y] = count
            return True
        else:
            if maze[x][y] == ' ':
                maze[x][y] = count
            s.pop()
    return False
