from concurrent import futures
import time

from google.protobuf import empty_pb2
import grpc

import shiny_pb2


_ONE_DAY_IN_SECONDS = 24 * 60 * 60


class Shiny(shiny_pb2.ShinyServicer):

    def DoNothing(self, request, context):
        context.set_code(grpc.StatusCode.OK)
        context.set_details('All systems go')
        return empty_pb2.Empty()


def serve(bind='[::]:50051'):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shiny_pb2.add_ShinyServicer_to_server(Shiny(), server)
    server.add_insecure_port(bind)
    server.start()
    print('gRPC server listening on {}.'.format(bind))
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
