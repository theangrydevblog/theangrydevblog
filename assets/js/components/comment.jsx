import React, { Component } from "react";
export default class Comment extends Component{

    // constructor(props) {
    //   super(props);
    //   this.state = {text: ""};
    // }


  render() {
    return <div className="comment-container nerd">
        <p>{ this.props.text }</p>
        <div style={{display: 'flex', paddingLeft: "80%", paddingRight: "5%"}}>
            <img className="user-avatar" src={ this.props.avatar } />
            <p style={{ paddingLeft: "6%", paddingTop: "2%", paddingRight: "2%" }}><strong>{ this.props.author }</strong></p>
        </div>
      </div>;
  }
}