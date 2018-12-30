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

#set(BUILD ${CMAKE_BINARY_DIR})
#message("BUILD: ${BUILD}")
#file(MAKE_DIRECTORY ${BUILD})

include_directories(${SRC})
#link_directories(${BUILD})

#SET(CMAKE_EXE_LINKER_FLAGS ${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath,'\$ORIGIN/'")
SET(CMAKE_BUILD_RPATH "\$ORIGIN")

if (MSVC)
    SET(PYTHON "C:\\Python37")
    include_directories(${PYTHON}\\include)
    link_directories(${PYTHON}\\libs)
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
    ${SRC}/example_py.cpp
    ${SRC}/person.cpp
    ${SRC}/person.h
    ${SRC}/person_py.cpp
    ${SRC}/python.cpp
    ${SRC}/export.h
)
if (MSVC)
    target_compile_definitions(example PRIVATE WIN_EXPORT)
endif()

#add_custom_command(
#    TARGET example POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:example> ${BUILD}
#    COMMENT "Copying binaries to build diretory..."
#)


################################################################################
# app exe
add_executable(app ${APP}/main.cpp)
target_include_directories(app PRIVATE ${SRC})
if (WIN32)
    target_link_libraries(app example python37)
else()
    target_link_libraries(app example python3.6m)
endif()

#add_custom_command(TARGET app POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:app> ${BUILD}
#    COMMENT "Copying binaries to build diretory..."
#)

################################################################################
# gtest exe
set(GOOGLE "${ROOT}/lib/gtest/googletest-1.8.0")
SET(CMAKE_CXX_COMPILER /usr/bin/g++)
add_executable(test-example
    ${TEST}/test_example.cpp
    ${GOOGLE}/googletest/src/gtest-all.cc
    ${GOOGLE}/googlemock/src/gmock-all.cc
    ${GOOGLE}/googlemock/src/gmock_main.cc
)
target_include_directories(test-example PRIVATE
    ${CMAKE_SOURCE_DIR}/src
    ${GOOGLE}/googletest
    ${GOOGLE}/googletest/include
    ${GOOGLE}/googlemock
    ${GOOGLE}/googlemock/include
)
if (WIN32)
    target_link_libraries(test-example example python37)
else()
    target_link_libraries(test-example example pthread python3.6m)
endif()

#add_custom_command(TARGET test-example POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:test-example> ${BUILD}
#    COMMENT "Copying binaries to build diretory..."
#)


################################################################################
# all files
FILE(GLOB_RECURSE all_files "*.*")
add_custom_target(all_files SOURCES ${all_files})

################################################################################
# package
FILE(GLOB_RECURSE pack "pack/*.*")
add_custom_target(pack SOURCES ${pack})
if (WIN32)
    add_custom_command(TARGET example POST_BUILD
        COMMAND ${PYTHON}\\python.exe ${ROOT}/tool/package.py .
        COMMENT "Packaging for windows..."
    )
else()
    add_custom_command(TARGET example POST_BUILD
        COMMAND ${ROOT}/tool/package.py .
        COMMENT "Packaging for linux..."
    )
endif()

################################################################################
# dependencies
add_dependencies(app example)
add_dependencies(test-example example)
add_dependencies(pack example)


