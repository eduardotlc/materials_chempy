from setuptools import setup, find_packages

# Define your package information
NAME = 'materials_chempy'
DESCRIPTION = 'Materials chemistry data analysis and visualization scripts'
VERSION = '0.0.1'
AUTHOR = 'Eduardo Toledo Campos'
AUTHOR_EMAIL = 'eduardotcampos@usp.br'
URL = 'https://github.com/eduardotlc/materials_chempy'
INSTALL_REQUIRES = [
    "packaging"
]

# Define the required dependencies
SETUP_REQUIRES = [
    "setuptools",
    "wheel"
]

# Optional: Define additional extras or tests_require for development dependencies
EXTRAS_REQUIRE = {
    'dev': [
        # List development dependencies here, e.g., 'pytest', 'coverage'
    ]
}

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.6",  # Modify the Python version as needed
    # Include non-Python files such as data files, templates, etc.
    include_package_data=True,
    # Add classifiers to help others understand your project
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Scientists",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.x",
        "Topic :: Science :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization"
    ],
    # Optional: entry_points for console scripts or plugins
    entry_points={
        'console_scripts': [
            'materials_chempy = materials_chempy:cli',
        ],
    },
)

