<head>
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Work+Sans:400,600">
    <title>State Information</title>
</head>

<body style="font-family: 'Work Sans', sans-serif">
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
    echo('<b>Recovered</b>');
    echo('</td><td>');
    echo('<b>Deaths<b>');
    echo('</td><td>');
    echo('<b>Δ Positive Cases</b>');
    echo('</td><td>');
    echo('<b>Δ Deaths</b>');
    echo('</td>');

    $data = $pdo->query("SELECT * FROM covid WHERE state_id=$id ORDER BY date DESC");
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

    echo("<br>");
    echo("**Note that some states may not have 'recovered' data because that data is not obtainable for certain states.**");
    echo('<p ><a href="./">Back to US Map</a></p>');
?>
</body>