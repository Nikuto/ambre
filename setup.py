from setuptools import setup, find_packages

setup(
    name='ambre',
    version='0.0',
    description='',
    author=[
        "Marc Souply",
        "Guillaume Roche",
        "Louanne Roger",
        "Anatole Gaudin"
    ],
    author_email=[
        "guillaume.roche@ftsn.me"
        # To fill for marc, louanne and anatole
    ],
    packages=find_packages(),
    install_requires=[
    ],
    include_package_data=True,
    data_files=[
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    test_suite='ambre.tests'
)
print(find_packages())
