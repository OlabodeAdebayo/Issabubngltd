# ISSABUB Nigeria Limited — Full-Stack Website v3 (Responsive Upgrade)

This version keeps the existing ISSABUB HTML/CSS/JavaScript + Django REST Framework architecture and upgrades its responsiveness, accessibility, API resilience and admin/API safety.

## What changed

### Frontend
- Fluid typography and spacing across desktop, tablet and mobile.
- Mobile navigation with accessible open/close state.
- Skip-to-content link and keyboard focus states.
- Active navigation state.
- Responsive hero/stat layout.
- Responsive service, project, value and contact grids.
- Touch-friendly project category filters.
- Project image viewer/lightbox with keyboard Escape support.
- Lazy-loaded/decode-async portfolio imagery.
- Reduced-motion support.
- API timeout and graceful source-derived fallback data.
- Same-origin `/api` support for production deployments, while local static development defaults to `http://127.0.0.1:8000/api`.
- Quote form now reports API validation errors and prevents duplicate submissions while a request is pending.

### Backend
- Added `/api/health/` health endpoint.
- API root now reports API version/status.
- Added anonymous/user API throttling.
- Added a dedicated quote submission throttle: 10 quote submissions/hour per throttle identity.
- Quote input validation for name, phone and project details.
- Quote status is server-controlled and cannot be changed through the public POST endpoint.
- Production security settings activate when `DJANGO_DEBUG=0`.
- Improved Django Admin displays/search/filtering for company, services, projects and quote requests.
- Added automated API tests for health, projects, services and quote creation.
- Removed Python cache files from the deliverable.

## Frontend local run

From `frontend/`:

```bash
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500/
```

The frontend will attempt the local API at:

```text
http://127.0.0.1:8000/api
```

You can override this before loading `site.js` with:

```html
<script>window.ISSABUB_API_BASE = 'https://your-api-domain.example/api';</script>
```

## Backend local run

From `backend/`:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python seed_data.py
python manage.py createsuperuser
python manage.py runserver 8000
```

API endpoints:

- `/api/`
- `/api/health/`
- `/api/company/`
- `/api/services/`
- `/api/services/<slug>/`
- `/api/projects/`
- `/api/projects/<slug>/`
- `/api/projects/?category=commercial`
- `/api/projects/?featured=1`
- `/api/quotes/`
- `/admin/`

Public clients can read company/services/projects and create quote requests. Administrative mutations and quote management require a staff/admin account.

## Production environment variables

At minimum set:

```text
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=your-api-domain.example
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.example
CSRF_TRUSTED_ORIGINS=https://your-frontend-domain.example
```

If the frontend and API share one origin, CORS requirements are reduced and the frontend can use `/api` automatically.

## Portfolio imagery

The 12 portfolio images in `frontend/assets/images/` are the image assets extracted from the supplied ISSABUB design PDF and mapped to the corresponding project entries.

Portfolio categories:

- Commercial
- Residential
- Retrofitting & Restoration
- Structural Steel

The implementation does not copy source code from the external reference website.
