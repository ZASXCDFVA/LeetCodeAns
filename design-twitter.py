from typing import List, Dict, Set


class User:
    def __init__(self):
        self.follow: Set[int] = set()


class Tweet:
    def __init__(self, id: int, userId: int):
        self.id: int = id
        self.userId: int = userId


class Twitter:
    def __init__(self):
        self.userDb: Dict[int, User] = {}
        self.tweetDb: List[Tweet] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userDb:
            self.userDb[userId] = User()

        self.tweetDb.append(Tweet(tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        usr: User = self.userDb.get(userId)

        if usr is None:
            return []

        result: List[int] = []

        for index in range(len(self.tweetDb) - 1, -1, -1):
            tweet = self.tweetDb[index]

            if tweet.userId in usr.follow or tweet.userId == userId:
                result.append(tweet.id)

            if len(result) >= 10:
                return result

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        usr = self.userDb.get(followerId)

        if usr is None:
            self.userDb[followerId] = usr = User()

        usr.follow.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        usr = self.userDb.get(followerId)

        if usr is None:
            self.userDb[followerId] = usr = User()

        if followeeId in usr.follow:
            usr.follow.remove(followeeId)


if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 5)
    print(obj.getNewsFeed(1))
    obj.follow(1, 2)
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    print(obj.getNewsFeed(1))
    obj.unfollow(1, 1)
    print(obj.getNewsFeed(1))
