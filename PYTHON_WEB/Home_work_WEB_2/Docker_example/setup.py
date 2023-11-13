from setuptools import setup, find_namespace_packages

setup(
    name="personal_assistant",
    version="1",
    description="Program includes features: address book; notes; sorting files",
    url="https://github.com/Baskina/personal_assistant",
    author="Group",
    author_email="baskina.development@gmail.com",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["colorama"],
    entry_points={"console_scripts": ["start-bot = src.main:main"]},
)
