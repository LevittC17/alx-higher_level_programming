#!/usr/bin/python3

"""
List 10 commits from the most recent to oldest
of the repo by user
Argument: repository name, owner name
use requests package
"""


import requests
import sys


def main():
    # Fetch
    repo_name = sys.argv[1]
    owner = sys.argv[2]

    # Fetch the Repository URL
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f'{sha}: {author_name}')


if __name__ == "__main__":
    main()
