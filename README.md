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
<html>
'
<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>plate</th>\n      <th>state</th>\n      <th>license_type</th>\n      <th>summons_number</th>\n      <th>issue_date</th>\n      <th>violation_time</th>\n      <th>violation</th>\n      <th>judgment_entry_date</th>\n      <th>fine_amount</th>\n      <th>penalty_amount</th>\n      <th>interest_amount</th>\n      <th>reduction_amount</th>\n      <th>payment_amount</th>\n      <th>amount_due</th>\n      <th>precinct</th>\n      <th>county</th>\n      <th>issuing_agency</th>\n      <th>summons_image</th>\n      <th>violation_status</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>DN9F942</td>\n      <td>TX</td>\n      <td>PAS</td>\n      <td>7000233503</td>\n      <td>01/11/2016</td>\n      <td>08:43A</td>\n      <td>NO PARKING-DAY/TIME LIMITS</td>\n      <td>04/28/2016</td>\n      <td>60</td>\n      <td>60</td>\n      <td>41.64</td>\n      <td>0</td>\n      <td>0</td>\n      <td>161.64</td>\n      <td>108</td>\n      <td>Q</td>\n      <td>TRAFFIC</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBOZWxWM1RYYzlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>GBJ3345</td>\n      <td>NY</td>\n      <td>PAS</td>\n      <td>7000233801</td>\n      <td>01/11/2016</td>\n      <td>02:47P</td>\n      <td>NO STANDING-DAY/TIME LIMITS</td>\n      <td>04/28/2016</td>\n      <td>115</td>\n      <td>60</td>\n      <td>59.49</td>\n      <td>0</td>\n      <td>0</td>\n      <td>234.49</td>\n      <td>111</td>\n      <td>Q</td>\n      <td>TRAFFIC</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBOZW1kM1RWRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>601030</td>\n      <td>NY</td>\n      <td>PAS</td>\n      <td>4659389017</td>\n      <td>07/16/2019</td>\n      <td>08:18A</td>\n      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n      <td>NaN</td>\n      <td>50</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>50</td>\n      <td>0</td>\n      <td>000</td>\n      <td>QN</td>\n      <td>DEPARTMENT OF TRANSPORTATION</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQVkVGNFRuYzlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>6HVZ40</td>\n      <td>MA</td>\n      <td>PAS</td>\n      <td>7000234040</td>\n      <td>01/12/2016</td>\n      <td>07:06A</td>\n      <td>NO PARKING-STREET CLEANING</td>\n      <td>04/28/2016</td>\n      <td>45</td>\n      <td>60</td>\n      <td>35.73</td>\n      <td>0</td>\n      <td>0</td>\n      <td>140.73</td>\n      <td>109</td>\n      <td>Q</td>\n      <td>TRAFFIC</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBPUkVFd1RVRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>C0YS82</td>\n      <td>FL</td>\n      <td>PAS</td>\n      <td>4659388979</td>\n      <td>07/16/2019</td>\n      <td>08:16A</td>\n      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n      <td>NaN</td>\n      <td>50</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>50</td>\n      <td>0</td>\n      <td>000</td>\n      <td>QN</td>\n      <td>DEPARTMENT OF TRANSPORTATION</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQUkdzelQxRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>VF16882</td>\n      <td>NY</td>\n      <td>ORG</td>\n      <td>4659389054</td>\n      <td>07/16/2019</td>\n      <td>08:20A</td>\n      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n      <td>NaN</td>\n      <td>50</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>50</td>\n      <td>0</td>\n      <td>000</td>\n      <td>BK</td>\n      <td>DEPARTMENT OF TRANSPORTATION</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQVkVFeFRrRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>PAP3813</td>\n      <td>MN</td>\n      <td>PAS</td>\n      <td>7000234090</td>\n      <td>01/12/2016</td>\n      <td>08:24A</td>\n      <td>NO STANDING-DAY/TIME LIMITS</td>\n      <td>04/28/2016</td>\n      <td>115</td>\n      <td>60</td>\n      <td>59.49</td>\n      <td>0</td>\n      <td>0</td>\n      <td>234.49</td>\n      <td>109</td>\n      <td>Q</td>\n      <td>TRAFFIC</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBPUkVFMVRVRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>T761267C</td>\n      <td>NY</td>\n      <td>OMT</td>\n      <td>4659388918</td>\n      <td>07/16/2019</td>\n      <td>08:15A</td>\n      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n      <td>NaN</td>\n      <td>50</td>\n      <td>0</td>\n      <td>0</td>\n      <td>0</td>\n      <td>50</td>\n      <td>0</td>\n      <td>000</td>\n      <td>BK</td>\n      <td>DEPARTMENT OF TRANSPORTATION</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VOVVUVFJQUkd0NFQwRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>HBE8891</td>\n      <td>NY</td>\n      <td>PAS</td>\n      <td>7000234325</td>\n      <td>01/15/2016</td>\n      <td>10:32A</td>\n      <td>INSP. STICKER-EXPIRED/MISSING</td>\n      <td>05/05/2016</td>\n      <td>65</td>\n      <td>60</td>\n      <td>43.4</td>\n      <td>0</td>\n      <td>0</td>\n      <td>168.4</td>\n      <td>114</td>\n      <td>Q</td>\n      <td>TRAFFIC</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wQmQwMUVTWHBPUkUxNVRsRTlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>1SPIDER3</td>\n      <td>NY</td>\n      <td>SRF</td>\n      <td>8728804053</td>\n      <td>03/02/2019</td>\n      <td>01:05P</td>\n      <td>INSP. STICKER-EXPIRED/MISSING</td>\n      <td>08/15/2019</td>\n      <td>65</td>\n      <td>60</td>\n      <td>0.37</td>\n      <td>0.09</td>\n      <td>125.28</td>\n      <td>0</td>\n      <td>025</td>\n      <td>NY</td>\n      <td>TRAFFIC</td>\n      <td>{\'url\': \'http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSamVVOUVaM2RPUkVFeFRYYzlQUT09&amp;locationName=_____________________\', \'description\': \'View Summons\'}</td>\n      <td>HEARING HELD-GUILTY</td>\n    </tr>\n  </tbody>\n</table>'
</html>
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

