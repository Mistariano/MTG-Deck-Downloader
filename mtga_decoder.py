# coding:utf-8
__author__ = 'Mistariano'

import os
import logging


class MTGA_Decoder:
    def __init__(self, filename):
        self.filename = filename

        logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

    def decode(self):
        filename = os.path.join(self.filename)

        cards = []
        try:
            with open(filename) as f:
                for line in f:
                    try:
                        # 4 Song of Freyalise (DAR) 179
                        line = line.strip()
                        words = line.split(' ')
                        number = int(words[0])
                        id_num = words[-1]
                        serie = words[-2].strip('()')
                        name = str.join(' ', words[1:-2])
                        cards.append((name, id_num, serie))
                    except Exception as e:
                        logging.warning(e)
        except Exception as e:
            logging.warning(e)

        return cards


if __name__ == '__main__':
    dec = MTGA_Decoder('test.txt')
    dec.decode()
