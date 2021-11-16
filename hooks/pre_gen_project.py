# -*- encoding: utf-8 -*-
# Copyright (c) 2019 Stephen Bunn <stephen@bunn.io>
# ISC License <https://opensource.org/licenses/isc>

import shutil

if not shutil.which("git"):
    raise OSError(
        "generating this project requires git <https://git-scm.com/>, "
        "but we can't find it on your system"
    )

if not shutil.which("poetry"):
    raise OSError(
        "initializing the virtual environment requires poetry "
        "<https://python-poetry.org/>, but we can't find it on your system"
    )
