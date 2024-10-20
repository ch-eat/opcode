
# The DGIM (Datar-Gionis-Indyk-Motwani) algorithm is a streaming algorithm used to estimate the count of 1s in the last
# N bits of a binary stream. It uses a clever bucketing technique to store a summary of the stream using logarithmic space, making 
# it efficient for large data streams. Instead of storing the entire stream, it approximates counts while keeping memory usage low.


import math

def checkAndMergeBucket(bucketList, k):
    """
    This function checks and merges buckets if there are more than 2 of the same size.
    """
    for i in range(k + 1):
        # If a bucket has more than 2 timestamps, merge them
        while len(bucketList[i]) > 2:
            # Remove the oldest timestamp
            bucketList[i].pop(0)

            # If we're not at the last bucket, merge with the next size
            if i + 1 >= len(bucketList):
                # Only remove from the current bucket if no next bucket
                break
            else:
                # Merge the remaining timestamp with the next bucket
                bucketList[i + 1].append(bucketList[i].pop(0))

# Constants for the DGIM algorithm
K = 1000  # Window size to track
N = 1000  # Stream size (total bits in the stream)
k = int(math.floor(math.log(N, 2)))  # Maximum bucket size (based on log of N)
t = 0  # Current time
onesCount = 0  # Estimated number of 1s in the last K bits

# Initialize bucket list (buckets for sizes 1, 2, 4, 8, ...)
bucketList = []
for i in range(k + 1):
    bucketList.append([])

# Open the stream file (engg5108_stream_data.txt) to read binary data
with open('data.txt') as f:
    while True:
        c = f.read(1)  # Read one character (bit) from the stream

        if not c:  # If no more characters, stop
            # Print the current bucket structure and calculate the number of 1s
            for i in range(k + 1):
                for j in range(len(bucketList[i])):
                    print(f"Size of bucket: {2 ** i}, timestamp: {bucketList[i][j]}")

            # Calculate the number of 1s in the last K bits
            earliestTimestamp = bucketList[-1][0] if bucketList[-1] else 0
            onesCount = 0
            for i in range(k + 1):
                for j in range(len(bucketList[i])):
                    if bucketList[i][j] != earliestTimestamp:
                        onesCount += pow(2, i)  # Add full size for each bucket
                    else:
                        onesCount += 0.5 * pow(2, i)  # Add half the size for the oldest bucket
            print(f"Estimated number of ones in the last {K} bits: {int(onesCount)}")
            break  # Exit the loop once the entire stream is processed

        t = (t + 1) % N  # Update time for each bit processed (mod N for circular time)

        # Remove buckets whose timestamps fall outside the window
        for i in range(k + 1):
            bucketList[i] = [bucketTimestamp for bucketTimestamp in bucketList[i] if bucketTimestamp > t - K]

        # If the bit is '1', add a new bucket of size 1 at the current time
        if c == '1':
            bucketList[0].append(t)
            checkAndMergeBucket(bucketList, k)

        # If the bit is '0', do nothing (continue processing the stream)
