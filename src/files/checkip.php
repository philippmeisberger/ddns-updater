<?php
  //E_ALL for testing
  //0 for productive
  error_reporting(0);
  header('Content-Type: text/plain');
  echo htmlspecialchars($_SERVER['REMOTE_ADDR'], ENT_QUOTES);
?>
