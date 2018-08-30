#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Init git repository and make initial commit."""

from subprocess import call

git_url = "git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}"

print("\nRunning post-project-generation hook...\n")

print("Initializing new Git repository:")
call(['git', 'init'])
print("Adding Git remote for plugin project:")
call(['git', 'remote', 'add', 'origin', git_url])
print("Making initial Git commit:")
call(['git', 'add', '-A'])
call(['git', 'commit', '-m', 'Initial commit'])

print("\nDone!")
