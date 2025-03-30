import math
import random

def generateCorerectAnswer ():
       return [random.randint(1, 5) for _ in range(1000)]

def randomNumberGuesser ():
        return [random.randint(1, 5) for _ in range(1000)]

def sameNumberGuesser ():
      num = math.floor(random.uniform(1, 5))
      return [num] * 1000

def evaluateGuess (correctAnswer, sameGuesser, randomGuesser):
    sameCorrect = sum(1 for c, s in zip(correctAnswer, sameGuesser) if c == s)
    randomCorrect = sum(1 for c, r in zip(correctAnswer, randomGuesser) if c == r)

    print(f"Same Guesser Correct: {sameCorrect} (Correct: {sameCorrect}/1000)")
    print(f"Random Guesser Correct: {randomCorrect} (Correct: {randomCorrect}/1000)")

    if sameCorrect > randomCorrect:
        print("Same Number Guesser performed better!")
    elif randomCorrect > sameCorrect:
        print("Random Number Guesser performed better!")
    else:
        print("It's a tie!")


correctAnswer = generateCorerectAnswer()
sameGuesser = sameNumberGuesser()
randomGuesser = randomNumberGuesser()

evaluateGuess(correctAnswer, sameGuesser, randomGuesser)

