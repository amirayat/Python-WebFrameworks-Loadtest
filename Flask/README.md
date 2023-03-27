### Note

To serve Flask with gunicorn, use this command:

```bash
gunicorn flask_sqlalchemy:app --bind 0.0.0.0:8000 --workers 10
```