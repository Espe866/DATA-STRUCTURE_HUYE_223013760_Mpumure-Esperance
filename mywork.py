score_stack = []
player_queue = []
leaderboard = []

def add_player(player_name):
    player_queue.append(player_name)
    print(f"{player_name} has joined the game.")

def submit_score(player_name, score):
    score_stack.append((player_name, score)) 
    leaderboard.append((player_name, score)) 
    leaderboard.sort(key=lambda x: x[1], reverse=True) 
    print(f"Score submitted: {player_name} - {score}")
    print_leaderboard()

def undo_score():
    if score_stack:
        last_score = score_stack.pop()
        print(f"Undoing score: {last_score[0]} - {last_score[1]}")
        leaderboard.remove(last_score)
        print_leaderboard()
    else:
        print("No scores to undo.")

def print_leaderboard():
    print("\nCurrent Leaderboard:")
    for i, (player, score) in enumerate(leaderboard, 1):
        print(f"{i}. {player}: {score}")
    print()  

def show_queue():
    print("\nCurrent Player Queue:")
    for i, player in enumerate(player_queue, 1):
        print(f"{i}. {player}")
    print() 

add_player("Kelia")
add_player("Keza")
add_player("Mucyo")

show_queue()

submit_score("Kelia", 100)
submit_score("Keza", 200)
submit_score("Mucyo", 150)

undo_score()

submit_score("Mucyo", 180)