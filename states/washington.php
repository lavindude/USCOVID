<?php
    require_once "pdo.php";

    echo('<table border="1">');
    echo('<tr><td>');
    echo('<b>Date</b>');
    echo('</td><td>');
    echo('<b>Positive</b>');
    echo('</td><td>');
    echo('<b>Recovered</b>');
    echo('</td><td>');
    echo('<b>Deaths<b>');
    echo('</td><td>');
    echo('<b>Positive Cases Increase (daily cases)</b>');
    echo('</td><td>');
    echo('<b>Death Increase (daily deaths)</b>');
    echo('</td>');

    $data = $pdo->query("SELECT * FROM covid WHERE state_id=47");
    while ($row = $data->fetch(PDO::FETCH_ASSOC)) {
        echo('<tr><td>');
        echo($row['date']);
        echo('</td><td>');
        echo($row['positive']);
        echo('</td><td>');
        echo($row['recovered']);
        echo('</td><td>');
        echo($row['deaths']);
        echo('</td><td>');
        echo($row['positiveincrease']);
        echo('</td><td>');
        echo($row['deathincrease']);
        echo("</td></tr>");
    }

    echo("</table>");


?>