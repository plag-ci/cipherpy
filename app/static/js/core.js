$(document).ready(function(){	
	$("input").addClass("form-control");

	$(".select-input button").click(function(e){
		e.preventDefault();
		if ($(this).text() == 'Text Field'){
			$(".text-area").removeClass("hide");
			$(".file-area").addClass("hide");
		}else{
			$(".text-area").addClass("hide");
			$(".file-area").removeClass("hide");
		}



		// $("text-area").removeClass()
	});

	$('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        
        var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;
        
        if( input.length ) {
            input.val(log);
        } else {
            if( log ) alert(log);
        }
        
    });

	$("#algorithms select").change(function(){
		var v = $(this).val();
		c(v);
	    if(v == 1){
	    	$("#key-2, #key-1").removeClass("hide");
	    }
	    else if(v == 8){
	    	$("#key-1, #key-2").addClass("hide");
	    }
	    else{
	    	$("#key-2").addClass("hide");
	    	$("#key-1").removeClass("hide");
	    }
	});

	function c (a) {
		console.log(a);
	}
});

$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});