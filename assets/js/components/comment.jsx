import React from "react";

function Comment(props){

  return(
    <div className="comment-container nerd">
        <p>{ props.text }</p>
        <div style={{display: 'flex', paddingLeft: "80%", paddingRight: "5%"}}>
            <img className="user-avatar" src={ props.avatar } />
            <p style={{ paddingLeft: "6%", paddingTop: "2%", paddingRight: "2%" }}><strong>{ props.author }</strong></p>
        </div>
    </div>
  )
}

export default Comment