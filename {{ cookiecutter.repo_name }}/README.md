{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------
<pre>
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
</pre>


--------

<p><small>Project based on the <a target="_blank" href="https://www.cookiecutter.io/templates">existing cookiecutter templates</a>.</small></p>
