# Cthulhu Streaming Proxy

![Cthulhu](cthulhu.png)

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