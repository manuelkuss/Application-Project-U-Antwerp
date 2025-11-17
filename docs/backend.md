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

## Testing

In backend folder run:

```
python manage.py test
```