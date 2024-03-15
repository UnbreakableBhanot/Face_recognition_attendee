<?php
$executeCommand = escapeshellcmd('C:\Users\shubh\PycharmProjects\Face\venv\Scripts\python.exe C:\Users\shubh\PycharmProjects\Face\main.py');
shell_exec($executeCommand);
#$output = shell_exec($executeCommand);

$showCommand = escapeshellcmd('C:\Users\shubh\PycharmProjects\Face\venv\Scripts\python.exe C:\Users\shubh\PycharmProjects\Face\show_sql.py');
$output = shell_exec($showCommand);
echo $output
?>