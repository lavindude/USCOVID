<div style="font-family: 'Work Sans', sans-serif; font-weight: 800;">

<head>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Work+Sans:400,600" rel='stylesheet' type='text/css'>
    <title>State Information</title>
</head>

<body>
<?php
    require_once "pdo.php";
    $id = $_GET['state_id'];

    $stateData = $pdo->query("SELECT * FROM states WHERE state_id=$id");
    echo("<h1>");
    while ($row = $stateData->fetch(PDO::FETCH_ASSOC)) {
        echo($row['name']);
    }
    
    echo("</h1>"); 


    echo('<table border="1">');
    echo('<tr><td>');
    echo('<b>Date</b>');
    echo('</td><td>');
    echo('<b>Positive</b>');
    echo('</td><td>');
    echo('<b>Deaths<b>');
    echo('</td><td>');
    echo('<b>Δ Positive Cases</b>');
    echo('</td><td>');
    echo('<b>Δ Deaths</b>');
    echo('</td>');

    $data = $pdo->query("SELECT * FROM covid WHERE state_id=$id ORDER BY date DESC");
    while ($row = $data->fetch(PDO::FETCH_ASSOC)) {
        if ($row['positiveincrease'] == 0) {
            echo('<tr><td>');
            echo($row['date']);
            echo('</td><td>');
            echo("No new data");
            echo('</td><td>');
            echo("No new data");
            echo('</td><td>');
            echo("No new data");
            echo('</td><td>');
            echo("No new data");
            echo("</td></tr>");
        }
        
        else {
            echo('<tr><td>');
            echo($row['date']);
            echo('</td><td>');
            echo($row['positive']);
            echo('</td><td>');
            echo($row['deaths']);
            echo('</td><td>');
            echo($row['positiveincrease']);
            echo('</td><td>');
            echo($row['deathincrease']);
            echo("</td></tr>");
        }
    }

    echo("</table>");

    echo("<br>");

    echo('<p ><a href="./">Back to US Map</a></p>');
?>

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.
</body>
<div>
