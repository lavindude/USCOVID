<?php
    require_once "pdo.php";

?>


<html>
    <head>
        <title>Detailed US COVID Map</title>
    </head>


    <body>
        <?php
            $data = $pdo->query("SELECT cases, deaths FROM Covid");
            
            while ($row = $data->fetch(PDO::FETCH_ASSOC)) {
                echo('Cases: ' . $row['cases']);
                echo('Deaths: ' . $row['deaths']);
            }
        ?>


        <p>Hello world</p>
    </body>




</html>