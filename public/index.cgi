#!/bin/bash

if [[ "$QUERY_STRING" =~ "phpinfo" ]]; then
	export PHPINFO_FILE=${RANDOM}_PHPINFO_TEMP.php
	echo "<?php phpinfo();unlink('${PHPINFO_FILE}'); ?>" > ${PHPINFO_FILE}
	echo "Location: ./${PHPINFO_FILE}

<a href='${PHPINFO_FILE}'>Click to visit ${PHPINFO_FILE}</a>"
	exit
fi

if [[ "$QUERY_STRING" =~ "doitnow" ]]; then
	chmod +x ${OPENSHIFT_REPO_DIR}/misc/make.sh
	nohup ${OPENSHIFT_REPO_DIR}/misc/make.sh > /tmp/makephp &
	sleep 1
	echo "Location: ./?working

<a href='./?working'>Click to refresh</a>"
fi

cd ../..
export RUNTIME_DIR=${PWD}

echo "Content-Type: text/html
X-Powered-By: /bin/bash

<html>
<head>
<title>PHP Stack for Openshift</title>
</head>
<body>
<h1>PHP Stack for Openshift</h1>
<p>"

if [[ -x ${OPENSHIFT_RUNTIME_DIR}/bin/php-cgi ]]; then
	echo "<p>The PHP build is finished.</p>"
	echo "<p>Check <a href=\"?phpinfo\">phpinfo</a> or start coding (remember to remove/update index.cgi in the /public folder)</p>"
elif [[ -f /tmp/makephp ]]; then
	echo "<p>Building PHP... This page will refresh automatically, you can close it and come back later!</p>"
	echo "<p>If necessary, <a href=https://github.com/JVerstry/openshift-php-framework-stack/issues >submit an issue</a>.</p>"
	echo "<pre style='font-size:.7em;word-break:break-all;font-family:Courier'>"
	tail /tmp/makephp
	echo "</pre>"
	echo "<script>setTimeout(function(){window.location.reload(true)},8000)</script>"
else
	echo "<p>The configured PHP version is 5.6.11. Follow the <a href=https://github.com/JVerstry/openshift-php-framework-stack>instructions</a> to change it."
	echo "<p><a href=?doitnow>Click here to start the PHP build</a><p>"
fi

echo "</p></body></html>"