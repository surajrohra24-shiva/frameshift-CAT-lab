# Publish FrameShift to GitHub Pages

1. Create an empty GitHub repository, for example `frameshift-cat-lab`.
2. Clone or extract the repository bundle, then set the GitHub remote and push the `main` branch.
3. In GitHub, open **Settings → Pages** and select **GitHub Actions** as the source.
4. Open **Actions**, verify that `Deploy FrameShift to GitHub Pages` completes, and open the deployment URL shown in the workflow summary.

The included workflow stages only `index.html` for the published site. If the source repository is public, its other files and Git history are still visible. Do not commit CSV exports, raw survey responses, personal data or secrets; review `git status` before every commit.

Official references:
- https://docs.github.com/en/pages/quickstart
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
