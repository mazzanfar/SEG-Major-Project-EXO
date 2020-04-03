import React, { Component, Fragment } from "react";
import axios from "axios";
import PropTypes from "prop-types";
import { Button, Comment, Form, Header } from "semantic-ui-react";
import { connect } from "react-redux";
import { getPosts } from "../../../actions/posts";
import CommentForm from "./CommentForm";

// TODO: pass posts in ways besides props
function Comments(props) {
    return (
        <Comment.Group>
            <Header as="h3" dividing>
                Comments ({props.post.total_comments})
            </Header>
            {/* Comment Lists */}
            {props.post.comments.map((comment) => (
                <Comment>
                    <Comment.Avatar src="https://react.semantic-ui.com/images/avatar/small/matt.jpg" />
                    <Comment.Content>
                        <Comment.Author as="a">
                            {props.post.author_username}
                        </Comment.Author>
                        <Comment.Metadata>
                            <div>Today at 5:42pm</div>
                        </Comment.Metadata>
                        <Comment.Text>{comment.content}</Comment.Text>
                        <Comment.Actions>Reply</Comment.Actions>
                    </Comment.Content>
                </Comment>
            ))}
            <CommentForm post={props.post} />
        </Comment.Group>
    );
}

export default Comments;
