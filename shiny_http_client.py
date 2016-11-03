from __future__ import print_function

import argparse

import requests


_DEFAULT_TARGET = 'localhost:8080'


def run(target):
    unicorn_name = 'Clover Sparkle Boy'
    url = 'http://{}/v1/do-nothing/{}'.format(target, unicorn_name)

    response = requests.post(url)

    print('Client received:')
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run Shiny client.')
    parser.add_argument(
        '--target', default=_DEFAULT_TARGET,
        help='Target host/port where the server is running.')

    args = parser.parse_args()

    run(args.target)
