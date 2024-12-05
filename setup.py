from setuptools import setup, find_packages

setup(
    name="fastapi_ndjson_logger",
    version="0.1.3",
    description="A FastAPI middleware for logging requests and responses in NDJSON format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Rajath Kumar",
    author_email="rajathkumarks@gmail.com",
    url="https://github.com/analogdata/fastapi-logger",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: FastAPI",
    ],
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    include_package_data=True,
    install_requires=["fastapi"],
    python_requires=">=3.12",
)
