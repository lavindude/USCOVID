<?php
    echo('style="background-color: #00bcff;"');
    echo("Welcome to my COVID map! I hope you are safe and healthy. ");
    echo("<br><br>");
    echo('<img src="graph.png">');
    echo("Red means that the the slope of the graph above is greater than 50.<br>");
    echo("Yellow means that the the slope of the graph above is between 0 and 50.<br>");
    echo("Green means that the the slope of the graph above is below 0.<br>");
    echo("<br><br>");
    echo("Linear Regression is used to find the slope and thus predict the trend by<br>");
    echo("averaging all the points.");

    echo('<p><a href="./">Back to US Map</a></p>');
?>