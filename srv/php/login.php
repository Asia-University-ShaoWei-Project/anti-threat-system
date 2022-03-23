<?php
require_once('db_conn.php');

header("Content-Type: application/json; charset=UTF-8");
$response = array('token' => '');
$id = $_POST['ID'];
$password = $_POST['password'];
if (!empty($id) and !empty($password)) {
  $db = NewDB('./db');
  $stmt = $db->prepare('SELECT ID FROM users WHERE ID=:id, password=:password)');
  $stmt->bindValue(':id', $id, SQLITE3_TEXT);
  $stmt->bindValue(':password', $password, SQLITE3_TEXT);
  $result = $stmt->execute();
  if ($result->fetchArray()) {
    $token = get_new_token();
    insert_user_token($db, $ID, $token);
    $response = $token;
  }
}
echo $response;
// 
function get_new_token(): string
{
  $token = uniqid();
  return $token;
}
function insert_user_token(DB $db, string $ID, $new_token)
{
  $stmt = $db->prepare('UPDATE users SET token=:new_token WHERE ID=:token');
  $stmt->bindParam(':new_token', $new_token, SQLITE3_TEXT);
  $stmt->bindParam(':token', $token, SQLITE3_TEXT);
  $stmt->execute();
}
$db->close();

echo http_response_code(200);