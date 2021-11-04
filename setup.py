# Standard library modules.
import os
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

# We can't just import the version module, as it won't exist until *after*
# installation, so instead treat it like a text file.
with open("brace_expand/version.py", "r") as f:
    # Splitting on '"' should give us ["VERSION = ", "{ver}", ""], so take the
    # 2nd element as the version.
    version = f.read().split('"')[1]

setup(
    name="brace-expand",
    version=version,
    description="Bash-like brace expansion for Python",
    long_description=long_description,
    long_description_content_type="text/markup",
    url="https://github.com/howamith/brace-expand",
    author="Howard Smith",
    author_email="hj_smith@live.com",
    license="MIT",
    zip_safe=False,
    package_data={"brace_expand": ["py.typed"]},
    packages=find_packages(),
    python_requires=">=3.5",
)
