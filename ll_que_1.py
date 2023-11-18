# use lists as Queue
head = tail = None

def add(data):
    global head, tail
    ptr = [data, None]
    if head is None:
        tail = head = ptr
    else:
        tail[1] = ptr
        tail = ptr

def pop():
    global head, tail
    if head is None:
        print("Queue is empty. Cannot pop.")
        return None
    data = head[0]
    head = head[1]
    if head is None:
        tail = None
    return data

def display():
    current = head
    while current:
        print(current[0], end=" -> ")
        current = current[1]
    print("None")

# Add elements to the queue
for i in range(1, 6):
    add(i)

# Display the queue
print("Queue:")
display()

# Remove elements from the queue and display them
print("Popped elements:")
while head is not None:
    print(pop())
