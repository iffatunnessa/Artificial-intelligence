#procedure to find out heuristic function(h3) for 8-Queens problem

state = [6,1,5,7,4,3,8,1]
total = 0

for i in range(len(state)):
    temp = state[i]

    for k in range(i+1, len(state),1):
        if(temp == state[k]):
            total +=1

    j = 1
    for k in range(i+1, len(state), 1):
        if((temp + j < len(state)) & (temp - j > -1)):
            if((state[k] == temp + j) | ( state[k] == temp - j)):
                total+=1
                state[k] = 9
        j+=1

    m = 1
    for k in range(i-1, -1, -1):
        if((temp + m < len(state)) & (temp - m > -1)):
            if((state[k] == temp + m) | (state[k] == temp - m)):
                total+=1
                state[k] = 9
        m+=1

print('h3:',total)
