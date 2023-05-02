import os
import argparse
import re
import traceback
from github import Github
from dotenv import load_dotenv


# Take what's in .env -> os.environ
load_dotenv()

# Load GitHub API key
github_api_key = os.environ['GITHUB_API_KEY']
g = Github(f"{github_api_key}")


# Add the ability to pass arguments when using python command
# In our case, we will pass a URL that will be treated like a string
parser = argparse.ArgumentParser(description="test")
parser.add_argument('text',action='store', type=str, help=" please pass a link to a github issue as parameter")
user_arg = parser.parse_args()
user_input = user_arg.text # take arg passed from the user and store its value in a variable


if len(user_input) > 100: # validate length of input.
    print("isn't this link too long?")
else:
    try:
        user_input = user_input.lower().strip() # convert to lowercase, and remove any whitespace
        issue_number = re.match(".*?([0-9]+)$",user_input).group(1) # find issue number and pass it to get_issue
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



