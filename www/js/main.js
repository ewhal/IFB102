$(document).on('change', '.btn-file :file', function() {
	var input = $(this),
	numFiles = input.get(0).files ? input.get(0).files.length : 1,
	label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
	input.trigger('fileselect', [numFiles, label]);
});

$(document).ready( function() {
	$('.btn-file :file').on('fileselect', function(event, numFiles, label) {

		var input = $(this).parents('.input-group').find(':text'),
		log = numFiles > 1 ? numFiles + ' files selected' : label;

		if( input.length ) {
			input.val(log);
		} else {
			if( log ) alert(log);
		}

	});
});
$(document).ready(function(){
        var ip = "http://" + location.host + "/cgi-bin/mpcinfo.py";
        $('.btn').click(function(){
                var clickBtnValue = $(this).val();
                var ajaxurl = 'mpdcontrol.php',
                data =  {'action': clickBtnValue};

                $.post(ajaxurl, data, function (response) {
                        alert("action performed successfully");
                        $.get(ip, function(data){
                                document.getElementById("p1").innerHTML = data;
                        });

                });
        });
        setInterval($.get(ip, function(data){
                document.getElementById("p1").innerHTML = data;
        }), 1000 * 60 * 1);


});
