# Openshift PHP Framework Stack

This cartridge can be used as a base to develop PHP applications relying on PHP frameworks requiring Composer to download dependencies (such as the ZendFramework or Symfony, for example).
The PHP version can be configured.

## Quick Start

1. Create a do-it-yourself application in Openshift (see https://openshift.redhat.com/app/console/application_type/cart!diy-0.1) 
2. Fill the **Source Code** text field with: https://github.com/JVerstry/openshift-php-framework-stack
3. Click **Create Application** and wait until ready
4. Visit your application's main page (e.g. https://myapp-mydomain.rhcloud.com/)
5. If you want to modify the PHP version to be built, clone the application's git repository locally, update `DIST_PHP_VER` in `/misc/make.sh`, then git commit and push this modification
6. Click the last link to start the build, it will take about an hour
7. To activate Composer, clone the application's repository locally (or pull changes if you have already cloned it) and rename the `_build` file to `build` in the `/.openshift/action_hooks/` directory 
9. Commit this file
10. Make it executable with `git update-index --chmod=+x .openshift/action_hooks/build`
11. Commit this file again and push it too when the build is finished
9. Starting coding your PHP application

## Using a PHP Framework

To demonstrate the usage of Composer, we will install the ZendFramework skeleton application:

1. Delete the `index.cgi` file in the `/public` directory
2. Rename the `_build` file to `build` in the `/.openshift/action_hooks/` directory if you have not done so already
3. Commit this file
4. Make it executable with `git update-index --chmod=+x .openshift/action_hooks/build`
5. Commit this file again and push it too
6. Download the ZendFramework skeleton application as a `.zip` file from https://github.com/zendframework/ZendSkeletonApplication
7. Unzip this file at the root of your git repository (i.e., the content of `/public` in the `.zip` must be poured in your local `/public` directory)
8. Commit and push all modifications
9. During the git push, Composer will download all dependencies found in `composer.json`
10. Visit your application's main page (e.g. https://myapp-mydomain.rhcloud.com/)

A similar procedure can be used for other PHP frameworks. 

## About Apache Configuration

The Apache server configuration can be found and modified in `/conf/httpd.conf`.
