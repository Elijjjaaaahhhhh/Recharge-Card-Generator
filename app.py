from flask import Flask, render_template, request
import random

app = Flask(__name__)

def middle_square(seed, digits):
    """Generate a pseudo-random number using the Middle Square Algorithm."""
    n = seed
    while True:
        square = str(n ** 2).zfill(2 * digits)
        start = (len(square) - digits) // 2
        n = int(square[start:start + digits])
        yield n

def generate_recharge_cards(seed, num_cards):
    generator = middle_square(seed, 16)
    cards = set()
    while len(cards) < num_cards:
        card = next(generator)
        card_str = f"{card:016}"
        formatted_card = '-'.join([card_str[i:i+4] for i in range(0, 16, 4)])
        cards.add(formatted_card)
    return list(cards)

@app.route('/', methods=['GET', 'POST'])
def index():
    cards = None
    if request.method == 'POST':
        amount = request.form.get('amount')
        seed = random.randint(1000, 9999)
        cards = generate_recharge_cards(seed, 20)
    return render_template('index.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
