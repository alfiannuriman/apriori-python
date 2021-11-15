from efficient_apriori import apriori

def aprioriProcess(transactions):
    itemsets, rules = apriori(transactions, min_support=0.25, min_confidence=0.7, max_length=8, verbosity=0)

    rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)

    for rule in sorted(rules_rhs, key=lambda rule:rule.lift):
        print(rule)

    return rules

transactions = [
    ('Kemeja Cole', 'Celana Carvil', 'Tas Ransel A-One'),
    ('Sandal Ardiles', 'Tas Ransel A-One', 'Kaos Kaki Mundo', 'Sepatu Adidas ABC'),
    ('Sandal Ardiles', 'Tas Ransel A-One', 'Kaos Kaki Mundo', 'Sepatu Adidas ABC')
]

aprioriProcess(transactions)