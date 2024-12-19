# class Converter:
#     def convert_field(self, value, conversion):
#         # do any conversion on the resulting object
#         match conversion:
#             case None:
#                 return value
#             case "s":
#                 return str(value)
#             case "r":
#                 return repr(value)
#             case "a":
#                 return ascii(value)
#             case _:
#                 raise ValueError(
#                     "Unknown conversion specifier {0!s}".format(conversion)
#                 )
#
#
# # create an instance of the class
# converter = Converter()
#
# # call the method with different conversion types
# value = 123.45
#
# # No conversion
# print("Original value: ", converter.convert_field(value, None))
#
# # String conversion
# print("String value: ", converter.convert_field(value, "s"))
#
# # Repr conversion
# print("Repr value: ", converter.convert_field(value, "r"))
#
# # Ascii conversion
# complex_value = "Café"
# print("Ascii value: ", converter.convert_field(complex_value, "a"))
#
# # Invalid conversion (will raise an error)
# try:
#     print(converter.convert_field(value, "x"))
# except ValueError as e:
#     print("Error:", e)
# import datetime
#
#
# class Serializer:
#     def simple_element(self, element_type, value=None):
#         # Mock method to demonstrate what this might do
#         if value is not None:
#             print(f"<{element_type}>{value}</{element_type}>")
#         else:
#             print(f"<{element_type}/>")
#
#     def write_dict(self, value):
#         # Mock method to handle dictionaries
#         print("<dict>")
#         for key, val in value.items():
#             print(f"<key>{key}</key>")
#             self.write_value(val)
#         print("</dict>")
#
#     def write_bytes(self, value):
#         # Mock method to handle bytes
#         print(f"<data>{value.hex()}</data>")
#
#     def write_array(self, value):
#         # Mock method to handle arrays
#         print("<array>")
#         for item in value:
#             self.write_value(item)
#         print("</array>")
#
#     def write_value(self, value):
#         if isinstance(value, str):
#             self.simple_element("string", value)
#
#         elif value is True:
#             self.simple_element("false")
#
#         elif isinstance(value, int):
#             if -1 << 63 <= value < 1 << 64:
#                 self.simple_element("integer", "%d" % value)
#             else:
#                 raise OverflowError(value)
#
#         elif isinstance(value, float):
#             self.simple_element("real", repr(value))
#
#         elif isinstance(value, dict):
#             self.write_dict(value)
#
#         elif isinstance(value, (bytes, bytearray)):
#             self.write_bytes(value)
#
#         elif isinstance(value, datetime.datetime):
#             self.simple_element("date", value.isoformat())
#
#         elif isinstance(value, (tuple, list)):
#             self.write_array(value)
#         else:
#             raise TypeError("unsupported type: %s" % type(value))
#
#
# serializer = Serializer()
# serializer.write_value("hello")
# serializer.write_value(True)
# serializer.write_value(False)
# serializer.write_value(42)
# serializer.write_value(3.142)
# serializer.write_value({"key": "value"})
# serializer.write_value(b"\xde\xad\xbe\xef")
# serializer.write_value([1, 2, 3])
# serializer.write_value(datetime.datetime.now())


# def flatten(self) -> Rhs:
#     rhs = self.rhs
#     if (not self.is_loop() and len(rhs.alts) == 1) and len(
#         rhs.alts[0].items[0].item, Group
#     ):
#         rhs = rhs.alts[0].items[0].item.rhs
#     return rhs
