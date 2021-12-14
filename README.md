# Cthulhu Streaming Proxy

![Cthulhu](app/static/images/cthulhu.png)

## About

**Why?**

Simple, I work for a large film studio and frequently need to push to multiple channels and platforms.
We have tried other solutions but each seem to have their own issues, at this point making our own seems
to be the best option.  Unlike most of our work, I wanted to make this an open project as others may see
some benefit from it.  I find the simplest solutions to often be the best so, at least initially, this
is going to focus on basic functionality of RTMP and, eventually, SRT.  We can add bells and whistles later.
I plan to deploy and test on Amazon AWS, but you should have no problems running it locally or on your 
cloud provider of choice.

**Project Plan**

1. Web server initialization scripts
	* Will most likely be NGinx based
	* Will configure a host to function as a single stream proxy, RTMP supported initially
2. Management front end
	* Will likely be Python and Flask
	* Stream preview monitors
	* Ability to record streams to cloud location
	* Ability to schedule prerecorded content to stream automatically with email based notifications
	* Several usefull test funcions and performance monitors will live here
3. RTMP support
	* Ability to transmit and ingest RTMP
	* Ability to push to multiple channels and platforms
4. SRT support
	* If you haven't used SRT yet, check it out!
	* https://www.srtalliance.org/
	* Ability to transmit and ingest SRT streams

### Project Status

**Curent Status**

I'll update this section with usefull information as we go.  I'm currently doing some research and hashing
out the cloud infrastructure needs.

9/15/2021 - Completed initial testing on the Nginx source build installer.  On a Debian based system it will dowload the latest version of Nginx and RTMP module, build it from source, and do some cleanup.  It creates a conf.d directory in /usr/local/nginx/conf/ and copies a basic rtmp.conf to it, making it useable as an RTMP proxy by manually editing the push lines.  Next I will be working on the code to configure Nginx as a RTMP proxy and start it as a service.

9/17/21 - Added logging and cleaned up repeating code in nginxMainlineLatest.py with addition of sublogger.py module.  When run STDOUT logs to nginx-build.log.

10/13/21 - Nginx with RTMP module build script completed and tested.  If you are on a Debian based distro just clone the repo, navigate to the Server/ subfolder and run "./buildDeps.py && ./nginxMainlineLatest.py".  That will churn out a build of Nginx ready to proxy RTMP!  Starting work on the web front end today.

12/09/21 - I've finally found some time to start working on this project again.  I'm working on the web UI, authentication, and event control system.

12/13/21 - I've been building out the Flask user interface, it's not usable yet, but it is coming along.  As with one of my prior projects I've added a basic admin page for account creation with PYOTP 2FA support.  This is more or less designed to be a single user system at this time, but you can create additional accounts if someone on your team is going to manage your streams.  The default admin account is Admin@admin.com with password 'admin', you'll have to manually browse the database to change the default password and recover the 2FA secret to enter into the Google Authenticator app.  Seriously though, if you use this, delete the default account after creating your new admin account.  If you do not do that anyone will have access to your stream keys and that would be generally bad.

At this point the skeleton of the web UI is there, authentication works, 2FA works, it just can't control anything useful from the front end yet.  Next, I'm going to start working on an installer script to run my build scripts and then configure the Flask app to be served by uWSGI which Nginx will act as the front-end reverse proxy for.  Once that is complete I can start hashing out the actual functionality of the front-end.