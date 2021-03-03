# MODULES
import praw # Reddit API wrapper
from prawcore import NotFound
from subreddit import sub # Subreddit mode
from os import system # To clear the screen
from datetime import datetime # To convert unix time to human-readable time

# MAKING A REDDIT INSTANCE
reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username = '',
                     password = '',
                     user_agent = '')

# FUNCTIONS
def sub_exists(sub): # Check if a subreddit exists
    exists = True
    try:
        reddit.subreddits.search_by_name(sub, exact=True)
    except NotFound:
        exists = False
    return exists

def clear(): # Clear the Screen
    system('clear')
    print('Reddit Terminal Viewer (RTV)')
    print('********')
    print('COMMANDS')
    print('i - Check Info')  
    print('s - Search for subreddit')
    print('g - Go to subreddit')
    print('-s - Saved posts')
    print('clear - Clear Screen')
    print('q/exit - Exit the Program')
    print('********')

# MAIN LOOP
clear()
while True:
    choice = input('> ')
    choice = choice.lower() # Managing case-sensitivity

    if choice == '': # If user wrote nothing
        print('Write something...')
        continue

    if choice == 'i': # Check Info
        user = reddit.user.me()
        joined = int(user.created_utc) # Date Joined
        
        # Converting unix time to human readable time and formatting it
        joined = datetime.utcfromtimestamp(joined).strftime('%d - %m, %Y | %H:%M:%S')

        cake_day = joined[:7] # Cake Day
        post_karma = user.link_karma # Post karma
        comment_karma = user.comment_karma # Comment karma
        total_karma = post_karma + comment_karma # Rough total karma
        subreddits = list(reddit.user.subreddits(limit=None)) # List of subscribed subreddits

        # Display the data
        print(f'NAME          |  {user.name}\n'
              f'DATE JOINED   |  {joined}\n'
              f'CAKE DAY      |  {cake_day}\n'
              f'TOTAL KARMA   |  {total_karma} (Roughly)\n'
              f'Post Karma    |  {post_karma}\n'
              f'COMMENT KARMA | {comment_karma}\n\n'
               'SUBSCRIBED SUBREDDITS:')
        for i in subreddits:
            print(f'[{subreddits.index(i)+1}] {i.display_name}')

    elif choice[0] == 's': # Search for subreddit
        if len(choice) < 3: # Check if syntax is correct
            print('Invalid syntax...')
            continue

        subreddits = list(reddit.subreddits.search(choice[2:], limit=10))
        for i in subreddits:
            print(f'[{subreddits.index(i)+1}] {i.display_name}')

    elif choice[0] == 'g': # Go to subreddit
        # Checks
        if len(choice) < 3: # Check if syntax is correct
            print('Invalid syntax...')
            continue
        if not sub_exists(choice[2:]): # Check if sub exists
            print('This subreddit does not exist...')
            continue
        
        subreddit = reddit.subreddit(choice[2:])
        sub(subreddit, subreddits=list(reddit.user.subreddits(limit=None))) # Send to subreddit mode
        clear()

    elif choice == '-s': # Saved posts
        saved = list(reddit.user.me().saved(limit=None))
        for i in saved:
            try:
                print(f'[{saved.index(i)+1}] {i.title} ( https://www.reddit.com{i.permalink} )')
            except AttributeError: # If it's a comment
                print(f'[{saved.index(i)+1}] Comment: {i.body} ( https://www.reddit.com{i.permalink} )')

    elif choice == 'clear': # Clear Screen
        clear()
    elif choice == 'q' or choice == 'exit': # Exit Program
        exit()
    else:
        print('Invalid Command...')
