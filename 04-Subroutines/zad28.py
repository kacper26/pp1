def rysujWykres(jezyki, wartosci):
    max_bar_length = 30
    bar_char = '#'
    max_value = max(wartosci)
    longest_word = len(max(jezyki, key=lambda x : len(x))) # length of the longest word

    for i, jezyk in enumerate(jezyki):
        bar_length = int((wartosci[i] / max_value) * max_bar_length)
        print(f'{jezyk: >{longest_word}}: {bar_char * bar_length}')


jezyki = ['Java', 'Python', 'JavaScript', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'C', 'Android']
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]


rysujWykres(jezyki, wartosci)