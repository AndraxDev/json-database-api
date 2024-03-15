# JSON Database API

## Introduction

This is a simple JSON database API that allows you to create, read, update and delete data from a JSON file.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
flask run
```

## Endpoints

### GET /api/v1/read

This endpoint returns all the data from the JSON file.

### GET /api/v1/write

This endpoint allows you to write data to the JSON file. If key already exists, it will be updated.

### GET /api/v1/delete

This endpoint allows you to delete data from the JSON file.

## Params

***path*** - The path to the JSON value. Example: `path=users/0/name` will return data at `users[0]['name']` in the JSON file `{"users": {"0": {"name": {<RETURN VALUE HERE>}}}}`.

***value*** - The value to write to the JSON file. Example: `value=John` will write `John` to the JSON file. JSON strings are supported.

***type*** - The type of the value to write to the JSON file. Example: `type=string` will write `John` as a string to the JSON file. Supported types: `string`, `json`, `float`, `bool`, `null`. If `type` is not provided, the value will be written as a JSON. If `null` is provided, the value will be deleted from the JSON file.

## Example

```bash
curl -X GET "http://localhost:5000/api/v1/read?path=users/0/name"
```

will return

```json
{
  "value": "John"
}
```

## License

```angular2html
Copyright (c) 2024 Dmytro Ostapenko. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
