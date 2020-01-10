const PLUGIN_ID = 'signalk-vanguard-plugin';
const SerialPort = require('serialport')
const _ = require("lodash")

const keyPrefix = 'environment.'

module.exports = function (app) {
	var plugin = {};

	plugin.id = PLUGIN_ID
	plugin.name = "Vanguard Piloting and Reporting";
	plugin.description = "Explores and maps water depth";

	plugin.start = function() {
		//here we put our function logic
		app.debug('Vanguard Plugin Started');
	};

	plugin.stop = function() {
		//Here we put logic we need when plugin stops
		app.debug('Vanguard Plugin Stopped')
	};

	plugin.schema = {
		//The plugin schema
	};

	return plugin;
}
