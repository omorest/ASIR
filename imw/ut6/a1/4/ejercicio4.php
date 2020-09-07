<html>
  <head>
  <meta charset="utf-8">
  <head/>
  <body>
    <table border = "2">
      <?php
      if (isset($_POST["filas"]) and isset($_POST["columnas"])) {
          $filas = $_POST["filas"];
          $columnas = $_POST["columnas"];

          if ($filas >= 1 and $columnas >= 1) {
            $c = 1;
            $f = 1;
              while ($f<=$filas) {
                  $f++;
                  echo("<tr>");
                  while ($c<=$columnas) {
                      $c++;
                      echo("<td>Prueba</td>");
                  }
                  $c = 1;
                  echo("</tr>");
              }
          }
          else{
              echo("Error: El número de columnas y filas tiene que ser de mínimo 1");
          }
      }

      ?>
      <table/>
    <body/>
<html/>
