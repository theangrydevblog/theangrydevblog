import React, { Component } from "react";
import ReactDOM from "react-dom";
export default class Comment extends Component{
  render() {
    return <h1>Hello, how are you</h1>;
  }
}


ReactDOM.render(
  <Comment />,
  document.getElementById('react-comment')
);