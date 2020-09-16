### Cross Origin 해결방법

- 파이썬 패키지 설치

```
pip install django-cors-headers
```

- settings.py 에서 설정 추가

```python
# settings.py

INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://127.0.0.1:3000'
)
```

