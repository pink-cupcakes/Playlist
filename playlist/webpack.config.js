const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: [
    './client/src/index.jsx'
  ],

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      },
      {
        test: /\.(css|scss)/,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' }
        ]
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: ['file-loader']
      },
      {
        test: /\.(jpg|jpeg|gif|png)$/,
        exclude: /node_modules/,
        use: ['url-loader']
      }
    ]
  },

  output: {
    path: __dirname + '/login/static/bundles/local/',
    publicPath: '/',
    filename: 'bundle.js'
  },

  resolve: {
    extensions: ['*', '.js', '.jsx']
  },

  devServer: {
    contentBase: './dist'
  }
};