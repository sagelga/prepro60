# Abort on errors
# set -e

# Build the file
npm run docs:build

# Navigate into the build output directory
cd docs/.vuepress/dist

# Push the repo
git init
git add -A
git commit -m "Deploy"
git push -f git@github.com:sagelga/PreProgramming-60.git master:gh-pages

# Return to the root directory
cd -
