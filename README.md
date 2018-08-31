cookiecutter-supercollider-plugin
=================================

A [cookiecutter] project template for [SuperCollider] server plugins.

To create a SuperCollider server plugin using this template, [install cookiecutter][installation
instructions] and then run:

    $ cookiecutter https://github.com/supercollider/cookiecutter-supercollider-plugin

and answer the questionnaire. See the [cookiecutter documentation] on how to change the default
values for these prompts.

After filling out the questionnaire, cookiecutter will clone the project, filling in all the
placeholders with your supplied values; run a Python script from the SuperCollider project to set up
your CMake files, and set up a git repository.

Here is an example:

    $ cookiecutter https://github.com/brianlheim/cookiecutter-supercollider-plugin
    full_path_to_supercollider_source [/home/wendy/supercollider (if you haven't cloned it yet, do that first! Press Ctrl-C to exit this script.]: /Users/brianheim/git/supercollider
    project_name [Simple Gain]:
    project_namespace [SimpleGain]:
    repo_name [simplegain]:
    plugin_name [SimpleGain]:
    plugin_description [A simple audio volume gain plugin]:
    full_name [Wendy Carlos]: Brian Heim
    github_username [brian.heim]: brianlheim
    email [brianlheim@site.com]: brianlheim@gmail.com

    Running pre-project-generation hook...

    Checking Python version...

    Checking for SuperCollider repository...

    Running post-project-generation hook...

    Initializing new Git repository
    Initialized empty Git repository in /Users/brianheim/git/simplegain/.git/

    Running CMake generation script
    Wrote project file to /Users/brianheim/git/simplegain/CMakeLists.txt
    Installed 2 CMake modules

    Adding Git remote for plugin project

    Making initial Git commit
    [master (root-commit) 261d980] Initial commit
     12 files changed, 1031 insertions(+)
     create mode 100644 .appveyor.yml
     create mode 100644 .gitignore
     create mode 100644 .travis.yml
     create mode 100644 CMakeLists.txt
     create mode 100644 LICENSE
     create mode 100644 README.md
     create mode 100644 cmake_modules/SuperColliderCompilerConfig.cmake
     create mode 100644 cmake_modules/SuperColliderServerPlugin.cmake
     create mode 100644 plugins/SimpleGain/SimpleGain.cpp
     create mode 100644 plugins/SimpleGain/SimpleGain.hpp
     create mode 100644 plugins/SimpleGain/SimpleGain.sc
     create mode 100644 plugins/SimpleGain/SimpleGain.schelp

    Done!

Enter the directory and build the project:

    $ cd simplegain
    $ mkdir build
    $ cd build
    $ cmake .. -DCMAKE_BUILD_TYPE=Debug
    $ cmake --build . --config Debug

If you add more plugins, or add or remove files, make sure to regenerate the CMakeLists.txt file
using the generation script. See the README in `tools/cmake_gen` for more info, or run the script
with `--help`.

    $ python ../supercollider/tools/cmake_gen/generate_server_plugin_cmake.py --help

Advanced instructions
---------------------

### Continuous Integration: Travis-CI and AppVeyor

Your auto-generated project will contain configuration files for the [Travis-CI][Travis] and
[AppVeyor] integration services. These are tools that let you see how your project compiles on a
totally fresh and isolated system. The Travis-CI script is configured for building on Linux (Ubuntu
14.04) and MacOS; the AppVeyor script is configured for both 32-bit and 64-bit Windows builds.

Every time you update your remote repository on GitHub, these scripts will run so you can see
whether or not your project builds properly in each of the tested environments.

To enable these services, you need to create accounts with both Travis-CI and AppVeyor, then follow
their instructions for adding projects. Do this after you create your repository on GitHub.

Travis: https://docs.travis-ci.com/user/getting-started/

AppVeyor: https://ci.appveyor.com/signup

Requirements
------------

* Basic development tools (C++ compiler, cmake, etc.)
* Python >= 3.2
* Git
* [cookiecutter]

Known issues and future work
----------------------------

- CMake >= 3.10 is required, but it should be possible to use >= 3.5. Flags for
`cmake_host_system_information` were not added until 3.10
- Linux build fails for previous reason
- Add ability & info for deploying releases to github
- Add info for post-project setup
- Better default install location

[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter documentation]: https://cookiecutter.readthedocs.io/en/0.9.1/advanced_usage.html#user-config-0-7-0
[SuperCollider]: https://github.com/supercollider/supercollider
[installation instructions]: http://cookiecutter.readthedocs.org/en/latest/installation.html
[Travis]: https://docs.travis-ci.com/user/getting-started/
[AppVeyor]: https://ci.appveyor.com/signup
