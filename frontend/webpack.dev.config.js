const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    devServer:{
        publicPath: 'http://localhost:9000',
        port: 9000,
        hot: true,
        headers: { 'Access-Control-Allow-Origin': '*' }
    },
    entry: './index',
    output: {
        publicPath: 'http://localhost:9000/',
        filename: "[name]-[hash].js",
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['react-hot-loader/webpack', 'babel-loader']
            }
        ]
    },
    resolve: {
        extensions: ['*', '.js', '.jsx']
    }
};