# csvProcesorAPI
### Introduction
csvProcessor is an open source API for processing csv files in the following way:

Input example: 
Song,Date,Number of Plays
Umbrella,2020-01-02,200
Umbrella,2020-01-01,100
In The End,2020-01-01,500
Umbrella,2020-01-01,50
In The End,2020-01-01,1000
Umbrella,2020-01-02,50
In The End,2020-01-02,500

Output for this input file:
Song,Date, Total Number of Plays for Date
Umbrella,2020-01-01,150
Umbrella,2020-01-02,250
In The End,2020-01-01,1500
In The End,2020-01-02,500


### Project Support Features
* Process csv files
### Installation Guide
* Clone this repository [here](https://github.com/yoeherrera/csvProcessor.git).
* It only has the master branch, so work with it.
* Create a virtual environment and install the dependencies from requirements.txt file

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /csv-uploader | To upload (the input file) and download (the processed file) |

### Technologies Used
* Python
* Django-rest-framework
### Authors
* [Yoe Herrera](https://github.com/yoeherrera)

### License
This project is available for use under the MIT License.