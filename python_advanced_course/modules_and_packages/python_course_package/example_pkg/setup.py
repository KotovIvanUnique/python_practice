import setuptools
setuptools.setup(
    name="python_course_package",
    version="0.0.1",
    author="KotovIvanUnique",
    long_description="test package",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)