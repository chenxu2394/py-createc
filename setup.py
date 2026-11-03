import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt', encoding='utf-8') as f:
    required = f.read().splitlines()

# Filter dependencies based on the platform
required = [req for req in required if req.strip() and not req.startswith('#')]
windows_specific = ['pywin32==306; sys_platform == "win32"']

setuptools.setup(
    name="createc",
    author="Chen Xu",
    author_email="cxu.self@gmail.com",
    description="A python interface with the Createc scanning probe microscope",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chenxu2394/py-createc",
    project_urls={
        "Documentation": "https://py-createc.readthedocs.io/en/latest/",
        "Source": "https://github.com/chenxu2394/py-createc",
    },
    license="MIT",
    packages=setuptools.find_packages(exclude=['examples']),
    package_data={
        'createc': ['*.yaml'],        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires='>=3.7, <3.10',
    install_requires=required + windows_specific,
    extras_require={
        "example_maps": [
            "bokeh==2.2.3",
            "Jinja2==3.0.1",
            "matplotlib>=3.3,<3.6",
        ],
        "osc": [
            "bokeh==2.2.3",
            "Jinja2==3.0.1",
            "psutil>=5.8,<6",
            "pyserial>=3.5,<4",
        ],
        "utility": [
            "bokeh==2.2.3",
            "Jinja2==3.0.1",
        ],
    },
)
