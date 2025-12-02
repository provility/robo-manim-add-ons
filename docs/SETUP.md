# GitHub Pages Setup Guide

Follow these steps to enable GitHub Pages for this documentation.

## Step 1: Push to GitHub

Make sure all documentation files are committed and pushed to GitHub:

```bash
git add docs/ .github/workflows/
git commit -m "Add documentation with GitHub Pages support"
git push origin main
```

## Step 2: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/provility/robo-manim-add-ons`

2. Click on **Settings** (top menu)

3. In the left sidebar, click **Pages**

4. Under **Source**, select:
   - Source: **GitHub Actions**

5. That's it! The GitHub Actions workflow will automatically deploy your documentation.

## Step 3: Wait for Deployment

1. Go to the **Actions** tab in your repository

2. You should see a workflow running: **"Deploy Documentation to GitHub Pages"**

3. Wait for it to complete (usually takes 1-2 minutes)

4. Once complete, your documentation will be available at:
   ```
   https://provility.github.io/robo-manim-add-ons/
   ```

## Step 4: Verify

Visit your documentation site:
```
https://provility.github.io/robo-manim-add-ons/
```

You should see the homepage with navigation to API reference and examples.

## Automatic Updates

From now on, whenever you push changes to the `docs/` folder on the `main` branch, GitHub Pages will automatically rebuild and deploy your documentation.

## Manual Deployment

You can also manually trigger a deployment:

1. Go to **Actions** tab
2. Select **Deploy Documentation to GitHub Pages**
3. Click **Run workflow**
4. Choose the `main` branch
5. Click **Run workflow**

## Troubleshooting

### Documentation not showing up

- Check the **Actions** tab for any failed workflows
- Make sure GitHub Pages is enabled in Settings > Pages
- Verify you selected **GitHub Actions** as the source (not "Deploy from a branch")

### 404 errors on pages

- Make sure all links use relative paths (e.g., `../images/file.png`)
- Check that file names match exactly (case-sensitive)

### Videos not playing

- Ensure MP4 files are in `docs/videos/` folder
- Check video file size (GitHub has a 100MB file limit)
- Compress large videos:
  ```bash
  ffmpeg -i input.mp4 -vcodec libx264 -crf 28 output.mp4
  ```

### Images not loading

- Verify images are in `docs/images/` folder
- Check image paths are relative (e.g., `../images/picture.png`)
- Ensure images are pushed to GitHub

## Custom Domain (Optional)

To use a custom domain:

1. Add a file `docs/CNAME` with your domain name
2. In GitHub Settings > Pages, enter your custom domain
3. Configure DNS with your domain provider:
   - Add CNAME record pointing to `provility.github.io`

## Need Help?

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Repository Issues](https://github.com/provility/robo-manim-add-ons/issues)
