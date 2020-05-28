# Trexa Service

This project aims to provide a weekly Trexa 100k list, which is created from the Tranco and Alexa lists. In theory it could be larger, so file an issue if that's
useful to someone.

The canonical repo for Trexa is https://github.com/mozilla/trexa, but the merge
code has been rewritten here to be more flexible.

## Running locally

1. clone the repo
2. run `python3 -m venv env`
3. run `source env/bin/activate`
4. run `pip3 install -r requirements.txt`

And then go to the next section to run tests or start the service.

## Running the tests

`FLASK_ENV=development pytest`

## Starting the service

From the project root:

Production mode:
`FLASK_APP=trexa flask run --host=0.0.0.0`

or

Development mode:
`FLASK_ENV=development FLASK_APP=trexa flask run`

## Environment variables

The following environment variables can be defined to override defaults:

```
ZIP_DOWNLOADS_DEST
CSV_DOWNLOADS_DEST
FINAL_LIST_DEST
```

## HTTP Endpoints

This app exposes the following HTTP endpoints

* `/lists`: see all lists available for download
* `/lists/trexa-2020-05-21.csv`: download a full, single list (150,000+ sites)
* `/api/lists/trexa-2020-05-21.csv?count=N`: download a single list, trimmed to N sites

## License

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/

## Code of Conduct

This project and repository is governed by Mozilla's code of conduct and
etiquette guidelines. For more details please see the [Code of Conduct](./CODE_OF_CONDUCT.md) file.