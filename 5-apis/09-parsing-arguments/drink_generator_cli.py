import argparse
import sys


DRINKS = {
    "caipirinha": {"cachaca", "sugar", "lime"},
    "mojito": {"white rum", "sugar cane juice", "lime juice", "soda water", "mint"},
    "gin tonic": {"gin", "tonic water", "ice"},
    "vodka martini": {"vodka", "vermouth", "ice", "olives"},
}


def print_debug(*args):
    print(args, file=sys.stderr)


def find_drink(ingredients):
    for drink, drink_ingredients in DRINKS.items():
        if set(ingredients) == drink_ingredients:
            return drink
    return None


def run_list():
    print("These drinks are available:")
    for drink in sorted(DRINKS):
        print(f"* {drink}")


def run_find_by_name(name):
    drink = DRINKS.get(name, None)
    if drink:
        print(', '.join(sorted(drink)))
    else:
        print(f"{name} does not exist.")


def run_find_by_ingredients(ingredients):
    drink = find_drink(ingredients)
    if drink:
        print(drink)
    else:
        print("No drink found.")


def run(args):
    # todo:
    # - Check which of the flags have been given
    # - Do additional manual checking, where needed
    # - Call correct run_... function
    if args.list:
        run_list()
    if args.ingredients:
        run_find_by_ingredients(args.ingredients)
    if args.drink:
        run_find_by_name(args.drink)
    return


def get_parser():
    parser = argparse.ArgumentParser()
    # todo: Configure parser correctly
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--list', action='store_true')
    group.add_argument('-i', '--ingredients', nargs='+')
    group.add_argument('-d', '--drink')
    return parser


def main(args=None):
    parsed = get_parser().parse_args(args)
    run(parsed)


# todo: call main() with no arguments, but only when run as a script
