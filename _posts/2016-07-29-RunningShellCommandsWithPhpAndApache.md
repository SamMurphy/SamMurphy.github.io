---
title: "Running Shell Commands with Php and Apache"
categories:
  - Technology
  - Tutorial
  - Linux
tags:
  - technology
  - linux
  - tutorial
  - apache
  - php
  - shellscript
  - server
  - admin
  - webhosting
  - html
  - css
---

My internet connection for my home server is slightly less than stable, as such the team speak server that I host on there often needs restarting. Rather than doing the sensible thing and just starting the teamspeak server when the system turns on, I decided to get creative and make a server admin web interface using; apache, php, a sprinkling of html, and a pile of shell scripts. The first step is to get apache and php up and running, then we'll sort out the php and the scripts.

## Installing Apache and Php
Thanks to Ubuntu's package manager, installing both of these packages is very straight forward. All you need to do is run the following commands:

```bash
sudo apt-get install apache2
sudo apt-get install php5
sudo apt-get install libapache2-mod-php5
sudo /etc/init.d/apache2 restart
```
Once the installation is completed, you have a fully functional web server up and running. Now any files in `/var/www/` will be hosted on the server. If you want your website to be available over the internet then you'll have to forward port `80` or if you want to use a custom port, you'll have to change `Listen 80` to your port of choice in `/etc/apache2/ports.conf` and then restart your apache server.

## Creating the web page
Now that we've got apache and php up and running it's almost time to move on to the fun bit, writing the php script and the html form to trigger it, but first we've got to make sure all the bash scripts that we want to run are set up properly and that we know where they are. To keep it simple I've stored all the scripts I want to run in `/serverscripts/' on the root of the system, this way I won't have to faf around trying to find them if something goes wrong.

Now it's finally time to write some php to run our scripts, I'll show you the code first and then explain what it does directly underneath.

```php
<?php
if ($_GET['run']) {
  # This code will run if ?run=true is set.
  exec("sh /PATH/TO/YOUR/SCRIPT.sh");
}
?>
```

Now that code's, pretty simple but in case this is your first time with php let me explain what it does. The first line identifies that this piece of code is a php script, this is so you can put it in amongst all the html you're using on your website. The second line is slightly more interesting, this is an if statement that will trigger if the `run` variable is set to true in the URL parameters. What does that actually mean I hear you ask? Well it means that if you visit the url `MY.IP.ADDRESS/myphppage.php?run=true` then the php script will be triggered and run the code. It's important to note that `run` can be anything you want it to be, so you should change it to something more specific to the script that you want to run like `startteamspeak`. Finally we come to the line that actually runs the script. The `exec` function will just run whatever bash command you put inside of the quotations, in this case `sh` is the command to run a bash script and then we give it the _absolute_ path to the script that we want to run. The last couple of lines are just closing the brackets and php tags that were opened up at the start of the script.

Now you can save that code in as .php file in `/var/www/` and if you navigate to `YOUR.IP.ADDRESS/YOURPHPFILE.php?run=true` then your script will run, but you won't be able to see anything on the page yet, in order to do that we need a little bit of Html.

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Launch Scripts</title>
</head>
<body>
<h2>Run my script</h2>
<form id="runScripts" method="post" action="?run=true">
<p>To run the script click this button:
<input type="submit" value="Click Me" id="submit" />
</p>
</form>
<p>To run the script click this <a href="?run=true">link</a></p>
</body>
</html>
```

Most of that html is just setup stuff, the import bits are the two lines in paragraph tags (`<p>`), these two lines offer two options to insert `?run=true` into the URL to trigger the script. The first option is a pretty button and the second is just a plain old link, but I'll leave the choice of which to use to you. Remember you'll need to put this code into the php file we made earlier to get it to run properly, and don't forget to change any instance `run` to whatever you named your php script. To make it so that you can run, more than one script you just need to repeat this process changing the php script name and the path to the different .sh files you want to run.

Hopefully you've got all that working now, but if you don't feel free to comment below and I'll do my best to help you along.

### Tips and Tricks
If you change `exec` to `echo exec` then it'll return the output of the script and show it on your webpage, but you might need to do some fiddling to get it to display nicely.
