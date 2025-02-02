class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = [0] * 26

        #Count the occurence of each task within tasks
        for task in tasks:
            taskCount[ord(task) - ord('A')] += 1

        maxHeap = []

        #Add the amount of tasks in a maxHeap
        for i in range(26):
            if taskCount[i] == 0:
                continue
            maxHeap.append(-taskCount[i])
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque([])
        while q or maxHeap:
            #If the maxHeap is nonempty, pop it and process one task
            if maxHeap:
                task = heapq.heappop(maxHeap)
            
            if task:
                #Process a task and enqueue it if its incomplete
                task += 1
                if task < 0:
                    #Schedule it to be reprocessed n cycles from now
                    q.append([time+n, task])
            
            #If the queue is unempty and the time is greater than the timestamp of the
            #First item added in queue
            if q and time >= q[0][0]:
                readyTask = q.popleft()
                
                heapq.heappush(maxHeap, readyTask[1]) 
            
            time += 1
        return time
            




