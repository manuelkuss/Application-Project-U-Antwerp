# Django Backend

## Admin page

Can be used for managing Users, Groups, and other database objects.

Access admin page at `http://localhost:8000/admin/`:
- Test admin credentials:
  - Username: `admin`
  - Password: `admin`

## API app

The backend runs a simple application that provides api endpoints for the frontend.

## Database

Type: sqlite3
- lightweight disk-based database
- Suitable for prototype applications (that may be changed to other databases).

## Data processing

The data processing logic is placed in `backend/api/utils/dataProcessing.py`. The api functionality accessed these function to preprocess or retrieve data.

The data processing function for the coding task (merge data files, annotations, and preparing objects for visualizations) is:
- `data_processing_for_coding_task`

## Testing

Existing Tests:
- Unit tests to test the Django objects (e.g. Notes, MgfFile).
- Integration tests to test the REST API the backend provides.
- (in future) System tests: Could be realized with Selenium to test the complete web-application with all the included components.

In backend folder run:

```
python manage.py test
```