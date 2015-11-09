<?php
  $site = $_POST['rss'];
  $python = "python ./python/rss.py $site";
  $handle = popen($python , 'r');
  $read = fread($handle, 2096);
  echo $read;
  pclose($handle);
?>
