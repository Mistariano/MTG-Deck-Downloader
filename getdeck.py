# coding:utf-8
__author__ = 'Mistariano'

import argparse
import logging
from mtga_decoder import MTGA_Decoder
from downloader import Downloader

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', help='The name of the deck.', required=True)
    parser.add_argument('--filename', '-f', help='The filename of MTGA encode file.', required=True)
    args = parser.parse_args()
    name = args.name
    filename = args.filename
    decoder = MTGA_Decoder(filename)
    cards = decoder.decode()
    downloader = Downloader(deck_name=name, cards=cards)
    downloader.start()
