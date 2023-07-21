import os
import argparse
import re
import traceback
from github import Github
from dotenv import load_dotenv
from pprint import pprint

# Take what's in .env -> os.environ
load_dotenv()

# Load GitHub API key
github_api_key = os.environ['GITHUB_API_KEY']
g = Github(f"{github_api_key}")


input_options = ["link", "keywords"]
input_type=""

# clasify type of input and call a function accordingly

# def check_input():

#     # Add the ability to pass arguments when using python command
#     # In our case, we will pass a URL that will be treated like a string
#     parser = argparse.ArgumentParser(description="test")
#     parser.add_argument('text',action='store', type=str, help=" please pass a link to a github issue as parameter")
#     user_arg = parser.parse_args()
#     user_input = user_arg.text # take arg passed from the user and store its value in a variable

#     #some regex to tell if it's a link or words
#     # input_type = ["link", "keywords"]
    
#     regex_link = re.match("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*",user_input).group(1) # find issue number and pass it to get_issue
#     print(regex_link)
#     if regex_link:
#         input_type = input_options[0]
#     else:
#         input_type = input_options[1]



def search_github_issue_number():

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
            repo_ = g.get_repo("grafana/grafana") # temporarily hardcoded owner/repo
            issue = repo_.get_issue(int(issue_number)).title
            print(f" title: {issue}")
            result = g.search_issues(query=issue, repo="grafana/grafana",)
            count = 0
            returned_issues = []
            # if len(result) >=5:
            for index, issue in enumerate(result):
                # print(index,issue)
                # count += 1
                returned_issues.append(issue)
                if len(returned_issues) > 4:
                    break
            # print(returned_issues)
            return returned_issues

        except AttributeError:
            return "this does not look like a valid GitHub issue link"
        except Exception as e:
            tb = traceback.format_exc()
            if "Not Found" in tb:
                return "issue not found!"

returned_issues = search_github_issue_number()
print(returned_issues)

