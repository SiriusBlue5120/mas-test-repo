import time

i = 0
sums = 0

while True:
    startTime = time.time()
    
    print(f"This is an infinite loop - we are now at iteration {i} and the sum of integers so far is {sums}")
    i = i + 1
    sums = sums + i
    endTime = time.time()
    
    print(f"This iteration took {endTime - startTime}")

print("This line will never print.")
