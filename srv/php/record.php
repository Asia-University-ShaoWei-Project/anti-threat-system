<?php
require_once('db_conn.php');

header("Content-Type: application/json; charset=UTF-8");
$db = NewDB('./db');

// TODO: auth the bearer
$date = $_POST['date'];
$time = $_POST['time'];

$stmt = $db->prepare('INSERT INTO infos(date, time) VALUES(:date, :time)');
$stmt->bindValue(':date', $date, SQLITE3_TEXT);
$stmt->bindValue(':time', $time, SQLITE3_TEXT);
$stmt->execute();
$db->close();
echo http_response_code(200);