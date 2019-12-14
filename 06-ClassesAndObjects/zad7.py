class University():
    def __init__(self):
        self.name = 'UEK'
    def print_name(self):
        print(self.name)
    def set_name(self, new_name):
        self.name = new_name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self, fullname):
        self.fullname = fullname
        self.print_fullname()   

x = University()
x.print_name()
x.set_name('AGH')
x.print_name()
x.set_fullname('Akademia Górniczo-Hutnicza')

 