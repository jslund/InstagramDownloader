from datetime import datetime
from itertools import dropwhile, takewhile

from instaloader import Instaloader, Hashtag


def generate_hashtag(USER, hashtag_to_search):
    L = Instaloader(download_videos=False, save_metadata=False, download_geotags=False, download_comments=False)
    L.load_session_from_file(USER)

    hashtag = Hashtag.from_name(L.context, hashtag_to_search)
    return hashtag


def resize():



def main():
    USER = "chopchopchope"
    hashtag_to_search = "shiba"
    follower_threshold = 0.1

    hashtag = generate_hashtag(USER, hashtag_to_search)

    for post in hashtag.get_posts():
        if post.likes > (post.owner_profile.followers * follower_threshold):
            L.download_post(post, target="#"+hashtag.name)
            #TODO Post message to MQ to resizing service



if __name__ == __main__:
    main()