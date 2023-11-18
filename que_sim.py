import random
print("Queue as a customer line\n")

queue = []              # Empty que
y = int(0)

# Queue up some customers
for i in range(1,20):
    x = random.randint(1, 20)
    if x >= 2 and x<= 8:
      queue.append(x)      # Add to the front
      

# Simulate cumstomer line processing
while True:
   x = random.randint(1, 20)
   if x >= 2 and x<= 8:
      queue.append(x *2)      # Add to the front
      print("Queued :", x)
   elif x >=9 and x <=14 and len(queue)>0:          
     y = queue.pop(0)
     print ("Removed: ",y)
   elif x == 17 and len(queue)>=10:
      print ("Line closing\n")
      while len(queue)>0:
         y = queue.pop(0)
         print ("Removed: ",y)
      break