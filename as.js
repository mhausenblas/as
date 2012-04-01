var cloudant_username = 'xxx';
var cloudant_password = 'xxx';

// requires that indexing has been enabled - looks up term in the database 'db' of the owner
function gen_cloudant_lookup_url(owner, db, term){
	return 'https://' +  cloudant_username + ':' + cloudant_password + '@cloudant.com/db/' + owner +'/'+  db + '/_search?q=' + $('#as_in').val() + '&limit=1&include_docs=true';
}

$(function() {
	$('#as_in').keyup(function(e){
		var code = (e.keyCode ? e.keyCode : e.which);
		if($('#as_in').val().length < 2) return;
		if(code == 13) { // user pressed 'ENTER'
			$('#as_out').html('looking up ' + $('#as_in').val() +  ' - a moment please ...');
			$.getJSON('http://localhost:6969/r/' + gen_cloudant_lookup_url('dequilibrium', 'as', $('#as_in').val()), null,
			 function(data){
				$('#as_out').html('<div>I found the following explanation for ' + $('#as_in').val() + ':</div>');
				$('#as_out').append('<div class="result"><strong>' + data.rows[0].doc.fulltitle + '</strong><div>... see also <a href="' + data.rows[0].doc.ref + '" target="_new">' + data.rows[0].doc.ref + '</a></div></div>');
			});
		}
	});
});