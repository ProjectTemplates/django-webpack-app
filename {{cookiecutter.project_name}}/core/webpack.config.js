var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './assets/lib/index.js',
  output: {
      path: path.resolve('./dist/bundle'),
      filename: "lib.js",
      library: 'lib',
      libraryTarget:'umd'
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ]
  /* TODO
  optimization: {
    runtimeChunk: true
  }
  */
}