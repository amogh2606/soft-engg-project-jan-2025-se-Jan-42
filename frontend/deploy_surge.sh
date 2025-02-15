#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Build the Vue.js project
echo "Building Vue.js project..."
npm run build

# Step 2: Navigate to the dist folder
cd dist

# Step 3: Copy index.html to 404.html to handle deep linking
echo "Creating 404.html for Surge routing..."
cp index.html 404.html

# Step 4: Deploy to Surge
echo "Deploying to Surge at iitm-se-project.surge.sh..."
surge . iitm-se-project.surge.sh

# Step 5: Return to root directory
cd ..

echo "Deployment successful! 🎉 Your app is live at https://iitm-se-project.surge.sh"
