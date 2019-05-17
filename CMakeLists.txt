cmake_minimum_required(VERSION 2.8)
project(aio C)

set(PROJECT_DESCRIPTION "The Linux-native asynchronous I/O facility")
set(PROJECT_HOMEPAGE_URL "https://pagure.io/libaio")
set(PROJECT_VERSION_MAJOR 0)
set(PROJECT_VERSION_MINOR 3)
set(PROJECT_VERSION_PATCH 111)
set(PROJECT_VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}")

include(conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCE_FILES source_subfolder/src/io_cancel.c
                 source_subfolder/src/io_getevents.c
                 source_subfolder/src/io_queue_init.c
                 source_subfolder/src/io_queue_run.c
                 source_subfolder/src/io_setup.c
                 source_subfolder/src/compat-0_1.c
                 source_subfolder/src/io_destroy.c
                 source_subfolder/src/io_queue_release.c
                 source_subfolder/src/io_queue_wait.c
                 source_subfolder/src/io_submit.c
                 source_subfolder/src/raw_syscall.c)

set(HEADER_FILES source_subfolder/src/libaio.h
                 source_subfolder/src/syscall-alpha.h
                 source_subfolder/src/syscall-generic.h
                 source_subfolder/src/syscall-i386.h
                 source_subfolder/src/syscall-ppc.h
                 source_subfolder/src/syscall-sparc.h
                 source_subfolder/src/vsys_def.h
                 source_subfolder/src/syscall-arm.h
                 source_subfolder/src/syscall.h
                 source_subfolder/src/syscall-ia64.h
                 source_subfolder/src/syscall-s390.h
                 source_subfolder/src/syscall-x86_64.h)

add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE source_subfolder/src)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE -fomit-frame-pointer)
set_target_properties(${CMAKE_PROJECT_NAME} PROPERTIES LINK_FLAGS -Wl,--version-script,${CMAKE_CURRENT_SOURCE_DIR}/source_subfolder/src/libaio.map)

install(TARGETS ${CMAKE_PROJECT_NAME}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)
install(FILES ${HEADER_FILES} DESTINATION include)
