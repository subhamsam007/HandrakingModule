import time

# Returns current time in seconds since epoch (Unix time)
# print(time.time())
# Convert epoch time to readable string
print(time.ctime())

# Convert epoch to structured time tuple
print(time.localtime())
# Pause the program for 2 seconds
print("Waiting...")
time.sleep(2)
print("Done!")

# Get structured local time
t = time.localtime()
print(t.tm_year, t.tm_mon, t.tm_mday)

