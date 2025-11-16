# REST API Definition:

For development: 

backend_url = `http://127.0.0.1:8000`

API definition:

- backend_url/api/notes/
- backend_url/api/chart-data/
- backend_url/api/sequence/<int:id>
- backend_url/api/sequence-plotly-data/<int:id>

- backend_url/api/mgf-files
- backend_url/api/mgf-file-info/<string:mgf-file-name>
- backend_url/api/mgf-file-sequence/<string:mgf-file-name>/<int:sequenec-id>

Media url: 

- backend_url/api/media/...
