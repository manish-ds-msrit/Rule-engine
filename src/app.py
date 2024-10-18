from flask import Flask, request, jsonify
from src.rule_engine import create_rule, combine_rules, evaluate_rule
from src.database import get_connection, create_table

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json['rule_string']
    ast = create_rule(rule_string)
    return jsonify(ast.__dict__)

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json['rules']
    combined_ast = combine_rules(rules)
    return jsonify(combined_ast.__dict__)

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    ast = request.json['ast']
    data = request.json['data']
    result = evaluate_rule(ast, data)
    return jsonify({'result': result})

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
