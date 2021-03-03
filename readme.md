# RTV (Reddit Terminal Viewer)

This is a simple app written in python which allows you to browse reddit from inside the terminal!

---
### Requirements
- Python
- Praw module (Reddit API wrapper) 
    - use `pip install praw` to install it
- Reddit account (obviously lol)
- Reddit app - to use the api
    - follow this video to learn how to make an app -> (https://www.youtube.com/watch?v=NRgfgtzIhBQ)

### Setup

###### rtv.py
- Open `rtv.py` using whichever text editor you prefer, and you'll see the reddit instance variable (just beneath the modules section), fill in your respective `client_id, client_secret, username, password and user_agent`.

###### subreddit.py
- Just below the modules, you'll see the `image_viewing_command` variable. Replace the command here with the respective command of whatever image viewer you use. Note that the name of the file to open is `temp.jpg`.
    - If you don't want to mess around with that, make sure you have `feh` installed to view those files
    - You can look up the command for your image viewer, here's the one for **Gwenview**: `gwenview temp.jpg`

### Usage 
- cd into the directory where this project is located.
- Run the program using `python rtv.py` (or `python3 rtv.py` if you have python 2.7 installed as well)

**Tip** As you have noticed, the process to launch this program is a bit tedious. What i would recommend is setting up an alias, here's an example:
```bash
# Tested on bash and fish
alias reddit='cd /path/to/project ; python rtv.py ; cd'
```

**Do not** run `subreddit.py`, it's not meant to be run directly by the user.

### Functions
**NOTE**: You can't use all the reddit features in this app. For example, you can't give an award to someone. But most common features are available, a list of available features is given below:

- Check your Info
- Search for subreddits
- Head over to a subreddit
- Check subreddit info
- Subscribe/Unsubscribe to a subreddit
- See subreddit posts (only text and images, not videos and gifs, those will be skipped)
    - You can sort by hot/top/new
- Upvote/Downvote/Comment/Save posts
- Check saved posts

The reason why other features like seeing comments and awarding are not available is because i wanted this to be a simple app. It's meant to be used for very basic purposes like seeing posts and browsing subs. For example, if you're doing some work and just want to take a quick break, you open this app and see a couple of posts and return back to your work. It's not meant to be a full-fledged alt to reddit.
