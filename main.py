from instaloader import Instaloader, Hashtag

from Helpers.RabbitMQClient import RabbitMQClient


def generate_insta(USER):
    insta = Instaloader(download_videos=False, save_metadata=False, download_geotags=False, download_comments=False)
    insta.load_session_from_file(USER)
    return insta


def generate_hashtag(insta, hashtag_to_search):
    hashtag = Hashtag.from_name(insta.context, hashtag_to_search)
    return hashtag


def main():
    USER = ""
    hashtag_to_search = ""
    follower_threshold = 0.1
    rabbitmq_host = 'host.docker.internal'
    rabbitmq_queue_name = 'instagram_pictures'

    insta = generate_insta(USER)
    hashtag = generate_hashtag(insta, hashtag_to_search)

    rabbitmq_client = RabbitMQClient(rabbitmq_host, rabbitmq_queue_name)

    for post in hashtag.get_posts():
        if post.likes > (post.owner_profile.followers * follower_threshold):
            print("Publishing " + post.url)
            rabbitmq_client.Publish(post.url)


if __name__ == "__main__":
    main()
