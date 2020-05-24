import React, { Component } from "react";
import ReactDOM from "react-dom";
import Comment from "./comment.jsx"

import gql from 'graphql-tag';
import ApolloClient from 'apollo-boost';

const GET_COMMENTS = gql`
query comments($postId: Int){
  comments(postId: $postId) {
    text
    author {
      username
      avatar
    }
  }
}
`;

console.log(process.env.GRAPHQL_URL);

const client = new ApolloClient({
  uri: "/graphql/",
  headers: {
      'X-CSRFToken': document.cookie.split("=")[1]
  }
});


export default class CommentList extends Component{

    constructor(props) {
      super(props);
      this.state = {comments: []};
    }

    grabComments = () => {
        const postId = document.querySelector(".post_title").getAttribute("postid");
        client
        .query({
            query: GET_COMMENTS,
            variables: {
                postId: postId
            }
        }).then(
            result => this.setState({
                comments: this.state.comments.concat(result.data.comments)
            }
          )
        );
    }

    render() {
    return <div>
        { this.state.comments.map((x,i) => <div key={i}><Comment text={x.text} avatar={x.author.avatar} author={x.author.username}/><br/></div>) }
        <br/>
        <div className="nerd angry-button" onClick={this.grabComments}>Show comments</div>
        </div>;
    }
}

const rootEl = document.getElementById('react-comment');

rootEl ? ReactDOM.render(
  <CommentList  />,
  rootEl
  ) : null;