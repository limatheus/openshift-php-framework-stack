# Openshift PHP Framework Stack

This cartridge can be used as a base to develop PHP applications relying on PHP frameworks (such as the ZendFramework or Symfony, for example).

## Quick Start

1. Create a do-it-yourself application in Openshift (see https://openshift.redhat.com/app/console/application_type/cart!diy-0.1) 
2. Fill the **Source Code** text field with: https://github.com/JVerstry/openshift-php-framework-stack
3. Click **Create Application** and wait until ready
4. If you want to modify the PHP version to be built, clone the application's git repository locally, update `DIST_PHP_VER` in `/misc/make.sh`, then git commit and push this modification
5. Visit your application's main page (e.g. https://myapp-mydomain.rhcloud.com/)
6. Click the last link to start the build, it will take about an hour
7. Clone the application's repository locally (or pull changes if you have already cloned it)
8. Starting coding your PHP application

## Using a PHP Framework

This cartridge installs Composer automatically. To demonstrate this, we will install the ZendFramework skeleton application:

1. Delete the `index.cgi` file in the `/public` directory
2. Download the ZendFramework skeleton application as a `.zip` file from https://github.com/zendframework/ZendSkeletonApplication
3. Unzip this file at the root of your git repository (i.e., the content of `/public` in the `.zip` must be poured in your local `/public` directory)
4. Commit and push all modifications
5. During the git push, Composer will download all dependencies found in `composer.json`
6. Visit your application's main page (e.g. https://myapp-mydomain.rhcloud.com/)

## About Apache Configuration

The Apache server configuration can be found and modified in `/conf/httpd.conf`.
