<?php
    require_once "pdo.php";

?>


<html>
    <head>
        <title>US COVID Map</title>
    </head>


    <body>
        <?php
            $data = $pdo->query("SELECT cases, deaths FROM Covid");
            
            while ($row = $data->fetch(PDO::FETCH_ASSOC)) {
                echo($row['cases']);
                echo($row['deaths']);
            }
        ?>

    </body>




</html>