<?php
$uploads_dir = 'uploads/';

foreach ($_FILES["files"]["error"] as $key => $error) {
    if ($error == UPLOAD_ERR_OK) {
        $tmp_name = $_FILES["files"]["tmp_name"][$key];
        $name = $_FILES["files"]["name"][$key];
		$upload = "$uploads_dir$name";
        move_uploaded_file($tmp_name, "$upload");
		chmod($upload, 0777);
		exec("mpc add $name");
    }
}
exec("mpc update");
echo "<a href=\"$_SERVER['SERVER_ADDR']:8000\/mpd\">IceCast Steam</a>"; 
?>

