# setup.py

from setuptools import setup, find_packages

setup(
    name='space_mission_planner',  # Name of your package
    version='0.1',  # Initial version of the package
    packages=find_packages(),  # Automatically discover and include your package and sub-packages
    install_requires=[  # List of external dependencies (if any)
        'numpy',
        'matplotlib',
        'math' 
        'astropy'
        'datetime' # Example: Remove this if you don’t need numpy
    ],
    description="A package for planning space missions FULLY FUNCTIONAL",
    author="Deepmalya Acharya",  # Replace with your name
    author_email="deepmalyaa@gmail.com",  # Replace with your email
    url="https://github.com/yourusername/space_mission_planner",  # Replace with your GitHub repository URL
    classifiers=[  # Optional: Add classifiers to make your package discoverable
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
