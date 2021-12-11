cmake_minimum_required(VERSION 3.17)
project(snake)

set(CMAKE_CXX_STANDARD 14)

add_executable(snake main.cpp Game.cpp Game.h)

set(SFML_DIR "~/Downloads/SFML-2.5.1/lib/cmake/SFML/")
find_package(SFML 2.5 COMPONENTS graphics REQUIRED)

target_link_libraries(snake sfml-graphics)