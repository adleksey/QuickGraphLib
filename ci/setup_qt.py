# SPDX-FileCopyrightText: Copyright (c) 2024 Refeyn Ltd and other QuickGraphLib contributors
# SPDX-License-Identifier: MIT

import subprocess
import sys

if sys.platform == "linux":
    qt_platform = "linux"
    qt_arch = "gcc_64"

elif sys.platform == "win32":
    qt_platform = "windows"
    qt_arch = "win64_msvc2019_64"

elif sys.platform == "darwin":
    qtPlatform = "mac"
    qtArch = "clang_64"

else:
    raise RuntimeError(f"Unknown platform {sys.platform}")

subprocess.run(["pip", "install", "aqtinstall==3.1.*"], check=True)
subprocess.run(
    [
        "aqt",
        "install-qt",
        qt_platform,
        "desktop",
        "6.7.2",
        qt_arch,
        "-O",
        "./qt",
        "--archives",
        "qttools",
        "qtdeclarative",
        "qtbase",
        "qtsvg",
        "icu",
    ],
    check=True,
)

if sys.platform == "linux":
    subprocess.run(
        ["dnf", "install", "-y", "libxslt", "llvm-devel", "clang-libs", "libxkbcommon"],
        check=True,
    )
