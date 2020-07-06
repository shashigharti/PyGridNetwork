"""Run webserver."""

import argparse
import os
import sys

from gridnetwork import create_app, raise_grid

parser = argparse.ArgumentParser(description="Run GridNetwork application.")
parser._action_groups.pop()

required = parser.add_argument_group("required arguments")
optional = parser.add_argument_group("optional arguments")

required.add_argument(
    "--port",
    "-p",
    type=int,
    help="Port number of the socket.io server, e.g. --port=8777. Default is os.environ.get('GRIDNETWORK_WS_PORT', None).",
    default=os.environ.get("GRIDNETWORK_WS_PORT", None),
    required=True,
)

optional.add_argument(
    "--host",
    type=str,
    help="GridNerwork host, e.g. --host=0.0.0.0. Default is os.environ.get('GRIDNETWORK_WS_HOST','http://0.0.0.0').",
    default=os.environ.get("GRIDNETWORK_WS_HOST", "0.0.0.0"),
)

optional.add_argument(
    "--start_local_db",
    dest="start_local_db",
    action="store_true",
    help="If this flag is used a SQLAlchemy DB URI is generated to use a local db.",
)

parser.set_defaults(use_test_config=False)


if __name__ == "__main__":
    args = parser.parse_args()
    db_config = None

    if args.start_local_db:
        db_path = "sqlite:///databaseGridNetwork.db"
        db_config = {"SQLALCHEMY_DATABASE_URI": db_path}

    app, server = raise_grid(host=args.host, port=args.port, db_config=db_config)
else:
    app = create_app()
