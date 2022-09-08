# Files Elementary

Meltano project [file bundle](https://docs.meltano.com/concepts/plugins#file-bundles) for [Elementary](https://docs.elementary-data.com/introduction)

Included Files:
- [`transform`](./bundle/transform/) (directory)
- [`transform/dbt_packages`](./bundle/transform/dbt_packages) (directory)
- [`transform/dbt_project.yml`](./bundle/transform/dbt_project.yml)
- [`transform/packages.yml`](./bundle/transform/packages.yml)
- [`transform/README.md`](./bundle/transform/README.md)


```
# Add elementary to your Meltano project
meltano add files elementary

# Introduce elementary dependencies (will appear in your [`transform/dbt_packages`](./bundle/transform/dbt_packages) directory)
meltano invoke dbt deps
