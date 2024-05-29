from setuptools import setup, find_packages

setup(
    name='py-habr-parser',
    version='1.0.0',
    description='Python library for scraping and retrieving articles, comments, and other content from the Habr website.',
    url='https://github.com/FlacSy/HabrParser',
    author='FlacSy',
    author_email='flacsy.x@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['Habr Parser', 'Habr', 'Habr API'],
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
)
