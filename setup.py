# read the contents of your README file
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "./README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)


def read_requirements():
    with open(path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
        requirements = [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]
    return requirements


setup(
    name="libero",
    packages=[package for package in find_packages() if package.startswith("libero")],
    install_requires=read_requirements(),
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
    author="Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone",
    # url="https://github.com/ARISE-Initiative/robosuite",
    author_email="bliu@cs.utexas.edu, yifengz@cs.utexas.edu",
    version="0.1.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "lifelong.main=libero.lifelong.main:main",
            "lifelong.eval=libero.lifelong.evaluate:main",
            "libero.config_copy=scripts.config_copy:main",
            "libero.create_template=scripts.create_template:main",
        ]
    },
)
