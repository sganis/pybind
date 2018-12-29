################################################################################
# example pybind11 cmake file
################################################################################
cmake_minimum_required(VERSION 3.10)
project (pybind)

set(CMAKE_VERBOSE_MAKEFILE on)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(APP ${CMAKE_CURRENT_SOURCE_DIR}/app)
set(SRC ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(TEST ${CMAKE_CURRENT_SOURCE_DIR}/test)
#set(BUILD ${CMAKE_CURRENT_SOURCE_DIR}/build)
#file(MAKE_DIRECTORY ${BUILD})
message("BUILD: ${BUILD}")

include_directories(
    ${SRC}
    /usr/include/python3.6
    /usr/local/include/python3.6
)
#link_directories(${BUILD})

#SET(CMAKE_EXE_LINKER_FLAGS
#    "${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath,'\$ORIGIN/'")
SET(CMAKE_BUILD_RPATH "\$ORIGIN")

################################################################################
# example lib
add_library(
    example SHARED
    ${SRC}/example.cpp
    ${SRC}/example.h
    ${SRC}/person.cpp
    ${SRC}/person.h
    ${SRC}/python.cpp
)
#add_custom_command(
#    TARGET example POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:example> ${BUILD}
#    COMMENT "Copying binaries to build diretory..."
#)


################################################################################
# app exe
add_executable(app ${APP}/main.cpp)
target_include_directories(app PRIVATE ${SRC})
target_link_libraries(app example pthread python3.6m)
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
target_link_libraries(test-example example pthread python3.6m)
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

add_custom_command(TARGET pack POST_BUILD
    COMMAND ${ROOT}/script/package.sh .
    DEPENDS example.done test.done app.done
    COMMENT "Packaging..."
)
################################################################################
# dependencies
add_dependencies(app example)
add_dependencies(test-example example)
add_dependencies(pack example)


