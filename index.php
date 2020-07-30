<?php
    //require_once "pdo.php";
    require_once "pdo2.php";

?>


<html>
    <head>
        <title>Detailed US COVID Map</title>
    </head>


    <body>
        <?php
            $data = $pdo->query("SELECT * FROM Covid");
            
            echo("<pre>");
            while ($row = $data->fetch(PDO::FETCH_ASSOC)) {
                echo($row['date'] . ' ' . $row['state'] . ' ' . $row['code'] . ' ' . $row['positive'] . ' ' . $row['deaths']);
                echo("<br>");
            }
            echo("</pre>");
        ?>

    </body>




</html>