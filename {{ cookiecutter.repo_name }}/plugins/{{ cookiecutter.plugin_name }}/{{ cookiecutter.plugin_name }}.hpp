// Plugin{{ cookiecutter.plugin_name }}.hpp
// {{ cookiecutter.full_name }} ({{ cookiecutter.email }})

#pragma once

#include "SC_PlugIn.hpp"

namespace {{ cookiecutter.project_namespace }} {

class {{ cookiecutter.plugin_name }} : public SCUnit {
public:
    {{ cookiecutter.plugin_name }}();

    // Destructor
    // ~{{ cookiecutter.plugin_name }}();

private:
    // Calc function
    void next(int nSamples);

    // Member variables
};

} // namespace {{ cookiecutter.project_namespace }}
