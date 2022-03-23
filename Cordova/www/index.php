<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="format-detection" content="telephone=no">
  <meta name="msapplication-tap-highlight" content="no">
  <meta name="viewport"
    content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@100&display=swap" rel="stylesheet">

  <!-- <script type="text/javascript" src="js/cordova.js"></script> -->
  <link rel="stylesheet" type="text/css" href="css/main.css">
  <script src="js/jquery-3.6.0.min.js"></script>
  <title>監控紀錄</title>
</head>

<body>
  <h1>監控紀錄</h1>
  <div class="hr"></div>
  <table id="data_box"></table>

  <script>
  const box = document.getElementById('data_box');

  function get_api(params) {
    var data;
    $.ajax({
        method: "POST",
        url: "http://localhost:8080/info.php",
        data: {
          ID: "userid"
        },
        dataType: 'json'
      })
      .done(function(response) {
        var elem = '';
        $.each(response, function(index, value) {
          elem = elem + createDomElement(value);
        });
        box.innerHTML = `<tr style="font-size: 20px;color: #e79047"><th>DATE</th><th>TIME</th></tr>${elem}`;

      })
      .fail(function(msg) {
        console.log(msg);
      });
  }

  function createDomElement(value) {
    return `<td>${ value }</td>`;
  }
  get_api();
  </script>
  <!-- <script type="text/javascript" src="js/cordova.js"></script> -->
  <script type="text/javascript" src="js/index.js"></script>
</body>

</html>