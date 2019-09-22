# raspberry pi

> You should always do a software shutdown before removing power. Failure to do so risks corrupting files, including OS ones, on the card.

## robots

First things to do:
`sudo apt-get update`
`sudo apt-get dist-upgrade`
`git pull` (in ~/greyboxes)

## Camera

`sudo raspi-config`

enable camera (interfaces —> camera —> yes)

### Reboot button

[https://www.hackster.io/glowascii/raspberry-pi-shutdown-restart-button-d5fd07](https://www.hackster.io/glowascii/raspberry-pi-shutdown-restart-button-d5fd07)

### Run Script at Startup

put the following in a `bash` script in `/etc/rc.local`

`(sleep 10;python [scriptname.py](http://scriptname.py/))&`

[https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

## Cloning SD Cards

to make a backup, run `diskutil list` (on OSX) to find your disks (run

then run

    sudo dd bs=4m if=/path/to/sd/card | gzip > /path/to/image.img.gz

or  if you don't want to zip

    sudo dd bs=4m if=/dev/rdisk2 of=/path/to/image.img

# Making a Reset Button

Used this tutorial for inspiration:

[https://github.com/scruss/shutdown_button](https://github.com/scruss/shutdown_button)

We want a shutdown button that uses standard python libraries  preinstalled on the Pi and which is simple to implement.

We'll short pin 27 to ground using a push-to-close button.

our [shutdown.py](http://shutdown.py) looks like



out `systemd` service looks like



which we will put in a folder we'll make called `usr/local/bin` and make it executable with `chmod +x` (change mode, add executable). then we'll enable and start the service.

    chmod +x shutdown_button.py
    sudo cp shutdown_button.py /usr/local/bin
    sudo cp shutdown_button.service /etc/systemd/system
    sudo systemctl enable shutdown_button.service
    sudo systemctl start shutdown_button.service

# Running a script at startup/reboot 2 ways

## 1. By editing `[rc.local](http://rc.local)`

run this command to open the `[rc.local](http://rc.local)` file using the `nano` text editor

    sudo nano /etc/rc.local

once you're in there, add a line like

    python /home/pi/path/to/your/script.py &

where the `&` signifies running the command in the background

## 2. By creating a `systemd` script

Like in the restart button example, we can make a shell script run a python script using `systemd`. Once  we have a python script tested and working, we can make it executable:

`chmod +x shutdown_button.py`

then copy it to `/usr/local/bin` where the system knows to look for the script

`sudo cp shutdown_button.py /usr/local/bin`
now make a service script using `systemd` trickery. See here for details:

[https://www.shellhacks.com/systemd-service-file-example/](https://www.shellhacks.com/systemd-service-file-example/)

copy the service script to it's proper place:

`sudo cp my_special_script.service /etc/systemd/system`

then enable and start things up:
`sudo systemctl enable my_special_script.service`
`sudo systemctl start my_special_script.service`

to check on the service, use this:

`sudo systemctl status my_special_script.service`

# Wifi / SSH

[https://www.raspberrypi.org/documentation/remote-access/ssh/](https://www.raspberrypi.org/documentation/remote-access/ssh/)

# Setup Notes

## General

Installing OS Raspbian Buster onto one SD card.

[RPi installation instructions](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)

OSX utility for flashing disk image onto an SD card.

[Balena Etcher](https://www.balena.io/etcher/)

It takes about 15mins for upload and validation of Raspbian Buster.

[If ACT light doesn't come on](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=58151)

> Protect the bottom of the Pi with plastic to reduce the chances of shorting.

[Instuctions for enlarging the filesystem](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/)

## Python Libraries

*NOTE*: we install OpenCV 3 as OpenCV4 is new and not easy to install on ARM chips yet. Must be installed and made from source.

- [delete bloatware](https://www.learnopencv.com/install-opencv-4-on-raspberry-pi/)
- `pip3 install scipy numpy matplotlib`
- `sudo apt install python3-opencv`
- `apt show python3-opencv`

Once one Pi is set up, we can copy the disk image and flash all the other cards. This is useful if one of the cards gets corrupted, as we can simply reflash the card.

Wifi must be set up on the day using the temporary networks's credentials.
