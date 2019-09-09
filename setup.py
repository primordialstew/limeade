from setuptools import find_packages
from setuptools import setup


install_requires = []

tests_require = [
    "pytest",
]

extras_require = {
    "test": tests_require,
}


setup(
    name="limeade",
    version="0.1.0",
    url="https://github.com/primordialstew/limeade",
    license='MIT',

    author="Brian Stewart",
    author_email="indelicate@gmail.com",

    description=("Object-oriented Python client for the LimeSurvey"
                 " RemoteControl 2 API (LSRC2)"),

    packages=find_packages(exclude=('tests',)),

    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],
)
