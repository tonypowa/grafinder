

from key_git import token

# add the path to the root of the projecy to sys.path 

# from pathlib import Path
# import sys
# path_root = Path(__file__).parents[2]
# sys.path.append(str(path_root))
# print(sys.path)

from PyGithub.github import Github

# using github api token from local file
g = Github(f"{token}")

##### create issue #####


# repo = g.get_repo("tonypowa/grafinder")
# repo.create_issue(title="issue created via API")

##### get issues from repo #####

# repo = g.get_repo("tonypowa/grafinder")
# issues = repo.get_issues(state="open")
# for i in issues:
#     print(i)

##### get issue details #####
#  https://docs.github.com/en/rest/issues/issues?apiVersion=2022-11-28#get-an-issue
repo = g.get_repo("tonypowa/grafinder")
issue = repo.get_issue(4)

print(issue)

##### get issue details via github rest api not via lib #####
# import requests


# url = "https://api.github.com/repos/{owner}/{repo}/issues/{issue_n}"

# payload = {}
# headers = {
#   'Accept': 'application/vnd.github+json',
#   'Authorization': 'Bearer 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',
#   'X-GitHub-Api-Version': '2022-11-28'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
