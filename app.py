import argparse
import re
import traceback
from github import Github
# ignore me: 
# from key_git import token

# in case you get errors when importing PyGithub lib:
# comment line 4 from github import Github
# clone the library repo into your project folder
# https://github.com/PyGithub/PyGithub
# uncomment bellow code block to add the path to the root of the project to sys.path 

# from pathlib import Path
# import sys
# path_root = Path(__file__).parents[2]
# sys.path.append(str(path_root))
# print(sys.path)
# from PyGithub.github import Github

g = Github("token")

# ignore me: 
# g = Github(f"{token}") 


# allows to pass arguments (e.g. -h, --help)
# . In our case we will pass a URL, that will be treated like a string
parser = argparse.ArgumentParser(description="test")
parser.add_argument('text',action='store', type=str, help=" please pass a link to a github issue as parameter")
user_arg = parser.parse_args()
user_input = user_arg.text # take arg passed from the user and store its value in a variable


if len(user_input) > 100: # validate length of input.
    print("isn't this link too long?")
else:
    try:
        user_input = user_input.lower().strip() # convert to lowercase, and remove any whitespace

        # IF GitHub link (future to-do):
        # extract issue number 
        # and pass it to the get_issue method

        issue_number = re.match(".*?([0-9]+)$",user_input).group(1)
        print(f" detected issue number: {issue_number}")
        repo = g.get_repo("grafana/grafana") # temporarily hardcoded owner/repo
        issue = repo.get_issue(int(issue_number)).title
        print(f" title: {issue}")
    
    except AttributeError:
        print("this does not look like a valid GitHub issue link")
    except Exception as e:
        tb = traceback.format_exc()
        if "Not Found" in tb:
            print("issue not found!")



