# PRTG Alert Counter

An intermediate solution to protect alerting workflows from anomalies and alert floods. This alert counter simply counts incoming alerts and executes an action based on a configured threshold. Initially inspired with AI in mind, there are implementations in place to route alerts to [ELK stack](https://www.elastic.co/what-is/elasticsearch-machine-learning) for machine learning analysis, monitoring, and prediction.

## Table of Contents
* [The Details](#the-details)
* [Getting Started](#getting-started)
    * [Requirements](#requirements)
    * [Installation](#installation)
    * [Usage](#usage)
* [Presentation](#presentation)
* [Author](#author)
* [License](#license)

## The Details

The alert counter API accepts any alerts from its `/log` endpoint. From PRTG, this can be accomplished with notification triggers using Execute HTTP action.

Any action can be easily configured and added to the `/log` endpoint/function to run after the threshold has been reached. By default, it pauses another notification trigger with ID configured in the `config.ini` file. It then alerts to Opsgenie but again, can be easily configured to another alerting platform.

The alert counter may pause and protect the typical workflow but alerts shouldn't completely stop reaching human eyes. It will also send alerts to Logstash and a syslog for futher analysis and logging. The ELK stack environment can be set up using the popular [Docker ELK](https://github.com/deviantony/docker-elk).

## Getting Started

### Requirements

* Python 3
    * _Tested and ran with version 3.8.7+. Some older versions will probably work but is not recommended._

### Installation

1. Clone repo from GitHub:
```bash
git clone https://github.com/CC-Digital-Innovation/prtg-alert-counter.git
```
* or download the [zip](https://github.com/CC-Digital-Innovation/prtg-alert-counter/archive/refs/heads/main.zip)

2. Configure and rename `config.ini.example` file to `config.ini`.

3. It is recommended to use Python's virtual environment:

```bash
python3 -m venv <env-name>
source <env-name>/bin/activate
```

4. Then, install all Python packages:

```bash
pip install -r requirements.txt
```

### Usage

Run the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Presentation

In 2022, Digital Innovation held a meeting where this project was presented by our team. The presentation was created using markdown and rendered with Marp. The HTML rendered version can be viewed under the `html` branch or [here](https://github.com/CC-Digital-Innovation/prtg-alert-counter/blob/html/index.html).

## Author
* Jonny Le <<jonny.le@computacenter.com>>
* Rakshit Kalra
* Bob Matos
* Gabrielle Woods
* Summer Markley
* Thomas Tar

## License
MIT License

Copyright (c) 2021 Computacenter Digital Innovation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.