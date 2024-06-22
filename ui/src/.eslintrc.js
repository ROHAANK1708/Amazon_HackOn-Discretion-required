module.exports = {
    parser: '@babel/eslint-parser', // Use babel-eslint for parsing
    env: {
      browser: true, // Enable browser globals like `window` and `document`
      es2021: true, // Enable ES2021 features
    },
    extends: [
      'eslint:recommended', // Use recommended ESLint rules
      'plugin:react/recommended', // Use recommended rules from eslint-plugin-react
    ],
    settings: {
      react: {
        version: 'detect', // Automatically detect the React version
      },
    },
    rules: {
      // Additional rules or overrides can go here
    },
  };
  