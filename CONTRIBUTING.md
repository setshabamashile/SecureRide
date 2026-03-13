# Contributing to SecureRide 
 
## Git Workflow 
 
1. **Always start from updated dev branch** 
   ```bash 
   git checkout dev 
   git pull origin dev 
   ``` 
 
2. **Create a feature branch** 
   ```bash 
   git checkout -b feature/your-feature-name 
   # or 
   git checkout -b bugfix/issue-description 
   ``` 
 
3. **Make your changes and commit** 
   ```bash 
   git add . 
   git commit -m "Clear description of what you changed" 
   ``` 
 
4. **Push and create Pull Request** 
   ```bash 
   git push origin feature/your-feature-name 
   ``` 
   Then go to GitHub and create a Pull Request to merge into `dev` 
 
## Commit Message Format 
- `feat:` New feature 
- `fix:` Bug fix 
- `docs:` Documentation only 
- `style:` Code style changes 
- `refactor:` Code change that neither fixes bug nor adds feature 
- `test:` Adding tests 
- `chore:` Changes to build process or tools 
 
Example: `feat: add face verification endpoint` 
