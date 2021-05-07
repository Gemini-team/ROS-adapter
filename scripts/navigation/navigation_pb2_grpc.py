# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import navigation_pb2 as navigation__pb2
#import navigation_pb2 as navigation__pb2


class NavigationStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendNavigationMessage = channel.unary_unary(
        '/navigation.Navigation/SendNavigationMessage',
        request_serializer=navigation__pb2.NavigationRequest.SerializeToString,
        response_deserializer=navigation__pb2.NavigationResponse.FromString,
        )


class NavigationServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendNavigationMessage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NavigationServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendNavigationMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SendNavigationMessage,
          request_deserializer=navigation__pb2.NavigationRequest.FromString,
          response_serializer=navigation__pb2.NavigationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'navigation.Navigation', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
