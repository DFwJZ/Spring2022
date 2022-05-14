"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner

"""


class Name:
    def __init__(self, fn, ln):
        if not isinstance(fn, str):
            raise TypeError
        if not isinstance(ln, str):
            raise TypeError
        if not fn or not ln:
            raise ValueError
        self.f_name = fn
        self.l_name = ln
        self.n_name = fn

    def get_first_name(self):
        return self.f_name

    def get_last_name(self):
        return self.l_name

    def get_full_name(self):
        return self.f_name + ' ' + self.l_name

    def set_nick_name(self, nick_name):
        if not isinstance(nick_name, str):
            raise TypeError
        if not nick_name:
            raise ValueError
        self.n_name = nick_name

    def get_nick_name(self):
        return self.n_name

    def __str__(self):
        output = self.f_name + ' "' + self.n_name + '" ' + self.l_name
        return output
