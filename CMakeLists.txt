# SPDX-FileCopyrightText: Copyright (c) 2024 Refeyn Ltd and other QuickGraphLib contributors
# SPDX-License-Identifier: MIT

cmake_minimum_required(VERSION 3.30.3)
set(CMAKE_OSX_ARCHITECTURES "arm64;x86_64" CACHE STRING "" FORCE)

project(QuickGraphLib VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(MSVC)
    add_compile_options(/W4)
else()
    add_compile_options(-Wextra -Wpedantic -fno-visibility-inlines-hidden)
endif()

if(NOT INSTALL_SUBPATH)
    set(INSTALL_SUBPATH
        ${CMAKE_INSTALL_LIBDIR}/qml
        CACHE STRING
        "Install subpath (defaults to lib/qml)"
    )
endif()

find_package(Qt6 REQUIRED COMPONENTS Quick Svg)
qt_standard_project_setup(REQUIRES 6.7)

add_subdirectory(QuickGraphLib)
