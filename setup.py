from setuptools import setup, find_packages
import os

README = os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md')
with open(README,encoding='utf-8') as f:
    long_description = f.read()

setup(name="well-behaved-logging",
      author="Yamada Hiroyuki",
      version="0.0.1",
      packages=find_packages("."),
      classifiers=["Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Libraries"],
      long_description=long_description,
      long_description_content_type = "text/markdown")
