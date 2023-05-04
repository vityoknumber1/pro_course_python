from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from time import sleep


# each social channel has a type and the current number of followers
class SocialChannel(ABC):  # = tuple[str, int] =
    @abstractmethod
    def channel_name(self):
        """Type of channel representing"""

    @abstractmethod
    def post_a_message(self, message: str) -> None:
        """Posting a message in channel"""


# each post has a message and the timestamp when it should be posted
class Post:
    def __init__(self, message: str, timestamp: datetime):
        self.message = message
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"\n{self.message}\nAt{self.timestamp}"


class Youtube(SocialChannel):
    def __init__(self, channel_name: str):
        self.channel_name = channel_name

    @property
    def channel_name(self):
        return "Youtube"

    def post_a_message(self, message: str) -> None:
        print(
            f"At {datetime.now()} on {self.channel_name} \
            posted next message:\n{message}"
        )


class Facebook(SocialChannel):
    def __init__(self, channel_name: str):
        self.channel_name = channel_name

    @property
    def channel_name(self):
        return "Facebook"

    def post_a_message(self, message: str) -> None:
        print(
            f"At {datetime.now()} on {self.channel_name} \
            posted next message:\n{message}"
        )


class Twitter(SocialChannel):
    def __init__(self, channel_name: str):
        self.channel_name = channel_name

    @property
    def channel_name(self):
        return "Twitter"

    def post_a_message(self, message: str) -> None:
        print(
            f"At {datetime.now()} on {self.channel_name} \
            posted next message:\n{message}"
        )


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    posts = [post for post in posts]
    while len(posts) > 0:
        i = 0
        while i < len(posts):
            post = posts[i]
            if post.timestamp <= datetime.now():
                for channel in channels:
                    channel.post_a_message(post.message)
        sleep(10)


def shift_time(start_time: datetime, milliseconds: int) -> datetime:
    delta = timedelta(milliseconds=milliseconds)
    end_time = start_time + delta
    return end_time


def main():
    channels = [Twitter, Youtube, Facebook]
    for channel in channels:
        print(channel)

    posts: list[Post] = [
        Post("Message 01", shift_time(datetime.now(), 1000)),
        Post("Message 02", shift_time(datetime.now(), 2000)),
        Post("Message 03", shift_time(datetime.now(), 3000)),
    ]

    for post in posts:
        print(post)

    process_schedule(posts, channels)


if __name__ == "__main__":
    main()
