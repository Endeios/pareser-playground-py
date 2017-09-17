'''main app for the calculator'''
import logging
import argparse
from calculator import Calculator

logging.basicConfig(
    format='[%(name)s](%(levelname)s) : %(message)s',
    level=logging.INFO)


def main():
    log = logging.getLogger("CalcApp")
    parser = argparse.ArgumentParser(
        description="A simple calcupatro that supports only '+' and '*'")
    parser.add_argument(
        "calculation",
        help="The calculation, only + and *, ex: 3*1+2")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Put app in debug mode")
    args = parser.parse_args()
    if(args.verbose):
        logging.getLogger().setLevel(logging.DEBUG)
    log.debug(args)
    calculator = Calculator()
    result = calculator.calculate(args.calculation)
    print(result)


if __name__ == "__main__":
    main()
