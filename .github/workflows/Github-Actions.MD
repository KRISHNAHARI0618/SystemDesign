## Git Hub Actions

Actions:
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
# 

