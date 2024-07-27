import praw

# Replace these values with your credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
USER_AGENT = 'your_script_name:v1.0 (by /u/your_username)'
USERNAME = 'your_reddit_username'
PASSWORD = 'your_reddit_password'


reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
    username=USERNAME,
    password=PASSWORD
)

# Function to delete all comments
def delete_all_comments():
    user = reddit.user.me()
    print("Fetching comments...")
    for comment in user.comments.new(limit=None):
        try:
            print(f"Deleting comment: {comment.id}")
            comment.delete()
            print(f"Deleted comment: {comment.id}")
        except Exception as e:
            print(f"Failed to delete comment: {comment.id}. Error: {e}")

if __name__ == '__main__':
    delete_all_comments()
