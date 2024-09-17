import random

# Daftar nama buah dalam bahasa Inggris
fruits = ["apple", "banana", "grape", "orange", "watermelon", "strawberry", "pineapple", "mango", "cherry", "papaya"]

# Fungsi untuk menjalankan game tebak-tebakan untuk dua pemain
def two_player_guessing_game():
    print("Welcome to the Two-Player Fruit Guessing Game!")
    print("Each player will take turns guessing the fruit. Correct guesses score a point!")
    
    # Meminta nama kedua pemain
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")
    
    # Inisialisasi skor untuk kedua pemain
    score_player1 = 0
    score_player2 = 0
    rounds = 5  # Jumlah ronde permainan

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")
        
        # Pilih buah secara acak
        selected_fruit = random.choice(fruits)
        
        # Menampilkan petunjuk
        print(f"The fruit has {len(selected_fruit)} letters.")

        # Giliran pemain 1
        print(f"{player1}'s turn to guess!")
        guess = input(f"{player1}, enter your guess: ").lower()
        if guess == selected_fruit:
            print("Correct!")
            score_player1 += 1
        else:
            print(f"Wrong! The correct fruit was: {selected_fruit}")
        
        # Pilih buah secara acak lagi untuk pemain 2
        selected_fruit = random.choice(fruits)
        
        # Menampilkan petunjuk
        print(f"The fruit has {len(selected_fruit)} letters.")

        # Giliran pemain 2
        print(f"{player2}'s turn to guess!")
        guess = input(f"{player2}, enter your guess: ").lower()
        if guess == selected_fruit:
            print("Correct!")
            score_player2 += 1
        else:
            print(f"Wrong! The correct fruit was: {selected_fruit}")

    # Menampilkan skor akhir
    print("\nGame Over!")
    print(f"Final Scores:\n{player1}: {score_player1}\n{player2}: {score_player2}")

    # Tentukan pemenang
    if score_player1 > score_player2:
        print(f"Congratulations {player1}, you win!")
    elif score_player2 > score_player1:
        print(f"Congratulations {player2}, you win!")
    else:
        print("It's a tie!")

    # Tanya apakah ingin bermain lagi
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        two_player_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")

# Menjalankan game
two_player_guessing_game()
