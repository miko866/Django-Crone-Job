
$(document).ready(function() {

	/*
	* START jQuery for generate minutes, hours and months in crone.html
	*/

	var selectionMinutes = "";
	for (var i = 0; i < 61; i++) {
		var j = zeroFill(i, 2);
		selectionMinutes += "<option value='" + j + "'>" + j + "</option>";
	}
	$(".minutes-select").html(selectionMinutes);

	function zeroFill(number, width) {
		width -= number.toString().length;
		if (width > 0) {
			return new Array(width + (/\./.test(number) ? 2 : 1)).join('0') + number;
		}
		return number + ""; // always return a string
	}


	var selectionHours = "";
	for (var i = 0; i < 25; i++) {
		var j = zeroFill(i, 2);
		selectionHours += "<option value='" + j + "'>" + j + "</option>";
	}
	$(".hours-select").html(selectionHours);

	function zeroFill(number, width) {
		width -= number.toString().length;
		if (width > 0) {
			return new Array(width + (/\./.test(number) ? 2 : 1)).join('0') + number;
		}
		return number + ""; // always return a string
	}


	var selectionMonths = "";
	for (var i = 0; i < 13; i++) {
		var j = zeroFill(i, 2);
		selectionMonths += "<option value='" + j + "'>" + j + "</option>";
	}
	$(".month-select").html(selectionMonths);

	function zeroFill(number, width) {
		width -= number.toString().length;
		if (width > 0) {
			return new Array(width + (/\./.test(number) ? 2 : 1)).join('0') + number;
		}
		return number + ""; // always return a string
	}

	//* END jQuery for generate minutes, hours and months in crone.html


	// Auto hide Django messages
	$.when($('.alert')).then((self) => {
		window.setTimeout(function () {
			$(".alert").remove()
		}, 4000);
	});

});


