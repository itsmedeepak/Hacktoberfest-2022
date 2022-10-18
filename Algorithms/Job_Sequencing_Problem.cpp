# Python3 program for the above approach
import heapq


def printJobScheduling(arr):
	n = len(arr)

	# arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit

	# sorting the array on the
	# basis of their deadlines
	arr.sort(key=lambda x: x[1])

	# initialise the result array and maxHeap
	result = []
	maxHeap = []

	# starting the iteration from the end
	for i in range(n - 1, -1, -1):

		# calculate slots between two deadlines
		if i == 0:
			slots_available = arr[i][1]
		else:
			slots_available = arr[i][1] - arr[i - 1][1]

		# include the profit of job(as priority), deadline
		# and job_id in maxHeap
		# note we push negative value in maxHeap to convert
		# min heap to max heap in python
		heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))

		while slots_available and maxHeap:

			# get the job with max_profit
			profit, deadline, job_id = heapq.heappop(maxHeap)

			# reduce the slots
			slots_available -= 1

			# include the job in the result array
			result.append([job_id, deadline])

	# jobs included might be shuffled
	# sort the result array by their deadlines
	result.sort(key=lambda x: x[1])

	for job in result:
		print(job[0], end=" ")
	print()


# Driver's Code
if __name__ == '__main__':
	arr = [['a', 2, 100], # Job Array
		['b', 1, 19],
		['c', 2, 27],
		['d', 1, 25],
		['e', 3, 15]]

	print("Following is maximum profit sequence of jobs")

	# Function Call
	printJobScheduling(arr)

# This code is contributed
# by Shivam Bhagat
