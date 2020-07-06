![pygrid-logo](https://raw.githubusercontent.com/OpenMined/design-assets/master/logos/PyGrid/horizontal-primary-trans.png)

<p align="center">
    <a href="https://github.com/OpenMined/PyGridNetwork/actions?query=workflow%3ATests">
        <img src="https://github.com/OpenMined/PyGridNetwork/workflows/Tests/badge.svg"
            alt="Tests"/></a>
    <a href="https://img.shields.io/github/license/OpenMined/PyGridNetwork">
        <img src="https://img.shields.io/github/license/OpenMined/PyGridNetwork"
            alt="License"/></a>
    <a href="https://img.shields.io/pypi/v/openmined.gridnetwork">
        <img src="https://img.shields.io/pypi/v/openmined.gridnetwork"
            alt="Version"/></a>
    <a href="https://img.shields.io/opencollective/all/openmined">
        <img src="https://img.shields.io/opencollective/all/openmined"
            alt="OpenCollective"/></a>
</p>

<p align="center">
    <a href="https://deploy.cloud.run">
        <img src="https://deploy.cloud.run/button.svg"
            alt="Run on Google Cloud"/></a>
</p>

# PyGridNetwork

PyGridNetwork is a network router used by the PyGrid platform. PyGridNetwork makes use of [WebRTC](https://webrtc.org/) to provide transparent connection between workers.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `openmined.gridnetwork`.

```bash
pip install openmined.gridnetwork
```

## Usage
```bash
python -m gridnetwork <arguments>
```

You can pass the arguments or use environment variables to set the gateway configs.  

**Arguments**
```
required arguments:
  --port PORT, -p PORT  Port number of the socket.io server, e.g. --port=8777.
                        Default is os.environ.get('GRIDNETWORK_WS_PORT',
                        None).

optional arguments:
  --host HOST           GridNerwork host, e.g. --host=0.0.0.0. Default is os.e
                        nviron.get('GRIDNETWORK_WS_HOST','http://0.0.0.0').
  --start_local_db      If this flag is used a SQLAlchemy DB URI is generated
                        to use a local db.
```

**Environment Variables**
- `GRIDNETWORK_WS_PORT` -  Port to run server on.
- `GRIDNETWORK_WS_HOST` - The gridnetwork host
- `DATABASE_URL` - The gateway database URL
- `SECRET_KEY` - The secret key

Example:

```bash
python -m gridnetwork --host=localhost --port=5000 --start_local_db
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contributors

See the list of [contributors](https://github.com/OpenMined/PyGridNetwork/contributors) who participated in this project.

## Support
For support in using this library, please join the  [**#lib_grid_network**](https://openmined.slack.com/archives/C012QNKEY05) Slack channel. If you’d like to follow along with any code changes to the library, please join the [**#code_gridnetwork**](https://openmined.slack.com/archives/C012KAP6A22) Slack channel. [Click here to join our Slack community!](https://slack.openmined.org)

## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
