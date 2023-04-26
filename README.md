# GRAFINDER
## a python app to find Grafana issues and community posts from one place

### To-do list:

1. when executing the script, pass a link as a arg. Take this input and store it in a variable
- create a function to:
  - validate length of input.  
  - format user input variable: convert string to lowercase
  - remove blank space from beginning and end of string
  - perhaps also clean characters like apostrophes and things like that
- be able to escape the app entering a keyword ('q')
- be able to search issues in github (grafana/grafana) and forum posts in community.grafana.com via HTTP request
  - import requests pygithub pydiscourse libraries
  - manually obtain API keys from GH and Discourse
  - store the API keys in variables as a start and later store in env variables for better security
  - create a funtion to:
    - pass the value of user input into the pygithub and pydiscourse search functions (decide which search params we need)
    - iterate (create a for loop in python) through the response
    - return the items from the response


### Nice-to-have:

- have functions for different types of search (search titles, search comments, etc) or make functions more powerful by adding function args, so the user can pass arguments to refine their search
