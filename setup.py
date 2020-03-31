import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pigeon_task",
    version="0.0.1",
    author="Moker",
    description="A small example script to count pigeon shifts",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':
            ['count_shifts = src.start:main']
    }
)
