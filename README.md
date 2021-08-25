# Cthulhu Streaming Proxy

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

