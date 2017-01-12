#!/usr/bin/env php
<?php

$sslVersions = [
  0, 1, 2, 3, 4, 5, 6
];

var_dump(curl_version());

foreach ($sslVersions as $sslVersion) {

    $uri = "https://api.reporting.cloud";

    printf("Trying %d", $sslVersion);
    echo PHP_EOL;

    $curl = curl_init($uri);

    curl_setopt($curl, CURLOPT_SSL_CIPHER_LIST, 'TLSv1');
    curl_setopt($curl, CURLOPT_SSLVERSION     , $sslVersion);
    curl_setopt($curl, CURLOPT_VERBOSE        , true);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER , 1);

    if (curl_exec($curl) === false) {
        var_dump(curl_error($curl));
    } else {
        curl_close($curl);
    }

    echo PHP_EOL;
    echo PHP_EOL;

}

exit(1);
