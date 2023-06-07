# Tutorials

This repo contains tutorials 

## Setup environment
1. Create virtual environment using conda
    ```
    conda create -n tutorials python=3.9 
    ```
2. Activate environment
    ```
    conda activate tutorials 
    ```
3. Install poetry and follow instructions to add Poetry's bin directory to your `PATH` environment variable.
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
4. Install packages via poetry
    ```
    poetry install
    ```
5. Run the scripts
    ```
    poetry run python scriptname.py
    ```

## Scripts and articles

### pythonscraper
Note that these tutorials are not maintained.
1. [Web scraping using python - websitescrapefasttrack.py](https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed)
2. [Web scraping javascript using python - websitescrapeJS](https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f?source=friends_link&sk=9caba08b835548b50c4297eff750bcfa)

### penguin-analysis
[Data Analysis: Getting started with pandas](https://medium.com/@_kaparker/data-analysis-in-python-getting-started-with-pandas-8cbcc1500c83?source=friends_link&sk=72a73f762bb36276b0832258b71a870c)

### data-viz
Comparison of matplotlib, altair and plotly.
