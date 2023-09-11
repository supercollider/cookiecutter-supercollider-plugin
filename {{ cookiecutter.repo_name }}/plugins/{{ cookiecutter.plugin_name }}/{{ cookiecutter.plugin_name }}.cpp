// Plugin{{ cookiecutter.plugin_name }}.cpp
// {{ cookiecutter.full_name }} ({{ cookiecutter.email }})

#include "SC_PlugIn.hpp"
#include "{{ cookiecutter.plugin_name }}.hpp"

static InterfaceTable* ft;

namespace {{ cookiecutter.project_namespace }} {

{{ cookiecutter.plugin_name }}::{{ cookiecutter.plugin_name }}() {
    mCalcFunc = make_calc_function<{{ cookiecutter.plugin_name }}, &{{ cookiecutter.plugin_name }}::next>();
    next(1);
}

void {{ cookiecutter.plugin_name }}::next(int nSamples) {

    // Audio rate input
    const float* input = in(0);

    // Control rate parameter: gain.
    const float gain = in0(1);

    // Output buffer
    float* outbuf = out(0);

    // simple gain function
    for (int i = 0; i < nSamples; ++i) {
        outbuf[i] = input[i] * gain;
    }
}

} // namespace {{ cookiecutter.project_namespace }}

PluginLoad({{ cookiecutter.plugin_name }}UGens) {
    // Plugin magic
    ft = inTable;
    registerUnit<{{ cookiecutter.project_namespace }}::{{ cookiecutter.plugin_name }}>(ft, "{{ cookiecutter.plugin_name }}", false);
}
