<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
		<title>Home Page</title>

		<!-- Bootstrap -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<link href="css/font-awesome.min.css" rel="stylesheet">
		<link href="css/main.css" rel="stylesheet">

		<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
		<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
		<!--[if lt IE 9]>
		<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
		<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
		<![endif]-->
 	</head>
	<body>
	<div class="container text-center">
		<div class="row">
			<div class="col-md-8">
				<input type="submit" class="btn btn-success" name="start" value="start" />
				<input type="submit" class="btn btn-danger" name="stop" value="stop" />
				<input type="submit" class="btn btn-primary" name="prev" value="prev" />
				<input type="submit" class="btn btn-primary" name="next" value="next" />
				<input type="submit" class="btn btn-primary" name="voldown" value="voldown" />
				<input type="submit" class="btn btn-primary" name="volup" value="volup" />
			</div>
		</div>

		<div class="row">
			<div class="col-md-8">
				<?php
				echo "<h1>Now Playing</h1>";
				echo "<p>",file_get_contents("http://localhost/cgi-bin/mpcinfo.py"),"</p>";

				?>
			</div>
		</div>


		<div class="row">
			<div class="col-md-8">
				<a href="upload.html">Upload songs</a>
				<a href="//git.pantsu.cat/ewhal/raspi">Git Repo</a>

			</div>
		</div>
	</div>

	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	<!-- Include all compiled plugins (below), or include individual files as needed -->
	<script src="js/bootstrap.min.js"></script>
	<script src="js/main.js"></script>
  </body>
</html>

