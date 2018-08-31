{{ cookiecutter.plugin_name }} : UGen {
	*ar { |input, gain|
		/* TODO */ ^this.multiNew('audio', input, gain);
	}
	checkInputs {
		/* TODO */
		^this.checkValidInputs;
	}
}
