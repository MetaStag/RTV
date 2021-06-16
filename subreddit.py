# SUBREDDIT MODE

import mimetypes # To check if url is image or not
import requests # To download images
from os import system # To clear the screen and call feh
import platform # For os-dependent image viewing commands

clear_command = 'clear'
# Replace this with your command to open images
if platform.system() == 'Darwin':
    image_viewing_command = 'open temp.jpg'
elif platform.system() == 'Linux':
    image_viewing_command = 'xdg-open temp.jpg'
elif platform.system() == 'Windows':
    image_viewing_command = 'start temp.jpg'
    clear_command = 'cls'
else:
    image_viewing_command = ''


def sub_clear(subreddit): # Clear the Screen
    system(clear_command)
    print(f'Welcome to r/{subreddit}!')
    print('********')
    print('COMMANDS')
    print('i - Check info')
    print('c - Check posts')
    print('s - Subscribe')
    print('u - Unsubscribe')
    print('clear - Clear Screen')
    print('q/exit - Exit subreddit mode')
    print('********')

def submission(post): # Work with posts
    while True:
        choice = input('(N)ext | (U)pvote | (D)ownvote | (C)omment | (S)ave | (Q)uit: ')
        choice = choice.lower()
        
        try:
            if choice == '' or choice == 'n' or choice == 'next': # Next post
                return True
            elif choice == 'u' or choice == 'upvote': # Upvote
                post.upvote()
            elif choice == 'd' or choice == 'downvote': # Downvote
                post.downvote()
            elif choice == 'c' or choice == 'comment': # Comment
                comment = input('Enter a comment: ')

                choice = input('Are you sure you want to comment(Y/N): ') # Confirmation before commenting
                if choice == '' or choice == 'y' or choice == 'yes':
                    post.reply(comment)
                else:
                    continue
            elif choice == 's' or choice == 'save': # Save
                post.save()
            elif choice == 'q' or choice == 'exit': # Quit
                return False
            else:
                print('Invalid Command...')
        except ValueError:
            print("There's some network issue, try again later...")
            return True


def sub(subreddit, subreddits):
    sub_clear(subreddit)
    
    while True:
        choice = input('> ')

        if choice == 'i': # Check info
            print(f'SUBREDDIT_NAME        | r/{subreddit.display_name}\n'
                  f'SUBSCRIBERS           | {subreddit.subscribers}\n'
                  f'ARE YOU A SUBSCRIBER? | {subreddit.user_is_subscriber}\n'
                  f'DESCRIPTION           | {subreddit.public_description}\n')

        elif choice == 'c': # Check posts
            sorting = input('Choose a sorting method (Hot/New/Top): ')
            sorting = sorting.lower() # Managing case-sensitivity

            if sorting not in ['hot', 'new', 'top']:
                print('Invalid sorting method...')
                continue

            for post in getattr(subreddit, sorting)(limit=5):
                print(f'Title -> {post.title} | Score -> {post.score} | By -> u/{post.author} | URL -> ( https://www/reddit.com{post.permalink} )\n')
                if post.is_self: # If post is text-only
                    print('------------------------------------------------------------------------------------------------')
                    print(post.selftext)
                    print('------------------------------------------------------------------------------------------------')
                else: # If post is image
                    file_type = mimetypes.guess_type(post.url)[0]
                    if file_type in ['image/png', 'image/jpg', 'image/jpeg']:
                        response = requests.get(post.url, stream=True) # Download Image
                        with open('temp.jpg', 'wb') as file: # Save to external file temporarily
                            for chunk in response.iter_content(chunk_size=1024):
                                file.write(chunk)
                        system(image_viewing_command) # Display Image
                    else:
                        input('File is neither an image nor text, press enter to skip...')
                        continue
                continue_posts = submission(post) # Send post to submission()
                if not continue_posts:
                    break

        elif choice == 's': # Subscribe
            choice = input(f'Are you sure you want to subscribe to r/{subreddit} (Y/N): ')

            if choice == 'y':
                if subreddit not in subreddits:
                    subreddit.subscribe()
                    print(f'Subscribed to r/{subreddit}!')
                else:
                    print("You're already subscribed to this subreddit...")
            elif choice == 'n':
                continue
            else:
                print('Invalid Choice...')
            
        elif choice == 'u': # Unsubscribe
            choice = input(f'Are you sure you want to unsubscribe to r/{subreddit} (Y/N): ')

            if choice == 'y':
                if subreddit in subreddits:
                    subreddit.unsubscribe()
                    print(f'Unubscribed from r/{subreddit}...')
                else:
                    print("You're not subscribed in the first place...")
            elif choice == 'n':
                continue
            else:
                print('Invalid Choice...')

        elif choice == 'clear': # Clear Screen
            sub_clear(subreddit)
        elif choice == 'q' or choice == 'exit': # Exit subreddit mode
            if platform.system == 'Windows':
                if path.exists('temp.jpg'):
                    system('del temp.jpg')
            else:
                system('rm -f temp.jpg')
            return
        else:
            print('Invalid Command...')
