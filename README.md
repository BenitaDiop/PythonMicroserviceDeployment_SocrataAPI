# ParkingViolations
Accessing Open Parking and Camera Violation API to analyze the parking violations issued in fiscal year 2020. In this project a Docker container will be created, the data will be loaded to an ElasticSearch instance and then visualized with Kibana.

## Getting Started

### Prerequisites

- Creating a Docker Account 
- Dowloading Docker to Ubuntu 18.04 
- Docker Configuration
- Dowloading Git 
- Git Configuration 


### Installing
```
import keys
import os
import json 
import pandas as pd
import docker

import keys
import os
from sodapy import Socrata 
client = Socrata("data.cityofnewyork.us", 
                 keys.access_token,
                 keys.api_key_name, 
                 keys.api_secret)

OPCV = client.get("nc67-uf89", limit=10)
OPCV_df = pd.DataFrame.from_records(OPCV)
OPCV_df
```

## Deployment



## Built With

* [Docker](https://hub.docker.com/r/benitad/bigdata1) - Containerization
* [Git](https://git-scm.com//) - Source Code Mangement 
* [Jupyter Notebook](https://jupyter.org/) - Interactive Computing Notebook

