goal = 28
#initial_state = [7, 3, 4, 6, 1, 5, 7, 8]
#73461211
#initial_state = [7, 3, 4, 6, 1, 2, 1, 1]
#61142345
#initial_state = [6, 1, 1, 4, 2, 3, 4, 5]
#67327364
#initial_state = [6, 7, 3, 2, 7, 3, 6, 4]
#44444444
initial_state = [4,4,4,4,4,4,4,4]
goal_state = []
iteration_count = 0

def non_attacking_pair_count(queens):
    count = 0
    for ind, val in enumerate(queens):
        num = val
        temp1 = num
        temp2 = num
        if ind < (len(queens) - 1):
            i = ind + 1
            while i < len(queens):
                if num == queens[i]: 
                    count += 1
        
                temp1 = temp1 + 1
                temp2 = temp2 - 1
                if temp1 == queens[i]: 
                    count += 1

                if temp2 == queens[i]:
                    count += 1
                i += 1
    #print("queens of non-attacking pairs of queens:", count)
    return 28 - count


def first_choice_hill_climb():
    global iteration_count
    file = open("local_database.txt", "w")
    i = 0
    while i < 8:
        #print(f"value of i is: {i}")
        temp = initial_state[i]
        val = 0
        current_val = non_attacking_pair_count(initial_state)
        better_move_found = False
        for j in range(1, 9):
            if (initial_state[i] == j):
                #print("milse")
                continue
            initial_state[i] = j
            iteration_count += 1
            val = non_attacking_pair_count(initial_state)
            file.write(f"State: {iteration_count} {initial_state} {val}\n")
            if(val == goal):
                goal_state.append((iteration_count, initial_state, val))
                return 
            if(val > current_val):
                iteration_count += 1
                i = 0
                print(f"choose the uphill move {initial_state} {val}")
                better_move_found = True
                break
        if not better_move_found: 
            initial_state[i] = temp
            i += 1
    file.close


first_choice_hill_climb()

if goal_state:
    print(f"Goal state is:\nstate no. -> {goal_state[0][0]}, state -> {goal_state[0][1]} fitness_val -> {goal_state[0][2]}")
    print()
    file = open("local_database.txt", "r")
    for ln in file:
        print(ln, end='')
else: print("Stuck at a local maxima")
            
