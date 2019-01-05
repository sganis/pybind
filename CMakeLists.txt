################################################################################
# example pybind11 cmake file
################################################################################
cmake_minimum_required(VERSION 3.0)
project (pybind)

set(CMAKE_VERBOSE_MAKEFILE on)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(APP ${CMAKE_CURRENT_SOURCE_DIR}/app)
set(SRC ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(TEST ${CMAKE_CURRENT_SOURCE_DIR}/test)

SET(CMAKE_BUILD_RPATH "\$ORIGIN")

include_directories(${SRC})

if (MSVC)
    SET(PYTHON C:\\Python37\\python.exe)
    include_directories(C:\\Python37\\include)
    link_directories(C:\\Python37\\libs)
else()
    include_directories(
        /usr/include/python3.6
        /usr/local/include/python3.6
    )
endif()

################################################################################
# example lib
add_library(
    example SHARED
    ${SRC}/example.cpp
    ${SRC}/example.h
    ${SRC}/python.cpp
    ${SRC}/export.h
    ${SRC}/version.h
)
if (WIN32)
    target_compile_definitions(example PRIVATE WIN_EXPORT)
else()
    add_custom_command(TARGET example POST_BUILD
        COMMAND ${ROOT}/tool/analyze.sh ${ROOT}/src
        COMMENT "Analysing..."
    )
endif()

################################################################################
# app exe
add_executable(app ${APP}/main.cpp)
if (WIN32)
    target_link_libraries(app example python37)
else()
    target_link_libraries(app example python3.6m)
    add_custom_command(TARGET app POST_BUILD
        COMMAND ${ROOT}/tool/analyze.sh ${ROOT}/app
        COMMENT "Analysing..."
    )
endif()

################################################################################
# gtest exe
set(GOOGLE "${ROOT}/lib/gtest/googletest-1.8.0")
SET(CMAKE_CXX_COMPILER /usr/bin/g++)
add_executable(test_example
    ${TEST}/test_example.cpp
    ${GOOGLE}/googletest/src/gtest-all.cc
    ${GOOGLE}/googletest/src/gtest_main.cc
)
target_include_directories(test_example PRIVATE
    ${GOOGLE}/googletest
    ${GOOGLE}/googletest/include
)
if (WIN32)
    target_link_libraries(test_example example python37)
else()
    target_link_libraries(test_example example pthread python3.6m)
    add_custom_command(TARGET test_example POST_BUILD
        COMMAND ${ROOT}/tool/analyze.sh ${ROOT}/test
        COMMENT "Analysing..."
    )
endif()


################################################################################
# all files
FILE(GLOB_RECURSE all_files "*.*")
add_custom_target(all_files SOURCES ${all_files})

################################################################################
# package
FILE(GLOB_RECURSE pack "pack/*.*")
add_custom_target(pack SOURCES ${pack})
add_custom_command(TARGET example POST_BUILD
    COMMAND ${PYTHON} ${ROOT}/tool/package.py .
    COMMENT "Packaging..."
)

################################################################################
# dependencies
add_dependencies(app example)
add_dependencies(test_example example)
add_dependencies(pack example)


