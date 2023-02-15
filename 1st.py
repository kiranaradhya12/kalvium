import random
import os

# function to read the highest score for a given player from a file
def read_score(player):
    if os.path.exists(player + '.txt'):
        with open(player + '.txt', 'r') as f:
            return int(f.read().strip())
    else:
        return 0

# function to update the highest score for a given player in a file
def update_score(player, score):
    with open(player + '.txt', 'w') as f:
        f.write(str(score))

# function to determine the winner of a round of Rock Paper Scissors
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return 'player'
    else:
        return 'computer'

# main function to play the game
def play_game():
    print('Welcome to Rock Paper Scissors!')
    player_name = input('Enter your name: ')
    highest_score = read_score(player_name)
    print(f'Your highest score is {highest_score}')

    while True:
        print('Choose your move: (rock, paper, scissors)')
        player_choice = input().lower()
        while player_choice not in ['rock', 'paper', 'scissors']:
            print('Invalid choice. Please enter rock, paper, or scissors.')
            player_choice = input().lower()

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f'Computer chooses {computer_choice}.')

        winner = get_winner(player_choice, computer_choice)
        if winner == 'player':
            print('You win!')
            highest_score += 1
            update_score(player_name, highest_score)
        elif winner == 'computer':
            print('Computer wins!')
        else:
            print('It\'s a draw!')

        print(f'Your current score is {highest_score}.')
        play_again = input('Do you want to play again? (y/n)').lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    play_game()
