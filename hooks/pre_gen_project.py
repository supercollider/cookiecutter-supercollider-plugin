#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Validate template arguments.'''

import os
import sys

sc_path = '{{ cookiecutter.full_path_to_supercollider_source }}'

print('\nRunning pre-project-generation hook...')

print('\nChecking Python version...')

version = sys.version_info
if version < (3, 2):
    print('Python version must be at least 3.2')
    exit(3)

print('\nChecking for SuperCollider repository...')

if not os.path.exists(sc_path):
    print('SuperCollider repo not found: {}'.format(sc_path))
    exit(1)

script_path = os.path.join(sc_path, 'tools/cmake_gen/generate_server_plugin_cmake.py')
if not os.path.exists(script_path):
    print('Could not find CMake generation script: {}'.format(script_path))
    exit(1)
