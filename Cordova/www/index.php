<?php
date_default_timezone_set("Asia/Taipei");
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

</head>
<style>
body {
  margin: 0;
  padding: 0;
  text-align: center;
  background: black;
  color: #c5c5c5;
  font-family: 'Gugi', cursive;
}

.hr {
  height: 2px;
  width: 80%;
  margin: 5% 10%;
  background-color: #0e5fb8;
}

th {
  border: 1px solid white;
}

i {
  cursor: pointer;
}

/*.tr1{*/
/*background-color: #b87c34;*/
/*}*/
/*.tr2{*/
/*background-color: #a0692f;*/
/*}*/
tr:nth-child(even) {
  background-color: #54575c;
}

td {
  height: 35px;
}

#check_count {
  font-size: 60px;
  letter-spacing: 20px;
  margin-top: 10%;
}

#table-IP_Date {
  width: 90%;
  margin: 0 5%;
  border: 1px solid #0e5fb8;
  font-size: 16px;
  text-align: center;

}
</style>

<body>
  <h1>監控紀錄</h1>
  <div class="hr"></div>
  <h5>登入時間 : <?php echo date("Y/m/d _ h:i 分"); ?></h5>
  <table id='table-IP_Date'>
    <tr style="font-size: 20px;color: #e79047">
      <th></th>
      <th>DATE</th>
      <th>TIME</th>
    </tr>
    <?php
        session_start();
        include('./db_connect.php');
        $Information = mysqli_query($link, "SELECT * FROM `date`");
        if (!$Information) {
            die('Invalid query:' . mysqli_error($link));
        }

        $Boolean = TRUE;

        for ($i = 0; $i < mysqli_num_rows($Information); $i++) {
            $rs = mysqli_fetch_row($Information);
            if ($Boolean == TRUE) {
        ?>
    <tr class='tr1'>
      <td><?php echo $rs[0] ?></td>
      <td><?php echo $rs[1] ?></td>
      <td><?php echo $rs[2] ?></td>
    </tr>
    <?php
            } else {
            ?>
    <tr class='tr2'>
      <td><?php echo $rs[0] ?></td>
      <td><?php echo $rs[1] ?></td>
      <td><?php echo $rs[2] ?></td>

    </tr>
    <?php
            }
            $Boolean = !$Boolean;
        } ?>
  </table>


  <?php
    session_destroy();
    mysqli_close($link);
    unset($link, $Information, $rs);
    ?>

</body>

</html>