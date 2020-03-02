# ParkingViolations
Accessing Open Parking and Camera Violation API to analyze the parking violations issued in fiscal year 2020. In this project a Docker container will be created, the data will be loaded to an ElasticSearch instance and then visualized with Kibana.

### Outline 
**Python:** The goal is to refactor our code to be able to create two sepearate functions. 
- *Part One:* Build a function to get the arguments from the command line . 
- *Part Two:* Build a function that does the real work and is capable of reproducibility. 



#### API DATA
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


### Prerequisites

- Open Parking and Camera Violations API
- Creating a Docker Account 
- Dowloading Docker to Ubuntu 18.04 
- Docker Configuration
- Docker Image Build
- Dowloading Git 
- Git Configuration 


### Docker Installation Code
```bash
docker build -t bigdata1:1.0 .
docker run -v $(pwd):/app -it bigdata1:1.0 /bin/bash
docker tag 005136a55f9f benitad/bigdata1:1.0
docker push benitad/bigdata1
```

## Deployment


## Built With

* [Docker](https://hub.docker.com/r/benitad/bigdata1) - Containerization
* [Git](https://git-scm.com//) - Source Code Mangement 
* [Jupyter Notebook](https://jupyter.org/) - Interactive Computing Notebook



```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>plate</th>\n",
       "      <th>state</th>\n",
       "      <th>license_type</th>\n",
       "      <th>summons_number</th>\n",
       "      <th>issue_date</th>\n",
       "      <th>violation_time</th>\n",
       "      <th>violation</th>\n",
       "      <th>fine_amount</th>\n",
       "      <th>penalty_amount</th>\n",
       "      <th>interest_amount</th>\n",
       "      <th>reduction_amount</th>\n",
       "      <th>payment_amount</th>\n",
       "      <th>amount_due</th>\n",
       "      <th>precinct</th>\n",
       "      <th>county</th>\n",
       "      <th>issuing_agency</th>\n",
       "      <th>summons_image</th>\n",
       "      <th>violation_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>JCJ3429</td>\n",
       "      <td>NY</td>\n",
       "      <td>PAS</td>\n",
       "      <td>4659360568</td>\n",
       "      <td>07/19/2019</td>\n",
       "      <td>04:46P</td>\n",
       "      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>000</td>\n",
       "      <td>ST</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>HWT5702</td>\n",
       "      <td>NY</td>\n",
       "      <td>PAS</td>\n",
       "      <td>4659360489</td>\n",
       "      <td>07/19/2019</td>\n",
       "      <td>04:46P</td>\n",
       "      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n",
       "      <td>50</td>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>75</td>\n",
       "      <td>0</td>\n",
       "      <td>000</td>\n",
       "      <td>BX</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>CUC5995</td>\n",
       "      <td>NY</td>\n",
       "      <td>PAS</td>\n",
       "      <td>4659360507</td>\n",
       "      <td>07/19/2019</td>\n",
       "      <td>04:46P</td>\n",
       "      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>000</td>\n",
       "      <td>BX</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>26493BB</td>\n",
       "      <td>NY</td>\n",
       "      <td>OMR</td>\n",
       "      <td>1434581986</td>\n",
       "      <td>01/18/2018</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>PH8554</td>\n",
       "      <td>FL</td>\n",
       "      <td>PAS</td>\n",
       "      <td>1434582425</td>\n",
       "      <td>02/27/2018</td>\n",
       "      <td>10:05A</td>\n",
       "      <td>NO PARKING-STREET CLEANING</td>\n",
       "      <td>45</td>\n",
       "      <td>10</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>55</td>\n",
       "      <td>072</td>\n",
       "      <td>K</td>\n",
       "      <td>DEPARTMENT OF SANITATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>GTD8882</td>\n",
       "      <td>NY</td>\n",
       "      <td>PAS</td>\n",
       "      <td>4659360556</td>\n",
       "      <td>07/19/2019</td>\n",
       "      <td>04:46P</td>\n",
       "      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>000</td>\n",
       "      <td>BK</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>T611511C</td>\n",
       "      <td>NY</td>\n",
       "      <td>OMT</td>\n",
       "      <td>5600045268</td>\n",
       "      <td>01/24/2020</td>\n",
       "      <td>03:38P</td>\n",
       "      <td>NO STANDING-SNOW EMERGENCY</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>000</td>\n",
       "      <td>MN</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>T773676C</td>\n",
       "      <td>NY</td>\n",
       "      <td>OMT</td>\n",
       "      <td>5600045270</td>\n",
       "      <td>01/24/2020</td>\n",
       "      <td>04:04P</td>\n",
       "      <td>NO STANDING-SNOW EMERGENCY</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>000</td>\n",
       "      <td>MN</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>86109MM</td>\n",
       "      <td>NY</td>\n",
       "      <td>COM</td>\n",
       "      <td>5600045232</td>\n",
       "      <td>01/24/2020</td>\n",
       "      <td>03:03P</td>\n",
       "      <td>NO STANDING-SNOW EMERGENCY</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>000</td>\n",
       "      <td>MN</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>HEARING HELD-GUILTY REDUCTION</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>11032MM</td>\n",
       "      <td>NY</td>\n",
       "      <td>COM</td>\n",
       "      <td>4659360684</td>\n",
       "      <td>07/19/2019</td>\n",
       "      <td>04:47P</td>\n",
       "      <td>PHTO SCHOOL ZN SPEED VIOLATION</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>0</td>\n",
       "      <td>000</td>\n",
       "      <td>QN</td>\n",
       "      <td>DEPARTMENT OF TRANSPORTATION</td>\n",
       "      <td>{'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      plate state license_type summons_number  issue_date violation_time  \\\n",
       "0   JCJ3429    NY          PAS     4659360568  07/19/2019         04:46P   \n",
       "1   HWT5702    NY          PAS     4659360489  07/19/2019         04:46P   \n",
       "2   CUC5995    NY          PAS     4659360507  07/19/2019         04:46P   \n",
       "3   26493BB    NY          OMR     1434581986  01/18/2018            NaN   \n",
       "4    PH8554    FL          PAS     1434582425  02/27/2018         10:05A   \n",
       "5   GTD8882    NY          PAS     4659360556  07/19/2019         04:46P   \n",
       "6  T611511C    NY          OMT     5600045268  01/24/2020         03:38P   \n",
       "7  T773676C    NY          OMT     5600045270  01/24/2020         04:04P   \n",
       "8   86109MM    NY          COM     5600045232  01/24/2020         03:03P   \n",
       "9   11032MM    NY          COM     4659360684  07/19/2019         04:47P   \n",
       "\n",
       "                        violation fine_amount penalty_amount interest_amount  \\\n",
       "0  PHTO SCHOOL ZN SPEED VIOLATION          50              0               0   \n",
       "1  PHTO SCHOOL ZN SPEED VIOLATION          50             25               0   \n",
       "2  PHTO SCHOOL ZN SPEED VIOLATION          50              0               0   \n",
       "3                             NaN         NaN            NaN             NaN   \n",
       "4      NO PARKING-STREET CLEANING          45             10               0   \n",
       "5  PHTO SCHOOL ZN SPEED VIOLATION          50              0               0   \n",
       "6      NO STANDING-SNOW EMERGENCY          50              0               0   \n",
       "7      NO STANDING-SNOW EMERGENCY          50              0               0   \n",
       "8      NO STANDING-SNOW EMERGENCY          50              0               0   \n",
       "9  PHTO SCHOOL ZN SPEED VIOLATION          50              0               0   \n",
       "\n",
       "  reduction_amount payment_amount amount_due precinct county  \\\n",
       "0                0             50          0      000     ST   \n",
       "1                0             75          0      000     BX   \n",
       "2                0             50          0      000     BX   \n",
       "3              NaN            NaN        NaN      NaN    NaN   \n",
       "4                0              0         55      072      K   \n",
       "5                0             50          0      000     BK   \n",
       "6                0              0         50      000     MN   \n",
       "7                0              0         50      000     MN   \n",
       "8                0             50          0      000     MN   \n",
       "9                0             50          0      000     QN   \n",
       "\n",
       "                 issuing_agency  \\\n",
       "0  DEPARTMENT OF TRANSPORTATION   \n",
       "1  DEPARTMENT OF TRANSPORTATION   \n",
       "2  DEPARTMENT OF TRANSPORTATION   \n",
       "3                           NaN   \n",
       "4      DEPARTMENT OF SANITATION   \n",
       "5  DEPARTMENT OF TRANSPORTATION   \n",
       "6  DEPARTMENT OF TRANSPORTATION   \n",
       "7  DEPARTMENT OF TRANSPORTATION   \n",
       "8  DEPARTMENT OF TRANSPORTATION   \n",
       "9  DEPARTMENT OF TRANSPORTATION   \n",
       "\n",
       "                                       summons_image  \\\n",
       "0  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "1  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "2  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "3  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "4  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "5  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "6  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "7  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "8  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "9  {'url': 'http://nycserv.nyc.gov/NYCServWeb/Sho...   \n",
       "\n",
       "                violation_status  \n",
       "0                            NaN  \n",
       "1                            NaN  \n",
       "2                            NaN  \n",
       "3                            NaN  \n",
       "4                            NaN  \n",
       "5                            NaN  \n",
       "6                            NaN  \n",
       "7                            NaN  \n",
       "8  HEARING HELD-GUILTY REDUCTION  \n",
       "9                            NaN  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import keys\n",
    "import os\n",
    "import json \n",
    "import pandas as pd\n",
    "import docker\n",
    "\n",
    "import keys\n",
    "import os\n",
    "from sodapy import Socrata \n",
    "client = Socrata(\"data.cityofnewyork.us\", \n",
    "                 keys.access_token,\n",
    "                 keys.api_key_name, \n",
    "                 keys.api_secret)\n",
    "\n",
    "OPCV = client.get(\"nc67-uf89\", limit=10)\n",
    "OPCV_df = pd.DataFrame.from_records(OPCV)\n",
    "OPCV_df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "latex_envs": {
   "LaTeX_envs_menu_present": true,
   "autoclose": false,
   "autocomplete": true,
   "bibliofile": "biblio.bib",
   "cite_by": "apalike",
   "current_citInitial": 1,
   "eqLabelWithNumbers": true,
   "eqNumInitial": 1,
   "hotkeys": {
    "equation": "Ctrl-E",
    "itemize": "Ctrl-I"
   },
   "labels_anchors": false,
   "latex_user_defs": false,
   "report_style_numbering": false,
   "user_envs_cfg": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}


```
