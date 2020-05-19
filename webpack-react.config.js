const path = require("path");
module.exports = {
    entry: "./assets/js/react-index.js",
    mode: process.env.DEBUG == 1 ? "development" : "production",
    output: {
        filename: "bundle-react.js",
        path: path.resolve(__dirname, "dist")
    },
    module:{
        rules:[
           {
                test: /\.jsx$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                } 
            }
        ]
    }
};