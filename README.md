# ParkingViolations
Accessing Open Parking and Camera Violation API to analyze the parking violations issued in fiscal year 2020. In this project a Docker container will be created, the data will be loaded to an ElasticSearch instance and then visualized with Kibana.

## Getting Started

### Prerequisites

- Open Parking and Camera Violations API
- Creating a Docker Account 
- Dowloading Docker to Ubuntu 18.04 
- Docker Configuration
- Docker Image Build
- Dowloading Git 
- Git Configuration 


### Installing
```
# Docker Image Build 
docker build -t bigdata1:1.0 .
docker run -v $(pwd):/app -it bigdata1:1.0 /bin/bash
docker tag 005136a55f9f benitad/bigdata1:1.0
docker push benitad/bigdata1
```

## Deployment

```
[{'plate': 'FFY8675',
  'state': 'NY',
  'license_type': 'PAS',
  'summons_number': '7148276779',
  'issue_date': '01/06/2011',
  'summons_image': {'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wRk1FOUVTVE5PYW1NelQxRTlQUT09&locationName=_____________________',
   'description': 'View Summons'}}]
```


## Built With

* [Docker](https://hub.docker.com/r/benitad/bigdata1) - Containerization
* [Git](https://git-scm.com//) - Source Code Mangement 
* [Jupyter Notebook](https://jupyter.org/) - Interactive Computing Notebook

