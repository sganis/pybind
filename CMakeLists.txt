################################################################################
# example pybind11 cmake file
################################################################################
cmake_minimum_required(VERSION 3.0)

project (pybind)

# subproject paths
set(ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(APP  ${ROOT}/app)
set(SRC  ${ROOT}/src)
set(TEST ${ROOT}/test)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${ROOT}/build)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${ROOT}/build)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${ROOT}/build)

# global compiler settings
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_VERBOSE_MAKEFILE ON)
SET(CMAKE_BUILD_RPATH "\$ORIGIN")
SET(CMAKE_C_COMPILER ${CMAKE_CXX_COMPILER})

# include paths
include_directories(${SRC})
if (WIN32)
    SET(PYWIN C:\\Python37)
    SET(PYTHON ${PYWIN}\\python.exe)
    include_directories(${PYWIN}\\include)
    link_directories(${PYWIN}\\libs)
else()
    # python3 -m pybind11 --includes
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
set(GOOGLE "${ROOT}/lib")
add_executable(test_example
    ${TEST}/test_example.cpp
    ${GOOGLE}/gtest/gtest-all.cc
    ${GOOGLE}/gtest/gtest_main.cc
)
target_include_directories(test_example PRIVATE  ${GOOGLE})
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


