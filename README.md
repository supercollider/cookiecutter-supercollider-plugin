cookiecutter-supercollider-plugin
=================================

A [cookiecutter] project template for [SuperCollider] server plugins.

To create a SuperCollider server plugin using this template, install cookiecutter (see the
[installation instructions]) and then run:

    $ cookiecutter https://github.com/supercollider/cookiecutter-supercollider-plugin

and answer the questionnaire. See the [cookiecutter documentation] on how to change the default
values for these prompts.

Here is an example:

    TODO

Enter the directory and run:

    $ cd myproject
    $ mkdir build
    $ cd build
    $ cmake .. -DCMAKE_BUILD_TYPE=Debug
    $ cmake --build . --config Debug

TODO more instructions

Advanced instructions
---------------------

### Continuous Integration: Travis-CI and AppVeyor

Your auto-generated project will contain configuration files for the [Travis-CI] and [AppVeyor]
integration services. These are tools that let you see how your project compiles on a totally fresh
and isolated system. The Travis-CI script is configured for building on Linux (Ubuntu 14.04) and
MacOS; the AppVeyor script is configured for both 32-bit and 64-bit Windows builds.

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
- Add more info on what setup script does
- Add git info for post-project setup
- Show example run

[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter documentation]: https://cookiecutter.readthedocs.io/en/0.9.1/advanced_usage.html#user-config-0-7-0
[SuperCollider]: https://github.com/supercollider/supercollider
[installation instructions]: http://cookiecutter.readthedocs.org/en/latest/installation.html
[Travis]: https://docs.travis-ci.com/user/getting-started/
[AppVeyor]: https://ci.appveyor.com/signup
