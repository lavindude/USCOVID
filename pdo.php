<?php

$host = "ec2-50-16-198-4.compute-1.amazonaws.com";
$user = "okuihecsskhgrn";
$password = "63ef2d42c5f65365bb37c5c391a37a9329c29cd9f757c1e0d8a58c595164be50";
$dbname = "davdlic7h5pev6";
$port = "5432";

try {
    $dsn = "pgsql:host=" . $host . ";port=" . $port . ";dbname=" . $dbname . ";user=" . $user . ";password=" . $password . ";";

    $pdo = new PDO($dsn, $user, $password);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
    $pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES,false);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
}

catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}