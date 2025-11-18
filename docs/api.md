# REST API Definition:

For development: 
- backend_url = `http://127.0.0.1:8000`

**API definition**:

- backend_url/api/mgf-files
  - Get information on the existing mgf-file in the database.
- backend_url/api/mgf-file-info/<string:mgf-file-name>
  - Get information on the existing sequences (including metadata) that are defined in an mgf-file. If it is not processed already, it will preprocess the data.
- backend_url/api/notes/
  - Fetch notes from database.
- (tmp) backend_url/api/chart-data/
  - Fetch data for charts.

Media url:

- backend_url/api/media/...
  - For loading additional data from the backend server, such as json file for generating interactive graphics.