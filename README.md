# Dr Sahanawaz — Academic Website

Personal academic site for **Md Sahanawaz, PhD** (Chemical Data Scientist · Lecturer).

Built with **Python** (Jinja2 + YAML). Hosted for free (GitHub Pages or Cloudflare Pages). Custom domain: `drsahanawaz.com` + `www.drsahanawaz.com`.

## Local commands

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 build.py
python3 serve.py
```

Open http://127.0.0.1:8000

## Website manager workflow

In Cursor, ask in plain language, for example:

- “Add this publication to my website”
- “Upload these slides for Applied Chemistry”
- “Add my new tool to Resources”
- “Use this photo as my portrait”

The agent updates YAML/assets, rebuilds, and (once deploy is connected) publishes.

## Content locations

- Global identity/links: `content/site.yaml`
- Publications: `content/publications.yaml`
- Pages: `content/home.yaml`, `about.yaml`, `research.yaml`, `teaching.yaml`, `resources.yaml`, `contact.yaml`
- Files: `assets/resources/`, `assets/images/`, `assets/cv/`

## Deploy (free) + custom domain

### Option A — GitHub Pages

1. Create a GitHub repo and push this project.
2. Enable GitHub Pages from the `site/` folder **or** use a GitHub Action that runs `build.py` and publishes `site/`.
3. In Pages settings, set custom domain to `drsahanawaz.com`.
4. At your domain registrar DNS, add:

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `<your-username>.github.io` |

5. Remove the old Google Sites domain mapping once this site is live.
6. Point both apex and `www` here (as requested).

### Option B — Cloudflare Pages (recommended free tier)

1. Push repo to GitHub.
2. Create a Cloudflare Pages project from the repo.
3. Build command: `pip install -r requirements.txt && python build.py`
4. Output directory: `site`
5. Attach custom domains `drsahanawaz.com` and `www.drsahanawaz.com` in Cloudflare (follow their DNS instructions).

## Still needed from you

1. Real Google Scholar URL and ORCID iD → `content/site.yaml`
2. Confirm GitHub username/profile URL
3. CV PDF → `assets/cv/Sahanawaz_CV.pdf`
4. Optional portrait photo → `assets/images/`
5. GitHub account access so the manager can push updates live
