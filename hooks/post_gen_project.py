#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Init git repository and make initial commit.'''

from subprocess import check_call
from subprocess import call
import os

git_url = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'
sc_path = '{{ cookiecutter.full_path_to_supercollider_source.strip() }}'
script_path = os.path.join(sc_path, 'tools/cmake_gen/generate_server_plugin_cmake.py')

print('\nRunning post-project-generation hook...')

print('\nInitializing new Git repository')
check_call(['git', 'init'])
print('\nRunning CMake generation script')
call([
    'python',
    script_path,
    '.',
    '-P', '{{ cookiecutter.project_name }}',
    '-p', 'plugins/{{ cookiecutter.plugin_name }}',
    '-a', '{{ cookiecutter.full_name }}',
    '--install-cmake'
    ])

print('\nAdding Git remote for plugin project')
check_call(['git', 'remote', 'add', 'origin', git_url])
print('\nMaking initial Git commit')
check_call(['git', 'add', '-A'])
check_call(['git', 'commit', '-m', 'Initial commit'])

print('\nYour project was successfully created!\n')

post_info = '''
Check the README in the cookiecutter project and the README in your generated
project for helpful information such as how to build your project, how to set up
continuous integration, how to automatically deploy releases to GitHub, and how
to tweak the project itself.
'''

print(post_info)
