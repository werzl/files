# CI / CD Pipeline for GitHub Pages
The CI workflow runs on any pull request into master; it will build the site using Yarn and report the outcome.
  
The CD workflow runs when a pull request is merged (or commit is pushed manually) into master; it builds the site with Yarn and then uses the action 'JamesIves/github-pages-deploy-action' to deploy to the gh-pages branch.

### Usage
Place the scripts in './.github/workflows' in your GitHub repo.