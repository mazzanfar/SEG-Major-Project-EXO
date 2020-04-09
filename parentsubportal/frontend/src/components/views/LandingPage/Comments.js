import React, { Component, Fragment, useEffect, useState } from "react";
import axios from "axios";
import PropTypes from "prop-types";
import { Button, Comment, Form, Header, TextArea } from "semantic-ui-react";
import { connect, useDispatch } from "react-redux";
import { getPosts } from "../../../actions/posts";
import { deleteComment } from "../../../actions/comments";
import CommentForm from "./CommentForm";

function CommentItem(props) {
    const [editing, setEditing] = useState(false);
    const dispatch = useDispatch();

    const handleDelete = () => {
        dispatch(deleteComment(props.comment));
    };

    const renderCommentText = () => {
        if (!editing)
            return (
                <Fragment>
                    <Comment.Text>{props.comment.content}</Comment.Text>
                    <Comment.Actions>
                        <Comment.Action onClick={() => setEditing(true)}>
                            Edit
                        </Comment.Action>
                        <Comment.Action onClick={() => handleDelete()}>
                            Delete
                        </Comment.Action>
                    </Comment.Actions>
                </Fragment>
            );
        else
            return (
                <Fragment>
                    <Comment.Text>Currently editing</Comment.Text>
                    <Comment.Actions>
                        <Comment.Action onClick={() => setEditing(false)}>
                            Save
                        </Comment.Action>
                    </Comment.Actions>
                </Fragment>
            );
    };

    return (
        <Comment>
            <Comment.Avatar src="https://react.semantic-ui.com/images/avatar/small/matt.jpg" />
            <Comment.Content>
                <Comment.Author as="a">
                    {props.post.author_username}
                </Comment.Author>
                <Comment.Metadata>
                    <div>Posted on {props.comment.tidy_date}</div>
                </Comment.Metadata>
                {renderCommentText(props.comment)}
            </Comment.Content>
        </Comment>
    );
}

// TODO: pass posts in ways besides props
function Comments(props) {
    const [post, setPost] = useState(props.post);

    useEffect(() => {
        setPost(props.post);
    }, [props.post]);

    return (
        <Comment.Group>
            <Header as="h3" dividing>
                Comments ({post.total_comments})
            </Header>
            {/* Comment Lists */}
            {post.comments.map((comment) => (
                <CommentItem comment={comment} post={post} />
            ))}
            <CommentForm post={post} />
        </Comment.Group>
    );
}

export default Comments;
