/*
* jQuery for generate minutes, hours and months in crone.html
*/

var selectionMinutes = "";
for(var i = 0; i < 61; i++)
{
    var j = zeroFill(i, 2);
    selectionMinutes += "<option value='"+ j +"00'>"+ j + "</option>";
}
$(".minutes-select").html(selectionMinutes);
function zeroFill( number, width )
{
  width -= number.toString().length;
  if ( width > 0 )
  {
    return new Array( width + (/\./.test( number ) ? 2 : 1) ).join( '0' ) + number;
  }
  return number + ""; // always return a string
}



var selectionHours = "";
for(var i = 0; i < 25; i++)
{
    var j = zeroFill(i, 2);
    selectionHours += "<option value='"+ j +"00'>"+ j + "</option>";
}
$(".hours-select").html(selectionHours);
function zeroFill( number, width )
{
  width -= number.toString().length;
  if ( width > 0 )
  {
    return new Array( width + (/\./.test( number ) ? 2 : 1) ).join( '0' ) + number;
  }
  return number + ""; // always return a string
}


var selectionMonths = "";
for(var i = 0; i < 13; i++)
{
    var j = zeroFill(i, 2);
    selectionMonths += "<option value='"+ j +"00'>"+ j + "</option>";
}
$(".month-select").html(selectionMonths);
function zeroFill( number, width )
{
  width -= number.toString().length;
  if ( width > 0 )
  {
    return new Array( width + (/\./.test( number ) ? 2 : 1) ).join( '0' ) + number;
  }
  return number + ""; // always return a string
}



//! Don't working
$(document).ready(function () {


		TriggerAlertClose();


		$('.alert').on('change', '.alert',function(e) {
    $(this).closest('.from-group').val(($('#want').is(':checked')) ? "yes" : "no");
    var ans=$(this).val();
    console.log(($('#want').is(':checked')));
});
});

function TriggerAlertClose() {
		window.setTimeout(function () {
			$(".alert").fadeTo(1000, 0).slideUp(1000, function () {
				$(this).remove();
			});
		}, 5000);
	}


