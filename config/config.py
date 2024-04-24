"""
This .py file is to create config file
"""
from params.params import Inputs


class Configs:
    def __int__(self):
        self.config = Inputs().get_parser()

