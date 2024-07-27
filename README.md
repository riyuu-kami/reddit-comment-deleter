### 1. Install PRAW

- Open a terminal or command prompt and run:
```ruby
  pip install praw
```

### 2. Create a Reddit App

- Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps).
- Create a new application and select "script" as the application type.
- redirect url should be http://localhost:8080 or something similar
- create app
- Note down your:
   ```
      - Client ID: it should be below your script name after creating the app
      - Client Secret: it should be next to "secret"
      - User Agent: if you havent made any changes after creating the app it's probably 'your_script_name:v1.0 (by /u/your_username)'

### 3. run the python script
- open comment_deleter.py and run it, if it stops after deleting a dozen of comments just run it again
