# Cookiecutter Geospatial Data Science

This is a cookiecutter template for a `Geospatial Data Science` project.

tags: data-science, geospatial, machine-learning, cookiecutter-template, python, boilerplate, project-template

## Requirements

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- [Cookiecutter Python package:](https://cookiecutter.readthedocs.io/en/latest/installation.html)
    - This can be installed with pip by or conda depending on how you manage your Python packages:

```
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```


## Create a new project, run:

In a folder where you want your project generated:
``` bash
cookiecutter https://github.com/dghorai/cookiecutter-gds
```

## The resulting directory structure

The directory structure of your new project looks like this: 

```
│───LICENSE
│───app.py                  <- Flask app
│───config.py               <- Project configurations
│───README.md               <- The top-level README for developers using this project
│───requirements.txt        <- The requirements file for reproducing the analysis environment (pip freeze > requirements.txt)
│───setup.py                <- makes project pip installable (pip install -e .) so src can be imported
|
├───artifacts
│   ├───features            <- Train and test split files consisting of final features of the model that is extracted from cleaned raw datasets
│   ├───models              <- Trained and serialized models, model predictions, or model summaries
│   ├───preprocessor        <- Pre-processor file of the trained model which will be using for model predictions pipeline
│   └───reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
│       └───figures         <- Generated graphics and figures to be used in reporting
├───data                    <- Project datasets
│   ├── external            <- Datasets from third party sources
│   ├── interim             <- Intermediate datasets that has been transformed
│   ├── processed           <- The final, canonical datasets for modeling
│   └── raw                 <- The original and immutable datasets
|
├───docs                    <- Project documents, notes, etc.
|
├───notebooks               <- Jupyter notebooks for EDA, modelling, and visualization
|
├───research                <- Research and development activity on local system
|
├───src                     <- Source code of the project
│   ├───geo_apps            <- Scripts to execute geospatial data science applications
│   ├───ml_features         <- Scripts to turn raw data into features for modeling
│   ├───ml_models           <- Scripts to train models and then use trained models to make predictions
│   ├───raster_ops          <- Scripts to process geospatial raster operations
│   ├───vector_ops          <- Scripts to process geospatial vector operations
│   └───visualization       <- Scripts to create exploratory and results oriented visualizations
|
├───static                  <- Static files of the project
|
├───templates               <- HTML files of the project
|
└───tests                   <- Scripts to test applications - unit test or integrated test
```


## Contributing Guide

We welcome all contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas.

## Reference
- The existing `Cookiecutter Templates` are available at [here](https://www.cookiecutter.io/templates)
