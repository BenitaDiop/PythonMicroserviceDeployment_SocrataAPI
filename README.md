# Python Microservice Architecture Deployment With Socrata API

In this project I leveraged Socrata OPCV API data to build a pipeline of logs from Docker Container to the Elasticsearch, Kibana Stack where data was collected, analyzed and transformed into visuals. Scripts were written in python and polished to be able to take in command line arguments from UNIX/LINUX operating systems. The scripts were tested for reproducibility by provisioning, configuring and executing an AWS EC2 instance which ran on a Docker container, read-in the python script, parsed in parameters from the command line and pull the API JSON logs. Additionally Git was utilized to maintain version control and prevent the confliction of concurrent work. 

***Table Of Content***

- [Project Overview](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#python-microservice-architecture-with-socrata-api)
  * [Python](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI/blob/master/README.md#python)
  * [Docker](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#docker)
  * [Amazon Web Serivces EC2](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#aws-ec2)
  * [ElasticSearch](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#elasticsearch)
  * [Kibana](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#kibana)
  * [API Data](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#api-data)
  * [Resources Documents](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#resourceful-documentation)


*********
# PYTHON

![image](https://user-images.githubusercontent.com/45861503/76188107-7c7f6800-6194-11ea-8f2a-ad4c177731c9.png)



**SOURCE CODE** `main.py`

``` python
from src.APIcall import get_data, get_stats

if __name__ == '__main__':
	options = get_stats()
	print('[+] Requested ', options.page_size,  ' Records From The API Per Call') 
	print('[+] Requested To Run Query ',  options.num_pages, 'x')
	print('[+] Requested To Load Data As A ', options.output, ' File Type')
	get_data(options)
```
**SOURCE CODE** `APICall.py`

```python

import os
import json 
import argparse
from sodapy import Socrata 

domain = 'data.cityofnewyork.us'
client_id = 'nc67-uf89'
data = Socrata(domain, os.getenv("APP_KEY"))
data_count = data.get(client_id, select ='COUNT(*)')
count = int(data_count[0]['COUNT'])

def get_stats():
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--page_size', 
	                    help= "To input records to request API", 
	                    type=int)
	parser.add_argument('-n', '--num_pages', 
	                    help= "The number of times to query for data", 
	                    type=int)
	parser.add_argument('-o', '--output', default = None, 
		help = "To print as .json or stdout")
	return parser.parse_args() 

def get_data(options):
	if not options.num_pages: 
		options.num_pages = count // options.page_size + 1 
	if options.output and '.json' in options.output:
		with open(options.output, 'w') as results:
			pass
	for runs in range(options.num_pages):
		offset = options.page_size*runs
		outfile = data.get(client_id, 
			limit=options.page_size, 
			offset=offset)
		for result in outfile:
			if not options.output or '.json' not in options.output:
				print(result)
			else:
				with open(options.output, "a") as results:
					results.write(json.dumps(result) + '\n')	


	




```



********

# DOCKER


![image](https://user-images.githubusercontent.com/45861503/76191046-abe5a300-619b-11ea-9eda-805a60dd6bd1.png)


<br/>


![image](https://user-images.githubusercontent.com/45861503/76193206-b6566b80-61a0-11ea-8151-b3260017da3b.png)



## DockerFile

**Dockerfile Requirements** 
<br/>

		1st.) Fudamental Instructions. 
		2nd.) Configuration Instructions. 
		3rd.) Execution Instructions. 
**Dockerfile Used to build** `Docker Image`

```python
ARG PYTHON_VERSION=3.7
FROM python:${PYTHON_VERSION}
WORKDIR /.app
COPY . .
RUN pip install -r requirements.txt
```

	
	
**Docker Commands Used to** `Build Image` ***and*** `Run Python API Call`
	
```python
docker build -t {docker_image.name:image_version} .
docker run -v $(pwd):/app -it {docker_account}/{docker_image.name:image_version} /bin/bash
docker tag {docker_image_tag} {docker_image.name:image_desired_tagname}
docker push {docker_image.name:image_version}
docker run -v ${PWD}:/app/foo -e APP_KEY=$APP_KEY {docker_image.name:image_version} python -m main --num_pages {parameter} --page_size {parameter} --output= {parameter}
```
		
## Docker Compose

**Docker-Compose.yml**
```yml
version: '3'
services:
  pyth:
    network_mode: host
    container_name: pyth
    build:
      context: .
    volumes:
      - .:/app:rw
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:6.3.2
    environment:
      - cluster.name=docker-cluster
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
      nofile:
        soft: 65536
        hard: 65536
    ports:
      - "9200:9200"
  kibana:
    image: docker.elastic.co/kibana/kibana:6.3.2
    ports:
      - "5601:5601"

```


**Running** `Docker-Compose`
```bash
docker-compose up -d
docker-compose build pyth
docker-compose run pyth bin/bash

# Additional Compands {optional use}
docker exec -it [container] bash 
docker run -it --link [container:version] --rm [] sh -c  'exec [] -h $ROOT_PRIVLEDGES bash
docker-compose config 
docker-compase config --services
docker-compose images
docker-compose logs 
docker-compose logs --tail=10
docker-compose top
docker-compose down 
```

*Will not delve into Docker Swarm in this project but below are some noteworthy DockerSwarm commands*
<br/>


```bash
docker-machine create --driver virtualbox {Swarm_Node}
docker-machine stop {Swarm_Manager} 
docker machine start {Swarm_Manager}
docker-machine ssh {Swarm_Node} 
docker swarm init -advertise-addr {Ip_Address}
docker swarm join --{docker_swarm_join_node_token}
docker node ls 
docker node inspect --pretty {Swarm_Node} 
docker service create --name {Network} -p {Ip_Address} -replace {docker_image}:{docker_image_tag}
docker service ls
docker service ps {docker_image}
docker node update -- availability drain {Swarm-Node} 
docker swarm leave 
docker node rm {Swarm_Node}
```



*******
# AmazonWebServices Elastic Compute Cloud (EC2)
![image](https://user-images.githubusercontent.com/45861503/76192979-43e58b80-61a0-11ea-91df-d6b01175b84f.png)

`SSH` **into** `EC2`
```
ssh -i file.pem ubuntu@{IP_address}
sudo apt install docker.io
sudo docker login --username={USERNAME}
sudo docker pull {docker_account}/{docker_image.name:image_version}
sudo docker run -it {docker_account}/{docker_image.name:image_version} /bin/bash
sudo docker run -it {docker_account}/{docker_image.name:image_version} python main.py --page_size {parameter} --num_pages {parameter} --output {parameter}
```
- [x] ***Our initial main.py file is EC2 certified*** 

![image](https://user-images.githubusercontent.com/45861503/76159406-05cf6580-60d5-11ea-992d-41ca4f79d5cc.png)

	
********

# ELASTICSEARCH

![image](https://user-images.githubusercontent.com/45861503/76170522-d570e100-613f-11ea-8e2c-9e7ebc12167f.png)
 

**Downloading `ElasticSearch` on `Ubuntu`**

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.1-amd64.deb
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.6.1-amd64.deb.sha512
shasum -a 512 -c elasticsearch-7.6.1-amd64.deb.sha512 
sudo dpkg -i elasticsearch-7.6.1-amd64.deb

```

```
docker-compose logs elasticsearch
sudo sysctl -w vm.max_map_count=262144
```


#### CODE

```python
from datetime import datetime
from elasticsearch import Elasticsearch
import os, sys
import json 
import argparse
from sodapy import Socrata 

domain = 'data.cityofnewyork.us'
client_id = 'nc67-uf89'
plug  = Socrata(domain, os.getenv("APP_KEY"))
data_count = plug.get(client_id, select ='COUNT(*)')
count = int(data_count[0]['COUNT'])


def get_stats():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--page_size', help= "To input records to request API", type=int)
    parser.add_argument('-n', '--num_pages', help= "The number of times to query for data",type=int)
    parser.add_argument('-o', '--output', default = None, help = "To print as .json or stdout")
    
    return parser.parse_args() 
    
 options = get_stats()



def its_elastic():
    es = Elasticsearch()
    try:
        es.indices.create('bigdata1')
    except:
        pass
    return es    

its_elastic()


def get_data(options, es):
    i = 0
    if not options.num_pages:
        options.num_pages = count // options.page_size + 1 

    if options.output and '.json' in options.output:
        with open(options.output, 'w') as results:
            pass

    for runs in range(options.num_pages):
        offset = options.page_size*runs
        outfile = plug.get(client_id, 
                         limit=options.page_size, 
                         offset=offset) #list        
        for r in outfile: 
            date = None
            time = None
            timestamp = datetime(1, 1, 1, 1, 1)
            for key, value in r.items(): 
                if "date" in key: 
                    date = datetime.strptime(value, '%m/%d/%Y').date()           
                if "time" in key: 
                    time = datetime.strptime(value+'M', '%I:%M%p').time()
                if 'amount' in key: 
                    r[key] = float(value)
            if date and time:
                timestamp = datetime.combine(date, time)
            if date and not time:
                timestamp = date
            if not date and time:
                timestamp = time
            r['timestamp'] = timestamp 
            
            i += 1
            
            res = es.index("bigdata", id=i, body = r)
get_data(options, es)


```

*******

# KIBANA
![image](https://user-images.githubusercontent.com/45861503/76170981-33072c80-6144-11ea-9b94-fa20e7655a1c.png)

### Kibana Ubuntu Installation

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-7.6.1-amd64.deb
shasum -a 512 kibana-7.6.1-amd64.deb 
sudo dpkg -i kibana-7.6.1-amd64.deb

ps -p 1

sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service

sudo systemctl start kibana.service
sudo systemctl stop kibana.service
```


```
docker-compose run -e APP_KEY=$APP_KEY pyth python -m _main --page_size 500 --num_pages 500 --output results.json

```



![image](https://user-images.githubusercontent.com/45861503/76892084-7a866a80-6860-11ea-8e5a-a8ed847bdf6c.png)

![image](https://user-images.githubusercontent.com/45861503/76879754-11e1c280-684d-11ea-9fa1-d4eb49764048.png)


![image](https://user-images.githubusercontent.com/45861503/76891494-786fdc00-685f-11ea-9555-d1a31e0e65fe.png)


![image](https://user-images.githubusercontent.com/45861503/76891852-0b107b00-6860-11ea-9f38-03a170377d87.png)






## API DATA


```json
{"plate": "27008JD", "state": "NY", "license_type": "COM", "summons_number": "1414761960", "issue_date": "10/17/2016", "violation_time": "02:53P", "violation": "DOUBLE PARKING", "fine_amount": "115", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "115", "payment_amount": "0", "amount_due": "0", "precinct": "041", "county": "BX", "issuing_agency": "POLICE DEPARTMENT", "violation_status": "HEARING HELD-NOT GUILTY", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VFZSUmVFNUVZekpOVkdzeVRVRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "86041MG", "state": "NY", "license_type": "COM", "summons_number": "1414761983", "issue_date": "10/17/2016", "violation_time": "03:04P", "violation": "DOUBLE PARKING", "fine_amount": "115", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "115", "payment_amount": "0", "amount_due": "0", "precinct": "041", "county": "BX", "issuing_agency": "POLICE DEPARTMENT", "violation_status": "HEARING HELD-NOT GUILTY", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VFZSUmVFNUVZekpOVkdzMFRYYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "68080JZ", "state": "NY", "license_type": "COM", "summons_number": "7054261800", "issue_date": "09/02/2016", "violation_time": "02:07P", "violation": "NO STANDING-DAY/TIME LIMITS", "fine_amount": "115", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "23", "payment_amount": "92", "amount_due": "0", "precinct": "013", "county": "NY", "issuing_agency": "TRAFFIC", "violation_status": "HEARING HELD-GUILTY REDUCTION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQk1VNUVTVEpOVkdkM1RVRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "EKS2203", "state": "NY", "license_type": "PAS", "summons_number": "5032717149", "issue_date": "10/25/2008", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGxSQmVrMXFZM2hPZWtVd1QxRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "YDY83T", "state": "NJ", "license_type": "PAS", "summons_number": "5032717150", "issue_date": "10/25/2008", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGxSQmVrMXFZM2hPZWtVeFRVRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "WBD64W", "state": "NJ", "license_type": "PAS", "summons_number": "5032717290", "issue_date": "10/28/2008", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGxSQmVrMXFZM2hPZWtrMVRVRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "XBSD23", "state": "NJ", "license_type": "PAS", "summons_number": "7054262268", "issue_date": "09/06/2016", "violation_time": "02:03P", "violation": "EXPIRED MUNI MTR-COMM MTR ZN", "fine_amount": "65", "penalty_amount": "10", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "75", "amount_due": "0", "precinct": "013", "county": "NY", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQk1VNUVTVEpOYWtreVQwRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "X4818A", "state": "NJ", "license_type": "PAS", "summons_number": "7081479911", "issue_date": "08/08/2016", "violation_time": "11:10A", "violation": "NO PARKING-STREET CLEANING", "fine_amount": "65", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "65", "payment_amount": "0", "amount_due": "0", "precinct": "019", "county": "NY", "issuing_agency": "TRAFFIC", "violation_status": "HEARING HELD-NOT GUILTY", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQk5FMVVVVE5QVkd0NFRWRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "HAM3170", "state": "NY", "license_type": "PAS", "summons_number": "1406722273", "issue_date": "03/15/2016", "violation_time": "09:02P", "violation": "FIRE HYDRANT", "judgment_entry_date": "06/30/2016", "fine_amount": "115", "penalty_amount": "60", "interest_amount": "0.1", "reduction_amount": "0.1", "payment_amount": "175", "amount_due": "0", "precinct": "052", "county": "BX", "issuing_agency": "POLICE DEPARTMENT", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VFZSUmQwNXFZM2xOYWtrelRYYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "483UKO", "state": "CT", "license_type": "999", "summons_number": "5032773141", "issue_date": "11/01/2008", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGxSQmVrMXFZek5OZWtVd1RWRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "U177562", "state": "TN", "license_type": "PAS", "summons_number": "1405578191", "issue_date": "06/08/2016", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VFZSUmQwNVVWVE5QUkVVMVRWRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "GLL5464", "state": "PA", "license_type": "PAS", "summons_number": "7940452836", "issue_date": "05/24/2008", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wck1FMUVVVEZOYW1kNlRtYzlQUT09&locationName=_____________________", "description": "View Summons"}}
```


```python
	plate	state	license_type	summons_number	issue_date	violation_time	violation	judgment_entry_date	fine_amount	penalty_amount	interest_amount	reduction_amount	payment_amount	amount_due	precinct	county	issuing_agency	summons_image	violation_status
0	DN9F942	TX	PAS	7000233503	01/11/2016	08:43A	NO PARKING-DAY/TIME LIMITS	04/28/2016	60	60	41.64	0	0	161.64	108	Q	TRAFFIC	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBOZWxWM1RYYzlQUT09&locationName=_____________________', 'description': 'View Summons'}	
1	GBJ3345	NY	PAS	7000233801	01/11/2016	02:47P	NO STANDING-DAY/TIME LIMITS	04/28/2016	115	60	59.49	0	0	234.49	111	Q	TRAFFIC	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBOZW1kM1RWRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
2	601030	NY	PAS	4659389017	07/16/2019	08:18A	PHTO SCHOOL ZN SPEED VIOLATION		50	0	0	0	50	0	000	QN	DEPARTMENT OF TRANSPORTATION	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQVkVGNFRuYzlQUT09&locationName=_____________________', 'description': 'View Summons'}	
3	6HVZ40	MA	PAS	7000234040	01/12/2016	07:06A	NO PARKING-STREET CLEANING	04/28/2016	45	60	35.73	0	0	140.73	109	Q	TRAFFIC	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBPUkVFd1RVRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
4	C0YS82	FL	PAS	4659388979	07/16/2019	08:16A	PHTO SCHOOL ZN SPEED VIOLATION		50	0	0	0	50	0	000	QN	DEPARTMENT OF TRANSPORTATION	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQUkdzelQxRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
5	VF16882	NY	ORG	4659389054	07/16/2019	08:20A	PHTO SCHOOL ZN SPEED VIOLATION		50	0	0	0	50	0	000	BK	DEPARTMENT OF TRANSPORTATION	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQVkVFeFRrRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
6	PAP3813	MN	PAS	7000234090	01/12/2016	08:24A	NO STANDING-DAY/TIME LIMITS	04/28/2016	115	60	59.49	0	0	234.49	109	Q	TRAFFIC	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBPUkVFMVRVRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
7	T761267C	NY	OMT	4659388918	07/16/2019	08:15A	PHTO SCHOOL ZN SPEED VIOLATION		50	0	0	0	50	0	000	BK	DEPARTMENT OF TRANSPORTATION	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQUkd0NFQwRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
8	HBE8891	NY	PAS	7000234325	01/15/2016	10:32A	INSP. STICKER-EXPIRED/MISSING	05/05/2016	65	60	43.4	0	0	168.4	114	Q	TRAFFIC	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBPUkUxNVRsRTlQUT09&locationName=_____________________', 'description': 'View Summons'}	
9	1SPIDER3	NY	SRF	8728804053	03/02/2019	01:05P	INSP. STICKER-EXPIRED/MISSING	08/15/2019	65	60	0.37	0.09	125.28	0	025	NY	TRAFFIC	{'url': 'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSamVVOUVaM2RPUkVFeFRYYzlQUT09&locationName=_____________________', 'description': 'View Summons'}	HEARING HELD-GUILTY

```





## TBD


## Resourceful Documentation 
* [Mottaqui Karim - Statistics 9760](http://taq.website/STA9760/)
* [Socrata Open Data API](https://dev.socrata.com/)
* [Docker Educational Resources](https://docs.docker.com/engine/docker-overview/)
* [Git Source Code Management](https://git-scm.com/docs/gittutorial)
* [EC2 Step-By-Step Guru99](https://www.guru99.com/creating-amazon-ec2-instance.html)
* [ElasticSearch Overview Stackify](https://stackify.com/elasticsearch-tutorial/)
* [Elastic.co Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html)
* [Elastic.co Elastic Search Reference](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)







