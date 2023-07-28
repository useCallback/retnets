from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'RETNETS is a powerful package designed to facilitate the usage of the Retentive Network by AI engineers. Whether you are working with Torch or Tensorflow, RETNET provides seamless integration and empowers you to harness the potential of Retentive Network for your AI projects.'
LONG_DESCRIPTION = 'RETNETS is a powerful package designed to facilitate the usage of the Retentive Network by AI engineers. Whether you are working with Torch or Tensorflow, RETNET provides seamless integration and empowers you to harness the potential of Retentive Network for your AI projects.'

# Setting up
setup(
    name="retnets",
    version=VERSION,
    author="useCallback (Khalfoun Mohamed El Mehdi)",
    author_email="<contact.khalfoun@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['torch', 'torchscale', 'fairseq', 'apex', 'fairscale'],
    keywords=['retnet', 'retnets', 'retentive networks',
              'LLM', 'large language models', 'ai', 'artificial intelligence'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
