const path = require("path");
module.exports = {
    entry: "./assets/js/index.js",
    mode: process.env.DEBUG == 1 ? "development" : "production",
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, "dist")
    },
    module:{
        rules:[
            {
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            }
        ]
    }
};