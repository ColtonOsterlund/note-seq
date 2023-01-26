# pylint: skip-file
# Copyright 2021 The Magenta Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: skip-file
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: note_seq/protobuf/generator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='note_seq/protobuf/generator.proto',
  package='magenta',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!note_seq/protobuf/generator.proto\x12\x07magenta\"3\n\x10GeneratorDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\xdd\x03\n\x10GeneratorOptions\x12\x41\n\x0einput_sections\x18\x01 \x03(\x0b\x32).magenta.GeneratorOptions.SequenceSection\x12\x44\n\x11generate_sections\x18\x02 \x03(\x0b\x32).magenta.GeneratorOptions.SequenceSection\x12\x31\n\x04\x61rgs\x18\x03 \x03(\x0b\x32#.magenta.GeneratorOptions.ArgsEntry\x1a\x37\n\x0fSequenceSection\x12\x12\n\nstart_time\x18\x01 \x01(\x01\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x01\x1a\x82\x01\n\x08\x41rgValue\x12\x14\n\nbyte_value\x18\x01 \x01(\x0cH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x15\n\x0b\x66loat_value\x18\x03 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\x05 \x01(\tH\x00\x42\x06\n\x04kind\x1aO\n\tArgsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".magenta.GeneratorOptions.ArgValue:\x02\x38\x01\"\xde\x01\n\x0fGeneratorBundle\x12\x34\n\x11generator_details\x18\x01 \x01(\x0b\x32\x19.magenta.GeneratorDetails\x12>\n\x0e\x62undle_details\x18\x04 \x01(\x0b\x32&.magenta.GeneratorBundle.BundleDetails\x12\x17\n\x0f\x63heckpoint_file\x18\x02 \x03(\x0c\x12\x16\n\x0emetagraph_file\x18\x03 \x01(\x0c\x1a$\n\rBundleDetails\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\tb\x06proto3')
)




_GENERATORDETAILS = _descriptor.Descriptor(
  name='GeneratorDetails',
  full_name='magenta.GeneratorDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='magenta.GeneratorDetails.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='magenta.GeneratorDetails.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=97,
)


_GENERATOROPTIONS_SEQUENCESECTION = _descriptor.Descriptor(
  name='SequenceSection',
  full_name='magenta.GeneratorOptions.SequenceSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='magenta.GeneratorOptions.SequenceSection.start_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='magenta.GeneratorOptions.SequenceSection.end_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=363,
)

_GENERATOROPTIONS_ARGVALUE = _descriptor.Descriptor(
  name='ArgValue',
  full_name='magenta.GeneratorOptions.ArgValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='byte_value', full_name='magenta.GeneratorOptions.ArgValue.byte_value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='magenta.GeneratorOptions.ArgValue.int_value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='magenta.GeneratorOptions.ArgValue.float_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='magenta.GeneratorOptions.ArgValue.bool_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='magenta.GeneratorOptions.ArgValue.string_value', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='magenta.GeneratorOptions.ArgValue.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=366,
  serialized_end=496,
)

_GENERATOROPTIONS_ARGSENTRY = _descriptor.Descriptor(
  name='ArgsEntry',
  full_name='magenta.GeneratorOptions.ArgsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='magenta.GeneratorOptions.ArgsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='magenta.GeneratorOptions.ArgsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=577,
)

_GENERATOROPTIONS = _descriptor.Descriptor(
  name='GeneratorOptions',
  full_name='magenta.GeneratorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_sections', full_name='magenta.GeneratorOptions.input_sections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='generate_sections', full_name='magenta.GeneratorOptions.generate_sections', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='magenta.GeneratorOptions.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GENERATOROPTIONS_SEQUENCESECTION, _GENERATOROPTIONS_ARGVALUE, _GENERATOROPTIONS_ARGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=577,
)


_GENERATORBUNDLE_BUNDLEDETAILS = _descriptor.Descriptor(
  name='BundleDetails',
  full_name='magenta.GeneratorBundle.BundleDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='magenta.GeneratorBundle.BundleDetails.description', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=766,
  serialized_end=802,
)

_GENERATORBUNDLE = _descriptor.Descriptor(
  name='GeneratorBundle',
  full_name='magenta.GeneratorBundle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='generator_details', full_name='magenta.GeneratorBundle.generator_details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle_details', full_name='magenta.GeneratorBundle.bundle_details', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_file', full_name='magenta.GeneratorBundle.checkpoint_file', index=2,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metagraph_file', full_name='magenta.GeneratorBundle.metagraph_file', index=3,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GENERATORBUNDLE_BUNDLEDETAILS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=580,
  serialized_end=802,
)

_GENERATOROPTIONS_SEQUENCESECTION.containing_type = _GENERATOROPTIONS
_GENERATOROPTIONS_ARGVALUE.containing_type = _GENERATOROPTIONS
_GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind'].fields.append(
  _GENERATOROPTIONS_ARGVALUE.fields_by_name['byte_value'])
_GENERATOROPTIONS_ARGVALUE.fields_by_name['byte_value'].containing_oneof = _GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind']
_GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind'].fields.append(
  _GENERATOROPTIONS_ARGVALUE.fields_by_name['int_value'])
_GENERATOROPTIONS_ARGVALUE.fields_by_name['int_value'].containing_oneof = _GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind']
_GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind'].fields.append(
  _GENERATOROPTIONS_ARGVALUE.fields_by_name['float_value'])
_GENERATOROPTIONS_ARGVALUE.fields_by_name['float_value'].containing_oneof = _GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind']
_GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind'].fields.append(
  _GENERATOROPTIONS_ARGVALUE.fields_by_name['bool_value'])
_GENERATOROPTIONS_ARGVALUE.fields_by_name['bool_value'].containing_oneof = _GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind']
_GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind'].fields.append(
  _GENERATOROPTIONS_ARGVALUE.fields_by_name['string_value'])
_GENERATOROPTIONS_ARGVALUE.fields_by_name['string_value'].containing_oneof = _GENERATOROPTIONS_ARGVALUE.oneofs_by_name['kind']
_GENERATOROPTIONS_ARGSENTRY.fields_by_name['value'].message_type = _GENERATOROPTIONS_ARGVALUE
_GENERATOROPTIONS_ARGSENTRY.containing_type = _GENERATOROPTIONS
_GENERATOROPTIONS.fields_by_name['input_sections'].message_type = _GENERATOROPTIONS_SEQUENCESECTION
_GENERATOROPTIONS.fields_by_name['generate_sections'].message_type = _GENERATOROPTIONS_SEQUENCESECTION
_GENERATOROPTIONS.fields_by_name['args'].message_type = _GENERATOROPTIONS_ARGSENTRY
_GENERATORBUNDLE_BUNDLEDETAILS.containing_type = _GENERATORBUNDLE
_GENERATORBUNDLE.fields_by_name['generator_details'].message_type = _GENERATORDETAILS
_GENERATORBUNDLE.fields_by_name['bundle_details'].message_type = _GENERATORBUNDLE_BUNDLEDETAILS
DESCRIPTOR.message_types_by_name['GeneratorDetails'] = _GENERATORDETAILS
DESCRIPTOR.message_types_by_name['GeneratorOptions'] = _GENERATOROPTIONS
DESCRIPTOR.message_types_by_name['GeneratorBundle'] = _GENERATORBUNDLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GeneratorDetails = _reflection.GeneratedProtocolMessageType('GeneratorDetails', (_message.Message,), dict(
  DESCRIPTOR = _GENERATORDETAILS,
  __module__ = 'note_seq.protobuf.generator_pb2'
  # @@protoc_insertion_point(class_scope:magenta.GeneratorDetails)
  ))
_sym_db.RegisterMessage(GeneratorDetails)

GeneratorOptions = _reflection.GeneratedProtocolMessageType('GeneratorOptions', (_message.Message,), dict(

  SequenceSection = _reflection.GeneratedProtocolMessageType('SequenceSection', (_message.Message,), dict(
    DESCRIPTOR = _GENERATOROPTIONS_SEQUENCESECTION,
    __module__ = 'note_seq.protobuf.generator_pb2'
    # @@protoc_insertion_point(class_scope:magenta.GeneratorOptions.SequenceSection)
    ))
  ,

  ArgValue = _reflection.GeneratedProtocolMessageType('ArgValue', (_message.Message,), dict(
    DESCRIPTOR = _GENERATOROPTIONS_ARGVALUE,
    __module__ = 'note_seq.protobuf.generator_pb2'
    # @@protoc_insertion_point(class_scope:magenta.GeneratorOptions.ArgValue)
    ))
  ,

  ArgsEntry = _reflection.GeneratedProtocolMessageType('ArgsEntry', (_message.Message,), dict(
    DESCRIPTOR = _GENERATOROPTIONS_ARGSENTRY,
    __module__ = 'note_seq.protobuf.generator_pb2'
    # @@protoc_insertion_point(class_scope:magenta.GeneratorOptions.ArgsEntry)
    ))
  ,
  DESCRIPTOR = _GENERATOROPTIONS,
  __module__ = 'note_seq.protobuf.generator_pb2'
  # @@protoc_insertion_point(class_scope:magenta.GeneratorOptions)
  ))
_sym_db.RegisterMessage(GeneratorOptions)
_sym_db.RegisterMessage(GeneratorOptions.SequenceSection)
_sym_db.RegisterMessage(GeneratorOptions.ArgValue)
_sym_db.RegisterMessage(GeneratorOptions.ArgsEntry)

GeneratorBundle = _reflection.GeneratedProtocolMessageType('GeneratorBundle', (_message.Message,), dict(

  BundleDetails = _reflection.GeneratedProtocolMessageType('BundleDetails', (_message.Message,), dict(
    DESCRIPTOR = _GENERATORBUNDLE_BUNDLEDETAILS,
    __module__ = 'note_seq.protobuf.generator_pb2'
    # @@protoc_insertion_point(class_scope:magenta.GeneratorBundle.BundleDetails)
    ))
  ,
  DESCRIPTOR = _GENERATORBUNDLE,
  __module__ = 'note_seq.protobuf.generator_pb2'
  # @@protoc_insertion_point(class_scope:magenta.GeneratorBundle)
  ))
_sym_db.RegisterMessage(GeneratorBundle)
_sym_db.RegisterMessage(GeneratorBundle.BundleDetails)


_GENERATOROPTIONS_ARGSENTRY._options = None
# @@protoc_insertion_point(module_scope)