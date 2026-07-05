class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        users = self.following[userId] | {userId}

        for user in users:
            tweets = self.tweets.get(user)
            if tweets:
                idx = len(tweets) - 1
                time, tweetId = tweets[idx]
                heapq.heappush(heap, (-time, tweetId, user, idx))

        result = []
        while heap and len(result) < 10:
            _, tweetId, user, idx = heapq.heappop(heap)
            result.append(tweetId)
            if idx > 0:
                idx -= 1
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweetId, user, idx))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
