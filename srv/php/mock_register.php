<?php
require_once('db_conn.php');
$db = NewDB('./db');

$id = 'id1';
$password = 'password';
$stmt = $db->prepare('INSERT INTO users(ID, password) VALUES(:id, :password)');
$stmt->bindValue(':id', $id, SQLITE3_TEXT);
$stmt->bindValue(':password', $password, SQLITE3_TEXT);
$stmt->execute();
$db->close();
echo http_response_code(200);
