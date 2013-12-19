ethosgame
=========

A game for the OLPC XO laptops, written using PyGame

Current Status
==============
The game is still in a *very* early stage of development, and I'm still ironing out it's most basic elements.

It currently is not ready to be run as a Sugar activity, but if you have python 2.7 installed, you can easily test it out by running the main game class (game.py).

Just make sure to install pygame, first! I would recommend using [pip](http://www.pip-installer.org/en/latest/) which can be installed from the linked website, or your favourite package manager.

The dependencies for pygame are (unless I am mistaken) as follows:

[libjpeg-turbo](http://libjpeg-turbo.virtualgl.org/)
[portmidi](http://portmedia.sourceforge.net/)
python
[sdl_image](http://www.libsdl.org/projects/SDL_image/)
[sdl_mixer](http://www.libsdl.org/projects/SDL_mixer/)
[sdl_ttf](http://www.libsdl.org/projects/SDL_ttf/)


Ubuntu users can just run the following command to get their dependencies in order:
```
sudo apt-get build-dep python-pygame
```

Again, you may obtain binaries from the linked webpages, but I would recommend using a package manager such as apt or yum.

Once you have all the dependencies installed, just run

```
pip install pygame
```
as root and you will be ready to run the game:

```
python game.py
```
