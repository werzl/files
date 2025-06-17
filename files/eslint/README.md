# ES Lint Configuration File

This is my custom ES Lint config file, feel free to use it as a template and change the coding style as you see fit.

### Prerequisites
- Node.js

- Yarn OR NPM

- NPM Packages: eslint, babel-eslint, eslint-plugin-react.

### Installation
#### Adding eslint
- yarn global add eslint
<br>OR
- npm install -g eslint

#### Adding the Babel Plugin
- yarn add --dev babel-eslint
<br>OR
- npm install --save-dev babel-eslint

#### Adding the React Plugin
- yarn add --dev eslint-plugin-react
<br>OR
- npm install --save-dev eslint-plugin-react

### Usage
If you're working in vscode, you can see linting errors live with an extension; the one I use is EsLint by Dirk Baeumer: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint.

Otherwise, run the following command in your project directory to get a detailed list of linting errors with line numbers.
- eslint .
