import random

# Parameters
starting_bankroll = 200.00
base_bet = 0.01
win_chance = 18 / 37  # European roulette red/black odds (~48.6%)
max_rounds = 100_000  # How long to simulate
verbose = False       # Set True to print each round

def simulate_martingale():
    bankroll = starting_bankroll
    bet = base_bet
    rounds = 0
    max_loss_streak = 0
    loss_streak = 0

    while bankroll >= bet and rounds < max_rounds:
        spin = random.random()
        win = spin < win_chance

        if win:
            bankroll += bet
            bet = base_bet
            loss_streak = 0
        else:
            bankroll -= bet
            bet *= 2
            loss_streak += 1
            if bet > bankroll:
                if verbose:
                    print(f"Busted after {rounds} rounds. Needed ${bet:.2f}, had ${bankroll:.2f}")
                break
        rounds += 1
        max_loss_streak = max(max_loss_streak, loss_streak)

        if verbose:
            print(f"Round {rounds}: {'Win' if win else 'Loss'}, Bankroll: ${bankroll:.2f}, Next bet: ${bet:.2f}")

    return {
        'Rounds Played': rounds,
        'Final Bankroll': bankroll,
        'Went Broke': bankroll < bet,
        'Max Loss Streak': max_loss_streak
    }

# Run multiple simulations
num_trials = 100
results = [simulate_martingale() for _ in range(num_trials)]

# Summarize results
busts = sum(1 for r in results if r['Went Broke'])
average_rounds = sum(r['Rounds Played'] for r in results) / num_trials

print(f"Out of {num_trials} runs:")
print(f" - Busts: {busts}")
print(f" - Average Rounds Survived: {average_rounds:.0f}")
