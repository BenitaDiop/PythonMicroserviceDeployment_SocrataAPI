# Python Microservice Development With Parking Violations API

Accessing Open Parking and Camera Violation API to analyze the parking violations issued in fiscal year 2020. 



## Objective:
*********
### PYTHON
The goal is to build and refactor code into two sepearate components that individually: <br/>
	1. Gets the arguments from the command line interface. 
	2. Does the real work of pulling API data but be capable of reproducibility. <br/>

``` python
import argparse

page_size = input("Type desired record per API Call > ") 
print("[+] Requested" + "  " + page_size + " " + "Records from the API per call")

num_pages = input("Type desired query quanity > ")
print("[+] Requested To query" + "  " + num_pages + "x")

output = input("Out Options: stdout or .json > ")
print("[+] Requested output" + " " +output)


def get_stats(page_size, num_pages, output):
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--page_size', 
	                    help= "To input records to request API", 
	                    type=int, dest = page_size)
	parser.add_argument('-n', '--num_pages', 
	                    help= "The number of times to query for data", 
	                    type=int, dest = num_pages)
	parser.add_argument('-o', '--output', default = None, dest=output, help = "To print as .json or stdout")

	(options, arguments) = parser.parse_args()

	if page_size >= 1 and type==int:
		options.page_size = page_size
	if not
		parser.error("[-] Please input an integer value, use --help for more info")
	
	if num_pages >= 1 and type==int: 
		options.num_pages = page_size
	if not
		parser.error("[-] Please input an integer value, use --help for more info")
	if output is not ".json" or "stdout": 
		raise Exception e 

return options

options = get_stats()

terminal_result_page_size = subprocess.check_output(["python", "main.py", options.page_size])
terminal_result_num_page = subprocess.check_output(["python", "main.py", options.num_page])
terminal_result_output = subprocess.check_output(["python", "main.py", options.output])

print(terminal_result_page_size)
print(terminal_result_num_page)
print(terminal_result_output)


```



********

### DOCKER
<b> Utilized docker open-source platform to build, ship and run  a conatinerizaed application </b>
<br/>
<br/>

<h10>
<b> Docker Engine: Managing individual containers on Docker command line interface by accessing Docker Daemon through UNIX socket. </b> <br/>
<b>BUILD </b>Designed Dockerfile to build a sequential set of instruction for Docker Engine. Str <br/>
<center> <h25>	1st.) Fudamental Instructions.
		2nd.) Configuration Instructions.
		3rd.) Execution Instructions. </h25> </center>
<br/>	
<b> SHIP </b> Developed Docker Image which hold the entire package need to run applications 
<br/>	
<b> RUN </b> Deployed Docker Container to boost application scalability shipping a ready to run isolated system accompanied by its neceassary dependencies
<br/>
<br/>
	
<b> 2.) Docker Compose: Defining multi-container applications in a single file and then spin up the same application in a single command </b>
1. Lorem ipsum dolor sit amet <br/>
2. Lorem ipsum dolor sit amet <br/>
3. Lorem ipsum dolor sit amet <br/>
	</br>
</h10>
</br> 

```bash
docker build -t bigdata1:1.0 .
docker run -v $(pwd):/app -it bigdata1:1.0 /bin/bash
docker tag 005136a55f9f benitad/bigdata1:1.0
docker push benitad/bigdata1
```

*******
### AWS EC2
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit
	
********

### ELASTICSEARCH
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit

*******

### KIBANA
1. Lorem ipsum dolor sit amet, consectetur adipiscing elit
2. Lorem ipsum dolor sit amet, consectetur adipiscing elit

</br>

</br>


### API DATA
</br> 


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




## Deployment


## Useful Documentation 

* [Socrata Open Data API](https://dev.socrata.com/)


