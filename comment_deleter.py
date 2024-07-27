import praw

# Replace these values with your credentials
reddit = praw.Reddit(
    client_id=your_client_id,
    client_secret=your_client_secret,
    user_agent=your_script_name:v1.0 (by /u/your_username),
    username=your_username,
    password=your_password
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
