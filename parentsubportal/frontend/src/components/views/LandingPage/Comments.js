import React, { Component, Fragment, useEffect, useState } from "react";
import axios from "axios";
import PropTypes from "prop-types";
import { Button, Comment, Form, Header } from "semantic-ui-react";
import { connect } from "react-redux";
import { getPosts } from "../../../actions/posts";
import CommentForm from "./CommentForm";

// TODO: pass posts in ways besides props
function Comments(props) {
    const [post, setPost] = useState(props.post);

    useEffect(() => {
        setPost(props.post);
        console.log(props.post);
    }, [props.post]);

    return (
        <Comment.Group>
            <Header as="h3" dividing>
                Comments ({post.total_comments})
            </Header>
            {/* Comment Lists */}
            {post.comments.map((comment) => (
                <Comment>
                    <Comment.Avatar src="https://react.semantic-ui.com/images/avatar/small/matt.jpg" />
                    <Comment.Content>
                        <Comment.Author as="a">
                            {post.author_username}
                        </Comment.Author>
                        <Comment.Metadata>
                            <div>Posted on {comment.tidy_date}</div>
                        </Comment.Metadata>
                        <Comment.Text>{comment.content}</Comment.Text>
                        <Comment.Actions>Reply</Comment.Actions>
                    </Comment.Content>
                </Comment>
            ))}
            <CommentForm post={post} />
        </Comment.Group>
    );
}

export default Comments;
