# 套牌卡图下载器 | MTG Deck Downloader

## Overview

This is a tool to decode a deck file with MTGA encoding and then download pics of the cards from iyingdi.com.
I use it to fast print tokens for my testing decks, as I'm a fresh man and have little money...
At least, it's cool & interesting. :)

## Requirements

* Python 3.4+

## Install

 ```
 python setup.py install
 ```

## Quickly Start

Just install it and use it as a script, like
```
getdeck.py -f filename -n deck_name
```
where ```-f``` and ```-n``` are required. They tell the script which deck file you want to download and the name of the deck.
Then it will run, read a file named 'filename' and download the pics, than save them into a new file under current direction named 'deck_name'.

The deck file should be encoded in MTGA encoding, for example:
```
2 Territorial Allosaurus (DAR) 184
4 Spore Swarm (DAR) 180
2 Wild Onslaught (DAR) 188
21 Forest (DAR) 266
```
