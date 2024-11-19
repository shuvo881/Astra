from setuptools import setup, find_packages

setup(
    name="Astra",
    version="0.1.0",
    author="Md. Golam Mostofa",
    author_email="golammostofa10001@gmail.com",
    description="A brief description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/shuvo881/Astra",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your package dependencies here
        # 'some_package>=1.0.0',
    ],
)