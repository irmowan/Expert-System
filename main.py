#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'
import json


def import_rules():
    rule_file = 'rules.json'
    with open(rule_file, 'r') as f:
        rules = json.load(f)
        return rules


def import_facts():
    facts = {'Freeway', 'Three lanes',
             'Middle lane', 'Safety distance 100 meters'}
    print('The facts are: ')
    print(facts)
    print()
    return facts


def match_rule(facts, rule):
    for condition in rule['IF']:
        if (condition not in facts):
            return False
    return True

if __name__ == "__main__":
    rules = import_rules()
    facts = import_facts()
    Max = 120
    Min = 0
    for rule in rules:
        if (match_rule(facts, rule)):
            print('Match rule: ' + str(rule['IF']))
            conclusions = rule['THEN']
            if 'Max' in conclusions.keys():
                print('Max ' + str(conclusions['Max']))
                Max = min(Max, conclusions['Max'])
            if 'Min' in conclusions.keys():
                print('Min ' + str(conclusions['Min']))
                Min = max(Min, conclusions['Min'])
    print('Max speed: ' + str(Max))
    print('Min speed: ' + str(Min))
