# Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). 
# The function will return the song composed by going through the musical notes beginning with the start position and following the moves given as parameter.
def compose(notes, moves, start_pos):
    song = []
    pos = start_pos
    for move in moves:
        song.append(notes[pos])
        pos = (pos + move) % len(notes)  
    return song

notes = input("Scrie notele muzicale (spatiu intre ele): ").split()
moves = list(map(int, input("Scrie mutarile (numere cu spatiu intre ele): ").split()))
start_pos = int(input("De la ce pozitie incepem? "))

melodie = compose(notes, moves, start_pos)

print("Melodia compusa:", melodie)
