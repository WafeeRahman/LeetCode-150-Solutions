class Twitter:

    def __init__(self):
        self.timeStamp = 0 #Timestamps to order tweets by recency
        self.followMap = defaultdict(set) #userId -> set of userIds
        self.tweetMap = defaultdict(set) #userId -< set of tweetIds
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #Max heap ordering property, elapsed time
        self.tweetMap[userId].add((self.timeStamp, tweetId))
        self.timeStamp -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        
        #Populate heap with tweets affiliated with user
        for tweet in self.tweetMap[userId]:
            maxHeap.append(tweet)

        for user in self.followMap[userId]:
            #We already added the users tweets to the heap
            #Skip it if they are following themselves
            if user == userId:
                continue
            for tweet in self.tweetMap[user]:
                maxHeap.append(tweet)
        
        heapq.heapify(maxHeap)
        #With ordering property, the heap is ordered with largest timestamp
        #To smallest, take the 10 most recent tweets and append to res
        while maxHeap and len(res) < 10:
            recentTweet = heapq.heappop(maxHeap)
            res.append(recentTweet[-1])
        return res

    
    #Add Followee to Follower Set of the User
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    #If the followee is in the follower set of the follower, remove it
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
