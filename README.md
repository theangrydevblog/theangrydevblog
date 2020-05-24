![theangrydevblog](https://res.cloudinary.com/dzmp7xptn/image/upload/v1589940358/theangrydevblogmd_ka0f3v.png)

## Asset pipeline

We use webpack to bundle all of our JS and CSS into one file and then use Django to collect that bundled file into one directory. The `assets` directory contains all the development versions of our JS and CSS files. The `assets/js/index.js` serves as the entry point for webpack. Once `npm run start` is run, webpack munches all of the assets into `dist/bundle.js`. Then we use `python manage.py collectstatic` to collect that bundled file to `STATIC_ROOT`

The following directories contain minified JS and should not be version controlled
* `dist`
* `static`

## Instructions

### How to add React components

Since the app is not a full-fledged SPA, we only need to load the React virtual DOM in certain pages. We maintain a separate Webpack config file for this and bundle our React components in a separate file called `bundle-react.js`. We define our React components as `.jsx` files in `assets/js/components` and Webpack bundles them with Babel, which has its own config file called `.babelrc`. Once run, the bundled file is created in `dist/bundle-react.js` and we load this file only in pages where a React virtual DOM is needed.

### How to install dependencies

* This project uses pipenv for Python dependency management. All Python packages should be installed with `pipenv install <package>`
* Update `requirements.txt`. We also maintain a `requirements.txt` because we don't need another virtual environment inside a container. The `pip` installed inside the container uses this to install the Python dependencies in the container
    ```sh
    pipenv lock -r > requirements.txt
     ```

### How to add new environment variables

* For your local dev environment, just add it to the `.env` file (not checked into Git)
* For production, update `.k8s/deployment.yml` first, then add environment variable to CircleCI BEFORE deploying
