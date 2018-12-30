import setuptools
import re

with open("../version.h", "r") as f:
    match = re.match(r'.*VERSION[ \t]+\"([0-9\.-]+)\"',
        f.read().replace('\n',''))
    if match:
        version = match.group(1)
        print(version)
assert version

with open("../README.md", "r") as f:
    long_description = f.read()

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
except ImportError:
    bdist_wheel = None

package = 'example'

setuptools.setup(
    version=f"{version}",
    name=f"{package}",
    author="Author",
    author_email="author@example.com",
    description="A python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=[f'{package}'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    package_data = {
        f'{package}': ['*.so', '*.pyd'],
    },
    data_files = [
        ('', ['LICENSE.txt', 'README.md']),
    ],
    # install_requires=[],
    cmdclass={ 'bdist_wheel': bdist_wheel, },
    entry_points={
        'console_scripts': [
            f'{package}={package}:main',
        ],
    },
)
