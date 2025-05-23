# Git Hub Actions

# Actions:
  uses Keyword: can be fetch from three places
    - public repo: 
        uses: {owner}/{repo}@{ref-name}
        uses: actions/checkout@v4
    - Local Repo: 
        uses: ./patch/to/action
    - Docker Registry: 
        uses: docker://{image}:{tag}
# Run Keyword:
  - run is used to execute commands in default shell 
  - run: {command} {parameters} {arguments}
  - run: single line commands
  - run: |
      multiline command1
      multiline command2
# Need Keyword :
  - Need key word is used for dependency in other jobs so we use needs keyword in deployment

# Conditions in Actions
  - we have multiple conditions 
  - on:
      push:
        branches:
          - master
          - develop
          - release
  - on:
      pull_request:
        branches:
          - master
          - develop
  - on:
      ignore_branches:
        branches:
          - master
          - 'release/*' <!-- This is regular expression using * means all ? means particular -->
# Workflow actions and Limitation:
- One workflow can run 60 Hours

# Passing Arguments:
- uses: {git hub account }/{action name}
  with: 
    key1: Value1
    key2: Value2
- with:
    repository: github repo
    ref: master
    path: /github-name

# Environement Variables
- we can have default env variables = ALL should be in Capital Letters
- we can have env varibale at workflow level,job level,step level
- workflows: all jobs, steps are included
- jobs: all jobs and steps are included
- steps: all steps are included

# How to read Environment variables
- we can read two ways 
  - using shell based
    - using linux/MacOS
      - $ENVIRONMENT_NAME
    - Using Windows
      - $Env=ENVIRONMENT_NAME
  - using yaml syntax based
    - ${{ env.VARIABLE_NAME }}

# Accesing Secrets
- Secrets like api keys/tokens/passwords can be stored as environment variables in setting once saved we cant see them again
- we can uses them like below
  - {{ secrets.VARIABLE_NAME }}
  
# Artifacts Upload and Download
- Upload artifacts has: action/upload-artifact
- Download Artifacts has: actions/download-artifacts


