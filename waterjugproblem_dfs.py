cap1=5
cap2=3
targ=4

initial=(0,0)

def is_valid(state):
    j1,j2=state
    return cap1>=j1>=0 and cap2>=j2>=0

def pour(from_j,to_j,state):
    j1,j2=state
    if from_j==1:
        amt=min(j1,cap2-j2)
        up_j1=j1-amt
        up_j2=j2+amt
        return(up_j1,up_j2)
    else:
        amt=min(cap1-j1,j2)
        up_j1=j1+amt
        up_j2=j2-amt
        return(up_j1,up_j2)

def soln():
    visited=set()
    stack=[]
    stack.append((initial,[]))

    while stack:
        curr_state,action=stack.pop()

        if curr_state[0]==targ or curr_state[1]==targ:
            return action
        
        visited.add(curr_state)

        for actions in ["Fill Jug 1", "Fill Jug 2", "Empty Jug 1", "Empty Jug 2", "Pour Jug 1 to Jug 2", "Pour Jug 2 to Jug 1"]:
            if actions=="Fill Jug 1":
                new_state=(cap1,curr_state[1])
            elif actions=="Fill Jug 2":
                new_state=(curr_state[0],cap2)
            elif actions=="Empty Jug 1":
                new_state=(0,curr_state[1])
            elif actions=="Empty Jug 2":
                new_state=(curr_state[0],0)
            elif actions=="Pour Jug 1 to Jug 2":
                new_state=pour(1,2,curr_state)
            elif actions=="Pour Jug 2 to Jug 1":
                new_state=pour(2,1,curr_state)

            if new_state not in visited:
                new_actions=action + [actions]
                stack.append((new_state,new_actions))

solution = soln()
if solution:
    print("Solution Found:")
    for i, action in enumerate(solution, start=1):
        print(f"Step {i}: {action}")
else:
    print("No solution found.")