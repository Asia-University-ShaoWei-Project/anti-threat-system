<?php
require_once('db_conn.php');
header('Access-Control-Allow-Origin: *');
header("Content-Type: application/json; charset=UTF-8");
$db = NewDB('./db');
$response = array();
$user_id = $_POST['ID'];
$stmt = $db->prepare('SELECT date, time FROM infos WHERE ID=:id');
$stmt->bindValue(':id', $user_id, SQLITE3_TEXT);
$result = $stmt->execute();
$data = $result->fetchArray(SQLITE3_ASSOC);
var_dump($data);
$db->close();
echo json_encode($data);