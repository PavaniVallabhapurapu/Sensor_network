import sys
import math

def command_input():
    num_sen,dist  = sys.argv[1],sys.argv[2]
    sen_coor = []
    for i in range(3, 2*int(num_sen)+2, 2):
        x,y = sys.argv[i],sys.argv[i+1]
        sen_coor.append((int(x), int(y)))
    return subset(int(num_sen), int(dist), sen_coor)

def distance(x1, y1,  x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def subset(num_sen, dist, sen_coor):
    subsets = []
    sen_distances = []
    for i in range(num_sen):
        for j in range(i+1, num_sen):
            sen_dist = distance(sen_coor[i][0], sen_coor[i][1], sen_coor[j][0], sen_coor[j][1])
            if  sen_dist <= dist:
                subsets.append((i+1, j+1))
                sen_distances.append(sen_dist)
    if len(set(sen_distances)) == 1:
        return len(subsets[0]),subsets[0]
    else :
        max_conn, max_conn_sens = 0, 0
        sens_connections = [0] * num_sen
        for sens1, sens2 in subsets:
            sens_connections[sens1 - 1] += 1
            sens_connections[sens2 - 1] += 1
            if sens_connections[sens1 - 1] > max_conn:
                max_conn = sens_connections[sens1 - 1]
                max_conn_sens = sens1
            if sens_connections[sens2 - 1] > max_conn:
                max_conn = sens_connections[sens2 - 1]
                max_conn_sens = sens2
        result = [max_conn_sens]
        for sens1, sens2 in subsets:
            if sens1 == max_conn_sens or sens2 == max_conn_sens:
                if sens1 not in result:
                    result.append(sens1)
                if sens2 not in result:
                    result.append(sens2)
    return len(result),result

max_sub = command_input()
print(max_sub[0])
print(max_sub[1])
