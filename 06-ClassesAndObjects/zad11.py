class telewizory():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f'Telewizor jest załączony, kanał {self.channel_no}')
        else:
            print('Telewizor nie jest załączony')


t1 = telewizory()
t1.show_status()
t1.on()
t1.show_status()
t1.off()