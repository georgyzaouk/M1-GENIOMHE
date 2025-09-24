
class book(object):
    def __init__(self, title, author, ISBN, deposit):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.deposit = deposit


class magazine(object):
    def __init__(self, title, volume, date, deposit):
        self.title = title
        self.volume = volume
        self.date = date
        self.deposit = deposit
    

class location(object):
    def __init__(self, beam, shelf, level):
        self.beam = beam
        self.shelf = shelf
        self.level = level


class copy(object):
    def __init__(self, barcode, date):
        self.barcode = barcode
        self.date = date


class user(object):
    def __init(self, name, balance, ID)
        self.name = name
        self.balance = balance
        self.ID = ID