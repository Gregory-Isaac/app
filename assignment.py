

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/simple-interest')
def simple_interest():
    principal = 20000
    rate = 7
    time = 8

    si = (principal * rate * time) / 100
    total_amount = principal + si

    return jsonify({
        "Principal": principal,
        "Rate": f"{rate}%",
        "Time (years)": time,
        "Simple Interest": si,
        "Total Amount": total_amount
    })

if __name__ == '__main__':
    app.run(debug=True)
