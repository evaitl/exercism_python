from string import ascii_uppercase as AU

def rows(letter):
    letters=[AU[i] for i in range(ord(letter)-ord('A')+1)]
    alpha=letters[:-1] + letters[::-1]
    dl=letters[::-1] + letters[1:]
    return [''.join(x if x==y else ' ' for y in dl) for x in alpha]

