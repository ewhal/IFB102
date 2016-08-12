#Raspberry Pi internet radio

## Motivation
For IFB102 we were instructed to make a simple raspberry pi project with a hardware, software, networking and security components.
After researching various different projects I decided to construct a fully functional Sonos like internet radio box.
The idea was that mpd handles most of the work while a series of basic scripts allows the user to upload new songs and control mpd through a basic web interface.
The user is also able to control the device through a series of hardware buttons.
For more details on the hardware schematics please visit [blog](https://blog.pantsu.cat/post/internet-radio-raspi/).

## Requirements
* git
* nfs
* nginx
* uwsgi 
* uwsgi-plugin-cgi
* python
* php-fpm
* php
* mpd
* mpc
* icecast2
* python-mpd

## Installation
```
git clone https://git.pantsu.cat/ewhal/raspi
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

