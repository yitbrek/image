# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='image.proto',
  package='image',
  syntax='proto2',
  serialized_options=_b('\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001'),
  serialized_pb=_b('\n\x0bimage.proto\x12\x05image\"\x1c\n\x0cimageRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nimageReply\x12\x0f\n\x07message\x18\x01 \x01(\t2A\n\x07Greeter\x12\x36\n\nprintimage\x12\x13.image.imageRequest\x1a\x11.image.imageReply\"\x00\x42\x30\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01')
)




_IMAGEREQUEST = _descriptor.Descriptor(
  name='imageRequest',
  full_name='image.imageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='image.imageRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=50,
)


_IMAGEREPLY = _descriptor.Descriptor(
  name='imageReply',
  full_name='image.imageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='image.imageReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['imageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['imageReply'] = _IMAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

imageRequest = _reflection.GeneratedProtocolMessageType('imageRequest', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEREQUEST,
  __module__ = 'image_pb2'
  # @@protoc_insertion_point(class_scope:image.imageRequest)
  ))
_sym_db.RegisterMessage(imageRequest)

imageReply = _reflection.GeneratedProtocolMessageType('imageReply', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEREPLY,
  __module__ = 'image_pb2'
  # @@protoc_insertion_point(class_scope:image.imageReply)
  ))
_sym_db.RegisterMessage(imageReply)


DESCRIPTOR._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='image.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=83,
  serialized_end=148,
  methods=[
  _descriptor.MethodDescriptor(
    name='printimage',
    full_name='image.Greeter.printimage',
    index=0,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_IMAGEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
