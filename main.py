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
        if not(condition in facts):
            return False
    return True

if __name__ == "__main__":
    rules = import_rules()
    facts = import_facts()
    for rule in rules:
        print('IF: ' + str(rule['IF']))
        print(match_rule(facts, rule))
