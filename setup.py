from setuptools import find_namespace_packages, setup

setup(
    name="fine_foods_eda",
    packages=find_namespace_packages(exclude=["*tests*"]),
    version="0.0.1",
    description="Package to do text cleaning in Fine Foods EDA for the NLP focus group",
    author="Inmeta Crayon",
    license="",
    python_requires=">=3.7",
    install_requires=["pandas>=1.0", "dask>=2.28", "tqdm>=4.50", "ftfy==5.8"],
    package_data={
        # If any package contains *.csv or *.parquet files, include them:
        "": ["*.csv", "*.parquet"],
    },
)
