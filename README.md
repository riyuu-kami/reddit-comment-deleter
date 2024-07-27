## Setup Instructions

### 1. Install PRAW

- Open a terminal or command prompt and run:
  ```bash
  pip install praw

### 2. Create a Reddit App

- Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps).
- Create a new application and select "script" as the application type.
- redirect url should be http://localhost:8080 or something similar
- Note down your:
      - Client ID: it should be below your script name after creating the app
      - Client Secret: it should be next to "secret"
      - User Agent: it's probably 'your_script_name:v1.0 (by /u/your_username)'
