"""Unit tests for Design Twitter.

Test pseudocode:
    for the worked example:
        publish a tweet and verify the author can see it
        follow another author and verify both authors' tweets are visible
        unfollow that author and verify only the user's own tweet remains

    for news-feed behavior:
        verify globally newer tweets appear first across different authors
        verify the feed contains no more than 10 tweets
        verify following is direct rather than transitive

    for follow edge cases:
        verify repeated follows do not duplicate tweets
        verify following oneself does not duplicate personal tweets
        verify unfollowing an absent relationship is safe
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solutions.design_twitter import Twitter


class TestTwitter(unittest.TestCase):
    def test_worked_example(self) -> None:
        twitter = Twitter()
        twitter.postTweet(1, 5)
        self.assertEqual(twitter.getNewsFeed(1), [5])

        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])

        twitter.unfollow(1, 2)
        self.assertEqual(twitter.getNewsFeed(1), [5])

    def test_tweets_from_multiple_authors_use_global_order(self) -> None:
        twitter = Twitter()
        twitter.postTweet(1, 101)
        twitter.postTweet(2, 201)
        twitter.postTweet(1, 102)
        twitter.follow(3, 1)
        twitter.follow(3, 2)

        self.assertEqual(twitter.getNewsFeed(3), [102, 201, 101])

    def test_news_feed_is_limited_to_ten_tweets(self) -> None:
        twitter = Twitter()
        for tweet_id in range(1, 13):
            twitter.postTweet(1, tweet_id)

        self.assertEqual(twitter.getNewsFeed(1), list(range(12, 2, -1)))

    def test_following_is_not_transitive(self) -> None:
        twitter = Twitter()
        twitter.follow(1, 2)
        twitter.follow(2, 3)
        twitter.postTweet(2, 20)
        twitter.postTweet(3, 30)

        self.assertEqual(twitter.getNewsFeed(1), [20])

    def test_repeated_follow_does_not_duplicate_tweets(self) -> None:
        twitter = Twitter()
        twitter.postTweet(2, 20)
        twitter.follow(1, 2)
        twitter.follow(1, 2)

        self.assertEqual(twitter.getNewsFeed(1), [20])

    def test_following_oneself_does_not_duplicate_tweets(self) -> None:
        twitter = Twitter()
        twitter.postTweet(1, 10)
        twitter.follow(1, 1)

        self.assertEqual(twitter.getNewsFeed(1), [10])

    def test_unfollow_absent_relationship_is_safe(self) -> None:
        twitter = Twitter()
        twitter.unfollow(1, 2)

        self.assertEqual(twitter.getNewsFeed(1), [])


if __name__ == "__main__":
    unittest.main()
