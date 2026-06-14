# Step-by-Step Deployment Guide: Dev, QA, UAT, and Prod

## 📋 Overview
This guide will help you deploy your code to 4 different environments automatically.

---

## ✅ SETUP COMPLETE!

Your repository now has:

### 1️⃣ **Three Branches Created**
- `develop` → Development Environment
- `staging` → QA & UAT Environment  
- `main` → Production Environment

### 2️⃣ **Configuration Files Created**
- `config/dev.py` → Dev settings
- `config/qa.py` → QA settings
- `config/uat.py` → UAT settings
- `config/prod.py` → Production settings

### 3️⃣ **Deployment Script Created**
- `deploy.py` → Handles deployment logic

### 4️⃣ **GitHub Actions Workflow Created**
- `.github/workflows/deploy.yml` → Automatic deployment

---

## 🚀 How to Use

### **To Deploy to DEV:**
```bash
git checkout develop
git add .
git commit -m "Changes for dev"
git push origin develop
```
✅ Code automatically deploys to Dev!

### **To Deploy to QA:**
1. Go to GitHub → Pull Requests
2. Click "New Pull Request"
3. Compare: `develop` → `staging`
4. Click "Create Pull Request" and merge
✅ Code automatically deploys to QA!

### **To Deploy to UAT:**
Same as QA (merge to `staging`)
✅ Code automatically deploys to UAT!

### **To Deploy to PROD:**
1. Go to GitHub → Pull Requests
2. Click "New Pull Request"
3. Compare: `staging` → `main`
4. Click "Create Pull Request" and merge
✅ Code automatically deploys to Prod!

---

## 📊 Deployment Flow

```
Your Code on Feature Branch
         ↓
    git push origin develop
         ↓
  Deploy to DEV ✅
         ↓
    Create PR: develop → staging
         ↓
  Deploy to QA/UAT ✅
         ↓
    Create PR: staging → main
         ↓
  Deploy to PROD ✅
```

---

## 👀 Monitor Deployments

1. Go to your GitHub repository
2. Click **Actions** tab
3. You'll see all deployments listed
4. Click any deployment to see details:
   - ✅ Success
   - ❌ Failed
   - 📋 What was deployed

---

## 📁 File Structure

```
mahadevgarad121/Data/
├── config/
│   ├── dev.py
│   ├── qa.py
│   ├── uat.py
│   └── prod.py
├── .github/workflows/
│   └── deploy.yml
├── deploy.py
├── Silver_Layer.py (your existing file)
└── DEPLOYMENT_GUIDE.md (this file)
```

---

## 🔐 Important: Update Credentials

Edit each config file with YOUR actual credentials:

**config/dev.py** - Replace with your dev credentials
**config/qa.py** - Replace with your qa credentials
**config/uat.py** - Replace with your uat credentials
**config/prod.py** - Replace with your prod credentials

To edit:
1. Go to GitHub
2. Click the file (e.g., `config/dev.py`)
3. Click the pencil ✏️ icon
4. Update the values
5. Click "Commit changes"

---

## ⚠️ For Sensitive Data (Passwords, Keys, Tokens)

**NEVER put passwords or secrets in config files!**

Use GitHub Secrets instead:

1. Go to your repo → Settings
2. Click "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. Name: `AZURE_CLIENT_SECRET_DEV`
5. Value: (your actual secret)
6. Repeat for QA, UAT, PROD

Then in config files, use:
```python
import os
CLIENT_SECRET = os.getenv('AZURE_CLIENT_SECRET_DEV')
```

---

## ✨ Next Steps

1. ✅ Update config files with your actual values
2. ✅ Make a test commit to `develop` branch
3. ✅ Go to Actions tab to see it deploy
4. ✅ Check if deployment succeeded
5. ✅ Test creating a PR from develop to staging

---

## 🆘 Troubleshooting

**Q: How do I see deployment logs?**
A: Go to Actions tab → Click the deployment → Scroll down to see logs

**Q: Can I manually trigger a deployment?**
A: Yes! Go to Actions tab → Select workflow → Click "Run workflow"

**Q: What if I need to rollback?**
A: Revert the commit and push again. The old version will redeploy.

**Q: How do I add more environments?**
A: Create a new config file + new branch + update `.github/workflows/deploy.yml`

---

## 📚 Learn More

- [GitHub Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
- [GitHub Actions](https://docs.github.com/en/actions)
- [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

**🎉 Setup Complete! Your multi-environment deployment is ready to use!**