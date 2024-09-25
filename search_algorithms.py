from collections import deque



## We will append tuples (state, "action") in the search queue
def breadth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.popleft()
        state_count += 1
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)

            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
                print("\n")
            print(f"Total states generated by BFS: {state_count}")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)

### Note the similarity to BFS - the only difference is the search queue

## use the limit parameter to implement depth-limited search
def depth_first_search(startState, action_list, goal_test, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState,""))
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        ## this is a (state, "action") tuple
        next_state = search_queue.pop()
        state_count += 1
        if goal_test(next_state[0]):
            print("Goal found")
            print(next_state)
            ptr = next_state[0]
            while ptr is not None :
                ptr = ptr.prev
                print(ptr)
                print("\n")
            print(f"Total states generated by DFS: {state_count}")
            return next_state
        else :
            successors = next_state[0].successors(action_list)
            if use_closed_list :
                successors = [item for item in successors
                                    if item[0] not in closed_list]
                for s in successors :
                    closed_list[s[0]] = True
            search_queue.extend(successors)



def depth_limited_search(startState, action_list, goal_test, use_closed_list=True, limit=5):
    search_queue = deque()
    closed_list = {}
    state_count = 0

    search_queue.append((startState, "", 0))  # Add the current depth as part of the state tuple
    if use_closed_list:
        closed_list[startState] = True

    while len(search_queue) > 0:
        next_state, action, depth = search_queue.pop()
        state_count += 1  # Increment the state count

        if goal_test(next_state):
            print("Goal found")
            print(next_state)
            ptr = next_state
            while ptr is not None:
                print(ptr)
                print("\n")
                ptr = ptr.prev
            print(f"Total states generated by DLS: {state_count}")
            return next_state

        if depth < limit or limit == 0:  # Only expand successors within depth limit
            successors = [(s, a, depth + 1) for s, a in next_state.successors(action_list)]

            if use_closed_list:
                successors = [(s, a, d) for s, a, d in successors if s not in closed_list]
                closed_list.update({s: True for s, _, _ in successors})

            search_queue.extend(successors)




