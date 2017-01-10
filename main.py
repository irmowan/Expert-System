#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'
import json


def import_rules():
    rule_file = 'rules/rules.json'
    with open(rule_file, 'r') as f:
        rules = json.load(f)
        return rules


def import_facts():
    facts = {'Freeway', 'Three lanes',
             'Middle lane', 'Safety distance 100 meters'}
    return facts


def import_cases():
    cases_file = 'cases/tests.json'
    with open(cases_file, 'r') as f:
        cases = json.load(f)
        return cases


def match_rule(facts, rule):
    for condition in rule['IF']:
        if (condition not in facts):
            return False
    return True


def test_one_case(rules, facts):
    print('The facts are: ')
    print(facts)

    Max = 120
    Min = 0
    for rule in rules:
        if (match_rule(facts, rule)):
            print('Match rule: ' + str(rule['IF']) + str(rule['THEN']))
            conclusions = rule['THEN']
            if 'Max' in conclusions.keys():
                # print('Max ' + str(conclusions['Max']))
                Max = min(Max, conclusions['Max'])
            if 'Min' in conclusions.keys():
                # print('Min ' + str(conclusions['Min']))
                Min = max(Min, conclusions['Min'])
            if Max < Min:
                Min = 0
    print('Max speed: ' + str(Max))
    print('Min speed: ' + str(Min))
    return Max, Min

if __name__ == "__main__":
    rules = import_rules()
    facts = import_facts()
    test_one_case(rules, facts)

    cases = import_cases()
    for case in cases:
        facts = case['Facts']
        conclusion = case['Conclusion']
        Max, Min = test_one_case(rules, facts)
        print(conclusion)
        print()
