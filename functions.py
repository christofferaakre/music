def get_notes_from_file(filename: str, choose_function = lambda x: int(x[0])) -> list:
    """
    Takes a file filled with numbers and a function
    to decide how to convert that list of numbers
    to a list of scale intervals
    """
    file = open(filename, 'r')
    notes = []
    for line in file.readlines():
        note = choose_function(line.replace('\n', ''))
        notes.append(note)
    return notes

def generate_fibonacci_numbers(N: int = 100, filename: str = "data/fib.txt") -> list:
    """
    Generates N fibonacci numbers and saves them to a .txt file
    """
    previous = 1
    current = 1
    fibs = []
    for i in range(0, N):
        fib = current + previous
        previous = current
        current = fib
        fibs.append(fib)
    file = open(filename, "w")
    for fib in fibs:
        file.write(f"{fib}\n")
    file.close()
    return fibs