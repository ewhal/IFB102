<?php
if (isset($_POST['action'])) {
	switch ($_POST['action']) {
	case 'start':
		start();
		break;
	case 'stop':
		stop();
		break;
	case 'prev':
		previousSong();
		break;
	case 'next':
		nextSong();
		break;
	case 'voldown':
		volDown();
		break;
	case 'volup':
		volUp();
		break;




	}
}

function start() {
	exec("mpc play");
	exit;
}

function stop() {
	exec("mpc stop");
	exit;
}
function previousSong() {
	exec("mpc prev");
	exit;
}
function nextSong() {
	exec("mpc next");
	exit;
}
function volDown() {
	exec("mpc volume -10");
	exit;
}
function volUp() {
	exec("mpc volume +10");
	exit;
}
?>

