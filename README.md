# scroll_currently-playing-on-spotify
What's currently playing on Spotify using the Last.fm API. 

The **MAX7219** LED matirix needs to be setup according to [these instructions](http://luma-led-matrix.readthedocs.io/en/latest/install.html)

steps to get this running on a [Raspbian-lite image](https://www.raspberrypi.org/downloads/raspbian/):

* add network info in `wpa_supplicant.conf` file at root of image. Mine looks something like this:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
  ssid="NETWORK NAME"
  psk="NETWORK PASSWORD"
  key_mgmt=WPA-PSK
}
```
* add a `ssh` file to the root of the image. Mine was empty.
* find the IP of the Pi with your router and `ssh` in - default `pi` user password is `raspberry`, you should change this using `passwd` command:
``` 
ssh pi@<IP ADDRESS>
```
* setup the Pi with the right settings: 
```
sudo raspi-config
```
* I changed (and then rebooted)

  * set local to en_US.UTF-8 UTF-8 (de-selecting the en_UK option) in `Localisation Options`
  * enable `SPI` in `Interfacinf Options`
  * `Expand Filesystem` in `Advanced Options` <-- probably not necessary... 

* update the image:
```
sudo apt-get update
```
 * install `git` and `pip`
```
sudo apt-get install git python-pip
```
* clone the repo:
```
git clone https://github.com/funkfinger/scroll_currently-playing-on-spotify.git
cd scroll_currently-playing-on-spotify
```
* `pip` install some stuff
```
pip install pylast
pip install 
```


  
