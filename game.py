from sample_madlibs import fav_mov
import random

if __name__ == "__main__":
    sentence = random.choice([fav_mov])
    sentence.play_madlib()