# app.py
from flask import Flask, request, jsonify
import builtwith

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze_domain():
    
    try:
        domain = request.args.get('domain')
        print(domain)

        if not domain:
            return jsonify({'error': 'Please provide a domain as a query parameter.'})

        # Perform the technology analysis using builtwith
        technology_info = builtwith.builtwith(f"http://{domain}")

        return jsonify(technology_info)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)