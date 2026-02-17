from flask import jsonify
from App import App


@App.route('/simple-interest')
def simple_interest():
    principal = 20000
    rate = 7
    time = 8
    simple_interest = (principal * rate * time) / 100
    si = (principal * rate * time) / 100
    total_amount = principal + si

    return jsonify({"Principal": principal,"Rate": f"{rate}%","Time (years)": time,"Simple Interest": si,"Total Amount": total_amount})


App.run(debug=True)  