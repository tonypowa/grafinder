# GRAFINDER
### A python app to find Grafana issues and community posts from one place


## Setup

```
$ pip install PyGithub
```

In `app.py`:

Replace `"token"` with your own GitHub API token

```
g = Github("token")
```

## Run

`python app.py -h` for information


## Get Github issue title

```
python app.py {your_URL}
```

That's it for now. The rest of the app is still being developed. 
Thanks for reading!

-----

### To-do list:

1. when executing the script, pass a link as a arg. Take this input and store it in a variable
- create a function to:
  - validate length of input.  :heavy_check_mark:
  - format user input variable: convert string to lowercase :heavy_check_mark:
  - remove blank space from beginning and end of string :heavy_check_mark:
- be able to search for issues in github by either giving a link, :heavy_check_mark:,  or a number of keywords 
- be able to search for forum posts in community.grafana.com by either giving a link, or a number of keywords 
  - import and implement pygithub lib :heavy_check_mark: 
  - import and implement pydiscourse lib
  - manually obtain API keys: 
    - GitHub :heavy_check_mark:
    - Discourse
  - store the API keys in separate untracked files for better security :heavy_check_mark:
  - create a funtion to:
  
    - IF URL: 
      - detect whether the link belongs to GitHub / Discourse,  
      - then , call the respective API to GET the issue/topic keywords
      - finally, pass them into the pygithub and pydiscourse search functions (decide which search params we need)
      
    - IF keywords, 
      - pass it into the pygithub and pydiscourse search functions (decide which search params we need)
      - return a number of issues/topics that hopefully are relevant to what was searched.
 
- add error handling :hammer:

### Nice-to-have:

- enable using args when executing the script to perform different types of search (search titles, search comments, etc) 
