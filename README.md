## PBFetcher for Monkeytype
Made with ❤️ by skill3472


**This is a python script that fetches your Personal Best from [Monkeytype](monkeytype.com), and puts it in a text file.**
**An example use case would be editing your Github README to reflect your current PB.**

## Getting an API key
To get a monkeytype API key visit your [monkeytype settings](https://monkeytype.com/settings) and find the *ape keys* section, under *danger zone*. Generate one, activate it with a tickbox that appears next to it and you're done!

## GitHub workflow
Here is an example GH Workflow for updating your README.md:
```yml
name: README Update

on:
  schedule:
    - cron: "1/15 * * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: "Fetch files"
        uses: actions/checkout@v2
        with:
          persist-credentials: false
          fetch-depth: 0
      - name: "Update"
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          pip3 install -r requirements.txt
          python3 fetcher.py $API_KEY
      - name: "Commit"
        run: |
          git config --global user.email "420+github-actions[bot]@users.noreply.github.com"
          git config --global user.name "github-actions[bot]"
          git add .
          git commit -am "README update Automation"
      - name: "Push changes"
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
```
1. Put this into your `.github/workflows/` directory and remember to change the actions permissions, so it can write to the repository. 
2. You also need to have all the files present in this repo for this to work (obviously not the README.md file, you should move it somewhere else, or remove it). 
3. Change the `outfile` option in `config.yml` to `README.md`
4. Watch it go!
