<?php

if(count($_FILES['files'])) {
	foreach ($_FILES['files'] as $file) {
	    
		//do your upload stuff here
		echo $file;
		
	}
}

?>
