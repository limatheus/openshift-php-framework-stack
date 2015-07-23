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
<title>PHP Stack</title>
</head>
<body>
<p>You have created a PHP Stack Openshift application</p><br />
<p>"

if [[ -x ${OPENSHIFT_RUNTIME_DIR}/bin/php-cgi ]]; then
	echo "Start coding or check <a href=\"?phpinfo\">phpinfo</a>. <b>Remember to remove or update index.cgi in the /public folder</b>"
elif [[ -f /tmp/makephp ]]; then
	echo "<p>Building PHP</p>"
	echo "<p>This page will refresh automatically, you can close it and come back later...</p>"
	echo "<p>If necessary, <a href=https://github.com/JVerstry/openshift-php-framework-stack/issues >submit an issue</a>.</p>"
	echo "<pre style='font-size:.7em;word-break:break-all;font-family:Courier'>"
	tail /tmp/makephp
	echo "</pre>"
	echo "<script>setTimeout(function(){window.location.reload(true)},8000)</script>"
else
	echo "<p>Follow the instructions available at <a href=https://github.com/JVerstry/openshift-php-framework-stack>https://github.com/JVerstry/openshift-php-framework-stack</a>."
	echo "<p><a href=?doitnow>Click here to start the PHP build</a><p>"
fi

echo "</p></body></html>"