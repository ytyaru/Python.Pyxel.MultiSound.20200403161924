[ja](./README.ja.md)

# Pyxel.MultiSound

Connect multiple sounds and play them.

# DEMO

<audio preload="metadata" controls>
  <source src="https://raw.githubusercontent.com/ytyaru/Python.Pyxel.MultiSound.20200403161924/master/doc/demo.mp3" type="audio/mp3">
  <source src="https://raw.githubusercontent.com/ytyaru/Python.Pyxel.MultiSound.20200403161924/master/doc/demo.ogg" type="audio/ogg">
  <source src="https://raw.githubusercontent.com/ytyaru/Python.Pyxel.MultiSound.20200403161924/master/doc/demo.flac" type="audio/flac">
  <source src="https://raw.githubusercontent.com/ytyaru/Python.Pyxel.MultiSound.20200403161924/master/doc/demo.wav" type="audio/wav">
  Current environment does not support audio playback
</audio>

# Features

* Play 2 sounds on 1 channel

# Requirement

* <time datetime="2020-04-03T16:19:15+0900">2020-04-03</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspbian](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2019-09-26 <small>[setup](http://ytyaru.hatenablog.com/entry/2019/12/25/222222)</small>
* bash 5.0.3(1)-release
* Python 3.7.3
* [pyxel][] 1.3.1

[pyxel]:https://github.com/kitao/pyxel

```sh
$ uname -a
Linux raspberrypi 4.19.97-v7l+ #1294 SMP Thu Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux
```

# Installation

Install Python 3.7 or higher.

Next, install [pyxel][] as follows.

* [pyxel/README](https://github.com/kitao/pyxel/blob/master/README.md#how-to-install)

```sh
sudo apt install python3 python3-pip libsdl2-dev libsdl2-image-dev
git clone https://github.com/kitao/pyxel.git
cd pyxel
make -C pyxel/core clean all
pip3 install .
```

# Usage

```sh
git clone https://github.com/ytyaru/Python.Pyxel.MultiSound.20200403161924
cd Python.Pyxel.MultiSound.20200403161924/src
./run.sh
```

# Author

ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

