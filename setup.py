from setuptools import setup, find_packages

# Define your package information
NAME = 'materials_chempy'
DESCRIPTION = 'General python uttilities for materials chemistry and engineering'
VERSION = '0.0.1'
AUTHOR = 'Eduardo Toledo Campos'
AUTHOR_EMAIL = 'eduardotcampos@usp.br'
URL = 'https://github.com/eduardotlc/materials_chempy'

# Define the required dependencies
INSTALL_REQUIRES = [
    # List your dependencies here, e.g., 'numpy', 'matplotlib', 'requests'
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
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.6",  # Modify the Python version as needed
    # Include non-Python files such as data files, templates, etc.
    include_package_data=True,
    # Add classifiers to help others understand your project
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.x",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # Optional: entry_points for console scripts or plugins
    entry_points={
        'console_scripts': [
            'your_command = your_package.module:main_function',
        ],
    },
)

