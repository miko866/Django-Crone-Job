/*
* START jQuery for generate minutes, hours and months in crone.html
*/
$(document).ready(function() {
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

	/*$.when($('.alert')).then((self) => {
		window.setTimeout(function () {
		$(".alert").fadeOut(300, onHide);
	}, 2000); });

	onHide = function() {
		$(".alert").remove();
	  };*/

//$(":radio").removeAttr("checked").parent().removeClass("custom-form_flex");

	/*var disableElement = function () {
		var radios = $(':radio');
		var radiosChecked = $(':radio:checked');

		if (radiosChecked) {
			$('.disabled').prop("disabled", false);
		} else {
			$('.disabled').prop("disabled", 'disabled');
		}

	};


	$(disableElement());
	$(":radio").change(disableElement());*/

	/*$(":radio").click(function(){
		if ($(':radio:checked')) {
			$(".disabled").prop("disabled", false)
		} else {
			$(".disabled").prop("disabled", true)
		}
	});*/

	/*$(":radio:checked").click(function(){
  		$(".custom-select").toggleClass("disabled");
	});*/

	// By Default Disable radio button
	/*$(".disabled").attr('disabled', true);
	// Disable radio buttons function on Check Disable radio button.
	$("form input:radio").change(function() {
		if ($(':radio:checked').val()) {
			$(".disabled").prop("disabled", true);
			$(".wrap").css('opacity', '.2');
		}
		// Else Enable radio buttons.
		else {
			$(".disabled").prop("disabled", false);
			$(".wrap").css('opacity', '1');
		}
	});*/

});
/*var update_radio = function () {
    if ($(":radio").is(":checked")) {
        $('.disable').prop('disabled', false);
    }
    else {
        $('.disable').prop('disabled', 'disabled');
    }
  };
  $(update_radio);
  $(":radio").change(update_radio);*/
