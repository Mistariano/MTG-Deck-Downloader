# coding:utf-8
__author__ = 'Mistariano'

import requests
import os
import logging


class Downloader:
    def __init__(self, deck_name, cards):
        """

        :param cards: [(card name, card id, card serie...]
        """

        self.deck_name = deck_name

        alter_serie_names = {
            'DAR': 'DOM',
        }
        cards = [
            (name, id_num, serie) if serie not in alter_serie_names.keys() else (name, id_num, alter_serie_names[serie])
            for name, id_num, serie in cards]

        self.cards = [
            (name, id_num, serie, 'http://static.iyingdi.cn/card/magic/series/{}/card/{}.png'.format(serie, id_num))
            for name, id_num, serie in cards]

    def start(self):
        deck_name = self.deck_name
        if not os.path.exists(deck_name):
            os.makedirs(os.path.join(deck_name))

        for card in self.cards:
            name, _, _, url = card
            r = requests.get(url)
            if r.status_code == 200:
                path = os.path.join(deck_name, '{}.png'.format(name))
                open(path, 'wb').write(r.content)
                logging.info('[200] {}'.format(name))
            else:
                url_spl = url.split('.')
                url_spl[-1] = 'jpg'
                url = str.join('.', url_spl)

                r = requests.get(url)
                if r.status_code == 200:
                    path = os.path.join(deck_name, '{}.jpg'.format(name))
                    open(path, 'wb').write(r.content)
                    logging.info('[200] {} (jpg)'.format(name))
                else:
                    logging.warning('[{}] Download {} failed.'.format(r.status_code, name))


if __name__ == '__main__':
    downloader = Downloader('test', [('test', 160, 'DAR')])
    downloader.start()
