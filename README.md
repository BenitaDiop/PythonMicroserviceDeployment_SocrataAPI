# ParkingViolations
Accessing Open Parking and Camera Violation API to analyze the parking violations issued in fiscal year 2020. In this project a Docker container will be created, the data will be loaded to an ElasticSearch instance and then visualized with Kibana.

## API DATA
```
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


```
'{"plate":{"0":"DN9F942","1":"GBJ3345","2":"601030","3":"6HVZ40","4":"C0YS82","5":"VF16882","6":"PAP3813","7":"T761267C","8":"HBE8891","9":"1SPIDER3"},"state":{"0":"TX","1":"NY","2":"NY","3":"MA","4":"FL","5":"NY","6":"MN","7":"NY","8":"NY","9":"NY"},"license_type":{"0":"PAS","1":"PAS","2":"PAS","3":"PAS","4":"PAS","5":"ORG","6":"PAS","7":"OMT","8":"PAS","9":"SRF"},"summons_number":{"0":"7000233503","1":"7000233801","2":"4659389017","3":"7000234040","4":"4659388979","5":"4659389054","6":"7000234090","7":"4659388918","8":"7000234325","9":"8728804053"},"issue_date":{"0":"01\\/11\\/2016","1":"01\\/11\\/2016","2":"07\\/16\\/2019","3":"01\\/12\\/2016","4":"07\\/16\\/2019","5":"07\\/16\\/2019","6":"01\\/12\\/2016","7":"07\\/16\\/2019","8":"01\\/15\\/2016","9":"03\\/02\\/2019"},"violation_time":{"0":"08:43A","1":"02:47P","2":"08:18A","3":"07:06A","4":"08:16A","5":"08:20A","6":"08:24A","7":"08:15A","8":"10:32A","9":"01:05P"},"violation":{"0":"NO PARKING-DAY\\/TIME LIMITS","1":"NO STANDING-DAY\\/TIME LIMITS","2":"PHTO SCHOOL ZN SPEED VIOLATION","3":"NO PARKING-STREET CLEANING","4":"PHTO SCHOOL ZN SPEED VIOLATION","5":"PHTO SCHOOL ZN SPEED VIOLATION","6":"NO STANDING-DAY\\/TIME LIMITS","7":"PHTO SCHOOL ZN SPEED VIOLATION","8":"INSP. STICKER-EXPIRED\\/MISSING","9":"INSP. STICKER-EXPIRED\\/MISSING"},"judgment_entry_date":{"0":"04\\/28\\/2016","1":"04\\/28\\/2016","2":null,"3":"04\\/28\\/2016","4":null,"5":null,"6":"04\\/28\\/2016","7":null,"8":"05\\/05\\/2016","9":"08\\/15\\/2019"},"fine_amount":{"0":"60","1":"115","2":"50","3":"45","4":"50","5":"50","6":"115","7":"50","8":"65","9":"65"},"penalty_amount":{"0":"60","1":"60","2":"0","3":"60","4":"0","5":"0","6":"60","7":"0","8":"60","9":"60"},"interest_amount":{"0":"41.64","1":"59.49","2":"0","3":"35.73","4":"0","5":"0","6":"59.49","7":"0","8":"43.4","9":"0.37"},"reduction_amount":{"0":"0","1":"0","2":"0","3":"0","4":"0","5":"0","6":"0","7":"0","8":"0","9":"0.09"},"payment_amount":{"0":"0","1":"0","2":"50","3":"0","4":"50","5":"50","6":"0","7":"50","8":"0","9":"125.28"},"amount_due":{"0":"161.64","1":"234.49","2":"0","3":"140.73","4":"0","5":"0","6":"234.49","7":"0","8":"168.4","9":"0"},"precinct":{"0":"108","1":"111","2":"000","3":"109","4":"000","5":"000","6":"109","7":"000","8":"114","9":"025"},"county":{"0":"Q","1":"Q","2":"QN","3":"Q","4":"QN","5":"BK","6":"Q","7":"BK","8":"Q","9":"NY"},"issuing_agency":{"0":"TRAFFIC","1":"TRAFFIC","2":"DEPARTMENT OF TRANSPORTATION","3":"TRAFFIC","4":"DEPARTMENT OF TRANSPORTATION","5":"DEPARTMENT OF TRANSPORTATION","6":"TRAFFIC","7":"DEPARTMENT OF TRANSPORTATION","8":"TRAFFIC","9":"TRAFFIC"},"summons_image":{"0":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VG5wQmQwMUVTWHBOZWxWM1RYYzlQUT09&locationName=_____________________","description":"View Summons"},"1":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VG5wQmQwMUVTWHBOZW1kM1RWRTlQUT09&locationName=_____________________","description":"View Summons"},"2":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VGtSWk1VOVVUVFJQVkVGNFRuYzlQUT09&locationName=_____________________","description":"View Summons"},"3":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VG5wQmQwMUVTWHBPUkVFd1RVRTlQUT09&locationName=_____________________","description":"View Summons"},"4":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VGtSWk1VOVVUVFJQUkdzelQxRTlQUT09&locationName=_____________________","description":"View Summons"},"5":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VGtSWk1VOVVUVFJQVkVFeFRrRTlQUT09&locationName=_____________________","description":"View Summons"},"6":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VG5wQmQwMUVTWHBPUkVFMVRVRTlQUT09&locationName=_____________________","description":"View Summons"},"7":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VGtSWk1VOVVUVFJQUkd0NFQwRTlQUT09&locationName=_____________________","description":"View Summons"},"8":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VG5wQmQwMUVTWHBPUkUxNVRsRTlQUT09&locationName=_____________________","description":"View Summons"},"9":{"url":"http:\\/\\/nycserv.nyc.gov\\/NYCServWeb\\/ShowImage?searchID=VDBSamVVOUVaM2RPUkVFeFRYYzlQUT09&locationName=_____________________","description":"View Summons"}},"violation_status":{"0":null,"1":null,"2":null,"3":null,"4":null,"5":null,"6":null,"7":null,"8":null,"9":"HEARING HELD-GUILTY"}}'
```

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

