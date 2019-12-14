class Music():
    def __init__(self, author, title, album, year):
        self.author = author
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f'{self.author}\n{self.title}\n{self.album}\n{self.year}'
    
m1 = Music('Dawid Podsiadlo','Nie ma fal', 'Malomiasteczkowy','2018')
print(m1)