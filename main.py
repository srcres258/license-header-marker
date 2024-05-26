# SPDX-License-Identifier: MIT

import sys
import os
import argparse


SUFFIXES = [".rs", ".vs", ".gs", ".fs"]
LICENSE_HEADERS = {
    "Apache-2.0":
"""// SPDX-License-Identifier: Apache-2.0

// Copyright 2024 src_resources
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License."""
}


def main() -> int:
    parser = argparse.ArgumentParser(description="The license header marker tool")
    parser.add_argument("dir", type=str, help="The directory containing the source files.")
    parser.add_argument("-l", "--license", type=str, help="The license type, currently only Apache-2.0 as default.")
    args = parser.parse_args();

    license = "Apache-2.0"
    dir = None

    if args.license:
        license = args.license
    if args.dir:
        dir = args.dir

    if dir is None:
        print("Fatal error: directory is not specified.")
        return -1

    for root, dirs, files in os.walk(dir, topdown=True):
        print("Entering: ", root)
        for file in files:
            for suffix in SUFFIXES:
                if file.endswith(suffix):
                    full_path = os.path.join(root, file)
                    print("Processing: ", full_path)

                    with open(full_path, "r") as f:
                        content = f.read()
                    header = LICENSE_HEADERS[license]
                    header += "\n"
                    header += "\n"
                    content = header + content
                    with open(full_path, "w") as f:
                        f.write(content)

    return 0


if __name__ == "__main__":
    sys.exit(main())
