<?php
require_once('db_conn.php');
header("Content-Type: application/json; charset=UTF-8");
$db = NewDB('./db');
$response = array();
$stmt = $db->prepare('SELECT date, time FROM infos');
$stmt->execute();
$db->close();
echo json_encode($result->fetchArray());
