<?php
    $pdo = new PDO('pgsql:ec2-50-16-198-4.compute-1.amazonaws.com;port=5432;dbname=davdlic7h5pev6', 'okuihecsskhgrn', '63ef2d42c5f65365bb37c5c391a37a9329c29cd9f757c1e0d8a58c595164be50');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);