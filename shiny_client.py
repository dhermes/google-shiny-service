from __future__ import print_function

import grpc

import shiny_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
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
    run()
