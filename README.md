# GRAFINDER
## a python app to find Grafana issues and community posts from one place

### To-do list:

1. when executing the script, pass a link as a arg. Take this input and store it in a variable
- create a function to:
  - validate length of input.  
  - format user input variable: convert string to lowercase
  - remove blank space from beginning and end of string
- be able to search issues in github, and forum posts in community.grafana.com by either giving a link, or a number of keywords (i.e. issue / topic description)
  - import requests pygithub pydiscourse libraries
  - manually obtain API keys from GH and Discourse
  - store the API keys in variables for better security
  - create a funtion to:
    - IF URL: GET the issue/topic keywords and pass it into the pygithub and pydiscourse search functions (decide which search params we need)
    - IF keywords, pass it into the pygithub and pydiscourse search functions (decide which search params we need)
    - return a number of issues/topics that hopefully are relevant to what was searched.
 


### Nice-to-have:

- enable using args when executing the script to perform different types of search (search titles, search comments, etc) 
