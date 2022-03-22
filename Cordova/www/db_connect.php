<?php
$link = mysqli_connect(
    "localhost",
    "root",
    "password",
    "data");
    if(!$link){
        echo "DATE BASE";
        echo "(1)Error : Unable to connect to MySQL : " . PHP_EOL;
        echo "(2)Debugging errno : " . mysqli_connect_errno() . PHP_EOL;
        echo "(3)Debugging error : " . mysqli_connect_error() . PHP_EOL;
        exit;
    }
    $link->set_charset("utf8") ;



