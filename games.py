import forca
import adivinhacao

print("#################")
print("Choose##your##game")
print("#################")

print("(1)Guess  (2)Forca")

choice = int(input("Which one?"));

if choice == 1:
    print("Guessing")
    adivinhacao.play()
elif choice == 2:
    print("Forca")
    forca.play()

