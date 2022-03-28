from re import L


class Movie:
    def __init__(self, rank: int, voice: int) -> None:
        self.voice = voice
        self.rank = rank

    def add_rank(self, rank):
        self.rank += rank
    
    def add_voice(self, voice):
        self.voice += voice
    
    def print_rank(self):
        print("Rank: ", self.rank)

    def print_voice(self):
        print("Voice: ", self.voice)


m1 = Movie(4, 4)

m1.add_voice(5)
m1.add_rank(4)

m1.print_rank()
m1.print_voice()
