import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='pyqtspecgram',
    version='0.1.0',
    packages=setuptools.find_packages(where='src'),
    package_dir={"": "src"},
    url='https://github.com/epeters13/pyqtspecgram',
    license='GPL3',
    author='Edwin G. W. Peters',
    author_email='edwin.g.w.peters@gmail.com',
    description='Python spectogram plotted using pyqtgraph.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3'
    ],
    keywords='spectrogram specgram waterfall pyqtgraph',
    python_requires=">=3.6",
    install_requires=[
        'scipy',
        'pyqtgraph'
    ],
)
