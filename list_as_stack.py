# Queue operations
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

# Stack operations
def push(stack, value):
    new_node = [value, stack]
    stack = new_node

def pop(stack):
    if stack:
        value = stack[0]
        stack = stack[1]
        return value
    else:
        return None

# Initialize the queue with a dummy node
queue = ["Head", None]

# Initialize the stack
stack = None

# Add elements to the queue and stack
for i in range(1, 6):
    qAdd(queue, i)
    push(stack, i)

# Print the queue and stack
print("Queue:")
cur = queue[1]
while cur is not None:
    print(cur[0])
    cur = cur[1]

print("Stack:")
while stack:
    print(stack[0])
    stack = stack[1]

# Pop elements from the queue and stack
print("Queue Pop:")
while True:
    value = qPop(queue)
    if value is not None:
        print("Popped:", value)
    else:
        break

print("Stack Pop:")
while True:
    value = pop(stack)
    if value is not None:
        print("Popped:", value)
    else:
        break
