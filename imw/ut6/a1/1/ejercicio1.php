<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Probando PHP!!</title>
    </head>
    <body>
        <?php
            $rand = mt_rand (1,2);
            echo("<img src='$rand.png'>");
        ?>
    </body>
</html>
