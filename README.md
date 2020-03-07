# Python Microservice Architecture With Socrata API

Accessing Open Parking and Camera Violation API to analyze the parking violations issued in fiscal year 2020. 

#####                                                     Table Of Content
- [Project Overview](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#python-microservice-architecture-with-socrata-api)
  * [Python](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI/blob/master/README.md#python)
  * [Docker](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#docker)
  * [Amazon Web Serivces EC2](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#aws-ec2)
  * [ElasticSearch](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#elasticsearch)
  * [Kibana](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#kibana)
  * [API Data](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#api-data)
  * [Resources Documents](https://github.com/BenitaDiop/PythonMicroserviceDeployment_SocrataAPI#resourceful-documentation)



## Objective:
*********
### PYTHON
The goal is to develope a script with sepearate components that will collectively: <br/>
	1. Recieve arguments from command line interface. <br/>
	2. Pull API data but be capable of reproducibility. <br/>
	3. Give client the option to print results as a .json file or stdout <br/>

``` python
from src.APIcall import get_data, get_stats

if __name__ == '__main__':
	options = get_stats()
	print('[+] Requested ', options.page_size,  ' Records From The API Per Call') 
	print('[+] Requested To Run Query ',  options.num_pages, 'x')
	print('[+] Requested To Load Data As A ', options.output, ' File Type')
	get_data(options)
```


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

### DOCKER
<b> Utilized docker open-source platform to build, ship and run  a conatinerizaed application </b>
<br/>
<br/>

<h10>
<b> 1.) Docker Engine: Managing individual containers on Docker command line interface by accessing Docker Daemon through UNIX socket. </b> <br/>
<b>BUILD </b>Designed Dockerfile to build a sequential set of instruction for Docker Engine. <br/>
		1st.) Fudamental Instructions. <br/>
		2nd.) Configuration Instructions. <br/>
		3rd.) Execution Instructions. <br/> 
<b> SHIP </b> Developed Docker Image which hold the entire package need to run applications 
<br/>	
<b> RUN </b> Deployed Docker Container to boost application scalability shipping a ready to run isolated system accompanied by its neceassary dependencies
<br/>
	
	
##### Docker Command Line Snippets 	
	
```bash
docker build -t bigdata1:1.0 .
docker run -v $(pwd):/app -it bigdata1:1.0 /bin/bash
docker tag 005136a55f9f benitad/bigdata1:1.0
docker push benitad/bigdata1
docker run -v ${PWD}:/app/foo -e APP_KEY=$APP_KEY benitad/bigdata1:1.0 python -m main --num_pages 5 --page_size 5 --output=/app/foo/results.json
```
		
<br/>
	
<b> 2.) Docker Compose: Defining multi-container full fledge applications in a single file and then spin up the same application in a single command. Docker compose allows for the development and integration of mulitple objects such as containers, networks and services in a single file known as blocks which will get passed on to Docker engine.   </b>

1) Docker Compose YAML File Datatypes:
	+ Scalars | Sequences | Mappings

```bash
docker-compose up -d  
	#Creates deafult network and makes sure all the network requirements of preceeding services will be fuffilled. 

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

<b> 3.) Docker Swarm -- The ability to make all host collabaorate and run in a an insync manner. Container Orchestrator is a tool used to provision, schedule and mange containers at large scale over one or more clusters of multiple hosts. Turns a cluster of host into one manager and multiple workers. The manager serves the services request and transfer task to the worker. 
</b> </br> 

1. Can Docker Swarm handle Failure? Yes, If one node goes down the work goes to another node. If the master goes down then another node will be elected. 
	+. (N/2)+1 is the total number of required working nodes to keep a swarm still functioning. (N=Total Number of Nodes)
3.

```bash
docker-machine create --driver virtualbox manager
docker-machine create --driver virtualbox worker-1
docker-machine stop manager 
docker machine start manager

docker-machiner ssh manager 

docker swarm init -advertise-addr 000.000.00.000
docker swarm join --token {[docker swarn join token worker]}

docker node ls 
docker node inspect --pretty self 

docker service create --name web-server -p 0000.00 -replace image:tag
docker service ls

docker service ps image

docker node update -- availability drain worker-2 
docker swarm leave 
docker node rm worker-2


```



</br> 

*******
### AmazonWebServices Elastic Compute Cloud (EC2)
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit


![EC2](https://lh3.googleusercontent.com/Vz-aMtbFjm29-xm4-dcTcTjFy1lZ191AZpNCpWC4HUyotHVtda6j6etWk6j3dMaalMm6nO8A1LDb6k_U8l825F_3vl8XYTO2RWK_zVQk01nwFm2DlA8f97dKjbJTtTbkN9HC_AY-6GH7n2NBbybRmaAzK5gOtwDvWvSRLqXnA_mdNJ81WtnBvvW0ZSb7NGrVLIXvfBSvNaQ7-XQrIJX3vtykI8gfGuBKnU_cqE-l35Q7zUBDNV0esvVUYUkAe1Ljgdvi_E2RQuMgxVhQQRXCKcFpML97xupSqgJvZXwJp8LiZgvNK9heYd68MPlvpkD4OOX-fNK9RkWE1NaV_QyICTU4aw5LVX9zHf1Xui7AXjvKV17pVSoIOhuOxIghsUXKWLa_MZEEoWxY0J_HFHbc9sYwNP1W4pKmjt0uCXToQpQXUA8UC9RF3V-dsk-6zgDN30TxjYrmy2hFfWd8qNPAcpnIBsFvng8LMkyS1Y_HSiZU8YI4v5krdSfKXTQPVMc2n06_j8MtYAxEqoOZh-WVjXxtxE9j6-D7xF8zDuLWQbqaYSJgRFv5D293EvZKHgsoLTV-Hv93AEg9IyG7et-F4n5a1fyeuWNdqh8lOoV7ZfszQYsrZHQS-6wiUgtTMxbs3_zVRGaaOIFSHlWxJ32lel7L657MGy-miN2nAPBin83KWT9A3RLbGnc=w1211-h544-no)
	
********

### ELASTICSEARCH
ElsticSearch can be definied as compelete data warehousing an business intelligence application. Elasticsearch coverts raw data such as log files into internal documents and stores them on a distributed storage where they can be quereied. 

##### Getting Started With ElasticSearch 

```
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit

```

*******

### KIBANA
Once data has been indexed by ElasticSearch, Kibana helps make sense of the data. Kibana is a  browser interface that can be used to search and visualize data. 

```
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit
```

</br>

</br>


### API DATA
</br> 

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







