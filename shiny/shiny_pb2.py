# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shiny.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='shiny.proto',
  package='google.shiny.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x0bshiny.proto\x12\x0fgoogle.shiny.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x17\n\x07Unicorn\x12\x0c\n\x04name\x18\x01 \x01(\t\"S\n\x10\x44oNothingRequest\x12)\n\x07unicorn\x18\x01 \x01(\x0b\x32\x18.google.shiny.v1.Unicorn\x12\x14\n\x0ctransmogrify\x18\x02 \x01(\t2v\n\x05Shiny\x12m\n\tDoNothing\x12!.google.shiny.v1.DoNothingRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f\"\x1d/v1/do-nothing/{unicorn.name}b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_UNICORN = _descriptor.Descriptor(
  name='Unicorn',
  full_name='google.shiny.v1.Unicorn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.shiny.v1.Unicorn.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=114,
)


_DONOTHINGREQUEST = _descriptor.Descriptor(
  name='DoNothingRequest',
  full_name='google.shiny.v1.DoNothingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unicorn', full_name='google.shiny.v1.DoNothingRequest.unicorn', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transmogrify', full_name='google.shiny.v1.DoNothingRequest.transmogrify', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=199,
)

_DONOTHINGREQUEST.fields_by_name['unicorn'].message_type = _UNICORN
DESCRIPTOR.message_types_by_name['Unicorn'] = _UNICORN
DESCRIPTOR.message_types_by_name['DoNothingRequest'] = _DONOTHINGREQUEST

Unicorn = _reflection.GeneratedProtocolMessageType('Unicorn', (_message.Message,), dict(
  DESCRIPTOR = _UNICORN,
  __module__ = 'shiny_pb2'
  # @@protoc_insertion_point(class_scope:google.shiny.v1.Unicorn)
  ))
_sym_db.RegisterMessage(Unicorn)

DoNothingRequest = _reflection.GeneratedProtocolMessageType('DoNothingRequest', (_message.Message,), dict(
  DESCRIPTOR = _DONOTHINGREQUEST,
  __module__ = 'shiny_pb2'
  # @@protoc_insertion_point(class_scope:google.shiny.v1.DoNothingRequest)
  ))
_sym_db.RegisterMessage(DoNothingRequest)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ShinyStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoNothing = channel.unary_unary(
        '/google.shiny.v1.Shiny/DoNothing',
        request_serializer=DoNothingRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ShinyServicer(object):

  def DoNothing(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ShinyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoNothing': grpc.unary_unary_rpc_method_handler(
          servicer.DoNothing,
          request_deserializer=DoNothingRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.shiny.v1.Shiny', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaShinyServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def DoNothing(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaShinyStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def DoNothing(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  DoNothing.future = None


def beta_create_Shiny_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('google.shiny.v1.Shiny', 'DoNothing'): DoNothingRequest.FromString,
  }
  response_serializers = {
    ('google.shiny.v1.Shiny', 'DoNothing'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
  }
  method_implementations = {
    ('google.shiny.v1.Shiny', 'DoNothing'): face_utilities.unary_unary_inline(servicer.DoNothing),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Shiny_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('google.shiny.v1.Shiny', 'DoNothing'): DoNothingRequest.SerializeToString,
  }
  response_deserializers = {
    ('google.shiny.v1.Shiny', 'DoNothing'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
  }
  cardinalities = {
    'DoNothing': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'google.shiny.v1.Shiny', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
