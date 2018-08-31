#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Init git repository and make initial commit.'''

from subprocess import check_call
from subprocess import call
import os

git_url = 'git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
sc_path = '{{ cookiecutter.full_path_to_supercollider_source }}'
script_path = os.path.join(sc_path, 'tools/cmake_gen/generate_server_plugin_cmake.py')

print('\nRunning post-project-generation hook...\n')

print('Initializing new Git repository')
check_call(['git', 'init'])
print('Running CMake generation script')
call([
    'python',
    script_path,
    '.',
    '-P', '{{ cookiecutter.project_name }}',
    '-p', 'plugins/{{ cookiecutter.plugin_name }}',
    '-a', '{{ cookiecutter.full_name }}',
    '--install-cmake'
    ])

print('Adding Git remote for plugin project')
check_call(['git', 'remote', 'add', 'origin', git_url])
print('Making initial Git commit')
check_call(['git', 'add', '-A'])
check_call(['git', 'commit', '-m', 'Initial commit'])

print('\nDone!')
