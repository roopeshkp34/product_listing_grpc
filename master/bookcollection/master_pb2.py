# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: master.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmaster.proto\"4\n\x0eProductRequest\x12\"\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x10.ProductCategory\"C\n\x0cProductsList\x12\x14\n\x0cproduct_name\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x05\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"2\n\x0fProductResponse\x12\x1f\n\x08products\x18\x01 \x03(\x0b\x32\r.ProductsList*A\n\x0fProductCategory\x12\x11\n\rHOME_APPIENTS\x10\x00\x12\x0f\n\x0b\x45LECTRONICS\x10\x01\x12\n\n\x06\x42\x45\x41UTY\x10\x02\x32:\n\x08Products\x12.\n\tRecommend\x12\x0f.ProductRequest\x1a\x10.ProductResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'master_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCTCATEGORY._serialized_start=191
  _PRODUCTCATEGORY._serialized_end=256
  _PRODUCTREQUEST._serialized_start=16
  _PRODUCTREQUEST._serialized_end=68
  _PRODUCTSLIST._serialized_start=70
  _PRODUCTSLIST._serialized_end=137
  _PRODUCTRESPONSE._serialized_start=139
  _PRODUCTRESPONSE._serialized_end=189
  _PRODUCTS._serialized_start=258
  _PRODUCTS._serialized_end=316
# @@protoc_insertion_point(module_scope)
