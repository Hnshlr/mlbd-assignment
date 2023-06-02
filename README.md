# AY22 Machine Learning and Big Data (A) - Assignment 2022-2023
Analysis of data from an environmental sensor network using Hadoop/Spark.

© Copyright 2023, All rights reserved to Hans Haller, CSTE-CIDA Student at Cranfield Uni. SATM, Cranfield, UK.

https://www.github.com/Hnshlr

### Presentation:

![alt text](https://github.com/Hnshlr/mlbd-assignment/blob/main/showcase.png?raw=true)

The following implementation serves the analysis of air quality data captured from a network of environmental sensors. To achieve such a goal, it is mandatory to acquire data for a long period of time and compute several tasks to extract the wanted results to allow a precise analysis. Ultimately, this allows us to see the impacts of major world events on the processed data, or potentially prevent other events in the future.


### Important notes:

- Upon loading the notebook, it may be necessary to File > Trust Notebook - in order to visualize the Folium maps.

- If the implementation must be re-executed for further verifications, it may be necessary depending on the machine that the MAX_MEMORY value allocated for the spark session is changed (in third cell).

### Installation:

There are packages that need to be installed in order to run the notebook. 

To create a virtual environment and install the packages, run the following commands in the terminal:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Air quality data:

The data used in this project is collected from the Sensor.Community website, a contributors-driven global sensor network that creates Open Environmental Data. The data is collected from sensors that measure the concentration of PM2.5 and PM10 particles in the air. The data is collected in real-time and is available for download in CSV format.

### You're set to go!

If you have any questions, please contact me at ```hans.haller.885@cranfield.ac.uk```.

### Acknowledgements

This code was developed as part of the Machine Learning and Big Data course at Cranfield University, UK. 