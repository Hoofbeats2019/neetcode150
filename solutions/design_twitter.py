"""Design Twitter.

Created: 16 August 2026
Created by: Yanlong Su

Implement a simplified Twitter service where users can publish uniquely
identified tweets, follow or unfollow other users, and request a news feed.

* ``Twitter()`` initializes the service.
* ``postTweet(userId, tweetId)`` publishes a tweet for ``userId``.
* ``getNewsFeed(userId)`` returns at most 10 tweet IDs, newest first, authored
  by ``userId`` or by users whom ``userId`` directly follows.
* ``follow(followerId, followeeId)`` creates a follow relationship.
* ``unfollow(followerId, followeeId)`` removes a follow relationship.

Following is not transitive, and a user's own tweets always belong in their
news feed. Tweet IDs are unique integers, but their numeric values do not
represent publication order.

Example:
    Input:
        Twitter()
        postTweet(1, 5)
        getNewsFeed(1)
        follow(1, 2)
        postTweet(2, 6)
        getNewsFeed(1)
        unfollow(1, 2)
        getNewsFeed(1)
    Output:
        null
        null
        [5]
        null
        null
        [6, 5]
        null
        [5]

Constraints:
    User IDs and tweet IDs are integers.
    Every tweet ID is unique.
    A news feed contains at most 10 tweet IDs.
    News-feed results are ordered from most recent to least recent.

Proposed pseudocode:
    Tweet(tweet_id, timestamp):
        store tweet_id and timestamp

    Twitter():
        create a map from user IDs to lists of tweets
        create a map from follower IDs to sets of followee IDs
        initialize a global timestamp

    postTweet(user_id, tweet_id):
        create the user's tweet list when absent
        append a Tweet containing the current timestamp
        increment the timestamp

    getNewsFeed(user_id):
        collect the user's tweets
        collect tweets from every directly followed user
        order the collected tweets from newest to oldest
        return the IDs of at most the first 10 tweets

    follow(follower_id, followee_id):
        create the follower's followee set when absent
        add the followee to the set

    unfollow(follower_id, followee_id):
        remove the followee when the relationship exists
"""

from dataclasses import dataclass


@dataclass
class Tweet:
    """A tweet ID paired with its global publication order."""

    tweet_id: int
    timestamp: int


class Twitter:
    """Store tweets and direct follow relationships for a news feed."""

    def __init__(self) -> None:
        self.user_tweets: dict[int, list[Tweet]] = {}
        self.following: dict[int, set[int]] = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Publish ``tweetId`` for ``userId``."""
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []

        tweet = Tweet(tweetId, self.timestamp)
        self.user_tweets[userId].append(tweet)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """Return at most 10 visible tweet IDs from newest to oldest."""
        candidates = list(self.user_tweets.get(userId, []))

        for followee_id in self.following.get(userId, set()):
            candidates.extend(self.user_tweets.get(followee_id, []))

        candidates.sort(key=lambda tweet: tweet.timestamp, reverse=True)
        return [tweet.tweet_id for tweet in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """Make ``followerId`` directly follow ``followeeId``."""
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Remove the direct follow relationship when it exists."""
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


def test_example_1() -> None:
    """Exercise the worked example once the TODOs are implemented."""
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]


if __name__ == "__main__":
    test_example_1()
    print("Example test passed.")
