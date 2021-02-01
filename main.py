from datetime import datetime
from itertools import dropwhile, takewhile

from instaloader import Instaloader, Hashtag

USER = "chopchopchope"
hashtag_to_search = "shiba"
follower_threshold = 0.1

L = Instaloader(download_videos=False)
L.load_session_from_file(USER)

hashtag = Hashtag.from_name(L.context, hashtag_to_search)

for post in hashtag.get_posts():
    if post.likes > (post.owner_profile.followers * follower_threshold):
        L.download_post(post, target="#"+hashtag.name)

