project(test_package CXX)
cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB SOURCE_FILES *.cpp)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY CXX_STANDARD 11)

if (WITH_ZLIB)
    target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE "WITH_ZLIB")
endif()
if (WITH_BZIP2)
    target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE "WITH_BZIP2")
endif()
if (WITH_LZMA)
    target_compile_definitions(${CMAKE_PROJECT_NAME} PRIVATE "WITH_LZMA")
endif()