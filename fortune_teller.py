import random

class FortuneTeller:
    def __init__(self):
        self.coins = ['Heads', 'Tails']

    def cast_coins(self):
        results = [random.choice(self.coins) for _ in range(3)]
        return results

    def interpret_results(self, results):
        interpretations = {
            ('Heads', 'Heads', 'Heads'): 'Good fortune is on your side!',
            ('Heads', 'Heads', 'Tails'): 'Expect some challenges ahead.',
            ('Heads', 'Tails', 'Heads'): 'A new opportunity is coming your way.',
            ('Heads', 'Tails', 'Tails'): 'Stay cautious in financial matters.',
            ('Tails', 'Heads', 'Heads'): 'Your creativity will shine this week.',
            ('Tails', 'Heads', 'Tails'): 'Time to relax and unwind.',
            ('Tails', 'Tails', 'Heads'): 'Someone from your past may reappear.',
            ('Tails', 'Tails', 'Tails'): 'Take a leap of faith in the coming days.'
        }

        return interpretations.get(tuple(results), 'Unknown')

if __name__ == "__main__":
    fortune_teller = FortuneTeller()
    results = fortune_teller.cast_coins()
    interpretation = fortune_teller.interpret_results(results)

    print(f"Coin Results: {results}")
    print(f"Interpretation: {interpretation}")