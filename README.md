# currently-playing-on-spotify
What's currently playing on Spotify using the Last.fm API

steps to get this running:

with a [Raspbian-lite image](https://www.raspberrypi.org/downloads/raspbian/):

* add network info in `wpa_supplicant.conf` file at root of image. Mine looks something like this:

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US

    network={
        ssid="NETWORK NAME"
        psk="NETWORK PASSWORD"
        key_mgmt=WPA-PSK
    }
* add a `ssh` file to the root of the image. Mine was empty.
* find the IP of the Pi with your router and `ssh` in:
    
    ssh

* update the image:

    sudo apt-get update

 * install `git`

    sudo apt-get install git

  
