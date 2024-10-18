from src.rule_engine import create_rule, combine_rules, evaluate_rule

def test_create_rule():
    rule_string = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule_string)
    assert ast is not None

def test_combine_rules():
    rules = ["age > 30 AND department = 'Sales'", "salary > 50000"]
    combined_ast = combine_rules(rules)
    assert combined_ast is not None

def test_evaluate_rule():
    data = {"age": 35, "department": "Sales", "salary": 60000}
    ast = create_rule("age > 30 AND department = 'Sales'")
    assert evaluate_rule(ast, data) == True
