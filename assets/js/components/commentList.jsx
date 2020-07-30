import React, { Component, useState } from "react";
import ReactDOM from "react-dom";
import Comment from "./comment.jsx"
import client from "../apolloClient"

import gql from 'graphql-tag';
import ApolloClient from 'apollo-boost';
import { ApolloProvider, useLazyQuery } from '@apollo/react-hooks';

const GET_COMMENTS = gql`
query comments($postId: Int){
  comments(postId: $postId){
    edges{
      node{
        id
        text
        author {
          username
          avatar
        }
      }
    }
  }
}`;

function CommentList(){
  const [ comments, setComments ] = useState([]);
  const [ getComments, { loading, data } ] = useLazyQuery(GET_COMMENTS);

  if (data?.comments?.edges?.length > 0 && comments.length == 0){
    const comments = data.comments.edges.map(function(node){
      return {
        author: node.node.author.username,
        text: node.node.text,
        avatar: node.node.author.avatar
      }
    });
    setComments(comments);
  }

  return (
    <div>
      { comments.map((x,i) => <div key={i}><Comment text={x.text} avatar={x.avatar} author={x.author}/><br/></div>) }
      <br/><br/>
      <div className="nerd angry-button" onClick={function(){
        const postId = document.querySelector(".post_title").getAttribute("postid");
        getComments({
        variables:{
          postId: postId
        }
      });
    }
      }>Show comments</div>
    </div>
  );

}

const rootEl = document.getElementById('react-comment');

rootEl ? ReactDOM.render(
  <ApolloProvider client={client}>
    <CommentList  />
  </ApolloProvider>,
  rootEl
  ) : null;