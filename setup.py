from setuptools import setup, find_packages

setup(
    name="files-elementary",
    version="0.1",
    description="Meltano project files for Elementary, a DBT extension",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/dbt_project.yml"
            "transform/packages.yml"
            "transform/README.md"
        ]
    },
)
