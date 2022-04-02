import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="shady_tr",
    version="0.0.1",
    author="Ka3u6y6a",
    author_email="",
    description="Helps to avoid spam-filters by replacing some characters in text with similar characters from other languages",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT License',
    url="https://github.com/Ka3u6y6a/shady_text_randomizer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=["tests"]),
    keywords='text randomizer random',
    python_requires='>=3.6',
)
