from setuptools import setup, find_packages


setup(
    name="fictional-tribble",
    version="0.0.1a",
    packages=['fictional-tribble',] + find_packages(exclude=['doc/*', 'docker/*', 'data/*', 'scripts/*', 'tests/*']),
    install_requires=['pandas',
                      'jupyter',
                      'pandas-datareader',
                      ],
)