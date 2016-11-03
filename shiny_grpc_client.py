from __future__ import print_function

import argparse

import grpc

from shiny import shiny_pb2


_DEFAULT_TARGET = 'localhost:50051'


def run(target):
    channel = grpc.insecure_channel(target)
    stub = shiny_pb2.ShinyStub(channel)
    unicorn = shiny_pb2.Unicorn(name='Clover Sparkle Boy')
    request = shiny_pb2.DoNothingRequest(
        unicorn=unicorn,
        transmogrify='doodad',
    )
    response = stub.DoNothing(request)
    print('Client received:')
    print(type(response))
    print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run Shiny client.')
    parser.add_argument(
        '--target', default=_DEFAULT_TARGET,
        help='Target host/port where the server is running.')

    args = parser.parse_args()

    run(args.target)
