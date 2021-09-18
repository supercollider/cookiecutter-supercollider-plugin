cookiecutter-supercollider-plugin
=================================

A [cookiecutter] project template for [SuperCollider] server plugins.

To create a SuperCollider server plugin using this template, first
[install cookiecutter][installation instructions].

This cookiecutter template requires at least Python 3.2. If you have multiple versions of python and
are installing via `pip`, you may need to be explicit about which version of Python you use to
install it to ensure cookiecutter uses a compatible version. For example, on macOS with Python 3.7:

    $ python3.7 -m pip install cookiecutter

Then run:

    $ cookiecutter https://github.com/supercollider/cookiecutter-supercollider-plugin

and answer the questionnaire. See the [cookiecutter documentation] on how to change the default
values for these prompts.

After filling out the questionnaire, cookiecutter will clone the project, fill in placeholders with
your supplied information, run a Python script from the SuperCollider project to set up your CMake
files, and finally set up a git repository.

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

Explanation of questionnaire terms:

- project\_name: The name of the project, used in the README and CMakeLists.txt. Furthermore, the
  project\_name with spaces removed will be used as the base install folder.
- project\_namespace: C++ namespace for your plugin(s).
- repo\_name: GitHub repository name
- plugin\_name: Name of the first plugin in your project

Licensing
---------

The generated project will be GPLv3-licensed. **Make sure that you change the LICENSE file if you
want to use a more permissive license!**

Advanced instructions
---------------------

### Use Github Actions to automatically build, compile and release your plugins

When generating a project using this cookiecutter recipe, a config file is included in `.github/workflows/build.yml` containing an action for Github Actions to build, compile and zip up your code for MacOS, Linux and Windows. 

It is set to trigger on one event: If you push a new tag prefixed with `v` (eg. `v1.0` or `v4.0.1`) to your repo, Github Actions will activate and start the process of building and releasing. If succesful, your finished builds should appear in the *Releases* column.

You should get an email from Github once the run is finished, but otherwise you can navigate to the *Actions* pane on your Github repository to see the details and command outputs of each build.

### Requirements
------------

* Basic development tools (C++ compiler, cmake, etc.)
* Python >= 3.2
* Git
* [cookiecutter]

Known issues and future work
----------------------------

[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter documentation]: https://cookiecutter.readthedocs.io/en/0.9.1/advanced_usage.html#user-config-0-7-0
[SuperCollider]: https://github.com/supercollider/supercollider
[installation instructions]: http://cookiecutter.readthedocs.org/en/latest/installation.html
[Travis]: https://docs.travis-ci.com/user/getting-started/
[AppVeyor]: https://ci.appveyor.com/signup
