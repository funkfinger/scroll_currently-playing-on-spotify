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
 * install `git` and `pip` and setup the OS...
```
sudo apt-get install git python-pip
sudo usermod -a -G spi,gpio pi
sudo apt-get install build-essential python-dev python-pip libfreetype6-dev libjpeg-dev
```
* clone the repo:
```
git clone https://github.com/funkfinger/scroll_currently-playing-on-spotify.git
cd scroll_currently-playing-on-spotify
```
* `pip` install some stuff
```
pip install pylast
sudo -H pip install --upgrade luma.led_matrix
```
copy the config.example.py file to config.py and edit it to have the correct Last.fm info:
```
cp config.example.py config.py
nano config.py
```
Save it and if all goes well, the scrolling display should work if you run the script:
```
python scroller.py 
```
`control-c` to stop the script and add some entries to `crontab`
```
crontab -e
```
add:
```
@reboot python /home/pi/scroll_currently-playing-on-spotify/scroller.py &
0 */4 * * * /home/pi/scroll_currently-playing-on-spotify/reboot.sh
```
also want to implement this at some time - but it's doesn't seem to be working now...
```
*/30 * * * * su -s /bin/sh pi -c 'cd /home/pi/scroll_currently-playing-on-spotify && /usr/bin/git pull origin master' >> ~/scrollergitupdate.log
```


  
