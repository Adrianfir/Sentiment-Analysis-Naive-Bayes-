"""
this .py file would pass the params to config.config.py
"""

import numpy as np
import tensorflow as tf
import argparse
import pathlib


class Inputs:
    def __int__(self):
        lr = 0.001  # learning rate for the optimizer
        moment = 0.009  # momentum for the optimizer (if needed)
        optimizer = tf.keras.optmizers.Adam()
        parser = argparse.ArgumentParser()
        parser.add_argument('--lr', type=float, default=lr,
                            help='this parameter is the learning rate used in the optimizer')
        parser.add_argument('--moment', type=float, default=moment,
                            help='this parameter is the momentum for the optimizer if needed')
        self.parser = parser

    def get_parser(self):
        return self.parser.parse_args()


