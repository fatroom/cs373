colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green', 'green', 'green']


motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]


def calculate():

    #DO NOT USE IMPORT
    #ENTER CODE BELOW HERE
    #ANY CODE ABOVE WILL CAUSE
    #HOMEWORK TO BE GRADED
    #INCORRECT
  
    p = []

    l = len(colors[1])
    h = len(colors)
    for i in range(h):
        p_row = []
        for j in range(l):
            p_row.append(1.0/h*l)
        p.append(p_row)

    def move(p, U):
        q = []
        for i in range(h):
            q_row = []
            for j in range(l):
                q_row.append(p_move*p[(i-U[0])%h][(j-U[1])%l]+(1-p_move)*p[i%h][j%l])
            q.append(q_row)
        return q

    def sense(p, Z):
        q=[]
        for i in range(h):
            q_row = []
            for j in range(l):
                hit = (Z == colors[i][j])
                q_row.append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
            q.append(q_row)
        s=0
        for i in range(len(q)):
            s+=sum(q[i])
    
        for i in range(h):
            for j in range(l):
                q[i][j] = q[i][j] / s
        return q


    for i in range(len(motions)):
        p = move(p, motions[i])
        p = sense(p, measurements[i])
    #Your probability array must be printed 
    #with the following code.

    #show(p)
    return p

