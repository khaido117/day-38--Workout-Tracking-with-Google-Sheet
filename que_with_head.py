def qAdd(queue, value):
    new_node = [value, None]
    if queue[1] is None:
        queue[1] = new_node
    else:
        cur = queue[1]
        while cur[1] is not None:
            cur = cur[1]
        cur[1] = new_node

def qPop(queue):
    if queue[1] is not None:
        removed_node = queue[1]
        queue[1] = removed_node[1]
        return removed_node[0]
    else:
        return None

# Initialize the queue with a dummy node
queue = ["Head", None]

# Add elements to the queue
for i in range(1, 5):
    qAdd(queue, i)

# Print the queue
cur = queue[1]
while cur is not None:
    print(cur[0])
    cur = cur[1]

# Pop elements from the queue
while True:
    value = qPop(queue)
    if value is not None:
        print("Popped:", value)
    else:
        break

# Print the queue after popping
cur = queue[1]
while cur is not None:
    print(cur[0])
    cur = cur[1]
