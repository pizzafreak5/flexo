from cffi import FFI
ffi = FFI()
lib = ffi.verify('#include <pcduino/Ardunio.h>') 

