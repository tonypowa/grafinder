import argparse
from key_git import token

# add the path to the root of the project to sys.path 
# This was needed to be able to import PyGithub lib

# from pathlib import Path
# import sys
# path_root = Path(__file__).parents[2]
# sys.path.append(str(path_root))
# print(sys.path)

from PyGithub.github import Github

# take input from user and store in a variable


# allows to pass arguments (e.g. -h, --help)
# . In our case we will pass a URL, that will be treated like a string
parser = argparse.ArgumentParser(description="test")
parser.add_argument('text',action='store', type=str, help='give me a link and I will do the rest')
user_arg = parser.parse_args()
user_input = user_arg.text


# validates the length of the input.

if len(user_input) > 100:
    print("the link is too long")
else:
    user_input = user_input.lower().strip() # convert string to lowercase, and removes any whitespace
    print(f"thank you for the link {user_input}")


# todo: take the link and use it to call github api
