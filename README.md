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

Requirements
------------

* Basic development tools (C++ compiler, make, pkg-config, etc.)
* Python >= 3.2
* Git
* [cookiecutter]


[cookiecutter]: https://github.com/audreyr/cookiecutter
[cookiecutter documentation]: https://cookiecutter.readthedocs.io/en/0.9.1/advanced_usage.html#user-config-0-7-0
[SuperCollider]: https://github.com/supercollider/supercollider
[installation instructions]: http://cookiecutter.readthedocs.org/en/latest/installation.html
