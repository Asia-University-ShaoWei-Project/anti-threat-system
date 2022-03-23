<?php
session_start();
date_default_timezone_set("Asia/Taipei");

$domain = "http://localhost";
$resource = '/info';

$URL = $domain . $resource;

$json = file_get_contents($URL);
$data = json_decode($json);
// TODO: test data response
echo $data;
// TODO: login
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>監控紀錄</title>
  <link href="https://fonts.googleapis.com/css?family=Gugi" rel="stylesheet">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css"
    integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
  <link rel="stylesheet" type="text/css" href="css/main.css">
</head>

<body>
  <h1>監控紀錄</h1>
  <div class="hr"></div>
  <table>
    <tr style="font-size: 20px;color: #e79047">
      <th>DATE</th>
      <th>TIME</th>
    </tr>
    <?php
        for ($i = 0; $i < count($data); $i++) {
            $row = $data[$i];
            $date = $row['date'];
            $time = $row['time'];
            echo "<tr><td>.$date.</td><td>.$time.</td></tr>";
        }
        ?>
  </table>
</body>

</html>