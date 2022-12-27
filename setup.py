import os
import setuptools

install_requires = [
    "torch >= 1.0",
    "pdf2image",
    "pdfplumber",
    "Pillow",
    "pydantic",
    "pytesseract",
    "transformers >= 4.25.1",
]

top_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(top_dir, 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="dockie",
    version="0.0.1",
    author="Mahesh Subramanian",
    author_email="maheshpec123@gmail.com",
    description="Dockie: A key information extractor inspired from Docquery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maheshpec/dockie",
    entry_points={
        "console_scripts": ["dockie = dockie.cmd.__main__:main"],
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7.0",
    install_requires=install_requires,
)
