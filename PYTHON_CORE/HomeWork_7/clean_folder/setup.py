from setuptools import setup,  find_packages
setup(
    name='clean_folder',
    version='0.0.1',
    description='Clean folder my desk',
    author='Oleksandr Chonka',
    license='MIT',
    packages=find_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.script:main'] }
)
