from setuptools import setup, find_packages

description = 'A tool for viewing 2- and 3-D multi-layered image data.'

setup(
    name='hdav',
    version='0.1.0',
    description=description,
    long_description=description,
    url='https://github.com/innolitics/hdav',
    author='Innolitics, LLC',
    author_email='info@innolitics.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='scientific image',
    packages=find_packages(),
    install_requires=['gitpython'],
    package_data={},
    data_files=[],
)
