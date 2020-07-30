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
            
            echo('<table border="1">');
            echo('<tr><td>');
            echo('<b>Date</b>');
            echo('</td><td>');
            echo('<b>State</b>');
            echo('</td><td>');
            echo('<b>Code</b>');
            echo('</td><td>');
            echo('<b>Cases<b>');
            echo('</td><td>');
            echo('<b>Deaths</b>');
            echo('</td>');

            while ($row = $data->fetch(PDO::FETCH_ASSOC)) {
                echo('<tr><td>');
                echo($row['date']);
                echo('</td><td>');
                echo($row['state']);
                echo('</td><td>');
                echo($row['code']);
                echo('</td><td>');
                echo($row['positive']);
                echo('</td><td>');
                echo($row['deaths']);
                echo("</td></tr>");
            }
            echo("</table>");
        ?>

        <br>
        <br>

        <p>By Lavindu Devadithya</p>
    </body>




</html>